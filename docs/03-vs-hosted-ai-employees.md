# Hosted AI employees vs an employee you own

Both shapes give you a role: a named worker that reads context, calls tools and reports back. The
difference is where the role, the memory and the approval rules live.

| | This starter (Kortix) | Hosted AI employee vendors |
| --- | --- | --- |
| Where the role is defined | `agents/<role>.md` in your repo | The vendor's console |
| Where the memory lives | Files in your repo | The vendor's platform |
| Approval rules | `policy` / `policies` in `kortix.yaml`, per tool and per argument | The vendor's approval settings |
| Who reviews a change to the rules | A pull request in your repo | The vendor's UI history |
| Where it runs | Kortix Cloud, your VPC, or on-prem | The vendor's cloud |
| Model choice | Any model, your own API keys | The vendor's model |

## When a hosted employee is the better buy

If you want a vendor to run the whole role — onboarding, tuning and support — and you have no
platform team, a hosted plan is simpler. You trade control for someone else's operations.

## When this starter is the better buy

If a security review has to read the rules before the employee touches a customer record, or if you
need the memory to survive a change of model vendor, keep the role in your repo.
