
#1
try:
    age = int(input("Enter your age: "))
    assert age >= 18, "Registration error: Participant must be at least 18 years old"
    assert age <= 60, "Registration error: Participant must be no older than 60 years old"
    print("Participant is eligible for registration.")
except AssertionError:
    print("Enter valid age")
#2
try:
    n1=int(input())
    n2=int(input())
    sum=n1+n2
    print(sum)
except ValueError:
    print("invalid literal for int() with base 10:")

#3
class NegativeWithdrawalError(Exception):
    pass

class InsufficientFundError(Exception):
    pass

am=int(input())
bal=int(input())
try:
    if am < 0:
        raise NegativeWithdrawalError("Error: Withdrawal amount cannot be negative.")
    elif am > bal:
        raise InsufficientFundError("Error: Insufficient funds in your account.")
    else:
        new_balance = bal - am
        print(f"Withdrawn successfully. Your new balance is {new_balance}")
except NegativeWithdrawalError as e:
    print(e)
except InsufficientFundError as e:
    print(e)


    
    
    
    
