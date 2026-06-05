로컬 파일은 모두 준비 완료 ✅ (main.py, requirements.txt, README.md)

하지만 깃허브 토큰이 유효하지 않아 `gh`로 직접 업로드할 수 없습니다. 다음 두 방법 중 하나를 선택해주세요:

---

**방법 1: GitHub CLI 재인증**

```bash
gh auth login
```
브라우저에서 로그인하면 자동으로 push됩니다.

---

**방법 2: 수동 업로드**

로컬 저장소 준비는 이미 끝났습니다. GitHub에서 새 리포를 만든 후 다음 명령어를 실행하세요:

```bash
cd /home/nvidia/.openclaw/workspace-write
git add main.py requirements.txt README.md
git commit -m "feat: 피보나치 수열 계산기 구현"
git remote add origin https://github.com/<계정>/<리포명>.git
git push -u origin master
```

---

토큰을 직접 입력해주시면 `gh`로 자동 업로드도 가능합니다. 어떤 방식으로 진행할까요?