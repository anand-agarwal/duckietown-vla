# Duckietown VLA

This project aims to build a vision-language-action (VLA) system for a Duckiebot. The goal is for a robot to use its camera and a natural-language instruction to determine and safely execute an appropriate driving action.

## Project status

This repository currently contains the Duckietown ROS development scaffold. The VLA pipeline and robot behaviors are not implemented yet.

## Intended system

The initial system will connect these parts:

- **Vision:** Read camera observations from the Duckiebot and identify relevant road features, obstacles, and landmarks.
- **Language grounding:** Interpret an instruction in the context of the current observation and the robot's capabilities.
- **Action interface:** Convert the selected behavior into commands supported by the Duckietown ROS stack.
- **Safety and evaluation:** Constrain motion, handle invalid or uncertain commands, and test behaviors in simulation before running on a physical robot.

The system should keep high-level interpretation separate from low-level motion control so that generated actions remain bounded by the robot's existing control and safety mechanisms.

## Repository layout

- `packages/` is where ROS packages and VLA components belong.
- `launchers/` contains scripts exposed as Duckietown container launchers. Keep `launchers/default.sh` available.
- `dependencies-apt.txt` and `dependencies-py3.txt` list system and Python dependencies.
- `dependencies-py3.dt.txt` lists additional Python dependencies for Duckietown.

## Development

Use the Duckietown ROS development environment defined by this repository's `Dockerfile` and dependency files. Add implementation under `packages/`, declare required dependencies in the appropriate dependency file, and provide a launcher in `launchers/` for runnable components.

Start by validating the perception-to-action path in simulation. Physical-robot testing should only follow once command limits, stop behavior, and failure handling are in place.