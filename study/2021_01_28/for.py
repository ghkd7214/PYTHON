# listset = [5, 8, 6, 3, 7]
# i = 0
# d = "524"
#
# for e in listset:
#     if i < 3:
#         print(e)
#     i += 1
import random

lst = []
for i in range(10):
    r = random.randint(1, 10)
    lst.append(r)

print('lst =', lst)

for i in range(10):
    print(lst[i] * 0.25)

# a = [random.randint(1,10)*0.25 for x in range(10)]        #11 ~ 19줄의 코드를 한줄도 줄인것
# print(a)                                                  #코드를 간소화할때 사용함
