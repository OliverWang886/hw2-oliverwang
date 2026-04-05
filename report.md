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
I built a Python prototype that reads meeting notes from a text file and sends them to the Gemini API to generate structured action items. The script runs from the command line and makes a real LLM API call.

During development, I encountered several issues, including model selection problems and free-tier quota limits. After updating the model choice and enabling billing, the prototype was able to successfully return structured action items from the Gemini API.

This means the final prototype successfully demonstrated the intended workflow: reading an input file, sending the content to a live LLM API, and returning a structured output that could support a business writing task.

## Remaining Failure Modes
This prototype still has important limitations. If the notes are vague, incomplete, or politically sensitive, the model may still produce output that appears cleaner or more certain than the source text justifies. It also depends on live API access, which means reproducibility can be affected by quota availability.

The workflow should not be trusted without human review in cases involving HR decisions, legal issues, confidential topics, or unclear ownership and deadlines. Even in normal cases, a human should verify the generated action items before sharing or acting on them.

## Deployment Recommendation
I would recommend deploying this workflow only as a draft-generation tool, not as a fully automated system. It can be useful for internal productivity if a human reviewer checks the output before it is used.

The prototype performs well on simple meeting-note cases, but it still requires human review for vague, incomplete, confidential, HR-related, or legally sensitive content. In a real deployment setting, the system would also need clear review procedures and monitoring for output quality.