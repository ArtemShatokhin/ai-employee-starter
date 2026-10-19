# The approval policy, line by line

The `policy` and `policies` keys decide what a connector call may do. The reference:
<https://kortix.com/docs/project/manifest>.

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

- `default_mode` is `allow_all` or `risk`. With `risk`, a call no rule matches is not run
  unattended. **Approval gates are off until you set them**, so a new project should set this first.
- `match` is a glob over tool names.
- `action` is one of `always_run`, `require_approval` or `block`.
- `conditions` narrows a rule to calls whose arguments match, for example `arg: to` with a glob or a
  regex.

## Order matters

The first matching rule wins, so the specific rules go above the catch-all. In this repo:

1. `*` → `block` is the fallback.
2. `*.read_*` and `*.list_*` → `always_run`.
3. `*.send_*`, `*.create_contact`, `*.update_deal` → `require_approval`.
4. `*.delete_*` → `block`.

## Reviewing a change

Because the policy is a file, a change to it is a pull request. A reviewer sees which tool a role
gains, which argument the rule now allows, and can revert the commit if the answer is wrong.

## Checking the roles

`python3 scripts/check_roles.py` walks `kortix.yaml` and fails when an agent has no `require_approval`
or `block` rule covering its writing calls. Run it in CI before `kortix validate`.
