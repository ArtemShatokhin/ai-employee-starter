# FAQ

**Is this open source?**
Yes. This starter is open source and runs on Kortix, the open-source AI Operating System.

**Do I need to self-host?**
No. Kortix runs on Kortix Cloud, in your VPC, or on your own on-prem network. The repo is the same in
all three.

**Which models can the employees use?**
Any major provider, per agent, per session or per message, with your own API keys.

**Can an employee send email without me?**
Not with this policy: `*.send_*` is `require_approval`, so the call waits for a person. Remove the
rule deliberately if you want otherwise — that is a diff in the repo, not a toggle in a vendor
console.

**How is this different from a prompt pack?**
A prompt pack gives you the instructions. This repo also ships the manifest, the connector grants and
the approval policy, and `scripts/check_roles.py` fails when a role's writing calls have no rule.

**Where do I start?**
[Setup](01-setup.md), then read the policy in [02-approval-policy.md](02-approval-policy.md).
