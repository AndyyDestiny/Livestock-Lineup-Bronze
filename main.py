cows = ["Beatrice", "Belinda", "Bella", "Bessie", "Betsy", "Blue", "Buttercup", "Sue"]
cow_num = [1, 2, 3, 4, 5, 6, 7, 8]
subs = cow_num.copy()
lines = int(input())


order = []
for b in range(lines):
    x = input()
    pairs = []
    for i in cows:
        if i in x:
            pairs.append(cows.index(i) + 1)
            try:
                subs.pop(subs.index(cows.index(i) + 1))
            except:
                pass
    order.append(pairs)
    pairs = []

order.append(subs)

sort = []
prev = 0
for i in range(4):
    lowest = 9
    for i in order:
        num = 0
        times = 1
        for b in i:
            num += b * times
            num = round(num, 2)
            times = times / 10
        if lowest > num and prev < num:
            lowest = num
    b = []
    for i in str(lowest):
        if i != ".":
            b.append(i)
    sort.append(b)
    prev = lowest

order = []
for i in sort:
    for b in i:
        order.append(int(b))
order = [order]

for i in range(len(order) - 1):
    sub1 = order[0].copy()
    sub2 = order[1].copy()
    if order[0][0] in order[1]:
        sub1.pop(0)
        sub2.pop(order[1].index(order[0][0]))
    if order[0][len(order[0]) - 1] in order[1]:
        sub1.pop(len(order[0]) - 1)
        sub2.pop(order[1].index(order[0][len(order[0]) - 1]))
    if sub1[0] > sub2[0]:
        order[0] = sub2 + order[0]
    else:
        order[0] = order[0] + sub2    
    order.pop(1)


for i in order[0]:
    order[0][order[0].index(i)] = cows[i - 1]

for i in order[0]:
    print(i)
