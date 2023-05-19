file =         open(r'C:\Users\Lolopo\Desktop\Обмен денег\input14.txt')
output_file = open(r'C:\Users\Lolopo\Desktop\Обмен денег\output14.txt')

line_1 = file.readline()
line_2 = file.readline()
line_3 = file.readline()
line_4 = file.readline()
line_5 = file.readline()

system_in_1 = {}

system_in_2 = {}

bad_number_in_1 = []

bad_number_in_2 = []

number_in_systeme_1 = {}

for i in range(1, int(line_1.split(' ')[0]) + 1):
    if i == int(line_1.split(' ')[0]):
        system_in_1[i] = 1
    else:
        system_in_1[i] = int(line_1.split(' ')[i])

for i in range(1, len(line_2.split(' '))):
    bad_number_in_1.append(int(line_2.split(' ')[i]))
bad_number_in_1.sort()

for i in range(1, int(line_3.split(' ')[0]) + 1):
    if i == int(line_3.split(' ')[0]):
        system_in_2[i] = 1
    else:
        system_in_2[i] = int(line_3.split(' ')[i])

for i in range(1, len(line_4.split(' '))):
    bad_number_in_2.append(int(line_4.split(' ')[i]))
bad_number_in_2.sort()

for i in range(0, int(line_1.split(' ')[0])):
    number_in_systeme_1[i + 1] = int(line_5.split(' ')[i])

# print("Система 1", system_in_1)
# print("плохие номер 1", bad_number_in_1)
# print("Система 2", system_in_2)
# print("плохие номер 2", bad_number_in_2)
# print("число в первой ситеме 1", number_in_systeme_1)

real_number = 0

for i in number_in_systeme_1.keys():
    count_number = 0
    for j in bad_number_in_1:
        if number_in_systeme_1[i] >= j:
            count_number += 1
    number_in_systeme_1[i] -= count_number


# print("число в системе 1 без плохих", number_in_systeme_1)

for i in number_in_systeme_1.keys():
    swap = 1
    for j in range(i, len(system_in_1.keys())):
        swap *= system_in_1[j]
    real_number += number_in_systeme_1[i] * swap

# print("реальное число", real_number)

result = {}

for i in system_in_2.keys():
    swap = 1
    for j in range(i, len(system_in_2.keys())):
        swap *= system_in_2[j]
    result[i] = real_number // swap
    real_number %= swap
    # print(swap, real_number, result[i])

# print(result)

for i in result.keys():
    count_number = 0
    for j in bad_number_in_2:
        if result[i] > j:
            count_number += 1
    while result[i] in bad_number_in_2:
        result[i] += 1
    past_result = result[i]
    result[i] += count_number
    count_number = 0
    while True:
        for j in range(past_result, result[i]):
            if j in bad_number_in_2:
                count_number += 1
        past_result = result[i]
        result[i] += count_number
        if count_number == 0:
            break
        count_number = 0

print(result)
print(output_file.readline())