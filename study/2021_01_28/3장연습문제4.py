line = """안녕하세요. 파이썬 세계로 오신걸
환영합니다.
파이썬은 비단뱀 처럼 매력적인 언어입니다."""

word = []
word2 = []

for i in line.split(sep="\n"):
    word.append(i)
    for j in i.split():
        word2.append(j)

for h in range(len(word2)):
    print(word2[h])

print(len(word2))
