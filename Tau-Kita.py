f = open(r"C:\Users\Lolopo\Desktop\Тау-Кита\input_s1_10.txt").readline()
l =open(r"C:\Users\Lolopo\Desktop\Тау-Кита\output_s1_10.txt").readline()
f = f.split(' ')
h = []
for i in f:
     list= ''
     j = len(i) // 2
     count = 1
     list += i[j]
     while len(list) != len(i):
          list += i[j - count]
          if j + count < len(i):
               list += i[j + count]
          count += 1
     h.append(list)
g = []
j = len(h) // 2
count = 1
g.append(h[j])
while len(g) != len(h):
     g.append(h[j - count])
     if j + count < len(h):
          g.append(h[j + count])
     count += 1
k = ""
for i in g:
     k += i + ' '
print(k[:-1], l)
if l in k:
     print(True)
else:
     print(False)