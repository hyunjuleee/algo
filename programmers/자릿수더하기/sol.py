def solution(n):
    answer = 0

    for num in str(n):
        answer += int(num)

    return answer

print(solution(1234))

# print(solution(1234)) = 1 + 2 + 3 + 4 = 10