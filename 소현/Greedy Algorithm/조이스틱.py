# 작성자 : SH_WON_96
# 2021-02-20
# 알고리즘 - Greedy
# 문제번호 : 프로그래머스 - level2, 조이스틱


def countA(name):
    max_a = 0  # 연속된 A의 최대 갯수
    maxloc = (0, 0)  # i ~ j 까지 연속된 A가 존재

    for i in range(len(name)):
        locs = (0, 0)
        if name[i] == "A":
            sum = 1
        else:
            sum = 0
        for j in range(i + 1, len(name)):
            if name[i] == "A" and name[j] == "A":
                sum += 1
                locs = (i, j)
            else:
                break
        if sum > max_a:
            maxloc = locs
            max_a = sum
    # print("A들 위치",maxloc, end = "   ")

    return maxloc, max_a


def solution(name):
    alphbet = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6,
               "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13,
               "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20,
               "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25}

    # "N 은 앞에서와도 12, 뒤에서 와도 12
    count = 0  # count 는 위아래로 알파벳 변경하는데 사용된 클릭 수
    direction = 0  # 좌우 커서 이동시 발생하는 클릭 수
    non_a = 0  # A 가 아닌 애들 갯수
    maxloc, max_a = countA(name)  # 연속된 최대 A의 갯수와 그 좌표?
    left_a = 0  # 연속에 포함되지 않은 A
    for i in range(len(name)):
        char = name[i]
        loc = alphbet.get(char)
        if char != "A":
            non_a += 1
        if loc > 13:
            loc = 26 - loc
        # print(loc)
        count += loc

    direction = non_a - 1
    print("알바펫 변경:", count, end="    ")
    print("커서이동:", direction, end="    ")

    # A 가 없는 경우
    if non_a == len(name):
        return direction + count
    # A만 있는 경우
    if max_a == len(name):
        return 0
    # 섞인 경우
    else:
        # 연속된 A의 길이가 절반보다 길때 (역방향으로 이동)
        if max_a > len(name) / 2:
            if name[0] == 'A' or name[-1] == "A":
                left_a = len(name) - non_a - max_a - 1
            else:
                left_a = len(name) - non_a - max_a

            return count + direction - max_a + left_a
        else:
            return count + len(name) - max_a - 1


# JEROEN -> 9+4+(26-17)+(26-14)+4+13 +len(name)-1
# 25+26+6-1 = 56
# BBBB -> 1*4 + 1*3 A갯수 -1
# ABABAAAAABA -> 1*3+1*2+8-1 =
# 연속된 A의 최대 갯수 빼기?
# 1*3+1*2+11-5 = 11

print(solution("BBBAAAB"))  # 8
print(solution("ABABAAAAABA"))  # 10
print(solution("CANAAAAANAN"))  # 48
print(solution("ABAAAAABAB"))  # 8
print(solution("ABABAAAAAB"))  # 8
print(solution("BABAAAAB"))  # 7
print(solution("AAA"))  # 0
print(solution("ABAAAAAAABA"))  # 6
print(solution("AAB"))  # 2
# 7 번 이동 (정방향)
# 5번 이동 (역방향) --> 이게 더 가까운 거지! i
print(solution("AABAAAAAAABBB"))  # 11 이동 2+2+
print(solution("ZZZ"))  # 5 이동 3 커서 2
print(solution("BBBBAAAAAB"))  # 10
print(solution("BBBBAAAABA"))  # 12