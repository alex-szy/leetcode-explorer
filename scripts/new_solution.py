import os
import re
import requests


def slug_from_url(url):
    match = re.search(r"/problems/([^/]+)/?", url)
    return match.group(1) if match else None


def fetch_problem_metadata(slug):
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }
    query = {
        "query": """
            query getQuestionDetail($titleSlug: String!) {
                question(titleSlug: $titleSlug) {
                    questionId
                    title
                    difficulty
                    topicTags { name }
                    codeSnippets { lang langSlug code }
                }
            }
        """,
        "variables": {"titleSlug": slug}
    }

    response = requests.get("https://leetcode.com/graphql",
                            headers=headers, json=query)
    response.raise_for_status()
    return response.json()["data"]["question"]


def create_solution_file(metadata, slug):
    id = metadata["questionId"]
    title = metadata["title"]
    difficulty = metadata["difficulty"]
    tags = [tag["name"] for tag in metadata["topicTags"]]
    link = f"https://leetcode.com/problems/{slug}/"

    # Get the Python3 starter code
    code_snippet = next(
        (snippet["code"] for snippet in metadata["codeSnippets"]
         if snippet["langSlug"] == "python3"),
        "# Solution not available in Python3"
    )

    filename = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "solutions", f"{id.zfill(2)}-{slug.replace("-", "_")}.py")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# ID: {id}\n")
        f.write(f"# Title: {title}\n")
        f.write(f"# Link: {link}\n")
        f.write(f"# Difficulty: {difficulty}\n")
        f.write(f"# Tags: {', '.join(tags)}\n\n")
        f.write(code_snippet + "\n")

    return filename


def generate_from_url(url):
    slug = slug_from_url(url)
    if not slug:
        print("Invalid LeetCode problem URL.")
        return

    print(f"Fetching metadata for: {slug}")
    metadata = fetch_problem_metadata(slug)
    path = create_solution_file(metadata, slug)
    print(f"✅ Solution file created at: {path}")


if __name__ == "__main__":
    url = input("Paste the url of the question you want to solve: ")
    generate_from_url(url)
