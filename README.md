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
- `math{...}.txt` contains the mapping of characters to their math font variants (bold, italic, caligraphic¹, blackboard bold, sans-serif, etc.)


## Copyright
The UnicodeData.txt file is © 1991-2015 Unicode, Inc. and is licensed under the [Unicode License](http://www.unicode.org/license.html).
The unicode-math-table.tex file is © 2019 Will Robertson and is licensed under the LPPL v1.3c or later.

---

¹ Unicode does not make a large distinction between caligraphic and script forms. The Unicode reference refers to the characters as SCRIPT font variants, but the capital characters resemble `\mathcal{}` and the lowercase resemble `\mathscr{}`.

