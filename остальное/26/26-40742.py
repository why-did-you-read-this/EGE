f = open('26-40742.txt')
n = int(f.readline())
unix_list = f.readlines()
start_time = 1633305600 - 1
end_time = start_time + 7 * 24 * 60 * 60
count = 0
time_process = [0] * (7 * 24 * 60 * 60 + 1)

for i in unix_list:
    start_process, end_process = map(int, i.split())
    if (start_process < start_time) and ((end_process > start_time) or (end_process == 0)):
        count += 1
    if start_time <= start_process <= end_time:
        time_process[start_process - start_time] += 1
    if start_time <= end_process <= end_time:
        time_process[end_process - start_time] -= 1

sum_time = 0
max_process = 0
for i in range(1, 7 * 24 * 60 * 60 + 1):
    count += time_process[i]
    if count > max_process:
        max_process = count
        sum_time = 0
    if count == max_process:
        sum_time += 1


print(max_process, sum_time)
