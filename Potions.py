file =      open(r"C:\Users\Lolopo\Desktop\Зельеварение\input10.txt").readlines()
new_file = open(r"C:\Users\Lolopo\Desktop\Зельеварение\output10.txt").readline()

def f(any_list):
    count_key_in_value = 0
    new_list_komand = {}

    for i in range(len(any_list)):
        if any_list[i] in list_komand.keys():
            count_key_in_value += 1
            new_list_komand[i] = any_list[i]

    if count_key_in_value == 0:
        return fin(any_list)
    else:
        for i in new_list_komand.keys():
            any_list[i] = f(list_komand[new_list_komand[i]])
        return fin(any_list)





def fin(any_list) -> str:
    line = ''

    for i in range(1, len(any_list)):
        line += any_list[i]
    kod = any_list[0]

    if kod == "MIX":
        line = "MX" + line + "XM"
        return line

    if kod == 'WATER':
        line = "WT" + line + "TW"
        return line

    if kod == 'DUST':
        line = "DT" + line + "TD"
        return line

    if kod == 'FIRE':
        line = "FR" + line + "RF"
        return line

for i in range(len(file)):
    file[i] = file[i].replace('\n', '')

list_komand = {}

for i in range(len(file)).__reversed__():
    list_komand[str(i + 1)] = file[i].split(' ')

result = f(list_komand[str(len(file))])

print(result)

print(new_file)