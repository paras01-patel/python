# 1.list ka sum(without sum() )


l=[1,2,3,4,5,5]
sum=0
for i in l:
    sum+=i
print("sum = ",sum)


# 2. mix, min (without min(),max())


l=[323,4,43,5332,236]
min1=l[0]
min2=l[0]
for i in l:
    if i > min1:
        min1=i
    if i< min2:
        min2=i
print("max",min1)
print("min",min2)


# 3. Reverse list (without reverse(), slicing)
l = [1, 2, 3, 4]
rev = []

for i in l:
    rev = [i] + rev

print(rev)


# 4.count even and odd


l=[1,2,3,4,5,6,7,8,9,10]
even=0
odd=0
for i in l:
    if i%2==0:
        even+=1
    if i%2!=0:
        odd+=1
print("even",even)
print("odd",odd)


# 5.marge two list 

a=[1,2,3]
b=[4,5,6]
for i in b:
    a.append(i)
print(a)

# 6.second largest number in list

l=[10,34,45,2,234]
lar=max(l)
l.remove(lar)
second=max(l)
print(second)


# 7.present elment in list 


n=[4,23,34,34,5,34453,30]
x=30
# found=False

for i in n:
    if i == x:
        found=True
        break
print(found)


