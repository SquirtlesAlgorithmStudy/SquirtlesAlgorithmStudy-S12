# 큰 수 만들기

def solution(number, k):
    result = []

    for appendNum in number:
        if k <= 0:
            result.append(appendNum)
        else:
            if not result:
                result.append(appendNum)

            else:
                while result[-1] < appendNum and k > 0 and result:
                    k -= 1
                    result.pop()

                    if not result:
                        break

                result.append(appendNum)

    while k > 0:
        result.pop()
        k -= 1

    return ''.join(result)
