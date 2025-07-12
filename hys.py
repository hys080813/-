import streamlit as st
import math

# 공비 계산 함수 정의
def calculate_geometric_ratio(first_term, nth_term, n):
    """
    등비수열의 첫째 항, n번째 항, 그리고 n을 입력받아 공비를 계산합니다.

    Args:
        first_term (float): 등비수열의 첫째 항 (a1).
        nth_term (float): 등비수열의 n번째 항 (an).
        n (int): n번째 항의 위치 (n은 1보다 커야 합니다).

    Returns:
        float: 등비수열의 공비 (r).
        str: 오류 메시지 (유효하지 않은 입력의 경우).
    """
    if n <= 1:
        return "n은 1보다 큰 정수여야 합니다. (첫째 항과 n번째 항이 같을 수 없습니다.)"
    if first_term == 0:
        return "첫째 항은 0이 될 수 없습니다."
    
    # 음수의 짝수 제곱근 처리 (복소수 공비가 아닌 실수 공비만 다루는 경우)
    # 예: a1=1, an=-4, n=3 일 때 (n-1)=2. r^2 = -4 이므로 실수 공비는 없음.
    if (nth_term / first_term) < 0 and (n - 1) % 2 == 0:
        return "음수의 짝수 제곱근은 실수 공비를 계산할 수 없습니다. (공비가 복소수가 될 수 있습니다.)"

    try:
        # an이 0이고 a1이 0이 아닐 때 공비는 0
        if nth_term == 0 and first_term != 0:
            return 0.0
        # 이 외의 경우 일반 공식 적용
        ratio = (nth_term / first_term)**(1 / (n - 1))
        
        # 부동소수점 오차로 인해 발생할 수 있는 아주 작은 값들을 0으로 처리
        if abs(ratio) < 1e-9: # 0.000000001 보다 작으면 0으로 간주
            ratio = 0.0
            
        return ratio
    except ZeroDivisionError:
        return "계산 중 0으로 나누는 오류가 발생했습니다. (첫째 항이 0일 때 발생할 수 있습니다.)"
    except OverflowError:
        return "계산 결과가 너무 커서 표현할 수 없습니다. 입력 값을 확인해 주세요."
    except Exception as e:
        return f"공비 계산 중 알 수 없는 오류가 발생했습니다: {e}"
