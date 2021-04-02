import time

start = time.time()

sum = 0
for i in range(1, 100000001):
    sum = sum + 1

end = time.time()

print(sum)
print("소요시간: ", end - start)
