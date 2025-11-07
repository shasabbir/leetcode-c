# Multi-Language Coding Workspace

A GitHub Codespaces-ready workspace for solving algorithm and data structure problems (like LeetCode) using both **C** and **Python**.

## Features

- **C Programming**: C17 standard with gcc compiler
- **Python Programming**: Python 3.11+ with pytest and black formatter
- **Pre-configured Development Environment**: Ready to use in GitHub Codespaces
- **Organized Structure**: Separate folders for different problem categories
- **Build Automation**: Makefile for C compilation, pytest for Python testing

## Folder Structure

```
problems/
├── c/
│   ├── arrays/          # Array-based problems in C
│   ├── linked_list/     # Linked list problems in C
│   └── dp/              # Dynamic programming problems in C
└── python/
    ├── arrays/          # Array-based problems in Python
    ├── linked_list/     # Linked list problems in Python
    └── dp/              # Dynamic programming problems in Python
```

## Getting Started

### Option 1: GitHub Codespaces (Recommended)

1. Click the **Code** button on the repository
2. Select **Codespaces** tab
3. Click **Create codespace on main** (or your branch)
4. Wait for the environment to set up automatically

All tools (gcc, make, gdb, Python, pytest, black) will be pre-installed!

### Option 2: Local Development

Install the required tools:

**For C:**
```bash
sudo apt-get update
sudo apt-get install -y gcc make gdb
```

**For Python:**
```bash
sudo apt-get install -y python3.11 python3-pip
pip install pytest black
```

## Working with C Programs

### Compile All C Programs

```bash
make
```

This compiles all `.c` files in `problems/c/` and places executables in the `build/` directory.

### Compile a Specific Problem

```bash
make build/arrays/two_sum
```

### Run a Compiled Program

```bash
./build/arrays/two_sum
```

### Run All Programs

```bash
make run
```

### Clean Build Artifacts

```bash
make clean
```

### Debug with GDB

```bash
gdb ./build/arrays/two_sum
```

## Working with Python Programs

### Run a Python Program

```bash
python problems/python/arrays/two_sum.py
```

### Run Tests with pytest

**Run all tests:**
```bash
pytest
```

**Run tests with verbose output:**
```bash
pytest -v
```

**Run tests for a specific category:**
```bash
pytest -m arrays
pytest -m linked_list
pytest -m dp
```

**Run tests in a specific file:**
```bash
pytest problems/python/arrays/test_two_sum.py
```

### Format Python Code with Black

**Format a single file:**
```bash
black problems/python/arrays/two_sum.py
```

**Format all Python files:**
```bash
black problems/python/
```

**Check formatting without changes:**
```bash
black --check problems/python/
```

## Adding New Problems

### For C Programs

1. Create a new `.c` file in the appropriate category folder:
   ```bash
   touch problems/c/arrays/problem_name.c
   ```

2. Write your solution with a `main()` function for testing

3. Compile and run:
   ```bash
   make build/arrays/problem_name
   ./build/arrays/problem_name
   ```

### For Python Programs

1. Create a new `.py` file in the appropriate category folder:
   ```bash
   touch problems/python/arrays/problem_name.py
   ```

2. Write your solution function

3. Create a test file (optional but recommended):
   ```bash
   touch problems/python/arrays/test_problem_name.py
   ```

4. Run your solution:
   ```bash
   python problems/python/arrays/problem_name.py
   ```

5. Run tests:
   ```bash
   pytest problems/python/arrays/test_problem_name.py
   ```

## Example Problems

The workspace includes example implementations of the "Two Sum" problem:

- **C**: `problems/c/arrays/two_sum.c`
- **Python**: `problems/python/arrays/two_sum.py` with tests in `test_two_sum.py`

Try compiling and running these examples to verify your setup!

## Development Tools

### VS Code Extensions (Pre-configured in Codespaces)

- **C/C++ Tools**: IntelliSense, debugging, and code formatting for C
- **Python**: IntelliSense, debugging, and linting for Python
- **Black Formatter**: Automatic Python code formatting
- **Makefile Tools**: Syntax highlighting and IntelliSense for Makefiles

### Compiler and Interpreter Versions

- **C Compiler**: gcc with C17 standard (`-std=c17`)
- **Python**: Python 3.11 or higher

## Tips for Algorithm Practice

1. **Start Simple**: Begin with array and string problems before moving to complex data structures
2. **Test Thoroughly**: Write multiple test cases including edge cases
3. **Use Debugging Tools**: Leverage gdb for C and pytest's verbose mode for Python
4. **Format Code**: Keep your code clean with consistent formatting
5. **Compare Solutions**: Implement the same problem in both C and Python to understand language differences

## License

This workspace is set up for personal algorithm practice and learning.