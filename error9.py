#1
import array as arr
sal=arr.array('i',[1200, 1500, 1100, 1700, 1600, 1800, 1300, 1900, 1750, 
1600, 1400, 1500])
print(sal[6])
new=sal.tolist()
new.reverse()
rev_sales=arr.array('i',new)
print(rev_sales)
sal1=[1600,1700]
sal2=sal.extend(sal1)
print(sal.tolist())

#2
import array as arr
sc=arr.array('i',[98,67,55,45,63,55,34,78,90,23])#a
sc.remove(63)
sc.insert(4,87)#b
for i in sc:
    print(i,end=" ")

print("\nHighest Score=",sc[0])#c
print("Lowest Score=",sc[9])#d
#3
import array as arr

prices = arr.array('d', [10.99, 5.49, 20.00, 7.95, 12.75])#a
print(prices)

total_cost = sum(prices)
print(total_cost)#b

del prices[1]
print("Prices after removing 2nd item:", prices)#c

prices.append(9.99)
print("Prices after adding new item:", prices)#d




