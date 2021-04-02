import pymysql

config = {
    'host': 'localhost',
    'user': 'root',
    'password': '11111',
    'database': 'work',
    'port': 3306,
    'charset': 'utf8',
    'use_unicode': True}
try:
    conn = pymysql.connect(**config)
    cursor = conn.cursor()

    sql = """create table goods(
                    code int primary key,
                    name varchar(30) not null,
                    su int default 0,
                    dan int default 0 
                    )"""

    cursor.execute(sql)

    #데이터 입력
    code = int(input('코드 입력 : '))
    name = input('상품명 입력 : ')
    su = int(input('수량 입력 : '))
    dan = int(input('단가 입력 : '))

    sql = f"insert into goods values({code}, '{name}', {su}, {dan})"
    cursor.execute(sql)
    conn.commit()  # db 반영

    '''     #데이터 수정
    code = int(input('수정할 코드 입력 : '))
    name = input('수정할 상품명 입력 : ')
    su = int(input('수정할 수량 입력 :'))
    dan = int(input('수정할 단가 입력 :'))

    sql = f"update goods set name='%{name}%', su=%{su}%, dan = %{dan}% where code=%{code}%"
    cursor.execute(sql)
    conn.commit()
    

    #데이터 삭제
    code = int(input('삭제할 코드 입력 : '))
    sql = f"select * from goods where code = {code}"
    cursor.execute(sql)  # sql문 실행
    rows = cursor.fetchall()

    if rows:
        # 레코드 1개 출력 : index 이용
        print('레코드 삭제')
         
        sql = f"delete from goods where code = {code}"
        cursor.execute(sql) # sql문 실행
        conn.commit()
        
    else:
        print('해당 code 없음 ')
        '''

    # 조회
    sql = "select * from goods"
    cursor.execute(sql)  # sql문 실행
    rows = cursor.fetchall()  # 전체 검색
    # print(type(dataset)) # <class 'tuple'>

    # 레코드 출력 : 양식문자
    for r in rows:  # fetchone()
        # print(r) # tuple type 출력
        print('%d    %s    %d     %d' % r)

    print('검색 레코드 수 :', len(rows))

    # 3. 조건 검색 : 상품명(포함 문자 검색)
    name = input('\n조회할 상품명 입력 : ')
    sql = f"select * from goods where name like '%{name}%' "
    cursor.execute(sql)  # sql문 실행
    rows = cursor.fetchall()

    if rows:
        # 레코드 1개 출력 : index 이용
        for r in rows:
            print(r[0], r[1], r[2], r[3])
    else:
        print('해당 상품 없음 ')

except Exception as e:
    print('db 연동 오류 : ', e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()
