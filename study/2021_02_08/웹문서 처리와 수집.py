# import urllib.request  # 원격 서버 파일 요청
# from bs4 import BeautifulSoup  # html 파싱
#
# # 요청할 url
# url = 'http://www.naver.com/index.html'
#
# # 1. 원격 서버 파일 요청
# res = urllib.request.urlopen(url)  # web 문서 get
# data = res.read()  # text 형태로 읽음
#
# # 2. source 디코딩
# src = data.decode("utf-8")  # 디코딩
# # print('source')
# # print(src)
#
# # 3. html 파싱
# html = BeautifulSoup(src, 'html.parser')  # html source 파싱
# # print('html 파싱')
# # print(html)
#
# # 4. 태그 내용
# a = html.find('a')
# print('a tag : ', a)
# print('a tag 내용 : ', a.string)


# from bs4 import BeautifulSoup
#
# # 1. 로컬 서버 파일 읽기
# file = open("html01.html", mode='r', encoding='utf-8')
# text = file.read()
# print(text)
#
# # 2. html 파싱
# html = BeautifulSoup(text, 'html.parser')
# print(html)
#
# # 3. 태그 내용 가져오기
#
# # 1) tag 이용
# h1 = html.html.body.h1 # 계층 접근
# print('h1 : ', h1.string) # h1 :   시멘틱 태그 ?
#
# # 2) find()함수 : 태그 찾기
# h2 = html.find('h2')
# print('h2 : ', h2.string) # h2 :   주요 시멘틱 태그
#
# # 3) find_all('tag')
# lis = html.find_all('li') # list 반환
# print(lis)
# # [<li> header : 문서의 머리말(사이트 소개, 제목, 로그 )</li>, <li> nav : 네이게이션(메뉴) </li>, <li> section : 웹 문서를 장(chapter)을 볼 때 절을 구분하는 태그</li>, <li> aside : 문서의 보조 내용(광고, 즐겨찾기, 링크) </li>, <li> footer : 문서의 꼬리말(작성자, 저작권, 개인정보보호) </li>]
#
# for li in lis :
#     print(li.string)


# from bs4 import BeautifulSoup
#
# # 1. html source 가져오기
# file = open('html03.html', mode='r', encoding='utf-8')
# source = file.read()
#
# # 2. html 파싱
# html = BeautifulSoup(source, 'html.parser')
#
#
# print('>> table 선택자 <<')
# table = html.select_one('#tab')  # <table id='tab'>
# print(table)
#
# # [문제] th 내용 출력
# ths = table.find_all('th')
# for th in ths:
#     print(th.string)
#
# print('>> 선택자 & 계층 <<')
# ths = html.select('#tab > tr > th')
# print(ths)  # list
# # [<th id="id"> 학번 </th>, <th id="name"> 이름 </th>, <th id="major"> 학과 </th>, <th id="email"> 이메일 </th>]
#
# for th in ths:
#     print(th.string)
#
# # 2) class 선택자 : tr tag class='odd'
# trs = html.select("#tab > .odd")  # 홀수 행
# print(trs)
#
# print('### tr > td 출력 ### ')
# for tr in trs:  # 행 : 2회 반복
#     # print(tr)
#     tds = tr.find_all('td')
#     for td in tds:  # 열
#         print(td.string)
#
# # 4) 태그[속성=값] 찾기
# trs = html.select("tr[class=odd]")
# print(trs)
#
# print('### tr > td 출력 ### ')
# for tr in trs:  # 행 : 2회 반복
#     # print(tr)
#     tds = tr.find_all('td')
#     for td in tds:  # 열
#         print(td.string)


# import pickle
#
# file = open("data.pickle", mode='rb')
# news_data2 = pickle.load(file)
# # print(news_data2)
#
#
# import re
#
#
# def clean_text(text_string):
#     text_string_re = re.sub('[,.?!:\'\";·]', '', text_string)
#     text_string_re = re.sub('[!@#$%^&*()]|[0-9]', '', text_string_re)
#     text_string_re.lower()
#     text_string_re = re.sub('[a-z]', '', text_string_re)
#     text_string_re = ' '.join(text_string_re.split())
#
#     return text_string_re
#
#
# clean_texts = [clean_text(row) for row in news_data2]
#
# # print('>>텍스트 전처리 결과<<')
# # print(clean_texts)
#
# word_count = {}
#
# for text in clean_texts:
#     for word in text.split():
#         word_count[word] = word_count.get(word, 0) + 1
#
# # print('>>워드 카운트<<')
# # print(word_count)
#
# del word_count['[바로잡습니다]']
#
# new_word_count = {}
# for word, cnt in word_count.items():  # (단어:빈도수)
#     if cnt >= 3 and len(word) >= 2 and len(word) <= 3:
#         # print(word, '->', word_count[word])
#         new_word_count[word] = new_word_count.get(word, cnt)
#
# # print('>>단어 전처리<<')
# new_word_count
#
# from collections import Counter
#
# counter = Counter(new_word_count)
# top5_word = counter.most_common(5)
# # print('>>top 5 단어<<')
# # print(top5_word)
#
#
# words = []
# counts = []
#
# for word, count in top5_word:
#     words.append(word)
#     counts.append(count)
#
# print(words)
# print(counts)
#
# import matplotlib.pyplot as plt
#
# from matplotlib import font_manager, rc
#
# font_name = font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
# rc("font", family=font_name)
#
# print("선그래프")
# plt.plot(words, counts)
# plt.show()
#
# print("막대 그래프")
# plt.bar(words, counts)
# plt.show()


import matplotlib.pyplot as plt
import random
import matplotlib

matplotlib.rcParams["axes.unicode_minus"] = False

print(random.randint(a=1, b=5))
print(random.random())
print(random.normalvariate(mu=0, sigma=1))
