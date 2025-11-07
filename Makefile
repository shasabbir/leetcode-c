# Makefile for C LeetCode Problems
# Supports C17 standard with gcc

CC = gcc
CFLAGS = -std=c17 -Wall -Wextra -Wpedantic -O2 -g
LDFLAGS = -lm

# Directories
C_DIR = problems/c
BUILD_DIR = build

# Find all C source files
SOURCES = $(shell find $(C_DIR) -name "*.c")
TARGETS = $(patsubst $(C_DIR)/%.c,$(BUILD_DIR)/%,$(SOURCES))

# Default target
.PHONY: all
all: $(BUILD_DIR) $(TARGETS)

# Create build directory
$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)
	mkdir -p $(BUILD_DIR)/arrays
	mkdir -p $(BUILD_DIR)/linked_list
	mkdir -p $(BUILD_DIR)/dp

# Compile individual C files
$(BUILD_DIR)/%: $(C_DIR)/%.c
	@mkdir -p $(dir $@)
	$(CC) $(CFLAGS) $< -o $@ $(LDFLAGS)
	@echo "Compiled: $< -> $@"

# Clean build artifacts
.PHONY: clean
clean:
	rm -rf $(BUILD_DIR)
	@echo "Cleaned build directory"

# Run all executables
.PHONY: run
run: all
	@for exec in $(TARGETS); do \
		if [ -f $$exec ]; then \
			echo "Running $$exec:"; \
			./$$exec; \
			echo ""; \
		fi \
	done

# Help target
.PHONY: help
help:
	@echo "Available targets:"
	@echo "  all     - Compile all C programs (default)"
	@echo "  clean   - Remove all build artifacts"
	@echo "  run     - Compile and run all programs"
	@echo "  help    - Display this help message"
	@echo ""
	@echo "To compile a specific file:"
	@echo "  make $(BUILD_DIR)/arrays/problem_name"
