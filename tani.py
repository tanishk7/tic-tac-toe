board = {'7':'7','8':'8','9':'9','4':'4','5':'5','6':'6','1':'1','2':'2','3':'3'}
def printboard():
 print(board['7'] + '|' + board['8'] + '|' + board['9'])
 print('-+-+-')
 print(board['4'] + '|' + board['5'] + '|' + board['6'])
 print('-+-+-')
 print(board['1'] + '|' + board['2'] + '|' + board['3'])
printboard()
def game():
    print('Lets roll it!!')
    print('Here we go')
    while True:
        player1 = input('player1 decide what you want to choose X or 0')
        if player1 == 'X' or player1 == '0':
            break
        else :
            print('wrong input: please renter')
    if player1 == 'X':
       player2 = '0'
       print('ohk so player2 you have assigned 0')
    else:
        player2 ='X'
        print('ohk so player2 you have assigned X')
    l = []
    for i in range(0,9):
        location = input('Enter the location')
        while (int(location) not in range(1, 10) or location in l):
           location = input('wrong input/repeated input: please enter again ')
        l.append(location)

        if(i==0 or i == 2 or i==4 or i==6 or i==8):
            board[location] = player1
        else: #2235789
            board[location] = player2
        printboard()
        if(board['7'] == board['8'] == board['9'] == player1 or board['4'] == board['5'] == board['6'] == player1):
            print('winner - player1')
            exit()
        if (board['7'] == board['8'] == board['9'] == player2 or board['2'] == board['5'] == board['8'] == player2):
            print('winner - player2')
            exit()
        if (board['1'] == board['4'] == board['7'] == player2 or board['1'] == board['2'] == board['3'] == player2 or board['4'] == board['5'] == board['6'] == player2 ):
            print('winner - player2')
            exit()
        if (board['2'] == board['5'] == board['8'] == player1 or board['1'] == board['4'] == board['7'] == player1 or board['1'] == board['2'] == board['3'] == player1):
            print('winner - player1')
            exit()
        if (board['7'] == board['5'] == board['3'] == player1 or board['1'] == board['5'] == board['9'] == player1 or board['3'] == board['6'] == board['9'] == player1):
            print('winner - player1')
            exit()
        if (board['7'] == board['5'] == board['3'] == player2 or board['1'] == board['5'] == board['9'] == player2 or board['3'] == board['6'] == board['9'] == player2):
            print('winner - player2')
            exit()
    print('Match is tied')
game()




