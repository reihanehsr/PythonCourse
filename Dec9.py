# learning about lists
a = list()
b = [1,2,3]
print (a,b)

print (b[0])
# print (b[4])

c = ['x','y', 10, 20,'z']
# slicing
print (c[2:])
print (c[0:])
print (c[0:2+1])
print (c[::-1])

# appending
b.append(5)
print (b)

# poping
b.pop()
print(b)

# length
print (len (b))

print (b+c)

d = [0]
print (d *10)

# repetition
e = ["Reihaneh"]*4
print (e)
print (e *4)

f = "a"*16
print (f)

# Membership
print ( 1 in b)
print (17 in b)

# max/min
print (min(b))
print (max(b))

g = ['a','b','q','v',"q"]
print (min(g))
print (max(g))

# insertion
g.insert(2,'j')
print(g)

# counting
h = g.count('q')
print (h)

#index
i = g.index("v")
print(i)

j = b.index(2)
print(j)

# remove
c.remove(10)
print(c)

# reverse
c.reverse ()
print (c)

#sort
b.sort ()
print (b)

g.sort()
print (g)

# for loop
for k in g:
    print(k)

# while
counter = 0
while counter < len(g):
    print(counter)
    counter += 1