#!/usr/bin/python3
import sys
import re
from collections import Counter
from functools import reduce
from operator import add

# Define the status codes we are interested in
STATUS_CODES = [200, 301, 400, 401, 403, 404, 405, 500]

# Initialize variables to store metrics
total_file_size = 0
status_code_count = Counter()

# Regular expression pattern to match the input format
input_pattern = re.compile(r"^(\S+) - \[(\S+)\] \"GET /projects/260 HTTP/1.1\" (\d+) (\d+)$")

try:
    # Read input line by line from stdin
    for line_count, line in enumerate(sys.stdin):
        # Remove trailing newline
        line = line.rstrip()

        # Try to match the input pattern
        match = input_pattern.match(line)
        if match:
            _, _, status_code, file_size = match.groups()

            # Convert status code and file size to integers
            status_code = int(status_code)
            file_size = int(file_size)

            # Update metrics
            total_file_size += file_size
            status_code_count[status_code] += 1

            # Print statistics after every 10 lines
            if line_count > 0 and line_count % 10 == 0:
                print_statistics()
        else:
            # Skip lines that don't match the input format
            continue

    # Print statistics at the end of input
    print_statistics()

except KeyboardInterrupt:
    # Print statistics when Ctrl+C is pressed
    print_statistics()

def print_statistics():
    """Print the current statistics."""
    print("Total file size: File size: {}".format(total_file_size))
    for code in sorted(STATUS_CODES):
        count = status_code_count.get(code, 0)
        if count > 0:
            print(f"{code}: {count}")
