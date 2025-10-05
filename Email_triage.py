#!/usr/bin/env python3
# email_triage.py - tiny social-engineering triage (human-assisted)

def ask_yes(prompt):
    ans = input(prompt + " (y/n): ").strip().lower()
    return ans.startswith("y")

def main():
    print("Email Triage — answer quickly (y/n).")
    known_sender       = ask_yes("Is the sender known/trusted?")
    attachment         = ask_yes("Contains unexpected attachment?")
    link               = ask_yes("Contains a link you weren't expecting?")
    creds_request      = ask_yes("Does it ask for passwords/2FA/credentials?")
    urgent_language    = ask_yes("Uses urgent language (act now / immediate)?")
    odd_salutation     = ask_yes("Strange greeting or tone (not how sender usually writes)?")
    domain_mismatch    = ask_yes("Display name differs from sender's email domain?")

    # scoring weights chosen to reflect typical risk
    score = 0
    if not known_sender:     score += 3
    if attachment:           score += 4
    if link:                 score += 2
    if creds_request:        score += 5
    if urgent_language:      score += 1
    if odd_salutation:       score += 1
    if domain_mismatch:      score += 2

    if score >= 8:
        risk = "HIGH RISK — very likely social-engineering"
    elif score >= 4:
        risk = "MEDIUM RISK — suspicious, verify before clicking"
    else:
        risk = "LOW RISK — likely OK but stay cautious"

    print("\n--- TRIAGE RESULT ---")
    print(f"Score: {score}   => {risk}")
    print("Quick next steps:")
    if score >= 4:
        print("- DO NOT click links or open attachments.")
        print("- Verify sender by calling them or messaging via a known channel.")
    else:
        print("- If unsure, verify via separate channel; otherwise safe to proceed carefully.")
    print("---------------------")

if __name__ == "__main__":
    main()
