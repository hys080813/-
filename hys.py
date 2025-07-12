import streamlit as st
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
    
    # 음수의 짝수 제곱근 처리 (복소수 공비가 아닌 실수 공비만 다루는 경우)
    if (nth_term / first_term) < 0 and (n - 1) % 2 == 0:
        return "음수의 짝수 제곱근은 실수 공비를 계산할 수 없습니다. (공비가 복소수가 될 수 있습니다.)"

    try:
        # 0으로 나누는 경우를 방지 (first_term이 0인 경우는 위에서 처리함)
        # 0의 거듭제곱이 0인 경우를 고려하여 예외 처리
        if nth_term == 0 and first_term != 0:
            return 0.0 # an이 0이면 공비가 0일 수 있음 (단, a1이 0이 아닐 때)
        elif nth_term != 0 and first_term == 0: # 이미 위에서 처리되지만 혹시 모를 상황 대비
            return "첫째 항은 0이 될 수 없습니다."

        ratio = (nth_term / first_term)**(1 / (n - 1))
        
        # 부동소수점 오차로 인한 미세한 음수 값 처리 (예: -0.0000000000000001 -> 0)
        if abs(ratio) < 1e-9: # 아주 작은 값은 0으로 간주
            ratio = 0.0
            
        return ratio
    except ZeroDivisionError:
        return "계산 중 0으로 나누는 오류가 발생했습니다. (일반적으로 첫째 항이 0일 때 발생)"
    except OverflowError:
        return "계산 결과가 너무 커서 표현할 수 없습니다."
    except Exception as e:
        return f"공비 계산 중 알 수 없는 오류가 발생했습니다: {e}"

st.set_page_config(page_title="등비수열 공비 계산기", layout="centered")

st.title("🔢 등비수열 공비 계산기")
st.markdown("첫째 항과 $n$번째 항의 값을 입력하여 등비(공비)를 계산합니다.")

st.sidebar.header("입력 값")
a1 = st.sidebar.number_input("첫째 항 ($a_1$)", value=1.0, step=0.1)
an = st.sidebar.number_input("$n$번째 항 ($a_n$)", value=2.0, step=0.1)
n = st.sidebar.number_input("몇 번째 항입니까? ($n$)", value=2, min_value=2, step=1)

if st.sidebar.button("공비 계산하기"):
    if n <= 1:
        st.error("오류: $n$은 1보다 커야 합니다.")
    else:
        result = calculate_geometric_ratio(a1, an, n)
        
        if isinstance(result, str):
            st.error(f"오류: {result}")
        else:
            st.success(f"계산된 공비 ($r$)는 **{result:.6f}** 입니다.")
            
            st.subheader("계산 확인")
            st.markdown(f"첫째 항 $a_1 = {a1}$")
            st.markdown(f"$n = {n}$")
            st.markdown(f"공비 $r = {result:.6f}$")
            
            # 계산된 공비로 n번째 항 다시 계산하여 비교
            calculated_an = a1 * (result**(n-1))
            st.markdown(f"계산된 공비로 구한 $n$번째 항 ($a_1 \\cdot r^{n-1}$) = **{calculated_an:.6f}**")
            
            if abs(calculated_an - an) < 1e-6: # 부동소수점 오차 고려
                st.info("입력된 $n$번째 항과 계산된 $n$번째 항이 일치합니다. (미세한 오차 범위 내)")
            else:
                st.warning(f"입력된 $n$번째 항 ({an})과 계산된 $n$번째 항 ({calculated_an:.6f}) 사이에 차이가 있습니다. (부동소수점 정밀도 문제일 수 있습니다.)")

st.markdown("---")
st.markdown("등비수열 일반항: $a_n = a_1 \\cdot r^{n-1}$")
st.markdown("공비 ($r$) 계산 공식: $r = (a_n / a_1)^{1/(n-1)}$")
