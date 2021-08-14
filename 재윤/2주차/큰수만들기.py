def solution(number, k):
    value = []
    for i in range(len(number)):
        while value and ( k > 0 ) and ( value[-1] < number[i]):
            value.pop()
            k -= 1

        value.append(number[i])
    result = ''.join(value[:len(value)-k])
    return result
