import random
i = 0
while True:
    r = random.random()
    print(random.random())
    if r < 0.01:
        break
    else:
        i += 1
print("난수개수 :", i)
