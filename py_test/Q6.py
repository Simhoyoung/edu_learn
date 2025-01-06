# <미출석 인원 찾기>
# 전체 출석부와 현재 출석한 인원이 리스트로 주어질 때, 출석하지 않은 인원을 출력하시오. (순서 굳이 상관 없음)
students = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']  # 전체 명단
attened = ['c', 'e', 'f', 'h']  # 출석 명단

def find_absent(total, present):
    absent_list = [person for person in total if person not in present]
    return absent_list

print(find_absent(students, attened))
