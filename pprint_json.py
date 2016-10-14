#!/usr/bin/env python3

import argparse
import json
import os


def load_data(filepath):
    if not os.path.exists(filepath):
        return None

    with open(filepath) as json_file:
        return json.load(json_file)


def pretty_print_json(data, indent=4):
    return json.dumps(data, indent=indent, ensure_ascii=False)


def main():
    description = "Pretty print for JSON"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "-f", "--filepath",
        required=True,
        help="Input file"
    )
    parser.add_argument(
        "-i", "--indent",
        help="Indentation size. Default: 4",
        default=4,
        type=int
    )

    args = parser.parse_args()

    data = load_data(args.filepath)
    print(
        pretty_print_json(data, args.indent)
    )


if __name__ == "__main__":
    main()
