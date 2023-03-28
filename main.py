seats = []
seats.append([str(1).zfill(2), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
seats.append([str(2).zfill(2), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
seats.append([str(3).zfill(2), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
seats.append([str(4).zfill(2), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
seats.append([str(5).zfill(2), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
seats.append([str(6).zfill(2), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
seats.append([str(7).zfill(2), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
seats.append([str(8).zfill(2), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
seats.append([str(9).zfill(2), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

while True:
    print("------------------------------")
    print("     1 2 3 4 5 6 7 8 9 10")
    print("------------------------------")

    for row in seats:
        count = 0
        for col in row:
            if(count == 0) :
                print("[" + str(col) + "]", end=" ")
                count = 1   
                continue
            print(col, end=" ")
        print("")

    row = int(input("좌석의 행번호를 입력하세요(종료는 -1): "))
    if row == -1:
        break
    col = int(input("좌석의 열번호를 입력하세요(종료는 -1): "))
    if col == -1:
        break

    if seats[row][col] == 1:
        print("이미 예약되어 있습니다.")
    else:
        seats[row][col] = 1

    print("------------------------------")
    print("     1 2 3 4 5 6 7 8 9 10")
    print("------------------------------")
    for row in seats:
        count = 0
        for col in row:
            if (count == 0):
                print("[" + str(col) + "]", end=" ")
                count = 1
                continue
            print(col, end=" ")
        print("")