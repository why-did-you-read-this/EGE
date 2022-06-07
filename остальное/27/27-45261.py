f = open('107_27_A.txt')
n = int(f.readline())
elems = [int(i) for i in f.readlines()]
answers = [0] * n
summ = 0
rightSum = 0
leftSum = 0
for i in range(1, (n // 2)):
    summ = summ + elems[i] * i + elems[n - i] * i
    rightSum += elems[i]
    leftSum += elems[n - i]

summ = summ + elems[n // 2] * (n // 2)
answers[0] = summ
for i in range(1, n):
    # новая сумма = предыдущая сумма + левая сумма + предыдущий центр обработки - правая сумма - текущий центр обработки
    answers[i] = answers[i - 1] + leftSum + elems[i - 1] - rightSum - elems[(i + (n // 2) - 1) % n]
    print(i, (i + (n // 2) - 1) % n)
    # правая сумма = правая сумма - < > + текущий центр обработки
    rightSum = rightSum - elems[i] + elems[(i + (n // 2) - 1) % n]
    # < > < > < >
    leftSum = leftSum - elems[(i + (n // 2)) % n] + elems[i - 1]

print(min(answers))
