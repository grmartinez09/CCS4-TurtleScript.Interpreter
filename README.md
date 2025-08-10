# CCS4 - TurtleScript Interpreter

## Overview
This project is a basic Python interpreter for a simplified '.turtlescript' language. It reads commands from a '.turtlescript' file and simulates turtle movements and actions step-by-step.

The interpreter must support the following core commands:
- 'move <number>' — Moves the turtle forward by the specified number of units.
- 'turn <number>' — Rotates the turtle by the specified number of degrees.
- 'loop <number> { ... }' — Repeats the enclosed commands the given number of times.

Optional extensions may include:
- Control structures: 'while', 'if', 'break'
- Actions: 'pick', drop'
- Condition checks: 'wall_in_front', 'empty_left', 'empty_right'
- Comments: '/* */' and '#'
  
## Instructions
Download the Following files:
1. 'interpreter.py' — The Python interpreter script.
2. 'example.turtlescript' — A sample script demonstrating supported commands.
3. 'README.txt' — This file, explaining usage and functionality.

Input the following on Terminal
  "./interpreter.py" "./sample.turtlescript"

## How the Interpreter Works
1. **Script Loading**: Reads a '.turtlescript' file line by line.
2. **Command Parsing**: Identifies and validates each command.
3. **Execution Engine**: Executes commands sequentially, updating the turtle's position and orientation.
4. **Loop Handling**: Recursively processes commands inside 'loop' blocks.
5. **Output Display**: Prints step-by-step updates showing the turtle’s actions and position.

## How to Run
1. Make sure Python is installed.
2. Place 'interpreter.py' and your '.turtlescript' file in the same folder.
3. Run the interpreter: python interpreter.py (Make sure that the directory of the folder is the correct path)
