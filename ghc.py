fileName = input("Name of the file: ")
file = open(fileName + '.txt', 'r')

count = -1
streets = []
cars = []

for line in file:
    values = line.strip('\n').split(' ')
    if values[0] != '':
        if count == -1:
            duration = int(values[0])
            interValue = int(values[1])
            streetValue = int(values[2])
            carValue = int(values[3])
            bonus = int(values[4])
        elif 0 <= count < streetValue:
            streets.append(values)
        else:
            cars.append(values)
    count += 1

dict_street = {}
set_inter = set()

for s in streets:
    dict_street[s[2]] = [s[0], s[1], s[3]]
    set_inter.add(s[0])
    set_inter.add(s[1])

#print(set_inter)
#print(dict_street)

dict_inter = {}

for inter in set_inter:
    dict_inter[inter] = {}


for v in cars:
    for k in range(1, len(v)-1):
        coming_inter = dict_street[v[k]][1]
        if v[k] in dict_inter.keys():
            dict_inter[coming_inter][v[k]] += 1
        else:
            dict_inter[coming_inter][v[k]] = 1

cycle = int(input('Enter the number of cycles: '))
time = duration/cycle
final_dict = {}

for k, v in dict_inter.items():
    total = 0
    for k1, v1 in v.items():
        total += v1
    final_dict[k] = {}
    for k1, v1 in v.items():
        final_dict[k][k1] = 1 if int(time*dict_inter[k][k1]/total) == 0 else int(time*dict_inter[k][k1]/total)

popKey = []

for k,v in final_dict.items():
    if v == {}:
        popKey.append(k)

for k in popKey:
    final_dict.pop(k)

out = open('generated/' + fileName + 'Res.txt', 'w')

out.write(str(len(final_dict)))
out.write('\n')
for k, v in final_dict.items():
    out.write(str(k))
    out.write('\n')
    out.write(str(len(v)))
    out.write('\n')
    for k1, v1 in v.items():
        out.write(str(k1) + " " + str(v1))
        out.write('\n')


