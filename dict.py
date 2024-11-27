d={"Name":"Geetha","Age":35,"degree":"B.tech,M.Tech"}
d.update({"Age":35})#updates already available data.
d.update({"Name":"Dia"})
print(d)

d["last name"] ="Dinesh"
print(d)

d.pop("Name")#remove the mentioned key from the dict.
print(d)

d.popitem()#removes the last inserted(undo)
print(d)

for i in d:
    print(i)#display the keynames in a line

for i in d:#display values in new line.
   print(d[i])
   
for i in d.values:#display values in new line.
    print(i)
 
for i in d.key:#display keynames in new line.
    print(i)

