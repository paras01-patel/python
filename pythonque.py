# 1.natural number


# n=10
# for i in range(1,n+1):
#     print (i)


# 2.even number 

# n=int(input("enter a number"))
# for i in range(1,n+1):
#     if i %2 ==0:
#         print(i)


# 3. odd number 

# n=int(input("enter a number"))
# for i in range(1,n+1):
#     if i%2!=0:
#         print(i)


# 4.factor of given number

# n=int(input("enter a number"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)


# 5.factorial number

# n=int(input("enter a number = "))
# fact=1
# for i in range(1,n+1):
#     fact*=i
#     print(fact)


# 6.armstronge

n=int(input("enter a number"))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum+=digit **3
    temp//=10
if sum == n:
    print("armstronge")
else:
    print("not armstronge")