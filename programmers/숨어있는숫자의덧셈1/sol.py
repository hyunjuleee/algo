def solution(my_string):
    answer = 0

    for char in my_string:
        if char.isdigit():
            answer += int(char)

    return answer

print(solution('aAb1B2cC34oOp'))

# 글자/숫자 판단
# 숫자만 골라내서 더하기
# print(solution('aAb1B2cC34oOp')) = 10