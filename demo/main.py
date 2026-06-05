# 1. math 모듈의 factorial 함수로 효율적 계산
# 2. sys.argv로 CLI 입력 처리
# 3. try-except로 유효성 검증
# 4. 깃허브에 push 시 README에 사용법 추가
import sys
import math

def main():
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
            if n < 0:
                print("음수는 입력할 수 없습니다.")
                return
            print(f"{n}! = {math.factorial(n)}")
        except ValueError:
            print("정수만 입력해주세요.")
    else:
        print("팩토리얼 계산기: python main.py <정수>")

if __name__ == "__main__":
    main()
