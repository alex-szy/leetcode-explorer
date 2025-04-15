import os
from jinja2 import Template
from typing import Dict

SOLUTION_DIR = "solutions"
OUTPUT_DIR = "build"
TEMPLATE_FILE = "scripts/template.html"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "index.html")


def parse_metadata(file_path: str) -> Dict:
    metadata = {
        "Title": "",
        "Link": "",
        "Difficulty": "",
        "ID": "",
        "Tags": []
    }

    COMMENT_STR = {
        "java": "//",
        "c": "//",
        "cpp": "//",
        "py": "#"
    }

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except:
        print("Error parsing file:", file_path, "- skipped")
        return None

    ext = file_path.split(".")[-1]
    if ext not in COMMENT_STR:
        print("Unsupported file:", file_path, "- skipped")
        return None

    c = COMMENT_STR[ext]

    start, end = None, None
    for i, line in enumerate(lines):
        if line.startswith(c):
            fields = line.removeprefix(c).lstrip().split(":", 1)
            if len(fields) != 2:
                continue
            field, data = fields
            template = metadata.get(field)
            if isinstance(template, list):
                metadata[field] = [tag.strip()
                                   for tag in data.split(",")]
            elif isinstance(template, str):
                metadata[field] = data.strip()
        elif line.startswith("class Solution") or start is None:
            start = i
        elif line.startswith("if __name__"):
            end = i
            break

    for value in metadata.values():
        if not value:
            return None

    metadata["code"] = "".join(lines[start:end]).strip()
    return metadata


def main():
    entries = []
    for filename in os.listdir(SOLUTION_DIR):
        path = os.path.join(SOLUTION_DIR, filename)
        metadata = parse_metadata(path)
        metadata and entries.append(metadata)

    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template = Template(f.read())

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(template.render(entries=entries))


if __name__ == "__main__":
    main()
