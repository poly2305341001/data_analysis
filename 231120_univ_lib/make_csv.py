import pandas as pd

# f = open('univ_score.txt', 'r')
f = open('univ_score_2023.txt', 'r')
lines = f.readlines()

# 학교별로 리스트에 저장
univ_list = []
for i in range(0, len(lines), 8):
    # 8줄씩 하나의 리스트로 만들고 개행 문자 제거
    univ_info = [line.strip() for line in lines[i:i+8]]
    univ_list.append(univ_info)
f.close()

# print(len(univ_list))

df = pd.DataFrame(univ_list, columns=['University', 'Overall Score', 'International Students Ratio',
                                      'International Faculty Ratio', 'Faculty Student Ratio',
                                      'Citations per Faculty', 'Academic Reputation', 'Employer Reputation'])

df.to_csv('univ_score_2023.csv', index=False)