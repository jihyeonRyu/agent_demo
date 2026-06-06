# OpenClaw Demo Prompt

Use this prompt during the GitHub issue-repair demo.

```text
Repo: https://github.com/jihyeonRyu/agent_demo
Issue: https://github.com/jihyeonRyu/agent_demo/issues/1

Open the GitHub issue and fix it end to end.

1. Research: read the issue and summarize the expected behavior.
2. Code: inspect issue-repair-demo, add a regression test for CSV input without a trailing newline, run the test to reproduce the failure, patch the parser, and rerun the full test suite.
3. Writer: write a PR title and concise PR description explaining the bug, root cause, test, and fix.
4. Screen: show the GitHub issue, the failing regression test, the code change, the passing pytest output, and the PR summary.

Do not read or print any .env file values.
```

## Presenter Notes

This repo intentionally starts with passing tests while still containing the issue #1 edge-case bug. The demo is strongest when the agent first creates a failing regression test, then makes it pass.
