# Ex2: Given a list, extract all elements whose frequency is greater than k.
data2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = 3

new_data2= {}
for i in data2:
    if i in new_data2:
        new_data2[i]+=1
    else:
        new_data2[i]=1

result = []
for x, y in new_data2.items():
    if y>k:
        result.append(x)
print(result)