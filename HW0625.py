# Homework 1 (四則運算)
n1=int(input("Enter a Number: "))
n2=int(input("Enter a Number: "))
op=input("輸入運算符號：＋,-,*,/: ")
if op=="+":
    result=n1+n2
elif op=="-":
    result=n1-n2
elif op=="*":
    result=n1*n2
elif op=="/":
    result=n1/n2
print("運算結果等於",int(result))

# Homework2 （開根號）
n=int(input("輸入一個正數: "))
result=n**0.5
print("開根號結果: ",result)

# sum=0
# n=int(input("輸入一個正數"))
# 算整數平方根 9=>3, 25=>5, 8=>沒有
# 1,2,3,4,5
# 用小朋友一個個的計算方式，依賴電腦的計算速度

# Homework3 （99 乘法表）
# 印出 99 乘法表
n1=1
n2=1
result=0
while n1<=9:
    while n2<=9:
        result=n1*n2
        print(n1,"*",n2,"=",result)
        n2+=1
    n2=1
    n1+=1
else:
    print("..........Nice Work")
