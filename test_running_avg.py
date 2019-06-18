# prove or disprove:
# (((a+b)/2)+c)/2 == (a+b+c)/3
a=[]
b=None
j=0
last = None
for i in range(1,4):
    print(i)
    j+=1
    a.append(i)
    if b is not None:
        b=(b+i)/2.
    else:
        b=i
    last = i
s = sum(a)
a=sum(a)/float(j)
print('sum {}'.format(s))
print('a {}'.format(a))
print('b {}'.format(b))
assert a==b, 'disproven'