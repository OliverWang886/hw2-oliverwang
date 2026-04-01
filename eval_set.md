# Evaluation Set

## Case 1: Normal Case
**Input:**  
Team sync notes:
- Sarah will update the budget spreadsheet by Friday.
- David will schedule the client follow-up meeting next week.
- We need to finalize the slide deck before Monday.

**Good output should:**  
List the main action items clearly, assign owners correctly, and preserve the deadline details.

---

## Case 2: Normal Case
**Input:**  
Marketing meeting notes:
- Emma will draft the launch email.
- Jason will check the social media calendar.
- The team will review the campaign performance next Wednesday.

**Good output should:**  
Create concise action items and keep the timeline information.

---

## Case 3: Edge Case
**Input:**  
Quick standup notes:
- fix login page
- maybe ask design about button color
- report issue from yesterday still not solved

**Good output should:**  
Handle incomplete notes carefully, avoid inventing owners or deadlines, and clearly mark unclear items.

---

## Case 4: Human Review Case
**Input:**  
Meeting notes:
- We may need to let two contractors go next month depending on budget.
- Finance will confirm the numbers later.
- Keep this confidential for now.

**Good output should:**  
Summarize carefully, preserve uncertainty, avoid overconfident wording, and signal that sensitive content may require human review.

---

## Case 5: Failure-Prone Case
**Input:**  
Project review:
- The vendor promised delivery "soon."
- Someone should follow up on the missing documentation.
- Legal concerns were mentioned but not resolved.

**Good output should:**  
Avoid hallucinating names, dates, or legal conclusions. It should identify ambiguous items as unclear.