# Week 2 Report

## Business Use Case
This project explores a simple GenAI workflow for turning meeting notes into action items. The target user is a project manager, team lead, or operations coordinator who needs to review written meeting notes and quickly identify next steps.

The system takes plain-text meeting notes as input and produces a structured list of action items. The goal is not to replace human judgment, but to create a useful first draft that saves time and improves consistency.

## Model Choice
I used the Gemini API because Google AI Studio was the recommended default in the assignment instructions, and it provided a simple way to connect a real LLM API to a small Python script. I focused on building a reproducible prototype rather than optimizing for the most advanced model.

## Baseline vs. Final Design
The baseline design used a very simple prompt that asked the model to turn meeting notes into action items. This version was too open-ended and did not provide enough instructions about structure, ambiguity, or unsupported details.

In Revision 1, I added a clearer output structure and instructed the model not to invent missing names or deadlines. This change was intended to reduce hallucinated details and improve consistency across the evaluation set.

In Revision 2, I added an even more structured format and a human-review warning for sensitive, confidential, HR, or legal content. This made the workflow safer for edge cases and more realistic for internal business use.

## Evaluation and Prompt Iteration
I created a small evaluation set with five representative inputs, including normal cases, an edge case, and a sensitive case requiring human review. The purpose of the evaluation set was to test not only whether the model could summarize routine meeting notes, but also whether it would behave more carefully when the notes were incomplete, ambiguous, or risky.

The prompt iterations improved the design in three ways. First, they made the output more structured. Second, they reduced the chance of unsupported details being added. Third, they made the workflow more cautious in situations where human review would still be necessary.

## Current Prototype Status
I built a Python prototype that reads meeting notes from a text file and sends them to the Gemini API to generate structured action items. The script runs from the command line and is designed to make a real LLM API call.

During testing, the script successfully reached the live API call stage, but repeated testing hit the free-tier quota and rate limit. This produced a 429 RESOURCE_EXHAUSTED error. As a result, the prototype demonstrated the intended technical workflow, but output generation was not always consistently available under the free-tier constraints.

## Remaining Failure Modes
This prototype still has important limitations. If the notes are vague, incomplete, or politically sensitive, the model may still produce output that appears cleaner or more certain than the source text justifies. It also depends on live API access, which means reproducibility can be affected by quota availability.

The workflow should not be trusted without human review in cases involving HR decisions, legal issues, confidential topics, or unclear ownership and deadlines. Even in normal cases, a human should verify the generated action items before sharing or acting on them.

## Deployment Recommendation
I would recommend deploying this workflow only as a draft-generation tool, not as a fully automated system. It could be useful for internal productivity if a human reviewer checks the output before it is used.

In a real deployment setting, the system would need more stable API quota access, clearer review procedures, and stronger controls for sensitive cases. Without those safeguards, I would not recommend relying on it as a final decision-making tool.