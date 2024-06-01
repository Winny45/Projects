import csv
import random
usernumber = 1
player_number = 1

score_1 = 0
score_2 = 0
round_number = 1

data_1 = ""
data_2 = ""


def reading():
    r = open('account.csv','r')
    reader = csv.reader(r)
    r.close


def writing():
    w = open('account.csv','a')
    writer = csv.writer(w)
    w.close


#def login():
    #with open('account.csv', mode = 'r') as csvfile:
       # final_username = ""
      #  reader = csv.reader(csvfile, delimiter = ',', quotechar = '"')
     #   insert_username = input(str("enter username"))
    #    insert_password = input(str("enter  password"))
   #     search_UN_PA = ("%s   %s" % (insert_username, insert_password))
  #      print (search_UN_PA)
 #       line_num = 0
#        for row in reader:
          #  search_UN_PA_Test = (''.join(row))
         #   print (search_UN_PA_Test)
        #    if search_UN_PA_Test == search_UN_PA:
       #         print("yield")
            #playgame(login)
      #      elif row != search_UN_PA:
     #           line_num += 1
    #        elif line_num > 101:
   #             break
  #          else:
 #               print("Incorrect Username or Password please try again")
#                login()









def roll_P1(data_1,data_2,score_1,score_2,round_number):
    roll_number = random.randint(1,6)
    roll_number_2 = random.randint(1,6)
    print (data_1, "You rolled,", roll_number, "and", roll_number_2)
    addition = (roll_number + roll_number_2)
    print ("Your dice values add to",addition)
    even_odd = (addition % 2)
    if even_odd == 0:
        print ("Score = +10")
        score_1 += (addition + 10)

    elif even_odd == 1:
        print ("Score = -5")
        score_1 += (addition - 5)
    print ("Your total score is now", score_1)
    if roll_number == roll_number_2:
        bonus_roll_text = print(("BONUS ROLL FOR%s ") % (data_1))
        bonus_roll_P1 (data_1,data_2,score_1,score_2,round_number)

    game_2 (data_1,data_2,score_1,score_2,round_number)

def roll_P2(data_1,data_2,score_1,score_2,round_number):
    roll_number = random.randint(1,6)
    roll_number_2 = random.randint(1,6)
    print (data_2, "You rolled,", roll_number, "and", roll_number_2)
    addition = (roll_number + roll_number_2)
    print ("Your dice values add to",addition)
    even_odd = (addition % 2)
    if even_odd == 0:
        print ("Score = +10")
        score_2 += (addition + 10)

    elif even_odd == 1:
        print ("Score = -5")
        score_2 += (addition - 5)
    print ("Your total score is now", score_2)
    if roll_number == roll_number_2:
        bonus_roll_text = print(("BONUS ROLL FOR%s ") % (data_2))
        bonus_roll_P2 (data_1,data_2,score_1,score_2,round_number)
    round_number += 1
    if (round_number >= 6) and (score_1 != score_2):
        end(data_1,data_2,score_1,score_2,round_number)
    game_1(data_1,data_2,score_1,score_2,round_number)
    if (round_number >= 6) and (score_1 == score_2):
        game_1(data_1,data_2,score_1,score_2,round_number)


def bonus_roll_P1 (data_1,data_2,score_1,score_2,round_number):
    roll_login_text = (("%s To Roll your bonus dice, Press 1\n\
To go to the quit, Press 2") % (data_1))
    roll_dice = input(roll_login_text)
    if (roll_dice == "1"):
        roll_P1(data_1,data_2,score_1,score_2,round_number)
    elif roll_dice == "2":
        start()
    else:
        print("That is not a valid option please try again")
        bonus_roll_P1 (data_1,data_2,score_1,score_2,round_number)

def bonus_roll_P2 (data_1,data_2,score_1,score_2,round_number):
    roll_login_text = (("%s To Roll your bonus dice, Press 1\n\
To go to the quit, Press 2") % (data_2))
    roll_dice = input(roll_login_text)
    if (roll_dice == "1"):
        roll_P1(data_1,data_2,score_1,score_2,round_number)
    elif roll_dice == "2":
        start()
    else:
        print("That is not a valid option please try again")
        bonus_roll_P2 (data_1,data_2,score_1,score_2,round_number)




def game_1(data_1,data_2,score_1,score_2,round_number):
    print ("---------------------------------------")
    if round_number <= 5:
        print ("Round", round_number)
        roll_login_text = (("%s To Roll, Press 1\n\
To go to the main menu, Press 2") % (data_1))
        roll_dice = input(roll_login_text)
    elif round_number >= 6 and score_1 == score_2:
        print ("SUDDEN DEATH")
        roll_login_text = (("%s To Roll, Press 1\n\
To go to the main menu, Press 2") % (data_1))
        roll_dice = input(roll_login_text)


    if roll_dice == "1":
        roll_P1(data_1,data_2,score_1,score_2,round_number)
    elif roll_dice == "2":
        start()
    else:
        print("That is not a valid option please try again")
        game_1 (data_1,data_2,score_1,score_2,round_number)


def game_2(data_1,data_2,score_1,score_2,round_number):
    roll_login_text = (("%s To Roll, Press 1\n\
To go to the main menu, Press 2") % (data_2))

    roll_dice = input(roll_login_text)

    if (roll_dice == "1"):
        roll_P2(data_1,data_2,score_1,score_2,round_number)
    elif roll_dice == "2":
        start()
    else:
        print("That is not a valid option please try again")
        game_2(data_1,data_2,score_1,score_2,round_number)


def end (data_1,data_2,score_1,score_2,round_number):
    if score_1 > score_2:
        print (data_1, "Has won the game with a score of", score_1)
        print (data_2, "You ended the game with a score of", score_2)
        scoreboard(data_1,data_2,score_1,score_2,usernumber)
    elif score_2 > score_1:
        print (data_2, "Has won the game with a score of", score_2)
        print (data_1, "You ended the game with a score of", score_1)
        scoreboard(data_1,data_2,score_1,score_2,usernumber)
    end = int(input("Type 1 to play again\n\
        Type 2 to go back to the main menu\n\
        Type 3 to Quit"))
    if end == 1:
            score_1 = 0
            score_2 = 0
            round_number=0
            game_1 (data_1,data_2,score_1,score_2,round_number)
    elif end == 2:
        start()
    elif end == 3:
        exit()

def scoreboard(data_1,data_2,score_1,score_2,usernumber):
    while usernumber <= 2:
        username_1 = data_1
        username_2 = data_2
        user_1 = ""
        user_2 = ""
        scoreboard_check(username_1,user_1,username_2,user_2,usernumber,data_1,data_2,score_1,score_2)
    if (usernumber == 3):
        usernumber = 1
        print ("end")


def scoreboard_check_player_1(username_1,user_1,username_2,user_2,usernumber,data_1,data_2,score_1,score_2):
    with open ('account.csv', 'w') as board:
        fieldnames=['Username', 'Score']
        writer=csv.DictWriter(board, fieldnames=fieldnames)
        writer.writerow ({'Score':score_1})
        writer.writerow ({'Score':score_2})
        account.close

def scoreboard_check_player_2(username_1,user_1,username_2,user_2,usernumber,data_1,data_2,score_1,score_2):
    with open ('account.csv', 'w') as board:
        fieldnames=['Username', 'Score']
        writer=csv.DictWriter(board, fieldnames=fieldnames)
        writer.writerow ({'Score':score_2})
        account.close




def scoreboard_check(username_1,user_1,username_2,user_2,usernumber,data_1,data_2,score_1,score_2):
    print ("check login")
    read = open('account.csv','r')
    reader=csv.reader(read)
    row_number = 0
    for row in reader:
        while row != "":
            print("login checkin")
            if row:
                row_value = row[1]
                score_1_1 = 0
                score_1_2 = 0
                print ("yes")
            elif row_number == 0:
               header=row
            else:
               column_number=0
               for col in row:
                if (col == ""):
                    break
               for col in row:
                   if column_number == 0:
                       if (user_1 == col) or (user_2 == col):
                        column_number += 2

            if (data_1 == user_1) and(score_1_1 < score_1) and (usernumber == 1):
                score_1_1 = score_1
                 #  print (data_1)
                   #print(usernumber)
                usernumber += 1
                  # print("working")
                print (usernumber)
                print (data_1,"Your new highscore is",score_1)
                 #  print(data_1)2
                scoreboard_check_player_1(username_1,user_1,username_2,user_2,usernumber,data_1,data_2,score_1,score_2)

            elif (data_2 == user_2) and (score_2_1 < score_2) and (usernumber == 2):
               # print(username,user)
                score_1_1 = score_1
                  #  print (password,col)
                usernumber += 1
                print (data_2, "Your new highscore is", score_2)
                scoreboard_check_player_2(username_1,user_1,username_2,user_2,usernumber,data_1,data_2,score_1,score_2)



 #           else:
  #              print("I got here")
   #             row_number += 1
    #            print("row number",row_number)





































































def login(usernumber,data_1,data_2,score_1,score_2,round_number):
    if usernumber == 1:
        data_1 == ""
        data_2 == ""
    while usernumber <= 2:
        username_login_text = ("Enter your username for player %d" %(usernumber))
        password_login_text= ("Enter your password for player %d" % (usernumber))
        username = input(username_login_text)
        password = input (password_login_text)

        if (password ==  "") or (username == ""):
            print ("Please type at least 1 character in each field")
            login(usernumber,data_1,data_2,score_1,score_2,round_number)

        else:
            user = ""
            check_login(username,password,user,usernumber,data_1,data_2,score_1,score_2,round_number)
    if (usernumber == 3) and (data_1 != data_2):
        game_1(data_1,data_2,score_1,score_2,round_number)




def check_login(username,password,user,usernumber,data_1,data_2,score_1,score_2,round_number):
   # print ("check login")
    read = open('account.csv','r')
    reader=csv.reader(read)

    row_number = 0
    for row in reader:
            if row_number == 0:
               header=row
            else:
               column_number=0
               for col in row:
                   if column_number == 0:
                       user = col
                       column_number += 1

            if (username == user) and (usernumber == 1):
            #   print(username,user)
               if password==col:
                 #  print(password,col)
                   data_1 = username
                 #  print (data_1)
                   #print(usernumber)
                   usernumber += 1
                  # print("working")
                   print (usernumber)
                 #  print(data_1)
                   login (usernumber, data_1,data_2,score_1,score_2,round_number)




            elif (usernumber == 2) and (username == user) and (data_1 != data_2):
               # print(username,user)
                if password==col:
                  #  print (password,col)
                    data_2 = username
                    usernumber += 1
                  #  print(usernumber)
                  #  print(data_2)
                    login (usernumber,data_1,data_2,score_1,score_2,round_number)

            elif (data_1 == data_2) and (usernumber == 3):
                print("The username for player 1 and player 2 cannot be the same. Please start again")
                data_1 = ""
                data_2 = ""
                usernumber = 1
                return ("error")




            row_number += 1

    print("incorrect username and/or password")
    login(usernumber,data_1,data_2,score_1,score_2,round_number)




#print("Incorrect Username or password. Please Try Again")
#login(usernumber)


def Add_New_Username():
    username = input("Please enter your username")
    password = input("Please enter your password")
    password_2 = input("Please type your password again")
    if password == password_2:
        user = ""
        check_register(username,password,user)
    else:
        print("Your passwords are not the same please try again")
        Add_New_Username()
def write(username,password):
    with open ('account.csv', 'a') as account:
        fieldnames=['Username', 'Password']
        writer=csv.DictWriter(account, fieldnames=fieldnames)
        writer.writerow ({'Username':username,'Password':password})
        account.close




def check_register(username,password,user):
    read = open('account.csv','r')
    reader=csv.reader(read)

    row_number = 0
    for row in reader:
        if row_number == 0:
            header=row
        else:
            column_number=0
            for col in row:
                #print ('%-8s: %-s'% (header[column_number],col))
                if column_number == 0:
                    user = col
                #column_number += 1
               # if column_number == 100:
                #        break
        if username == user:
            print ("Username taken")
            Add_New_Username ()
    write(username,password)


def start():
    start = int(input("Would you like to login/register?\n\
        1. Login\n\
        2. Register\n\
        3, View Scoreboard\n\
        4. Quit D:\n\
        "))
    if start == 1:
        login(usernumber,data_1,data_2,score_1,score_2,round_number)
    elif start == 2:
        Add_New_Username()
    elif start == 3:
        print("In Progress")

    elif start == 4:
        exit()

    else:
        print ("That's not a valid option")
        start()
start()