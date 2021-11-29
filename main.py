''' 기본 읽기 기능 완료
    f = open("movies_exp.txt", "rt")
    for line in f:
        print(line, end='')
    f.close()
'''

import sys
import datetime # 날짜를 요일로 환산하기 위함

fileName = sys.argv[1] #입력 파일
output = sys.argv[2]   #출력 파일

f = open(fileName, "rt")
out = open(output, "w")

#f = open("uber_exp.txt", "rt")
#out = open("output.txt", "w")
'''
장르와 그 수를 저장할 공간을 4열을 가진 2차원 리스트로 만들어서 print 문에서 엮어서 파일에 쓴다,
[region][day][vehicles][trips] 
[region][day][vehicles][trips]
[region][day][vehicles][trips]
...
'''
genre_lol = []

for line in f:
    line = line.strip()  # 개행 문자 제거
    row = line.split(",")  # 쉼표를 기준으로 정보가 나뉜다.
    col = row[1]
    # print(col) # 여기까지 디버깅o
    col_date = col.split("/")

    # 해당 열의 요일 정보 받아오기
    days = ['Mon', 'TUE', 'WED', 'THR', "FRI", "SAT", "SUN"]
    day =  days[datetime.date(int(col_date[2]), int(col_date[0]), int(col_date[1])).weekday()]
    
    genre_lol.append([row[0], day, row[2], row[3]])
f.close()

#print(genre_lol)

for i in range(0, len(genre_lol)):
    li = str(genre_lol[i][0]) + "," + str(genre_lol[i][1]) + " " + str(genre_lol[i][2]) + "," + str(genre_lol[i][3]) + "\n"
    out.write(li)

out.close()
