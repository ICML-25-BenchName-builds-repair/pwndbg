import ast
import sys

# Set the target version to Python 3.8
target_version = (3, 8)

# Read the heap_tracking.py file
with open('pwndbg/gdblib/heap_tracking.py', 'r') as f:
    code = f.read()

try:
    # Parse the code with Python 3.8 features
    ast.parse(code, feature_version=target_version)
    print("The code is compatible with Python 3.8")
except SyntaxError as e:
    print(f"Syntax error when parsing with Python 3.8 features: {e}")