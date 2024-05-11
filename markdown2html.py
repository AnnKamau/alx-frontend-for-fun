#!/usr/bin/python3

import argparse
import sys
import os
import markdown

def convert_markdown_to_html(markdown_file, output_file):
    with open(markdown_file, 'r') as md_file:
        md_content = md_file.read()
        html_content = markdown.markdown(md_content)
        with open(output_file, 'w') as html_file:
            html_file.write(html_content)

def main():
    parser = argparse.ArgumentParser(description='Convert Markdown to HTML')
    parser.add_argument('markdown_file', type=str, help='Input Markdown file')
    parser.add_argument('output_file', type=str, help='Output HTML file')
    args = parser.parse_args()

    markdown_file = args.markdown_file
    output_file = args.output_file

    if not os.path.exists(markdown_file):
        sys.stderr.write(f"Missing {markdown_file}\n")
        sys.exit(1)

    convert_markdown_to_html(markdown_file, output_file)
    sys.exit(0)

if __name__ == '__main__':
    main()
