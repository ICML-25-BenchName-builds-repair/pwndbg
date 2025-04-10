#!/usr/bin/env python3
import sys

# Test 1: Check Python version and type annotation compatibility
print(f"Python version: {sys.version}")

try:
    # This will fail in Python < 3.10
    def test_func(x: str) -> int | None:
        return None
    print("Type annotation with pipe operator works")
except SyntaxError:
    print("Type annotation with pipe operator fails - needs Python 3.10+")

# Test 2: Check context sections
try:
    import pwndbg.gdblib.config
    import pwndbg.commands.context
    
    print(f"Default context sections: {pwndbg.commands.context.config_context_sections.value}")
    
    # Check if 'heap-tracker' is in the default sections
    if 'heap-tracker' in pwndbg.commands.context.config_context_sections.value:
        print("'heap-tracker' is in default context sections - this will cause test failures")
    else:
        print("'heap-tracker' is not in default context sections")
except ImportError:
    print("Could not import pwndbg modules - run this in GDB with pwndbg loaded")