for i in range(123450708, 123459799):
    if (f'12345{str(i)[5]}7{str(i)[7]}8' == str(i)) and (i % 23 == 0):
        print(i, i / 23)
