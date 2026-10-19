# Setup: run the starter in your own account

1. **Clone and validate.**

   ```bash
   git clone https://github.com/kortix-ai/ai-employee-starter
   cd ai-employee-starter
   python3 scripts/check_roles.py
   kortix validate
   ```

2. **Connect the tools.** In `kortix.yaml`, keep only the connectors you have: `gmail`, `hubspot`,
   `slack` and the `http` connector to your own OpenAPI document are declared here. A connector an
   agent is granted but the project does not declare fails validation.

3. **Ship it.**

   ```bash
   kortix ship
   ```

4. **Start a session.** In the Kortix app, open the project and start a session with
   `@support-triage`. The first run reads the queue; a send waits for your approval in the thread.

## What "the employee" is, technically

The role is a markdown file. The permissions are `kortix.yaml`. Each session boots an isolated cloud
computer with the repo on it, so the employee can read and run the project without touching your
laptop. Work that lands comes back as a change request you read as a diff.

## Next

- [The approval policy, line by line](02-approval-policy.md)
