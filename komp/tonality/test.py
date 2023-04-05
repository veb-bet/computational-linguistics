lst = []

s = ["a", "b", "c"]
for i in range(20):
    x = []
    x.append(i)
    x.append(s[i%3])
    lst.append(x)

with open("output.txt", "w", encoding='utf-8') as f:
    for i in lst:
        print(i)
        k = ",".join([str(x) for x in i])+"\n"
        f.write(k)