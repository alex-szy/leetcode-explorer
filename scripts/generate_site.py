import os
from jinja2 import Template

SOLUTION_DIR = "solutions"
OUTPUT_DIR = "build"
TEMPLATE_FILE = "scripts/template.html"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "index.html")


def parse_metadata(file_path):
    metadata = {
        "filename": os.path.basename(file_path),
        "code": "",
        "title": "",
        "link": "",
        "difficulty": "",
        "id": "",
        "tags": []
    }
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    start, end = None, -1
    for i, line in enumerate(lines):
        if line.startswith("# ID:"):
            metadata["id"] = line.split(":", 1)[1].strip()
        if line.startswith("# Title:"):
            metadata["title"] = line.split(":", 1)[1].strip()
        elif line.startswith("# Link:"):
            metadata["link"] = line.split(":", 1)[1].strip()
        elif line.startswith("# Difficulty:"):
            metadata["difficulty"] = line.split(":", 1)[1].strip()
        elif line.startswith("# Tags:"):
            metadata["tags"] = [tag.strip()
                                for tag in line.split(":", 1)[1].split(",")]
        elif line.startswith("class Solution") or not line.startswith("#") and start is None:
            start = i
        elif line.startswith("if __name__"):
            end = i
            break

    metadata["code"] = "".join(lines[start:end]).strip()
    return metadata


def main():
    entries = []
    for filename in os.listdir(SOLUTION_DIR):
        if filename.endswith(".py") and filename != "00-template.py":
            path = os.path.join(SOLUTION_DIR, filename)
            entries.append(parse_metadata(path))

    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template = Template(f.read())

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(template.render(entries=entries))


if __name__ == "__main__":
    main()
