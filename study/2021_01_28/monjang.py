string = """나는 홍길동 입니다.
주소는 서울시 입니다.
나이는 35세 입니다."""

sents = []
words = []

for sent in string.split(sep=".\n"):
    sents.append(sent)
    for word in sent.split():
        words.append(word)


print(sents)
print(words)
