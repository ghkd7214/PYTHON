charset = ["과장", "부장", "대리", "사장", "대리", "과장"]

wc = {}

wc1 = set(charset)

for key in charset:
    wc[key] = wc.get(key, 0) + 1

print(wc1)
print(wc)
