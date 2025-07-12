import math

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
    if nth_term / first_term < 0 and (n - 1) % 2 == 0:
        return "음수 비율의 짝수 제곱근은 실수 공비를 계산할 수 없습니다."

    try:
        ratio = (nth_term / first_term)**(1 / (n - 1))
        return ratio
    except Exception as e:
        return f"공비 계산 중 오류가 발생했습니다: {e}"
