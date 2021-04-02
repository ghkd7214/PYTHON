def month_range(year, month):
    ins_year = 1
    ins_month = 1

    ins_now_month = 0

    while True:
        now_month = 31

        if ins_month == 4 or ins_month == 6 or ins_month == 9 or ins_month == 11:
            now_month = 30

        elif ins_month == 2:
            if (ins_year % 4 == 0 and ins_year % 100 != 0) or ins_year % 400 == 0:
                now_month = 29

            else:
                now_month = 28

        if ins_year == year and ins_month == month:
            break

        ins_now_month += now_month
        ins_month += 1

        if ins_month > 12:
            ins_month = 1
            ins_year += 1

    wodIndex = (1 + ins_now_month) % 7

    return wodIndex, now_month
