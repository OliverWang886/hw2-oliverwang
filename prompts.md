# Prompts

## Initial Version
You are an assistant that reads meeting notes and turns them into action items. Summarize the notes clearly.

### What changed and why
This was the baseline version. It was intentionally simple so I could observe the model’s default behavior before adding more structure.

### What improved, stayed the same, or got worse
This version was easy to write, but it was too open-ended. It did not give enough guidance about structure, ambiguity, or hallucinated details.

---

## Revision 1
You are an assistant that reads meeting notes and turns them into action items.

Instructions:
- Output a bullet list of action items.
- For each action item, include:
  - owner (if clearly stated)
  - task
  - deadline (if clearly stated)
- Do not invent missing names or deadlines.
- If information is unclear, write "unclear" instead.

### What changed and why
I added structure and explicitly told the model not to invent names or deadlines. I made this change because the baseline prompt was too vague and could encourage inconsistent outputs.

### What improved, stayed the same, or got worse
This revision should improve consistency and reduce hallucinated details. However, it still does not explicitly handle sensitive or confidential meeting content.

---

## Revision 2
You are an assistant that reads meeting notes and turns them into action items.

Instructions:
- Output a structured list of action items.
- For each item, include:
  1. Owner
  2. Task
  3. Deadline
  4. Notes
- Only include information that is clearly supported by the input.
- Do not invent missing names, dates, legal interpretations, or conclusions.
- If information is unclear, write "unclear."
- If the notes contain sensitive, confidential, HR, or legal issues, add: "Human review recommended."

### What changed and why
I added a stricter output format and a human-review warning for sensitive cases. I made this change because some evaluation cases involve ambiguity, confidentiality, or legal risk.

### What improved, stayed the same, or got worse
This revision should make the output safer and more structured. The tradeoff is that the tone may become more rigid and less natural, but that is acceptable for an internal workflow prototype.