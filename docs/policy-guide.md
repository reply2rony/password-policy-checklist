# Password Policy Guide (starter)

This guide explains each checklist item in plain language. It is a
learning template for a small-office IT review, not a compliance
standard, and it replaces no legal, audit, or vendor requirement.

## The checklist items

1. **Minimum length** — longer passwords are harder to guess. The
   sample recommends at least 12 characters for staff accounts.
2. **Multi-factor authentication (MFA)** — a second factor (app code
   or hardware key) so a leaked password alone is not enough.
3. **Password reuse** — the same password must not be reused across
   work systems. A password manager helps staff keep unique ones.
4. **Password change on suspicion** — if an account may be
   compromised, change that password at once; routine forced expiry
   alone is not a security fix.
5. **Shared accounts** — avoid shared logins where possible, so
   access can be traced to one person and removed when they leave.
6. **Leaver process** — when someone leaves, disable their accounts
   promptly and check the shared-account list.
7. **Admin accounts** — admin rights only for staff who need them,
   with a separate admin account from the everyday account.
8. **Password storage** — passwords are never written in plain text
   in documents, chats, or spreadsheets. Systems must store only a
   salted hash, never a readable password.
9. **Lockout / throttling** — after repeated failed sign-ins, the
   account or sign-in is temporarily slowed or locked, to slow down
   guessing.
10. **Staff awareness** — a short reminder, once a quarter, on
    phishing, MFA, and reporting a suspected compromise.

## Quarterly review routine

1. Go through the checklist row by row and mark each rule Met,
   Partial, or Missing for your own policy.
2. For every Missing or Partial row, write one action, one owner,
   and one date.
3. Run `python scripts/policy-check.py` and compare its summary
   with your own marks.
4. Update the checklist and file it with the date of the review.

## What this template never does

- It never asks for, stores, or checks a real password.
- It never describes a real employer's policy or systems.
- It never claims compliance with any standard.
