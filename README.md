# Open-source AI employee starter

Open source. An AI employee you can deploy from a repo: three roles, each with a real
`kortix.yaml` policy that sets every connector call to allow, require approval, or block.

This starter is meant to be forked. It runs on [Kortix](https://kortix.com), the open-source AI
Operating System, and it is the code behind
[opensourceaiemployee.com](https://opensourceaiemployee.com).

## What is in here

| Path | What it is |
| --- | --- |
| `kortix.yaml` | The manifest: three agents, their connector grants, and the approval policies. |
| `agents/support-triage.md` | A support-triage employee: classify, draft, and stop at refunds. |
| `agents/sales-ops.md` | A sales-ops employee: enrich the lead, update the CRM, hold the send. |
| `agents/research-brief.md` | A research employee: gather sources, write the brief, link every claim. |
| `scripts/check_roles.py` | A validator: fails when a role has no approval rule for its writing calls. |
| `docs/` | Setup, approval policy, the comparison with hosted AI employees, and FAQ. |

## Run it

```bash
git clone https://github.com/kortix-ai/ai-employee-starter
cd ai-employee-starter
python3 scripts/check_roles.py          # every writing call has a policy
kortix validate                          # the manifest against the published schema
kortix ship                              # push the project to your Kortix account
```

`kortix validate` exits 0 with no errors and 1 with one or more. It reads the schema from
`https://kortix.com/schema/kortix.v2.schema.json`, so an unknown key fails before anything runs.

## The three roles

| Role | Reads | Writes | Stops for a person |
| --- | --- | --- | --- |
| `support-triage` | Help desk, docs, the customer thread | Ticket labels, reply drafts | Any refund, any send to a customer |
| `sales-ops` | Inbox, CRM, the lead list | CRM fields, email drafts | Every outbound email |
| `research-brief` | Web pages, the source notes | The brief, the source table | Publishing the brief outside the team |

## Where the rules live

The role is a markdown file in `agents/`. The permissions are in `kortix.yaml`. Both are in git, so a
change to what an employee may do is a diff someone reviews — and reverts the same way.

```yaml
policy:
  default_mode: risk
policies:
  - match: "*"
    action: block
  - match: "*.read_*"
    action: always_run
  - match: "*.send_*"
    action: require_approval
```

`default_mode: risk` is the safe default: a connector call that no rule matches is not run
unattended. Read the policy reference in [docs/02-approval-policy.md](docs/02-approval-policy.md).

## Docs

- [Setup](docs/01-setup.md)
- [The approval policy, line by line](docs/02-approval-policy.md)
- [Hosted AI employees vs an employee you own](docs/03-vs-hosted-ai-employees.md)
- [FAQ](docs/04-faq.md)

## More

- Product: <https://kortix.com>
- Docs: <https://kortix.com/docs>
- The site this repo supports: <https://opensourceaiemployee.com>
