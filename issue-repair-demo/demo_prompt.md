# OpenClaw Demo Prompt

Use this prompt during the GitHub issue-repair demo.

```text
내 GitHub repo의 열린 issue 하나를 골라서 Code와 Validator가 협업하는 방식으로 고쳐줘. Code는 issue를 읽고 증상을 재현하는 실패 테스트를 먼저 추가한 뒤 pytest 실패를 보여주고, Validator는 그 실패가 issue 증상과 맞는지 검증해서 수정 기준을 제시해줘. 그 다음 Code가 원인을 고치고 테스트를 다시 통과시키면, Validator가 최종 검증 후 PR 제목과 설명 초안을 승인해줘. 마지막으로 Screen은 GitHub issue, Code와 Validator의 대화 transcript, 수정 코드, 테스트 결과, PR 초안을 실제 Chromium 새 창으로 보여줘.
```

## Demo Context

- Repo: https://github.com/jihyeonRyu/agent_demo
- Issue: https://github.com/jihyeonRyu/agent_demo/issues/1
- Local project: `/home/nvidia/agent_demo/issue-repair-demo`
- Result URL: http://127.0.0.1:7878/demo-artifacts/issue-repair/issue_repair_dialogue.html

## Intended Agent Flow

Code first adds a regression test for CSV input without a trailing newline and confirms pytest fails. Validator then checks that the failure matches the issue. Code fixes the parser and reruns pytest. Validator approves the final result and PR draft. Screen opens the GitHub issue and the result HTML in real Chromium new windows.

Do not read or print any `.env` file values.
