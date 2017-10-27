print('\nX O game by Codemanga\n')
print(' 1  |  2  |  3')
print('____|_____|____')
print('    |     |   ')
print(' 4  |  5  |  6')
print('____|_____|____')
print('    |     |   ')
print(' 7  |  8  |  9')
print('\nlooking at the positions,give proper inputs :) \n')
# creating a list for appending numbers
list_empty = []
for i in range(1,10):
    list_empty.append(i)

def display():
    print(' %s  | %s   | %s ')%(list_empty[0],list_empty[1],list_empty[2])
    print('____|_____|____')
    print('    |     |    ')
    print(' %s  | %s   | %s ')%(list_empty[3],list_empty[4],list_empty[5])
    print('____|_____|____')
    print('    |     |    ')
    print(' %s  | %s   | %s ')%(list_empty[6],list_empty[7],list_empty[8])

win=0
#print list_empty
user_input = raw_input('Enter x or o :')
while win == 0:
    import random
    user_pos = input('ENTER POSITION : ')
    if type(list_empty[user_pos-1]) == str:
        print "\nInput given already has value stored,so invalid\n \nKindly re-execute the program\n"
    else:
        list_empty.pop(user_pos -1)
        list_empty.insert(user_pos - 1,user_input)
    if user_input =='x':
        #print ('user_pos',+user_pos)
        #print ('machine_pos',+machine_pos)
        machine_input = 'o'
    else:
        machine_input='x'
    #creating function for machine ,so to save 4 lines
    def machine(machine_input, machine_pos):
        list_empty.pop(machine_pos - 1)
        list_empty.insert(machine_pos - 1, machine_input)
    # inserting machine input and position
    machine_pos = random.randrange(1, 10)
    if type(list_empty[machine_pos - 1]) == str:
        machine_pos = random.randrange(1, 10)
        if type(list_empty[machine_pos - 1]) == str:
            machine_pos = random.randrange(1, 10)
        else:
            machine(machine_input, machine_pos)
    else:
        machine(machine_input, machine_pos)
    #checking status whether player won or not
    if list_empty[0:3] == [user_input, user_input, user_input]:
        win = 1
    elif list_empty[3:6] == [user_input, user_input, user_input]:
        win = 1
    elif list_empty[6:9] == [user_input, user_input, user_input]:
        win = 1
    elif [list_empty[0], list_empty[3], list_empty[6]] == [user_input, user_input, user_input]:
        win = 1
    elif [list_empty[1], list_empty[4], list_empty[7]] == [user_input, user_input, user_input]:
        win = 1
    elif [list_empty[2], list_empty[5], list_empty[8]] == [user_input, user_input, user_input]:
        win = 1
    elif [list_empty[0], list_empty[4], list_empty[8]] == [user_input, user_input, user_input]:
        win = 1
    elif [list_empty[2], list_empty[4], list_empty[6]] == [user_input, user_input, user_input]:
        win = 1
    else:
        win = 0
    #displaying the elements after inserting 'x' or 'o'
    display()
if win == 1:
    print("\n*****  PLAYER WINS  *****\n")
elif win == 0:
    print("\n*****  DRAW for now  *****\n")
if (win == 1) == False and (win == 0) == False:
    print("\n*****  MACHINE WINS  *****\n")
