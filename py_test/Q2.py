# 입력된 문자열을 뒤집은 문자열을 구하시오.
# ex) banana 입력 시 ananab 출력
word = input()
# 로직 작성
reversed_word = word[::-1]
# 문자열은 불변 원본 변경되지 않음,새로 담을 변수 작성, 문자열은 시퀀스 타입이라 슬라이싱 가능

print(reversed_word)

# print(reversed_word)  # 'banana' 입력 시 reversed_word == 'ananab'