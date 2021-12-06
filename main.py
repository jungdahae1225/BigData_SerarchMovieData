import sys
import datetime

# fileName = sys.argv[1]
# output = sys.argv[2]
#
# f = open(fileName, "rt")
# out = open(output, "w")

f = open("uber_exp.txt", "rt")
out = open("output.txt", "w")

regionPlusDay_lol = []
vehiclesTrips_lol = []

day_lol = ['Mon', 'TUE', 'WED', 'THR', "FRI", "SAT", "SUN"]
vehicles = []
trips = []

for line in f:
    line = line.strip()  # 개행문자 자름
    row = line.split(",")  # 쉼표단위로 자름

    # 요일을 구하기 위한 이라 4줄 코드
    col = row[1]
    col_date = col.split("/")

    days = ['Mon', 'TUE', 'WED', 'THR', "FRI", "SAT", "SUN"]
    day = days[datetime.date(int(col_date[2]), int(col_date[0]), int(col_date[1])).weekday()]
    ########################여기까지 데이터 자른 부분 ############################

    # 수정
    '''
    1.장르가 있는 경우
        1-1 . 장르와 요일이 같은 것이 있다면 +
        1-2 . 장르는 있으나 요일은 없으면 
    2.장르도 없는 경우
    
    배열을 다 따로 하지 말고 
    '''

    regionPlusDay = row[0] + "," + day
    vehiclesTrips = row[2] + "," + row[3]

    # print(regionPlusDay)
    #print(vehiclesTrips)

    # 경우 1 - regionPlusDay정보가 들어있으면

    if regionPlusDay in regionPlusDay_lol:
        forCut = vehiclesTrips_lol[regionPlusDay_lol.index(regionPlusDay)]
        forCut_row = forCut.split(",")  # 쉼표단위로 자름 => [row[2]],[row[3]]

        #print(forCut_row)

        i = int(forCut_row[0]) + int(row[2])
        j = int(forCut_row[1]) + int(row[3])

        forCut_row[0] += row[2]
        forCut_row[1] += row[3]

        new_data = str(i) + "," + str(j)

        vehiclesTrips_lol[regionPlusDay_lol.index(regionPlusDay)] = new_data

    # 경우 2 - 장르가 없는 경우
    else:
        regionPlusDay_lol.append(regionPlusDay)

        vehiclesTrips_lol.append(vehiclesTrips)
        #vehiclesTrips_lol[regionPlusDay_lol.index(regionPlusDay)].append(vehiclesTrips)

f.close()

result = []

for i, c in zip(regionPlusDay_lol, vehiclesTrips_lol):
    result.append([i, c])

for i in range(0, len(result)):
    print(result[i])

wr = ''

for a in result:
    for b in a:
        wr = wr + str(b) + ' '
    wr = wr.rstrip(" ")
    wr = wr + '\n'

out.writelines(wr)

out.close()
