'''
[Question 2] = (20점)
한 반 학생들의 이름과 수학 점수가 담긴 2차원 리스트가 주어질 때, ex) [이름, 점수]
수학 점수가 가장 높은 사람의 이름을 출력하시오.
'''

scores = [['alex', 30], ['rachel', 25], ['fred', 50], ['june', 80],
          ['jane', 90], ['elle', 40], ['ken', 65], ['jun', 85],
          ['chelsea', 60], ['gorden', 75], ['kelly', 100], ['kate', 55],
          ['jacob', 15], ['harry', 70], ['haley', 55], ['kyle', 95]]

# 결과값 저장 변수
max_name = ''
max_num = 0

for names, nums in scores: #2차 배열에서 이름과 숫자 반복하기 위해
    if nums > max_num: # 30 > 0 ..30저장 30 > 25 ... 가장 큰 수 100
        max_num = nums
        max_name = names # 동시에 이름도 저장

print(max_name)