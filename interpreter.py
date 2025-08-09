import sys
import turtle
import os

def init_turtle():
    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(1)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    return t


if len(sys.argv) != 2:
    print("Usage: python interpreter.py <filename.turtlescript>")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, 'r') as file:
        screen = turtle.Screen()
        t = init_turtle()
        
        lines = file.readlines()
        def strip_comments(script):
            import re
            script = re.sub(r'/\*.*?\*/', '', script, flags=re.DOTALL)
            script = re.sub(r'#.*', '', script)
            return script

        script_text = ''.join(lines)
        script_text = strip_comments(script_text)
        script_lines = [l for l in script_text.splitlines() if l.strip()]

        def execute_commands(commands, t):
            env = {
                'holding': False,
                'wall_in_front': False,
                'empty_left': True,
                'empty_right': True
            }
            i = 0
            break_flag = False
            def eval_condition(cond):
                cond = cond.strip()
                negate = False
                if cond.startswith('!'):
                    negate = True
                    cond = cond[1:].strip()
                val = False
                if cond == 'wall_in_front':
                    val = env['wall_in_front']
                elif cond == 'empty_left':
                    val = env['empty_left']
                elif cond == 'empty_right':
                    val = env['empty_right']
                elif cond == 'holding':
                    val = env['holding']
                if negate:
                    return not val
                return val

            while i < len(commands):
                line = commands[i].strip()
                if line.startswith('move '):
                    try:
                        num = float(line.split()[1])
                        t.forward(num)
                        env['wall_in_front'] = False
                    except Exception as e:
                        print(f"Error in move: {e}")
                elif line.startswith('turn '):
                    try:
                        num = float(line.split()[1])
                        t.right(num)
                    except Exception as e:
                        print(f"Error in turn: {e}")
                elif line.startswith('loop '):
                    try:
                        parts = line.split()
                        count = int(parts[1])
                        if '{' in line:
                            block = []
                            i += 1
                            while i < len(commands) and '}' not in commands[i]:
                                block.append(commands[i].strip())
                                i += 1
                            for _ in range(count):
                                execute_commands(block, t)
                        else:
                            print("Malformed loop block.")
                    except Exception as e:
                        print(f"Error in loop: {e}")
                elif line.startswith('while '):
                    try:
                        cond = line[6:].split('{')[0].strip()
                        if '{' in line:
                            block = []
                            i += 1
                            while i < len(commands) and '}' not in commands[i]:
                                block.append(commands[i].strip())
                                i += 1
                            while eval_condition(cond):
                                execute_commands(block, t)
                                if break_flag:
                                    break_flag = False
                                    break
                        else:
                            print("Malformed while block.")
                    except Exception as e:
                        print(f"Error in while: {e}")
                elif line.startswith('if '):
                    try:
                        cond = line[3:].split('{')[0].strip()
                        if '{' in line:
                            block = []
                            i += 1
                            while i < len(commands) and '}' not in commands[i]:
                                block.append(commands[i].strip())
                                i += 1
                            if eval_condition(cond):
                                execute_commands(block, t)
                        else:
                            print("Malformed if block.")
                    except Exception as e:
                        print(f"Error in if: {e}")
                elif line == 'break':
                    break_flag = True
                    return
                elif line == 'pick':
                    if not env['holding']:
                        env['holding'] = True
                        print("Picked up item.")
                    else:
                        print("Already holding item.")
                elif line == 'drop':
                    if env['holding']:
                        env['holding'] = False
                        print("Dropped item.")
                    else:
                        print("Not holding anything to drop.")
                i += 1
        script_lines = [l for l in lines if l.strip() and not l.strip().startswith('#')]
    execute_commands(script_lines, t)
except FileNotFoundError:
    print("File not found:", filename)
    sys.exit(1)

# Keeps the window open
turtle.done()
