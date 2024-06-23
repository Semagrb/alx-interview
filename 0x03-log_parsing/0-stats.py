#!/usr/bin/python3
import sys
import signal

# Initialize metrics
total_file_size = 0
status_code_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

line_count = 0

def print_stats():
    global total_file_size, status_code_count
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    line_count += 1
    parts = line.split()
    
    # Validate the format of the line
    if len(parts) != 10:
        continue
    
    ip, dash, date, request, status_code, file_size = parts[0], parts[1], parts[2], parts[3] + " " + parts[4] + " " + parts[5], parts[8], parts[9]
    
    try:
        status_code = int(status_code)
        file_size = int(file_size)
    except ValueError:
        continue

    if request == "\"GET /projects/260 HTTP/1.1\"":
        total_file_size += file_size
        if status_code in status_code_count:
            status_code_count[status_code] += 1
    
    if line_count % 10 == 0:
        print_stats()

# Print final stats if the script finishes without interruption
print_stats()
