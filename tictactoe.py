print('\nX O game by Codemanga\n')
print('[1] | [2] | [3]')
print('____|_____|____')
print('    |     |   ')
print('[4] | [5] | [6]')
print('____|_____|____')
print('    |     |   ')
print('[7] | [8] | [9]')
print('\nlooking at the positions,give proper inputs :) \n')

# creating a 3x3 list of all zeros
list1=[],[],[]
list2=[],[],[]
list3=[],[],[]
data=[list1,list2,list3]

#arrangement of output with function
def display():
    print(' %s | %s  | %s ')%(data[0][0],data[0][1],data[0][2])
    print('_______|________|______')
    print('       |        |    ')
    print(' %s | %s  | %s ')%(data[1][0],data[1][1],data[1][2])
    print('_______|________|______')
    print('       |        |    ')
    print(' %s | %s  | %s  ')%(data[2][0],data[2][1],data[2][2])

#display()


#getting user input and machine digit randomization
import random
import sys
options = ['x','o']
l1 = [1,2,3,4,5,6,7,8,9]
l2 = [data[0][0],data[0][1],data[0][2],data[1][0],data[1][1],data[1][2],data[2][0],data[2][1],data[2][2]]

for a in range(5):
#machine random position and input
    #m_p1 = random.randrange(0,9)
    #m_p2 = random.randrange(0,9)
    
    user_position = input('Enter position : ')
    user_option = raw_input('Enter x or o :')
    if user_option == 'x':
        m_option = 'o'
    else:
        m_option = 'x'
    
    #cases
    if user_position != None:
        l2[user_position-1].append(user_option)
        
        #data[2][2].append(user_option)
        m_p1 = random.randrange(0,9)
        #m_p2 = random.randrange(0,9)
        if len(l2[m_p1]) == 0:
            l2[m_p1].append(m_option)
        else:
            m_p1 = random.randrange(0,9)
            #m_p2 = random.randrange(0,3)
            if len(l2[m_p1]) == 0:
                l2[m_p1].append(m_option)


    display()
    win=3
    def status(user_option):
        
        if [l2[0],l2[1],l2[2]] == [user_option,user_option,user_option]:
            win=1
        elif [l2[3],l2[4],l2[5]] == [user_option,user_option,user_option]:
            win=1
        elif [l2[6],l2[7],l2[8]] == [user_option,user_option,user_option]:
            win=1
        elif [l2[0],l2[3],l2[6]] == [user_option,user_option,user_option]:
            win=1
        elif [l2[1],l2[4],l2[7]] == [user_option,user_option,user_option]:
            win=1
        elif [l2[2],l2[5],l2[8]] == [user_option,user_option,user_option]:
            win=1
        elif [l2[0],l2[4],l2[8]] == [user_option,user_option,user_option]:
            win=1
        elif [l2[2],l2[4],l2[6]] == [user_option,user_option,user_option]:
            win=1
        else:
            win=0
        

        if win==1:
            print("\n*****  PLAYER WINS  *****\n")
        elif win==0:
            print("\n*****  DRAW for now  *****\n")
        if (win==1)==False and (win==0)==False:
            print("\n*****  MACHINE WINS  *****\n")
        
        if win==1:
            sys.exit()
        
    
    
    if a==3:
        status([user_option])
