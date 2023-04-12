from pathlib import Path
from read_unicodedata import read_datafile, FontVariantType
from read_unicode_tex import read_texfile
from symbols import latex_symbols


def main():
    script_path = Path(__file__).parent
    output_path = script_path / "output"
    output_path.mkdir(exist_ok=True)

    data = read_datafile()
    superscripts = data.superscript_mapping
    subscripts = data.subscript_mapping

    write_to_file(output_path / "superscripts.txt", superscripts)
    write_to_file(output_path / "subscripts.txt", subscripts)

    font_variants = data.font_variants

    variants = {
        "mathbb": FontVariantType.DOUBLE_STRUCK | FontVariantType.MATHEMATICAL,
        "mathbf": FontVariantType.BOLD | FontVariantType.MATHEMATICAL,
        "mathbfcal": FontVariantType.BOLD | FontVariantType.SCRIPT | FontVariantType.MATHEMATICAL,
        "mathbfit": FontVariantType.BOLD | FontVariantType.ITALIC | FontVariantType.MATHEMATICAL,
        "mathbffrak": FontVariantType.BOLD | FontVariantType.FRAKTUR | FontVariantType.MATHEMATICAL,
        "mathbfsfit": FontVariantType.BOLD | FontVariantType.SANS_SERIF | FontVariantType.ITALIC | FontVariantType.MATHEMATICAL,
        # The difference between calligraphic and script types is not emphasized in Unicode, one could argue that this
        # should be named mathscr instead (especially because of the forms of the lowercase characters) but I will
        # leave it as is.
        "mathcal": FontVariantType.SCRIPT | FontVariantType.MATHEMATICAL,
        "mathfrak": FontVariantType.FRAKTUR | FontVariantType.MATHEMATICAL,
        "mathit": FontVariantType.ITALIC | FontVariantType.MATHEMATICAL,
        "mathsf": FontVariantType.SANS_SERIF | FontVariantType.MATHEMATICAL,
        "mathsfbfit": FontVariantType.SANS_SERIF | FontVariantType.BOLD | FontVariantType.ITALIC | FontVariantType.MATHEMATICAL,
        "mathsfit": FontVariantType.SANS_SERIF | FontVariantType.ITALIC | FontVariantType.MATHEMATICAL,
        "mathtt": FontVariantType.MONOSPACE | FontVariantType.MATHEMATICAL,
    }

    for name, matches in variants.items():
        write_to_file(
            Path(output_path / f"{name}.txt"),
            {k: x.text for k, v in font_variants.items() for x in v if x.kind == matches}
        )

    tex_data = read_texfile()

    # Now, we need to add the symbols that are not in the tex file
    for key, value in latex_symbols.items():
        if key not in tex_data:
            tex_data[key] = value

    write_to_file(
        Path(output_path / "symbols.txt"),
        tex_data
    )


def write_to_file(path: Path, data: dict[str, str]):
    with path.open("w", encoding="utf-8") as f:
        for key, value in data.items():
            f.write(f"{key}={value}\n")


if __name__ == "__main__":
    main()
