import argparse


def compress_code(input_code, max_length=80):
    """
    Compresses input code into fewer lines based on these rules:
      - Code is separated by empty lines into different code blocks.
      - Empty lines are omitted in the output.
      - Within the same code block, the first line retains its indent.
      - Subsequent lines have their leading whitespace removed and are appended with a space.
      - Lines are accumulated until appending another line would exceed max_length characters.
    """
    # Split input into lines and group them into blocks using empty lines as delimiters
    lines = input_code.splitlines()
    blocks = []
    current_block = []
    for line in lines:
        if line.strip() == "":
            if current_block:
                blocks.append(current_block)
                current_block = []
        else:
            current_block.append(line)
    if current_block:
        blocks.append(current_block)

    # Process each block
    output_lines = []
    for block in blocks:
        # Start with the first line (keep its indent)
        accumulator = block[0]
        # Process subsequent lines in the block
        for line in block[1:]:
            stripped_line = line.strip()  # remove leading whitespace
            if len(accumulator) + 1 + len(stripped_line) > max_length:
                output_lines.append(accumulator)
                accumulator = line
            else:
                accumulator += " " + stripped_line
        output_lines.append(accumulator)

    return "\n".join(output_lines)


def main():
    parser = argparse.ArgumentParser(description="Compress code into fewer lines.")
    parser.add_argument("input_file", help="Path to the input file containing code.")
    parser.add_argument(
        "output_file", help="Path to the output file to save the compressed code."
    )
    parser.add_argument(
        "--line-length",
        type=int,
        default=80,
        help="Maximum length of a line (default: 80).",
    )
    args = parser.parse_args()

    # Read input file
    with open(args.input_file, "r", encoding="utf-8") as f:
        input_code = f.read()

    # Compress code using the specified max line length
    compressed = compress_code(input_code, max_length=args.line_length)

    # Write the compressed code to the output file
    with open(args.output_file, "w", encoding="utf-8") as f:
        f.write(compressed)

    print(f"Compressed code written to {args.output_file}")


if __name__ == "__main__":
    main()
