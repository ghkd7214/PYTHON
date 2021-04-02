from re import findall
from re import match
from re import sub

# st1 = "1234 abc홍길동 ABC_555_6 이사도시"
#
# print(findall("1234", st1))
# print(findall("[0-9]", st1))
# print(findall("[0-9]{3}", st1))
# print(findall("[0-9]{3,}", st1))
# print(findall("\\d{3,}", st1))
# print()
# print(findall("[가-힣]{3,}", st1))
# print(findall("[a-z]{3}", st1))
# print(findall("[a-z|A-Z]{3}", st1))
# print()
#
# st2 = "test1abcABC 123mbc 45test"
#
# print(findall("^test", st2))
# print(findall("st$", st2))
# print(findall(".bc", st2))
# print(findall("...bc", st2))


# jumin = "123456-4234567"
# rs = match("[0-9]{6}-[1-4][0-9]{6}", jumin)
# print(rs)
#
# if rs:
#     print("주민번호 일치")
# else :
#     print("잘못된 주민번호")


# st3 = "test^홍길동 abAAAASDc 대한*민국 123$tbc"
#
# text1 = sub("[/^*$]+", "", st3)
# print(text1)
#
# t2 = sub("[a-z]|[A-Z]|[0-9]", "", text1)
# print(t2)


texts = ["우리나라    대한민국, 우리나라$# 만세", "비아그%라 500GRAM 정력최고!",
         "나는 대한민국 사람", "보험료 15000원에 평생 보장 마감 임박",
         "나는 홍길동"]

texts_re1 = [t.lower() for t in texts]
print(texts_re1)        #소문자으로 변환

texts_re2 = [sub("[0-9]|[,.?!:;`~!@#$%^&*()_+]", "", text) for text in texts_re1]
print(texts_re2)        #숫자제거 #특수문자 제거

texts_re3 = ["".join(findall("[^a-z]", text)) for text in texts_re2]
print(texts_re3)        #소문자 제거

texts_re4 = [" ".join(text.split()) for text in texts_re3]
print(texts_re4)        #공백제거
