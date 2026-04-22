from __future__ import annotations

import argparse
from pathlib import Path

from corruptpm.generator import generate_construct_from_yaml


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Turtle from a YAML construct file.")
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    _, ttl = generate_construct_from_yaml(args.input, output_path=args.output)
    if args.output:
        print(args.output)
        return
    print(ttl)


if __name__ == "__main__":
    main()
