# Verify that our fixes work with Python 3.8
import sys
import ast

print(f"Python version: {sys.version}")

# Check if the type annotation in heap_tracking.py is compatible with Python 3.8
with open('pwndbg/gdblib/heap_tracking.py', 'r') as f:
    heap_tracking_code = f.read()

try:
    ast.parse(heap_tracking_code)
    print("heap_tracking.py: Syntax is valid")
except SyntaxError as e:
    print(f"heap_tracking.py: Syntax error: {e}")

# Check if the context sections in context.py match the expected value
with open('pwndbg/commands/context.py', 'r') as f:
    for line in f:
        if 'config_context_sections' in line and 'add_param' in line:
            # Found the start of the config_context_sections definition
            # Read the next line which should contain the default value
            default_value_line = next(f)
            if 'heap-tracker' in default_value_line:
                print("context.py: 'heap-tracker' is still in the default context sections")
            else:
                print("context.py: 'heap-tracker' is not in the default context sections")
            break