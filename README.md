# LaTeX-Unicode-Map
An attempt at mapping as many LaTeX special characters as possible to Unicode characters.  

This is done in 2 ways:
1. Parsing the UnicodeData.txt file and finding font variants of the characters
2. Maintaining a large list of LaTeX symbols and their Unicode equivalents

## Usage
Run generate.py, which will populate the output folder with the generated output files.
- `symbols.txt` contains the mapping of LaTeX symbol names to Unicode characters
- `superscript.txt` contains the mapping of characters to their superscript equivalents
- `subscript.txt` contains the mapping of characters to their subscript equivalents
- `math{...}.txt` contains the mapping of characters to their math font variants (bold, italic, caligraphic, blackboard bold, sans-serif, etc.)