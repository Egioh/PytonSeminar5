data="aaaaaabbbbbccccccdfggrrttttdd"
count =1
temp =""
cod=""
for char in data:
    if char!=temp:
        if temp:
            cod+=str(count)+temp
        count=1
        temp = char
    else:
        count+=1
cod += str(count)+temp
print(data)
print(cod)
decoded=""
for i in range(0,len(cod),2):
    decoded+=int(cod[i])*cod[i+1]
print(decoded)


