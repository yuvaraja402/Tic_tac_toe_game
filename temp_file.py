list_empty = []
for i in range(1,10):
    list_empty.append(i)
print list_empty

list_empty[3:6]= 'x','x','x'
print list_empty

user_input = 'x'

print list_empty[3],list_empty[4],list_empty[5] == [user_input,user_input,user_input]

while list_empty[3]=='x':
    print 'yeah'
    break