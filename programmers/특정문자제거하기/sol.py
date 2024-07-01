def solution(my_string, letter):
    return my_string.replace(letter,'')

print(solution('BCBdbe','B'))

# my_string 안에서 letter을 찾는다
# 그 문자를 빼거나, 그 문자를 제외하고 추출하거나~

# print(solution('BCBdbe','B')) = 'Cdbe'