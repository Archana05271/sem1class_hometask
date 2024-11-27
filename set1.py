s={10,20,20,30,40}
s.add(70)#to include a data in the set
print(s)
#bool
s1={}
text=""
print(bool(s1))
print(bool(s))
print(bool(text))

s2={100,200,300}
s.update(s1)#join s1 set to s(set)
print(s)

s.remove(20)
s.discard(20)
print(s)

s.pop()
print(s)

s.clear()
print(s)

del(s)
print(s)

