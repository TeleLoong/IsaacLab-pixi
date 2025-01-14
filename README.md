# IsaacLab-pixi

Installing IsaacLab using pixi, an opensource package management tool for developers.

## Usage

- Install Pixi

```bash
curl -fsSL https://pixi.sh/install.sh | bash
```

- Clone this repository into your workspace

```bash
git clone https://github.com/TeleLoong/IsaacLab-pixi.git --recursive
```

- Install/Build the environment

```bash
cd IsaacLab-pixi
pixi install
```

- Try a simple example

```bash
pixi shell # Activate the environment
python IsaacLab/source/standalone/tutorials/00_sim/create_empty.py
```
