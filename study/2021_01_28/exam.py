# fat = int(input("지방의 그램을 입력하세요 :"))
# carbo = int(input("탄수화물의 그램을 입력하세요"))
# pro = int(input("단백질의 그램을 입력하세요 :"))
#
# all = fat * 9 + pro * 4 + carbo * 4
#
# print("총칼로리 :", format(all, "3,d"), "cal")

word1 = (input("첫번째 단어 :")).upper()
word2 = (input("두번째 단어 :")).upper()
word3 = (input("세번째 단어 :")).upper()

print("=" * 10)

# addr = word1[0].upper() + word2[0].upper() + word3[0].upper()
addr = word1[0] + word2[0] + word3[0]
print(addr)
