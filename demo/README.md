Here's a thinking process:

1.  **Analyze User Input:**
   - **Language:** Korean
   - **Format:** Markdown (`README.md`)
   - **Sections Required:** `# 제목`, `## 개요`, `## 사용법` (specifically `python main.py`), `## 핵심 구현`
   - **Constraint:** Base it ONLY on the provided files and run output. Do not invent.
   - **Request:** "팩토리얼 계산기를 파이썬으로 구현해서 깃허브에 올려줘" (Implement a factorial calculator in Python and upload to GitHub)
   - **Provided Files:** `main.py` with comments and code
   - **Run Output:** `팩토리얼 계산기: python main.py <정수>`

2.  **Extract Key Information from `main.py`:**
   - Uses `math.factorial` for efficient calculation.
   - Uses `sys.argv` for CLI input handling.
   - Uses `try-except` for validation (handles negative numbers and non-integers).
   - Prints usage message if no argument is provided.
   - Output format: `n! = result`
   - Error messages: "음수는 입력할 수 없습니다.", "정수만 입력해주세요."

3.  **Map to Required Sections:**
   - `# 제목`: Needs a title. Based on the request, something like `# 팩토리얼 계산기` or `# Python 팩토리얼 CLI 계산기` works. I'll stick to `# 팩토리얼 계산기`.
   - `## 개요`: Briefly describe what the project does based on the code. It's a CLI tool that calculates factorials using Python's `math` module, handles CLI arguments, and validates input.
   - `## 사용법`: Must include `python main.py`. Show how to run it, give examples based on the code/output.
   - `## 핵심 구현`: List the key implementation points directly from the comments/code: `math.factorial` for efficiency, `sys.argv` for CLI, `try-except` for validation.

4.  **Draft - Section by Section (Mental Refinement in Korean):**
   *# 제목*
   # 팩토리얼 계산기

   *## 개요*
   명령줄 인터페이스(CLI) 기반의 팩토리얼 계산 도구입니다. Python 내장 `math` 모듈을 활용하여 효율적으로 계산을 수행하며, 사용자 입력에 대한 유효성 검증을 통해 안정적으로 동작합니다.

   *## 사용법*
   ```bash
   python main.py <정수>
   ```
   - 인자를 입력하지 않으면 사용법이 출력됩니다.
   - 예시: `python main.py 5` → `5! = 120`
   - 음수 또는 정수가 아닌 값 입력 시 오류 메시지가 표시됩니다.

   *## 핵심 구현*
   - `math.factorial` 함수를 사용하여 효율적인 팩토리얼 계산
   - `sys.argv`를 활용한 CLI 인자 처리
   - `try-except` 블록을 통한 입력값 유효성 검증 (음수 및 비정수 처리)

5.  **Check Constraints:**
   - Concise? Yes.
   - Korean? Yes.
   - Markdown? Yes.
   - Sections: `# 제목`, `## 개요`, `## 사용법` (`python main.py`), `## 핵심 구현`? Yes.
   - Based ONLY on provided files/output? Yes. No extra features, no invented dependencies, no installation steps. Matches comments exactly.
   - Run output considered? Yes, used for the usage example and default message.

   One minor adjustment: Ensure the exact section titles match the prompt exactly: `# 제목`, `## 개요`, `## 사용법`, `## 핵심 구현`. The prompt says `# 제목`, so I'll literally use `# 제목` or replace it with the actual title but keep the structure. Actually, the prompt says "Sections: # 제목, ## 개요, ## 사용법 (`python main.py`), ## 핵심 구현." This usually means the section headers should be exactly those, or I should replace `# 제목` with the actual title. I'll use `