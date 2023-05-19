import pprint
file = open(r"C:\Users\Lolopo\Desktop\Не съем, так надкушу\input_s1_1.txt").readlines()
new_file = open(r"C:\Users\Lolopo\Desktop\Не съем, так надкушу\output_s1_1.txt").readline()

n, m = int(file[0].split(' ')[0]), int(file[0].split(' ')[1])

k = float('inf')

tree = [[k for i in range(n + 1)] for j in range(n + 1)]
count = 1
for i in range(1, n+1):
    line_input = file[i].replace('\n', '').split(' ')
    k, l = int(line_input[0]), int(line_input[1])
    tree[k][count] = l
    tree[count][k] = l
    count += 1

# pprint.pprint(tree)

apple_dict = dict()

for i in range(n + 1, n + 1 + m):
    line_input = file[i].replace('\n', '').split(' ')
    c, s = int(line_input[0]), int(line_input[1])
    apple_dict[c] = s

point_warm = int(file[-1].split(' ')[0])

apple_ripeness = int(file[-1].split(' ')[1])

# print(point_warm, apple_ripeness)

list_delete_apple = []

for i in apple_dict.keys():
    if apple_dict[i] < apple_ripeness:
        list_delete_apple.append(i)

for i in list_delete_apple:
    del apple_dict[i]

# print(apple_dict)

k = float('inf')

result = 0

while len(apple_dict.keys()) != 0:

    h = []
    my = [k for i in range(n + 1)]
    my[point_warm] = 0

    for l in range(n + 1):
        if l == point_warm:
            continue
        for i in range(n + 1):
            if i == point_warm:
                continue
            for j in range(n + 1):
                h.append(my[j] + tree[j][i])
            my[i] = min(h)
            h = []

    # print(my)

    dict_branch_of_apple = {}

    for i in apple_dict.keys():
        dict_branch_of_apple[i] = my[i]

    # print(dict_branch_of_apple)

    result += min(dict_branch_of_apple.values())

    delete_count = 0

    for i in dict_branch_of_apple.keys():
        if dict_branch_of_apple[i] == min(dict_branch_of_apple.values()):
            delete_count = i
            break

    del apple_dict[delete_count]

    # print(apple_dict)
    # print(delete_count)
    # print('-------------------')
    point_warm = delete_count



print(result)

print(new_file)