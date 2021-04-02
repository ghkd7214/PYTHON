bal = int(input("최초 계좌의 잔액을 입력하세요 :"))

def bank_account(bal):

    balance = bal

    def getBalance():
        return balance

    def deposit():
        y = int(input("입금액을 입력하세요 :"))
        nonlocal balance
        balance += y
        print("입금후 잔액은", balance, "원 입니다")

    def withdraw():

        z = int(input("출금액을 입력하세요 :"))
        nonlocal balance
        if balance < z:
            print("잔액이 부족합니다.")
        else:
            balance -= z
            print("출금후 잔액은", balance, "원 입니다")

    return getBalance, deposit, withdraw


bank_account(1000)
getBalance, deposit, withdraw = bank_account(bal)

getBalance()
deposit()
withdraw()

