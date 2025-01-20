#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""
import re
import sys

codeCounts = {}
file_size = 0
count = 0
while count < 10:
    for line in sys.stdin.readlines():
        lineRegexPattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
        if re.match(lineRegexPattern, line):
            lineParts = line.split()
            dateStart = line.find('[') + 1
            dateEnd = line.find(']')
            date = line[dateStart:dateEnd]
            file_size += int(lineParts[-1])
            status_code = lineParts[-2]
            if not codeCounts.get(status_code):
                codeCounts[status_code] = 0
            codeCounts[status_code] += 1
            count += 1
        try:
            if count == 10:
                print(f'File size: {file_size}')
                codeCountKeys = sorted(codeCounts)
                for key in codeCountKeys:
                    print(f'{key}: {codeCounts[key]}')
                    file_size = 0
                    codeCounts = {}
        except KeyboardInterrupt:
            pass
