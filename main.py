''' 기본 읽기 기능 완료
    f = open("movies_exp.txt", "rt")
    for line in f:
        print(line, end='')
    f.close()
'''

'''
각 영화 장르의 영화가 얼마나 개봉 하였는가를 분석하는 과제이다.
설계: 각 줄의 맨 끝에 영화의 장르를 바탕으로 장르 list를 만들어 장르별 수를 셀 것.
각 영화가 여러 장르에 속할 수 있다.


'''
import sys

fileName = sys.argv[1]
output = sys.argv[2]

f = open(fileName, "rt")
out = open(output, "w")
'''
장르와 그 수를 저장할 공간을 이차원 리스트로 만들 것임
[장르명][개수]
[장르명2][개수]
[장르명3][개수]
...
'''
genre_lol = []
genre_cnt = []

for line in f:
    row = line.split("::")  # ::기준으로 3번째에 장르가 나온다.
    col = row[2]
    # print(col) # 여기까지 디버깅o

    col = col.strip()  # 개행 문자 제거
    genre = col.split("|")
    for data in genre:  # data[0] data[2] ,,, 한 행의 장르 줄을 돌면서
        if data in genre_lol:
            genre_cnt[genre_lol.index(data)] += 1  # 리스트에 해당 장르가 이미 잇다면 해당 장르가 저장된 행의 index를 찾아 그것의 [장르][1]에 수 증가
        else:
            genre_lol.append(data)
            genre_cnt.append(1)
f.close()

print(genre_lol)
print(genre_cnt)
print(len(genre_lol))
print(len(genre_cnt))

i = 0
for i in range(0, len(genre_lol)):
    print(genre_lol[i], genre_cnt[i], sep=" ")

# 2차원 배열로 합치기

result = []

for l, c in zip(genre_lol, genre_cnt):
    result.append([l, c])
print(result)

wr = ''

for a in result:
    for b in a:
        wr = wr + str(b) + ' '
    wr = wr.rstrip(" ")  # 마지막에도 추가되는 sep을 삭제
    wr = wr + '\n'

out.writelines(wr)

out.close()
