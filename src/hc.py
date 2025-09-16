import re
import sys
import subprocess
import json
from pathlib import Path

# Devanagari Unicode block for identifiers
IDENT_START = r"[A-Za-z_\u0900-\u097F]"
IDENT_CONT = r"[A-Za-z0-9_\u0900-\u097F]"

token_re = re.compile(
    r'"([^"\\]|\\.)*"'   # string literals
    r"|\'([^'\\]|\\.)*\'"  # char literal
    r"|//.*?$"  # line comment
    r"|/\*.*?\*/"  # block comment
    r"|" + IDENT_START + IDENT_CONT + r"*"  # identifiers
    r"|\s+"  # whitespace
    r"|.",  # everything else
    re.DOTALL | re.MULTILINE,
)


def load_map(json_file="hindi.json"):
    with open(json_file, "r", encoding="utf-8") as f:
        return json.load(f)


def translate_code(code, mapping, devanagari=True):
    if not devanagari:
        mapping = {v: k for k, v in mapping.items()}

    out_parts = []
    for m in token_re.finditer(code):
        tok = m.group(0)
        if re.fullmatch(IDENT_START + IDENT_CONT + r"*", tok) or (
            not devanagari and re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", tok)
        ):
            out_parts.append(mapping.get(tok, tok))
        else:
            out_parts.append(tok)
    return "".join(out_parts)


def remove_map_include(code):
    return re.sub(r'^\s*#include\s+"hindi\.h"\s*\n?', "", code, flags=re.MULTILINE)


def rename_devanagari_identifiers(code):
    identifier_map = {}
    var_counter = 1
    func_counter = 1

    out_parts = []
    for m in token_re.finditer(code):
        tok = m.group(0)
        if tok.startswith('"') or tok.startswith("'") or tok.startswith("//") or tok.startswith("/*"):
            out_parts.append(tok)
        elif re.fullmatch(IDENT_START + IDENT_CONT + r"*", tok):
            if re.search(r"[\u0900-\u097F]", tok):
                next_index = m.end()
                is_func = code[next_index:].lstrip().startswith("(")
                if tok not in identifier_map:
                    if is_func:
                        identifier_map[tok] = f"f{func_counter}"
                        func_counter += 1
                    else:
                        identifier_map[tok] = f"var{var_counter}"
                        var_counter += 1
                out_parts.append(identifier_map[tok])
            else:
                out_parts.append(tok)
        else:
            out_parts.append(tok)

    return "".join(out_parts)


def main():
    if len(sys.argv) < 2:
        print("Usage: python hc.py file.c [!suppress] [!preserve]")
        sys.exit(1)

    src = Path(sys.argv[1])
    silent = "!suppress" in sys.argv
    preserve = "!preserve" in sys.argv

    if not src.exists():
        print(f"Error: input file not found: {src}")
        sys.exit(1)

    mapping = load_map()

    if src.stem.startswith("_"):
        out_file = Path("a.c")
        exe_file = Path("a.exe")

        code = src.read_text(encoding="utf-8")
        code = remove_map_include(code)
        translated = translate_code(code, mapping, devanagari=True)
        translated = rename_devanagari_identifiers(translated)  # second pass

        out_file.write_text(translated, encoding="utf-8")
        if not silent:
            print(f"Translated {src} → {out_file}")

        gcc_cmd = ["gcc", str(out_file), "-o", str(exe_file)]
        if not silent:
            print("Compiling", " ".join(gcc_cmd))
        try:
            subprocess.run(gcc_cmd, check=True)
            if exe_file.exists() and not silent:
                print(f"Compiled {exe_file}")
            if not preserve:
                out_file.unlink()
                if not silent:
                    print(f"Deleted intermediate file: {out_file}")
        except subprocess.CalledProcessError as e:
            print("GCC failed with exit code", e.returncode)
            sys.exit(e.returncode)
    else:
        out_file = src.with_name("_" + src.stem + ".c")
        code = src.read_text(encoding="utf-8")
        translated = translate_code(code, mapping, devanagari=False)
        translated = '#include "hindi.h"\n\n' + translated
        out_file.write_text(translated, encoding="utf-8")
        if not silent:
            print(f"Converted {src} → {out_file} (Hindi C)")


if __name__ == "__main__":
    main()
