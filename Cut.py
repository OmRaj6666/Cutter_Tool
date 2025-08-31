#!/usr/bin/env python3
import sys
import argparse

def parse_fields(fields_arg):
    # Accept both comma and whitespace separated lists
    fields = []
    for part in fields_arg.replace(',', ' ').split():
        if part.isdigit():
            n = int(part)
            if n > 0:
                fields.append(n)
    return fields

def cut_fields(source, fields, delimiter):
    for line in source:
        row = line.rstrip('\n').split(delimiter)
        output = []
        for i in fields:
            if 1 <= i <= len(row):
                output.append(row[i-1])
        print(delimiter.join(output))

def main():
    parser = argparse.ArgumentParser(description='cut: Extract fields from lines of a file or standard input.')
    parser.add_argument('-f', '--fields', required=True,
                        help='List of fields to extract (comma or whitespace separated, 1-based)')
    parser.add_argument('-d', '--delimiter', default='\t',
                        help='Field delimiter (default: tab)')
    parser.add_argument('filename', nargs='?', default='-',
                        help='Input file (default: stdin)')
    args = parser.parse_args()
    fields = parse_fields(args.fields)
    if not fields:
        print('Error: No valid fields specified.', file=sys.stderr)
        sys.exit(1)

    # Open file or stdin
    if args.filename == '-' or args.filename == '':
        source = sys.stdin
    else:
        source = open(args.filename, encoding='utf-8')

    # Run
    try:
        cut_fields(source, fields, args.delimiter)
    finally:
        if source is not sys.stdin:
            source.close()

if __name__ == '__main__':
    main()
