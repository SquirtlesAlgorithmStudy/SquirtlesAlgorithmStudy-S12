# 작성자 : SH_WON_96
# 2021-02-20
# 알고리즘 - Greedy
# 문제번호 : 프로그래머스 - level2, 큰 수 만들기


def solution(number, k):
    idx = 0
    while idx < len(number) - 1 and k > 0:
        # idx 번째 숫자가 뒤에 숫자보다 앞에 숫자가 작으면앞에 숫자 없애기
        if number[idx] < number[idx + 1]:
            number = number[:idx] + number[idx + 1:]  # idx 번째 숫자 없애기
            if idx != 0:  # idx 번째 없앴으니까 인덱스 바뀌므로 idx -= 1 해야함
                idx -= 1
            k -= 1  # 1개 뺐으니 줄어들어야지

        else:
            idx += 1  # 이제 다음 idx에대해서 분석
    if k > 0:  # 여전히 k 남으면 sort 된상태인거임. 뒤에 k 개 없애기
        return number[:-k]
    return number
