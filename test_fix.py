#!/usr/bin/env python3
import sys
from typing import Optional, Union

# Test 1: Check Python version and type annotation compatibility
print(f"Python version: {sys.version}")

# This should work in all Python versions
def test_func(x: str) -> Optional[int]:
    return None

print("Type annotation with Optional[int] works")

# Test 2: Import the fixed modules to check for syntax errors
try:
    import pwndbg.gdblib.heap_tracking
    print("Successfully imported heap_tracking module")
except SyntaxError as e:
    print(f"SyntaxError in heap_tracking module: {e}")
except ImportError as e:
    print(f"ImportError: {e}")