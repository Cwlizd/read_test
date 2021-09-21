data = []
with open('reviews.txt','r') as f:
    for line in f:
        data.append(line.strip())
        x = int(len(data))
        y = x / 10000

        if y % 1 == 0:
            print(y,'%')

print(len(data))
print(data[0])
