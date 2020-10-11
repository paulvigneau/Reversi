from localGame import *

from RandomPlayer import RandomPlayer

from playerV4 import playerV4
from processPlayerV3 import processPlayerV3

from itertools import permutations
from datetime import datetime
import os

def benchmark(n,players,writeToFile=False):
    
    matches = list(permutations(players,2))
    data = []
    for match in matches:       
        print(match[0].getPlayerName()," vs ",match[1].getPlayerName())
        matchData = [0,0,0]
        for j in range(0,n):
            players = []
            player1 = match[0]
            player2 = match[1]
            players.append(player1)
            players.append(player2)
            result = localGame(players)
            matchData[result] +=1
            players.clear()
            print("Game ",j+1," done")
        data.append(matchData)
    if(writeToFile):
        now = datetime.now()
        filename = "data/data-"+now.strftime("%d-%m-%Y")+".txt"
        if not os.path.exists("data"):
            os.mkdir("data")
        dataFile = open(filename,"a")
        dataFile.write("On the "+ now.strftime("%d-%m-%Y %H:%M:%S")+"\n")
    for i in range(0,len(matches)):
        
        black = matches[i][0]
        white = matches[i][1]
        if(writeToFile):
            header = "===[Results of " + black.getPlayerName()  + " vs " + white.getPlayerName() + "]===\n"
            dataFile.write(header)
        else:
            print("===[Results of ",black.getPlayerName()," vs ",white.getPlayerName(),"]===")
        blackWins = data[i][2]
        whiteWins = data[i][1]
        draws = data[i][0]
        blackRate = (blackWins/n)*100
        whiteRate = (whiteWins/n)*100
        drawRate = (draws/n)*100
        if(writeToFile):
            dataFile.write("%s won %d %% (%d) of the time\n" % (black.getPlayerName(), blackRate,blackWins))
            dataFile.write("%s won %d %% (%d) of the time\n" % (white.getPlayerName(), whiteRate,whiteWins))
            dataFile.write("Draw %d %% (%d) of the time\n" % (drawRate,draws))
            dataFile.write("===============================\n")
            
        else:
            print("%s won %d %% (%d) of the time" % (black.getPlayerName(), blackRate,blackWins))
            print("%s won %d %% (%d) of the time" % (white.getPlayerName(), whiteRate,whiteWins))
            print("Draw %d %% (%d) of the time" % (drawRate,draws))
            print("===============================")
        
    if(writeToFile):
        dataFile.write("\n")
        dataFile.close()

    
n = 20

missingno = RandomPlayer()


raikou = processPlayerV3()
suicune = playerV4()


players = []
players.append(missingno)
players.append(suicune)




benchmark(n,players,writeToFile=True) #enables result to be written to a file
# benchmark(n,players)