import os
import sys
from pathlib import Path
from google import genai

SYSTEM_PROMPT = """
You are an assistant that turns meeting notes into action items.

Instructions:
- Output a structured list of action items.
- For each item, include:
  1. Owner
  2. Task
  3. Deadline
  4. Notes
- Only include details clearly supported by the input.
- Do not invent missing names, dates, or conclusions.
- If information is unclear, write "unclear."
- If the notes contain sensitive, confidential, HR, or legal issues, add: "Human review recommended."
"""

def load_input(file_path: str) -> str:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")
    return path.read_text(encoding="utf-8")

def run_llm(notes: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Missing GEMINI_API_KEY environment variable.")

    client = genai.Client(api_key=api_key)

    prompt = f"""{SYSTEM_PROMPT}

Meeting notes:
{notes}

Convert these meeting notes into structured action items.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return response.text

def main():
    if len(sys.argv) < 2:
        print("Usage: py app.py <input_file>")
        sys.exit(1)

    notes = load_input(sys.argv[1])
    output = run_llm(notes)

    print("\n=== INPUT ===\n")
    print(notes)
    print("\n=== OUTPUT ===\n")
    print(output)

if __name__ == "__main__":
    main()