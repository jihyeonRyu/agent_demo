import math
from typing import List

def is_prime(n: int) -> bool:
    """
    주어진 정수 n이 소수인지 판별합니다.
    알고리즘: 6k±1 최적화 (시간 복잡도 O(√n))
    GitHub 배포용 모듈로 설계되었습니다.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def get_primes_in_range(start: int, end: int) -> List[int]:
    """지정된 범위 [start, end] 내의 모든 소수를 효율적으로 추출합니다."""
    return [num for num in range(start, end + 1) if is_prime(num)]

def main() -> None:
    print("🔢 소수 판별 함수 데모")
    print("-" * 35)
    
    # 개별 숫자 판별 테스트
    test_cases = [1, 2, 3, 4, 17, 18, 97, 100, 101, 121]
    for num in test_cases:
        status = "✅ 소수" if is_prime(num) else "❌ 소수 아님"
        print(f"{num:>3} : {status}")
        
    print("-" * 35)
    
    # 범위 내 소수 추출 테스트
    primes = get_primes_in_range(100, 120)
    print(f"100 ~ 120 사이의 소수:
