from random import randint
from re import T

bord = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
valid_input=[' ',1,2,3,4,5,6,7,8,9]
player1_info = ['','']
player2_info = ['','']
count=0
player_turn=1
playing = True


def init():
    global count , player_turn , playing, bord, valid_input , player1_info , player2_info
    bord = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    valid_input=[' ',1,2,3,4,5,6,7,8,9]
    player1_info = ['','']
    player2_info = ['','']
    count=0
    player_turn=1
    playing = True


def display(l,r):
    line1='-------------                -------------'
    line2=f'| {l[1]} | {l[2]} | {l[3]} |                | {r[1]} | {r[2]} | {r[3]} |'
    line3='-------------                -------------'
    line4=f'| {l[4]} | {l[5]} | {l[6]} |                | {r[4]} | {r[5]} | {r[6]} |'
    line5='-------------                -------------'
    line6=f'| {l[7]} | {l[8]} | {l[9]} |                | {r[7]} | {r[8]} | {r[9]} |'
    line7=f'-------------                -------------'
    print('\n'*20)
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    print(line6)
    print(line7)
def player_info():
    player1_info[0]=input('Enter first player name : ')
    while True:
        player1_info[1]=input('Choose X or O : ')
        if player1_info[1]=='x' or player1_info[1]=='o':
            break
        else :
            print('INVALID VALUE')
    player2_info[0]=input('Enter second player name : ')
    if player1_info[1]=='x':
        player2_info[1]='o'
    else:
        player2_info[1]='x'
def player_input():
    global count
    count +=1
    if player_turn ==1:
        print(f'player 1 {player1_info[0]} turn')
    else :
        print(f'player 2 {player2_info[0]} turn')
    while True:
        try:
            result=int(input('choose a cell from displayng bord : '))
        except:
            print('please enter a valid cell !! try again')
        else:
            if result in valid_input :
                valid_input[result]=' '
                return result
            else : 
                print('please enter a valid cell !! try again')
def set_bord(index , player_turn , bord):
    if player_turn ==1:
        bord[index]= player1_info[1]
    else : 
        bord[index]= player2_info[1]
    return bord
def switch_turn(turn):
    if player_turn == 1:
        return 2
    else :
        return 1
def check_winner(bord):

    if bord[1] == bord [2] == bord[3] != ' ':
        return True
    elif bord[4] == bord [5] == bord[6] != ' ':
        return True
    elif bord[7] == bord [8] == bord[9] != ' ':
        return True
    elif bord[1] == bord [4] == bord[7] != ' ':
        return True
    elif bord[2] == bord [5] == bord[8] != ' ':
        return True
    elif bord[3] == bord [6] == bord[9] != ' ':
        return True
    elif bord[1] == bord [5] == bord[9] != ' ':
        return True
    elif bord[3] == bord [5] == bord[7] != ' ':
        return True
    else : 
        return False

while playing :
    init()
    player_info()
    player_turn = randint(1,2)
    display(bord,valid_input)
    while True :
        index = player_input()
        bord = set_bord(index,player_turn, bord)
        display(bord,valid_input)
        if check_winner(bord):
            if player_turn == 1 :
                print(f'{player1_info[0]} is wooooon !!')
                break
            if player_turn == 2 :
                print(f'{player2_info[0]} is wooooon !!')
                break
        elif count >= 9 :
            print('no one wooon !!')
            break
        player_turn = switch_turn(player_turn)
        
    
    
                
            

    
            
        