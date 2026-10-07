# ChronoExtract 

A tiny command-line tool that pulls the main historical events for any era or topic you throw at it and spits them out in clean, chronological order using OpenAI's Structured Outputs and Pydantic.

I built this to play around with modern schema-enforced AI responses instead of dealing with messy, unpredictable raw text parsing. 

## What it does
- Takes any historical topic directly from your terminal.
- Enforces a strict Pydantic model so the AI *has* to return data cleanly structured into names and dates.
- Prints out a neat, chronological timeline straight to your console.

## Getting Started

### 1. Clone the repo
```bash
git clone [https://github.com/kvasken/chrono-extract.git](https://github.com/kvasken/chrono-extract.git)
cd chrono-extract