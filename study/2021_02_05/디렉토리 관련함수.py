import pandas as pd

import os

# score = pd.read_csv("score.csv")
# print(score.info())  # str(data)
#
# print(score.head())
#
# # 칼럼 추출
# kor = score.kor  # 객체.칼럼명
# eng = score['eng']  # 객체['칼럼명']
# mat = score['mat']
# dept = score['dept']
#
# # 과목별 최고 점수
# print('max kor = ', max(kor))  # max height =  190
# print('max eng = ', max(eng))  # max weight =  85
# print('max mat = ', max(mat))
#
# # 과목별 최하 점수
# print('min kor = ', min(kor))  # max height =  190
# print('min eng = ', min(eng))  # max weight =  85
# print('min mat = ', min(mat))
#
# # 과목별 평균 점수
# from statistics import mean
#
# print('국어 점수 평균 : ', round(mean(kor), 3))
# print('영어 점수 평균 : ', round(mean(eng), 3))
# print('수학 점수 평균 : ', round(mean(mat), 3))
#
# # dept 빈도수
# dept_count = {}  # 빈 set
#
# for key in dept:
#     dept_count[key] = dept_count.get(key, 0) + 1
#
# print(dept_count)  # dict



# sam = pd.ExcelFile("sam_kospi.xlsx")
# # ImportError: Missing optional dependency 'xlrd'.
# print(sam) # <pandas.io.excel._base.ExcelFile object at 0x1347FE50>
#
# kospi = sam.parse("sam_kospi")
# print(kospi) # [247 rows x 6 columns]
# print(kospi.info())
# '''
# RangeIndex: 247 entries, 0 to 246
# Data columns (total 6 columns):
# '''
#
# high = kospi['High']
# low = kospi['Low']
#
# from statistics import mean
# print('high mean=', mean(high)) # high mean= 1307947.3684210526
# print('low mean=', mean(low)) # low mean= 1280919.028340081
#
# print('High mean :', high.mean())
# print('Low mean :', low.mean())
#
# '''
# High mean : 1307947.3684210526
# Low mean : 1280919.028340081
#
# 기타 통계, 차트 시각화 Python2에서
# '''


# import json
#
# # 1. json encoding
# '''
#  - Python 객체(dict) ->  json 문자열 변경
#    형식) json.dumps(object)
# '''
# user = {'id': 1234, 'name': '홍길동'}  # Python Dict
# print(type(user))  # <class 'dict'>
# print(user['name'])  # 홍길동
#
# #  json 인코딩 : dict -> string, ensure_ascii=False -> 한글 사용시
# jsonString = json.dumps(user)  # , ensure_ascii=False) # ASCII 인코딩 방식 적용 안함
#
# # 문자열 출력
# print(jsonString)  # {"id": 1234, "name": "홍길동"}
# print(type(jsonString))  # class str
# # print(jsonString['name']) # Error 발생
# print()
# print(jsonString[:5])  # {"id"
#
# # 2. json decoding
# '''
#  - json 문자열 -> Python 객체(dict or list)
#    형식) json.loads(jsonString)
#    에) json 파일(문자열)  -> Python 객체(dict or list)
# '''
#
# # json  디코딩
# pyObj = json.loads(jsonString)
# print(type(pyObj))  # <class 'dict'>
#
# # Dict 자료 체크
# print(pyObj['name'])  # 홍길동
# for key in pyObj:
#     print(key, ':', pyObj[key])
#
# '''
# id : 1234
# name : 홍길동
# '''


# 3. json file 읽기
import json
'''
- json 디코딩 : json 문자열 -> Python 객체(dict or list)
'''

# json file(json 문자열) -> python dict 객체
print('json 객체 형식 읽기')
file = open("usagov_bitly.txt", mode='r', encoding='utf-8')
# print(file.read()) # 전체 문서 읽기
lines = file.readlines()  # 줄단위 전체 읽기

# 줄 단위 읽기(json string) -> dict 객체 변환  -> list 저장
rows = [json.loads(row) for row in lines]
# print(recodes) # [dict] 결과 확인
# [{'a': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 ...]
print('rows :', len(rows))  # rows : 3560

# 전체 행 출력
# for row in rows[:10]:
#     print(row)
#     print(type(row))

file.close()

# dict -> DataFrame 변환
'''
 {} -> row, 'key:value' -> column
'''
import pandas as pd

recode_df = pd.DataFrame(rows)
print(recode_df.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3560 entries, 0 to 3559
Data columns (total 18 columns):
'''