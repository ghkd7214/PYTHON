# s = {1, 2, 3, 4, 5, 4, 5, 3, 2, 1}
# print(len(s))
# print(s)
#
# for d in s:
#     print(d,end="")
#
# print()
#
# s2 = {3, 6}
# print(s.union(s2))
# print(s.difference(s2))
# print(s.intersection(s2))
#
# s3 = {1,3,5}
# print(s3)
#
# s3.add(7)
# print(s3)
#
# s3.discard(3)
# print(s3)
#

# gender = ["남", "여", "남", "여"]
# sgender = set(gender)
# lgender = list(sgender)
# print(lgender)
# print(lgender[1])
# print(sgender)

# dic = dict(key1=100, key2=200, key3=300)
# print(dic)
#
# person = {"name": "홍길동", "age": "35", "address": "서울시"}
# print(person)
# print(person["name"])
# print(type(dic), type(person))
#
# person["age"] = 45
# print(person)
#
# del person["address"]
# print(person)
#
# person["pay"] = 350
# print(person)
#
# print(person["age"])
# print("age" in person)
#
# for key in person.keys():
#     print(key)
# for v in person.values():
#     print(v)
# for i in person.items():
#     print(i)

# charset = ["abc", "code", "band", "band", "abc"]
#
# wc = {}     # 셋 객체
#
# for key in charset:
#     wc[key] = wc.get(key, 0) + 1
#
# print(wc)   # 딕트 객체가 됨


# import random
#
# dataset = []
# for i in range(10):
#     r = random.randint(1, 100)
#     dataset.append(r)
# print(dataset)
#
# vmax = vmin = dataset[0]
#
# for i in dataset:
#     if vmax < i:
#         vmax = i
#     if vmin > i:
#         vmin = i
#
# print("max =", vmax, " min =", vmin)


dataset = [5, 10, 18, 22, 35, 55, 75, 103]
value = int(input("검색할 값 입력:"))

low = 0
high = len(dataset) - 1

loc = 0
state = False

while (low <= high):
    mid = (low + high) // 2

    if dataset[mid] > value:
        high = mid - 1
    elif dataset[mid] < value:
        low = mid + 1
    else:
        loc = mid
        state = True
        break
if state:
    print("찾은 위치 : %d번째" % (loc + 1))
else:
    print("찾는 값이 없습니다")
