import re


def read_texfile() -> dict[str, str]:
    """
    Reads the unicode-math-table.tex file and returns a dictionary of mappings from symbol name to unicode character.
    """
    line_regex = re.compile(
        r"\\UnicodeMathSymbol\{\"(?P<codepoint>[^}]+)\}\{\\(?P<name>[^}\ ]+)"
    )

    result = {}
    with open("./unicode-math-table.tex", encoding="utf-8") as f:
        for line in f:
            if m := line_regex.match(line):
                result[m["name"]] = chr(int(m["codepoint"], 16))

    return result
