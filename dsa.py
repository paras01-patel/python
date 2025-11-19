# # print reverse 


# s="Paras patel "
# print(s[::-1])


# # 2.palandrome

# def pal():
#     s="madam"
    
#     if s ==s[::-1]:
#         print("palendrome")
#     else:
#         print("not palindrome")
# pal()





# # 3.find maximum in list


# l=[1,2,3,4,56,6,7]
# print(max(l))



# # 4.sum of list element

# l=[1,2,3,4,5,6,7,8,9,10]
# print(sum(l))



# # 5.count voiwels

# n="paraspatel"
# v="aeiou"
# count=0
# for i in n:
#     if i in v:
#         count+=1
# print("count",count)




# # 6. maximum in thre number

# a,b,c=10,20,30
# print(max(a,b,c))


# # 7.factorial in 10 natural number

# n=10
# fac=1
# for i in range(1,n+1):
#     fac*=i
#     print(fac)
    
    
# 8. Largest element without using max()

# l=[1,2,3,4,5,6]
# largest=l[0]
# for i in l:
#     if i>largest:
#         largest=i
# print(largest)


# 9.count digits in a number 

# n = 123456
# count = 0

# while n > 0:
#     count += 1
#     n //= 10

# print("Digits:", count) 
    



# 10.second largest number

# l=[1,2,23,45,24,466]
# l.sort()
# print(l[-2])



# 11.even & odd 1 to 50

# for i in range(1,50+1):
#     if i %2==0:
#         print(i,"even")
    
    
    
# 12.count word in string

s="hello mister paras patel"
word=s.split()
print("words",len(word))