# Test script to verify Python version compatibility issue
import sys

print(f"Python version: {sys.version}")

try:
    # This will fail in Python < 3.10
    def test_function() -> int | None:
        return None
    
    print("Pipe operator in type annotations is supported")
except SyntaxError:
    print("Pipe operator in type annotations is NOT supported")