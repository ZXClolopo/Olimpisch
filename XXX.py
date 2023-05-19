file = open(r"C:\Users\Lolopo\Desktop\Компания ХХХ\input_s1_16.txt")
file_f = []
d_lider = {}
d = {}
d_num = []
d_name = []
lider = ''
num_lider = ''
flag1 = False
for i in file.readlines():
    i = i.replace('\n', '')
    if flag1:
        lider = i
        break
    if i == "END":
        flag1 = True
        continue
    file_f.append(i)
    d_num.append(i[0:4])
    if i[5:] == '':
        d_name.append('Unknown Name')
    else:
        d_name.append(i[5:])
flag2 = False
if len(lider) == 4:
    num_lider = lider
    flag2 = True
for i in range(len(file_f)):
    d[d_num[i]] = d_name[i]
    if d_name[i] == lider and not flag2:
        num_lider = d_num[i]
    if d_name[i] == 'Unknown Name':
        for j in range(len(file_f)):
            if d_num[i] == d_num[j] and d_name[j] != 'Unknown Name':
                d[d_num[i]] = d_name[j]
d_lider = {}
i = 0
while i < len(d_num) - 1:
    d_lider[d_num[i]] = []
    i += 2
i = 0
while i < len(d_num) - 1:
    d_lider[d_num[i]].append(d_num[i+1])
    i += 2
s = ''
try:
    for i in d_lider.keys():
        try:
            for i in d_lider.keys():
                for j in d_lider[i]:
                    d_lider[i] += d_lider[j]
        except KeyError:
            continue
    for i in d_lider[num_lider]:
        try:
            d_lider[num_lider] += d_lider[i]
        except KeyError:
            continue
    list = sorted(d_lider[num_lider])
    for i in list:
        s += i + " " + d[i] + "\n"
except KeyError:
    s = 'NO'
print(s)