# Email Triage — Simple Social-Engineering Helper

A tiny, human-assisted Python triage tool that asks a few quick yes/no questions about an email and outputs a simple risk label (LOW / MEDIUM / HIGH). Purpose: help non-technical users or first responders decide if a message needs escalation.

## Usage
Run:
python3 email_triage.py
Answer the prompts (y/n). The script returns a numeric score and a risk label and then suggests quick next steps.

## Why this is useful
- Covers the most common social-engineering indicators (unknown sender, unexpected attachments, credential requests, urgency, and domain mismatch).
- Easy to explain and defend in interviews — each rule maps to industry-standard red flags.
