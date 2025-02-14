import os
import re


ISAACSIM_DIR = "/home/lamb/isaaclab/IsaacLab-git/.pixi/envs/default/lib/python3.10/site-packages/isaacsim"
ISAACLAB_DIR = "/home/lamb/isaaclab/IsaacLab-git/IsaacLab"


def overwrite_python_analysis_extra_paths(isaaclab_settings):
    """Overwrite the python.analysis.extraPaths in the Isaac Lab settings file.

    The extraPaths are replaced with the path names from the isaac-sim settings file that exists in the
    "{ISAACSIM_DIR}/.vscode/settings.json" file.

    If the isaac-sim settings file does not exist, the extraPaths are not overwritten.

    Args:
        isaaclab_settings: The settings string to use as template.

    Returns:
        The settings string with overwritten python analysis extra paths.
    """
    path_names = []

    isaacsim_extensions = os.listdir(os.path.join(ISAACSIM_DIR, "exts"))
    path_names.extend(
        [
            '"${workspaceFolder}/.pixi/envs/default/lib/python3.10/site-packages/isaacsim/exts/'
            + ext
            + '"'
            for ext in isaacsim_extensions
        ]
    )

    isaacsim_extensions_deprecated = os.listdir(
        os.path.join(ISAACSIM_DIR, "extsDeprecated")
    )
    path_names.extend(
        [
            '"${workspaceFolder}/.pixi/envs/default/lib/python3.10/site-packages/isaacsim/extsDeprecated/'
            + ext
            + '"'
            for ext in isaacsim_extensions_deprecated
        ]
    )

    isaacsim_extensions_physics = os.listdir(os.path.join(ISAACSIM_DIR, "extsPhysics"))
    path_names.extend(
        [
            '"${workspaceFolder}/.pixi/envs/default/lib/python3.10/site-packages/isaacsim/extsPhysics/'
            + ext
            + '"'
            for ext in isaacsim_extensions_physics
        ]
    )

    # add the path names that are in the Isaac Lab extensions directory
    isaaclab_extensions = os.listdir(os.path.join(ISAACLAB_DIR, "source"))
    path_names.extend(
        [
            '"${workspaceFolder}/IsaacLab/source/' + ext + '"'
            for ext in isaaclab_extensions
        ]
    )

    # combine them into a single string
    path_names = ",\n\t\t".expandtabs(4).join(path_names)
    # deal with the path separator being different on Windows and Unix
    path_names = path_names.replace("\\", "/")

    # replace the path names in the Isaac Lab settings file with the path names parsed
    isaaclab_settings = re.sub(
        r"\"python.analysis.extraPaths\": \[.*?\]",
        '"python.analysis.extraPaths": [\n\t\t'.expandtabs(4)
        + path_names
        + "\n\t]".expandtabs(4),
        isaaclab_settings,
        flags=re.DOTALL,
    )
    # return the Isaac Lab settings string
    return isaaclab_settings


if __name__ == "__main__":
    with open("/home/lamb/isaaclab/IsaacLab-git/.vscode/settings.json") as f:
        isaaclab_settings = f.read()
    print(overwrite_python_analysis_extra_paths(isaaclab_settings))
