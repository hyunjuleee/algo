import sys
sys.stdin = open('input.txt', encoding='utf-8')
# 한글 오류

man1 = input()
man2 = input()

# print(man1, man2)

# if man1 == '바위' and man2 == '가위':
#    print('man1 win')
# elif man1 == '바위' and man2 == '바위':
#    print('draw')
# elif man1 == '바위' and man2 == '보':
#    print('man2 win')
# ...

rcp = ['바위', '가위', '보']

man1_idx = rcp.index(man1)
man2_idx = rcp.index(man2)

result = man1_idx - man2_idx

if result == 0:
    print('draw')
elif result > 0:
    print(f'man{result} win')
else:
    print(f'man{result+3} win')