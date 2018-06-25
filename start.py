# 3.5
# # print(資料)
# print(3.5)
# # 字串
# "任意文字"
# print("hahaha")
# # 布林值
# True
# False
# print(True)
# # 變數 (可以被覆蓋); >> 程式真正能夠操作的只有資料 <<
# input=3
# print(input)
# input="hello World"
# print(input)
# 運算符號; 兩個斜線 // 是整數除法; 兩個星星 ** 是次方
# data=5//2
# print(data)
# data=6**3
# print(data)
# print ("hello"+"world")
# input (提示文字) 以 [字串的型態] 取得使用者輸入
# n1=input("Enter a Number:")
# n2=input("Enter a Number:")
# n1=int(n1) #int(資料) 將資料轉換成數字型態
# n2=int(n2)
# result=n1+n2
# print(result)
# 讓使用者輸入5個數字; 1. 算總和？ 2. 哪個數字最大?
n1=input("Enter Number 1:")
n2=input("Enter Number 2:")
n3=input("Enter Number 3:")
n4=input("Enter Number 4:")
n5=input("Enter Number 5:")
n1=int(n1)
n2=int(n2)
n3=int(n3)
n4=int(n4)
n5=int(n5)
list1=[n1,n2,n3,n4,n5]
print ("Sum=",sum(list1),"and Max=",max(list1))
# 使用 list 列表處理 