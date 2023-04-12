from dataclasses import dataclass
from enum import IntFlag, auto
import typing


class FontVariantType(IntFlag):
    NONE = 0
    BOLD = auto()
    DOUBLE_STRUCK = auto()
    FRAKTUR = auto()
    ITALIC = auto()
    MATHEMATICAL = auto()
    MONOSPACE = auto()
    SANS_SERIF = auto()
    SCRIPT = auto()


@dataclass
class CharacterFontVariant:
    text: str
    kind: FontVariantType


class ParsedUnicodeData:
    def __init__(self):
        self.subscript_mapping: dict[str, str] = {}
        self.superscript_mapping: dict[str, str] = {}
        self.font_variants: dict[str, list[CharacterFontVariant]] = {}


def read_datafile() -> ParsedUnicodeData:
    result = ParsedUnicodeData()

    # TODO: Fix finding superscript alpha, iota, epsilon
    # Their fallbacks are listed as the "Latin" variants, meaning they aren't found
    # when looking for ^{\alpha} as it looks for the Greek variants
    with open("./UnicodeData.txt", encoding="utf-8") as f:
        for line in f:
            fields = line.split(";")
            assert len(fields) == 15

            codepoint = fields[0]
            name = fields[1]
            decomposition = fields[5]

            char = chr(int(codepoint, 16))

            if decomposition:
                # Help out mypy with redefinitions
                map_type: typing.Any
                basechars: typing.Any

                # print(f"{name} has decomposition {decomposition}")
                *map_type, basechars = decomposition.split(maxsplit=1)

                # We aren't looking for 2 -> 1 mappings, skip any that decompose to
                # multiple characters.
                basechars = basechars.split()
                if len(basechars) > 1:
                    continue

                basechar = chr(int(basechars[0], 16))

                assert len(map_type) < 2
                map_type = "".join(map_type)

                if map_type == "<super>":
                    # Intentionally overwrite if there's multiple
                    # Later unicode values tend to look more consistent with one another
                    result.superscript_mapping[basechar] = char

                elif map_type == "<sub>":
                    # Intentionally overwrite if there's multiple
                    result.subscript_mapping[basechar] = char

                elif map_type == "<font>":
                    variant = CharacterFontVariant(
                        char,
                        FontVariantType.MATHEMATICAL * ("MATHEMATICAL" in name)
                        | FontVariantType.BOLD * ("BOLD" in name)
                        | FontVariantType.DOUBLE_STRUCK * ("DOUBLE-STRUCK" in name)
                        | FontVariantType.FRAKTUR * (any(x in name for x in ["FRAKTUR", "BLACK-LETTER"]))
                        | FontVariantType.ITALIC * ("ITALIC" in name)
                        | FontVariantType.MONOSPACE * ("MONOSPACE" in name)
                        | FontVariantType.SANS_SERIF * ("SANS-SERIF" in name)
                        | FontVariantType.SCRIPT * ("SCRIPT" in name)
                    )

                    result.font_variants.setdefault(basechar, []).append(variant)

    # HACK: Fix up some missing mappings
    result.superscript_mapping["α"] = "ᵅ"
    result.superscript_mapping["ϵ"] = "ᵋ"
    result.superscript_mapping["ι"] = "ᶥ"
    result.superscript_mapping["ϕ"] = "ᶲ"

    # Planck's constant already fulfills this role, but isn't detected because it was added before
    # the Unicode standard had a group of mathematical variants
    result.font_variants["h"].append(
        CharacterFontVariant(
            text="\u210E",
            kind=FontVariantType.ITALIC | FontVariantType.MATHEMATICAL
        )
    )

    return result
