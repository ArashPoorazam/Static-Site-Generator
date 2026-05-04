# Static-Site-Generator
Render Markdown files into a static HTML files, written in Python.

# Requirements

- Python 3.12+

# Run Local Server

    $ ./main.sh

# Run Tests
    $ ./test.sh

    Run file individually:
    
    $ python3 src/<file name>.py    # No unittest in the commmand

# Limitations
- Markdown must be valid
    - Code blocks cannot have blank lines
    - No nested Markdown
