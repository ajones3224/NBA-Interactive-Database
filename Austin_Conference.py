import sqlite3

db = sqlite3.connect('DataForConference.db')

cursor = db.cursor()

##Austin "Stin" Jones NBA Database



def repl():
    while True:

        x = input("\n Welcome to the Austin NBA DATABASE, \n Here are you options \n 1. Elite_Scorers \n 2. theclub \n 3. AveragePoints \n 4. findteammates \n 5. tripledoubles \n 6. top10scorers \n"      
                  " 7. top10assists \n 8. top10rebounds \n 9. top10steals \n 10.Average_for_theyear \n 11.Season_high \n 12.over20over50 \n 13.players_who_scored_40against_eachother"
                  "\n 14.Quit \n Enter number Here:  ")                                    
        try:
            x= int(x)
        except:
            print("Not a number")

            
        if (x== 1):
            a =int(input(" Enter a number to find the players who have total career points above that number \n I recommend  choosing numbers greater than 15000 \n"))
            b = Elite_Scorers(a)
            for val in b:
                print(val +  "\n")
                
        elif (x==2):
            print(" These are the NBA Players who have shot 50 percent from the field, 40 percent from 3, and 90 Percent from the free throw line in a given season \n")
            club = theclub()
            for val in club:
                print(val +  "\n")
                
        elif(x==3):
            p1 = input(" Enter the name of a player who you want to know how much they averaged of their career. After typing the name add % to it \n")
            averpt = AveragePoints(p1)
            points = str(averpt[0])
            print(p1 + " averaged "+ points + " ppg over his career ")
            
        elif(x==4):
            year=int(input("Enter a year of whatever team you are looking for \n"))
            team = input("Enter the three letter abbreviaiton of the team you are looking for \n")
            teammates = findteammates(year,team)
            for val in teammates:
                 print(val)
                 
        elif( x==5):
            print(" These are the people who had a triple double during the 2016-2017 season")
            tripdoub = tripledoubles()
            for val in tripdoub:
                print(val)
                
        elif(x==6):
            print("These are the top 10 scorers in NBA history")
            scorer = top10scorers()
            for val in scorer:
                print(val)
                
        elif(x==7):
            print("These are the top 10 assists leaders in NBA history")
            dimers = top10assists()
            for val in dimers:
                print(val)
 
        elif(x==8):
            print(" These are the top 10 rebound leaders in NBA history")
            boards = top10rebounds()
            for val in boards:
                print(val)

        elif(x==9):
            print("These are the top 10 steals leaders in NBA history")
            theifs = top10steals()
            for val in theifs:
                print(val)
                
        elif(x==10):
            player = input(" Enter a player first and last name from the 2016-2017 \n")
            average = Average_for_theyear(player)
            stringpt= str(average[0])
            print(player + " averaged " + stringpt + " ppg for during the 2016-2017 season")
                  
        elif(x==11):
            player2 = input(" Enter a player first and last name from the 2016-2017 \n")
            high = Season_high(player2)
            h1= str(high[0])
            h2= str(high[1])
            print(h1 + " is the high for the season high and he scored it on " + h2 + " against " + high[2])
            
        elif(x==12):
            print(" Here are the players who have scored 50 points during the 2016-2017 season and have a career average of over 20 points")
            elite = over20over50()
            for val in elite:
                print(val + "\n")
                
        elif (x== 13):
            print("Here are the players who have scored 40 point agaisnt each other")
            double40 = players_who_scored_40against_eachother()
            for val in double40:
                print(val)
                  
        elif(x== 14):
            break



                   
        else:
                print( "Choose a number between 1 and 13")
                repl()
            
            
            
            
            
            
            
        
            
        
        
            
    
                                                                                                                                                                                            
        
    

def Elite_Scorers(points):
    """ Find all the scorers whose total points for their career is over the number entered"""

    global db
    cursor = db.cursor()
    q = "SELECT Player as hoopers FROM Seasons_Stats GROUP bY hoopers Having SUM(PTS) >?"
    scorers = set()
    cursor.execute(q, (points, ))
    for tup in cursor:
        scorers.add(tup[0])

    return scorers

def theclub():
    """ Finds he player who have shot 50 percent from the field,40 percent from three, 90 percent from the free throw line for a whole season"""
    global db
    cursor = db.cursor()
    club = set()
    q ="SELECT DISTINCT Player FROM Seasons_Stats WHERE FGpercentage >=.50 AND  threePpercentage >= .40 AND FTpercentage >=.90"
    cursor.execute(q)
    for tup in cursor:
        club.add(tup[0])
    
    return club

def AveragePoints(x):
    """ Find a player career average"""
    global db
    cursor = db.cursor()
    q = "SELECT sum(PTS) /sum(G), Player FROM Seasons_Stats  WHERE Player LIKE?"
    cursor.execute(q, (x,))
    average = []
    for tup in cursor:
        average.append(tup[0])
    
    
    return average


    
    


def findteammates(year,team ):
    """ Find all the players of a certain from that year"""
    
    global db
    cursor = db.cursor()
    teammates = []
    q = "SELECT Player FROM Seasons_Stats WHERE Year =? AND Tm =?"
    cursor.execute(q, (year,team ))
    for tup in cursor:
        teammates.append(tup[0])
    return teammates
    
        

def tripledoubles():
    """ All the players who recorded a triple double during the 2016-2017 season"""
    global db
    cursor = db.cursor()
    tb = []
    q = "SELECT DISTINCT playDispNm , opptAbbr FROM  _playerBoxScore20162107 WHERE playPTS >= 10 AND playAST>= 10 AND playTRB >= 10"
    cursor.execute(q)
    for tup in cursor:
        tb.append(tup[0])
        tb.append(tup[1])
        
       

    return tb



def top10scorers():
    """ A list of the top10 scorers of all time"""
    global db
    cursor = db.cursor()
    scorers= []
    s = "SELECT Player, sum(PTS) as scorers FROM Seasons_Stats GROUP By Player ORDER BY scorers DESC"
    cursor.execute(s)
    for tup in cursor:
        if len(scorers)< 20:
            scorers.append(tup[0])
            scorers.append(tup[1])
            
            
    return scorers
        

    

def top10assists():
    """ A lis of the top10 assist leaders of all time"""
    global db
    cursor = db.cursor()
    leaders = []
    a = "SELECT Player, sum(AST) AS total_assists FROM Seasons_Stats GROUP By Player ORDER BY total_assists DESC"
    cursor.execute(a)
    for tup in cursor:
        if len(leaders)< 20:
            leaders.append(tup[0])
            leaders.append(tup[1])
    return leaders
   
        

def top10rebounds():
    """ A list of the top10 rebound leaders of all time"""
    global db
    cursor = db.cursor()
    boardleaders = []
    r = "SELECT Player, sum(TRB) AS total_rebounds FROM Seasons_Stats GROUP By Player ORDER BY total_rebounds DESC"
    cursor.execute(r)
    for tup in cursor:
         if len(boardleaders)< 20:
             boardleaders.append(tup[0])
             boardleaders.append(tup[1])
    return boardleaders
        

                
def top10steals():
    """ A list of the top10 steal leaders of all time"""
    global db
    cursor = db.cursor()
    stl = []
    s = "SELECT Player, sum(STL) AS total_steals FROM Seasons_Stats GROUP By Player ORDER BY total_steals DESC"
    cursor.execute(s)
    for tup in cursor:
        if len(stl)< 20:
             stl.append(tup[0])
             stl.append(tup[1])
    return stl

def Average_for_theyear(name):
    """ How many points a player averaged during the 2016-2017 season"""
    global db
    cursor = db.cursor()
    average = []
    q = "SELECT playDispNm, sum(playPTS)/ count(playDispNm) FROM _playerBoxScore20162107  WHERE playDispNm =?"
    cursor.execute(q, (name,))
    for tup in cursor:
        average.append(tup[1])
        

    return average

def Season_high(Name):
    """ A player season high for the 2016-2017 season""" 
    global db
    cursor = db.cursor()
    high = []
    q = "SELECT Max(playPTS), gmDate, opptAbbr FROM _playerBoxScore20162107 Where playDispNm =?"
    cursor.execute(q, (Name,))
    for tup in cursor:
        high.append(tup[0])
        high.append(tup[1])
        high.append(tup[2])


    return high


    
     
    
def over20over50():
    """Finds the players who have scored over 50 points in a game during the 2016-2017 season and who have a career average over 20 points"""
    global db
    cursor = db.cursor()
    over20 = set()
    over50 = set()
    prod = "SELECT Player, sum(PTS)/ sum(G) as Buckets FROM  Seasons_Stats GROUP By Player HAVING buckets >= 20 Order By Buckets DESC"
    prod1 = "SELECT  playDispNm, playPTS as Points, teamAbbr FROM _playerBoxScore20162107 WHERE points >=50 ORDER By Points DESC"
    cursor.execute(prod)
    for tup in cursor:
        over20.add(tup[0])    
    cursor.execute(prod1)
    for tup in cursor:
        over50.add(tup[0])
    both = over20.intersection(over50)

    return both
    
        ## how to join the arrays

def players_who_scored_40against_eachother():
    """ Finds the players who have scored 40 against each other in the same game"""
    global db
    cursor = db.cursor()
    club40 = []
    q = "SELECT A.playDispNm, A.gmDate, A.playPTS , A. opptAbbr FROM _playerBoxScore20162107 as A, _playerBoxScore20162107 as B WHERE A.playPTS >= 40 AND B.playPTS >=40 AND A.gmDate = B.gmDate AND A.opptAbbr = B.teamAbbr"
    cursor.execute(q)
    for tup in cursor:
        club40.append(tup[0])
        club40.append(tup[1])
        club40.append(tup[2])
        club40.append(tup[3])
        

    return club40


if __name__ == "__main__":
    repl()
        
    
   
    
        


    


