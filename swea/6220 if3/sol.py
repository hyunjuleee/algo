import sys
sys.stdin = open('input.txt')

T = int(input())
# input.txt의 값을 한줄씩 가져옴 input 함수는 문자로 출력

# print(T)
# 실행하는 법 1. 해당 폴더로 이동 2. python sol.py(해당 파일)

# 데이터가 2개 이상일 경우 => 반복문 test case
for tc in range(1, T+1):
    char = input()

    if char.islower():
        print(f'#{tc} {char} 는 소문자입니다.')
    else:
        print(f'#{tc} {char} 는 대문자입니다.')