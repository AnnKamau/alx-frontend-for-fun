#!/usr/bin/python3
"""
Takes an argument 2 strings
"""
import sys
import os
import markdown
"""
Markdown

    Arguments:
    First argument is the name of the Markdown file
    Second argument is the output file name

    Return:
    If the number of arguments is less than 2: print in STDERR Usage: ./markdown2html.py README.md README.html and exit 1
    If the Markdown file doesn’t exist: print in STDER Missing <filename> and exit 1
    Otherwise, print nothing and exit 0
"""

if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

md_file = sys.argv[1]
html_file = sys.argv[2]

if not os.path.exists(md_file):
    print(f"Missing {md_file}", file=sys.stderr)
    sys.exit(1)

with open(md_file, 'r') as f:
    markdown_text = f.read()

html_text = markdown.markdown(markdown_text)

with open(html_file, 'w') as f:
    f.write(html_text)
