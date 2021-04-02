# import os
# print("\n현재경로 :", os.getcwd())
#
# try:
#     ftest1 = open("C:/Users/user/Documents/ftest.txt", mode="r")
#     print(ftest1.read())
#     ftest1.close()
#
#     ftest2 = open("C:/Users/user/Documents/ftest.txt", mode="w")
#     ftest2.write("my first text~~~")
#     ftest2.close()
#
#     ftest3 = open("C:/Users/user/Documents/ftest.txt", mode="a")
#     ftest3.write("\nmy first text~~~")
#     ftest3.close()
#
# except Exception as e:
#     print("오류발생")


try:
    ftest1 = open("ft.txt", mode="r")
    fulltext = ftest1.read()
    print(fulltext)
    print(type(ftest1))
    ftest1.close()

    # ftest2 = open("C:/Users/user/Documents/ftest.txt", mode="w")
    # ftest2.write("my first text~~~")
    # ftest2.close()
    #
    # ftest3 = open("C:/Users/user/Documents/ftest.txt", mode="a")
    # ftest3.write("\nmy first text~~~")
    # ftest3.close()

except Exception as e:
    print("오류발생")