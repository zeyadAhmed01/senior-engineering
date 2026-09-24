# Clarification Protocol

Use this protocol when a material UNKNOWN prevents part of the requested workflow.

## Ask before affected work

- Ask every currently known material question before inspecting, deciding, or changing anything that depends on its answer.
- Use the structured clarification interface when available. Ask one to three short questions, offer two or three mutually exclusive choices, put the recommended choice first, and leave room for a free-form answer.
- Prefer the asynchronous question interface when available so independent work can continue. A successful return means only that the question was presented; it does not mean the user answered or that the interaction is waiting.

## Continue independent work

- After asking, continue parts of the request that do not depend on the answer.
- Keep answer-dependent inspection, decisions, and changes paused. If the user replies while other work is underway, incorporate the answer and continue without asking the same question again.
- If the answer creates a new material UNKNOWN, ask about it before doing the newly affected work.

## Wait when the answer is the only blocker

- Start a 30-minute deadline when the question is presented.
- Once no independent work remains and the next step depends on the answer, explicitly wait with `clock.sleep` for the remaining time, up to the 30-minute deadline. Do not end the response after presenting the question or assume the asynchronous question call keeps the interaction open.
- A new user message interrupts the wait. Treat it as the answer, resolve the clarification, and resume the task. If independent work used part of the deadline, wait only for the remaining time.
- If the structured async interface is unavailable, ask one concise consolidated question and follow the same independent-work and wait rules.
- If the current surface has no tool that can wait for user input, state that limitation plainly. Do not claim the interaction will stay open when it cannot.
