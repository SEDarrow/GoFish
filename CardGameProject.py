from random import *
from time import sleep

class Deck():
    def __init__(self, name):
        self.name = name
        self.cards = []
    
    def __len__(self):
        return len(self.cards)
        
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
        
    def addCard(self, card):
        self.cards.append(card)
        return True
    
    def fix(self):
        new = []
        for each in self.cards:
            if each != None:
                new.append(each)
        self.cards = new
    
    def getSize(self):
        return len(self.cards)
    
    def removeCard(self, card):
        if(type(card) == Card):
            for i in range(len(self.cards)):
                if(self.cards[i] == card):
                    return self.cards.pop(i)
            return None
        elif(type(card)  == int):
            if card >= len(self.cards):
                return None
            return self.cards.pop(card)
        
    def makeDefaultDeck(self):
        self.cards = []
        suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        for suit in suits:
            for val in range(1, 14):
                self.cards.append(Card(suit, val))
    

    #Return a dictionary of how many of each value card there are
    def mostAbundant(self):
        cardAbundance = [0] *14
        for card in self.cards:
            if type(card) != Card:
                continue
            cardAbundance[card.value]+=1
        abundance = {3:[], 2:[], 1:[]}
        for i in range(1, len(cardAbundance)):
            try:
                abundance[cardAbundance[i]].append(i)
            except KeyError:
                continue
        return abundance
            
    
    def shuffle(self):
        newDeck = []
        size = len(self.cards)
        while len(newDeck) < size:
            if len(self.cards) ==1:
                element = self.cards[0]
            else:
                element = self.cards.pop(randint(0,len(self.cards)-1))
            newDeck.append(element)
        self.cards = newDeck
    
    #Removes cards delt from the deck and returns a list of decks delt
    def deal(self, piles, numCards=52):
        card = 0
        decks = [None]*piles
        for i in range(0,piles):
            decks[i] = Deck(str(i))
        card = 0
        while card < numCards and len(self.cards) >0:
            decks[card%piles].addCard(self.cards.pop(0))
            card+=1
        return decks
    
    def getSize(self):
        return len(self.cards)
    
    #removes 4 of a kind from the deck and returns a list of cards removed
    def hasFour(self):
        matches = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[], 13:[]}
        removed = []
        for card in self.cards:
            if type(card) != Card:
                continue
            matches[card.value].append(card)
            if len(matches[card.value]) == 4:
                for each in matches[card.value]:
                    removed.append(each)
                matches[card.value] = []
        for each in removed:
            self.removeCard(each)
        
        if len(removed) >= 1:
            scoredString = removed[0].value
            if scoredString == 11:
                scoredString = 'J'
            elif scoredString == 12:
                scoredString = "Q"
            elif scoredString == 13:
                scoredString = "K"
                
            print(self.name+" scored a set of "+str(scoredString)+"\'s\n")
            
        return removed
                
    def order(self):
        newCards = []
        for card in self.cards:
            inserted = False
            if len(newCards) == 0:
                newCards.append(card)
                continue
            for i in range(0, len(newCards)):
                if card.value < newCards[i].value:
                    newCards.insert(i, card)
                    inserted = True
                    break
            if not inserted:
                newCards.append(card)
        self.cards = newCards
                
            
                
    def __str__(self):
        self.order()
        cardString = []
    
        for i in range(0, len(self.cards)):
            if i%5 == 0:
                cardString.append([])
                j = i//5
            cardString[j].append(str(self.cards[i]).split('\n'))
                
        if len(cardString) == 0:
            return ''        
        
        output = ''
        for k in range(0, len(cardString)):
            for j in range (0, len(cardString[k][0])):
                for i in range(0, len(cardString[k])):
                    try:
                        output+= cardString[k][i][j]+ ' '
                    except:
                        continue
                output+= '\n'
        return output
    
    def draw(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop(0)
            
        
class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def __eq__(self, other):
        if type(self) != Card or type(other) != Card:
            return False
        if self.suit == other.suit and self.value == other.value:
            return True
        return False
        
    def __str__(self):
        if self.value == 1:
            number = [' 11 ', '111 ', ' 11 ', ' 11 ', '1111']
        elif self.value == 2:
            number = ['2222', '   2', '2222', '2   ', '2222']
        elif self.value == 3:
            number = ['3333', '   3', ' 333', '   3', '3333']           
        elif self.value == 4:
            number = ['4  4', '4  4', '4444', '   4', '   4']
        elif self.value == 5:
            number = ['5555', '5   ', '5555', '   5', '5555']
        elif self.value == 6:
            number = ['6666', '6   ', '6666', '6  6', '6666']          
        elif self.value == 7:
            number = ['7777', '   7', '  7 ', ' 7  ', '7   '] 
        elif self.value == 8:
            number = ['8888', '8  8', '8888', '8  8', '8888']           
        elif self.value == 9:
            number = ['9999', '9  9', '9999', '   9', '   9']  
        elif self.value == 10:
            number = ['1000', '10 0', '10 0', '10 0', '1000']
        elif self.value == 11:
            number = ['JJJJ', '  J ', '  J ', 'J J ', ' J  ']          
        elif self.value == 12:
            number = ['QQQQ', 'Q  Q', 'QQ Q', 'QQQQ', '  Q ']             
        else:
            number = ['K  K', 'K K ', 'KK  ', 'K K ', 'K  K']  
        
        if self.suit == "Diamonds":
            output = "*----------------*"+"\n"
            output+= "| /\\    /\\    /\\ |"+"\n"
            output+= "|//\\\\  /  \\  /* \\|"+"\n"
            output+= "|\\\\// /    \\ \\ */|"+"\n"
            output+= "| \\/ /      \\ \\/ |"+"\n"
            output+= "|   /        \\   |"+"\n"
            output+= "|  /   "+number[0]+"   \\  |"+"\n"
            output+= "| / /  "+number[1]+"  \\ \\ |"+"\n"
            output+= "|* >   "+number[2]+"   < *|"+"\n"
            output+= "| \\ \\  "+number[3]+"  / / |"+"\n"
            output+= "|  \\   "+number[4]+"   /  |"+"\n"
            output+= "|   \\        /   |"+"\n"
            output+= "| /\\ \\      / /\\ |"+"\n"
            output+= "|/* \\ \\    / //\\\|"+"\n"
            output+= "|\\ */  \\  /  \\\\//|"+"\n"
            output+= "| \\/    \\/    \\/ |"+"\n"
            output+= "*----------------*"+"\n"
        else: #self.suit == "Hearts": SHOULD BE AN ELIF
            output = "*----------------*"+"\n"
            output+= "|<3 _        _ <3|"+"\n"
            output+= "|  / \ /\\/\\ / \\  |"+"\n"
            output+= "| /   \\\\**//   \\ |"+"\n"
            output+= "||     \\\\//     ||"+"\n"
            output+= "||      \\/      ||"+"\n"
            output+= "||     "+number[0]+"     ||"+"\n"
            output+= "||     "+number[1]+"     ||"+"\n"
            output+= "||     "+number[2]+"     ||"+"\n"
            output+= "| \\    "+number[3]+"    / |"+"\n"
            output+= "|\\ \\   "+number[4]+"   / /|"+"\n"
            output+= "|*\\ \\        / /*|"+"\n"
            output+= "|\\*\\ \\      / /*/|"+"\n"
            output+= "| \\*\\ \\    / /*/ |"+"\n"
            output+= "|  \\*\\ \\  / /*/  |"+"\n"
            output+= "|<3 \\*\\ \\/ /*/ <3|"+"\n"
            output+= "*----------------*"+"\n"            
        #else:
            #output = self.suit + ' ' +str(self.value)
        return output

class Player:
    def __init__(self, name):
        self.score = 0
        self.name = name
        self.deck = Deck(name)
    
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def getScore(self):
        return self.score
    
    def setDeck(self, deck):
        self.deck = deck
    
    def ask(self, name, card):
        result = []
        for each in self.deck.cards:
            if type(each) != Card:
                continue            
            if each.value == card:
                result.append(each)
        
        for each in result:
            self.deck.removeCard(each)
        
        return result
        
class Computer(Player):
    names = ["Carl", "Cameron", "Claire", "Cass", "Cody"]
    def __init__ (self, mode):
        self.mode = mode
        name = self.names.pop(randint(0, len(self.names)-1))
        super().__init__(name)
        self.otherPlayers = []
        self.lastCard = -1
        self.memory = []
        
    
    def setOtherPlayers(self, players):
        for each in players:
            if self != each:
                self.otherPlayers.append(each)
            self.memory.append(PlayerData(each))
        
    #After someone asks for a card, the probability that each person has each card is updated
    def updateMemories(self, asker, number, asked, result):
        for i in range(len(self.memory)):
            if self.memory[i].player == asker:
                asker = i
            elif self.memory[i].player == asked:
                asked = i
        
        self.memory[asked].update(number, [0, 0, 0])
        prob = [None, None, None]
        for each in range(1, result+1):
            prob[each-1] = 1

        if result <= 2:
            if self.memory[asker].numbers[number-1].data[result] != 1:
                prob[result] = .99
        self.memory[asker].update(number, prob)
        
        self.updateOwnMemory()
        
        for card in range(1, 14):
            x = self.numCardsFound(card) #I know where x number of (card) cards are
            global cardsInDeck
            for p in self.memory:
                if p.player == self:
                    continue
                numCardsNotKnown = self.getUnknown(p) #How many of their cards could be a certain card
                totalUnknown = 0 #How many of all players cards are unknown
                doesntHave = self.getDoesntHave(p, card) #Cards known that the player doesn't have
                for p2 in self.memory:
                    totalUnknown+= self.getUnknown(p)
                for amount in range(1, 4):
                    if p.numbers[card-1].data[amount-1] >= .99 or p.numbers[card-1].data[amount-1] == 0:
                        continue
                    elif p.numbers[card-1].data[amount-1] == None:
                        break
                    if amount == 1:
                        prob = (4-x)*numCardsNotKnown/(totalUnknown+cardsInDeck-doesntHave)
                        p.numbers[card-1].data[amount-1] = prob
                    if amount == 2:
                        prob = (3-x)*(numCardsNotKnown-1)/(totalUnknown+cardsInDeck-1-doesntHave)
                        if prob < 0:
                            prob = 0
                        p.numbers[card-1].data[amount-1] = prob*p.numbers[card-1].data[amount-2]
                    if amount == 3:
                        prob = prob = (2-x)*(numCardsNotKnown-2)/(totalUnknown+cardsInDeck-2-doesntHave)
                        if prob < 0:
                            prob = 0
                        p.numbers[card-1].data[amount-1] = prob*p.numbers[card-1].data[amount-3]
                                   
        for each in self.memory:
            print(each)
    
    #Number cards player doesn't have   
    def getDoesntHave(self, p, card): 
        total = 0
        for each in p.numbers:
            if each.number == card:
                continue
            for i in range (0, 3):
                if each.data[i] == 0:
                    if 4-self.numCardsFound(each)-i >= 0:
                        total += 4-self.numCardsFound(each.number)-i
        return total
    
    #Update memory after player p went fish indicating that they could have any card now
    def wentFish(self, p):
        for each in self.memory:
            if each.player == p:
                p = each
        for card in p.numbers:
            for amount in range(0, 3):
                if card.data[amount] == 0 and 4-self.numCardsFound(card) >= amount+1:
                    card.data[amount] = .1 ###
                    break
        return

    #How many of a certain card that has unknown ownership
    def numCardsFound(self, card):
        numFound = 0
        if type(card) != int:
            card = card.number
        for each in self.memory:
            for i in range(0, 3):
                if each.numbers[card-1].data[i] >= 0.99:
                    numFound += 1
        return numFound
    
    #Returns amount of cards player has that I don't know the value of
    def getUnknown(self, p):
        numUnknown = len(p.player.deck)
        for num in p.numbers:
            for amount in range(0, 3):
                if num.data[amount] >= 0.99:
                    numUnknown -= 1
        if numUnknown < 0:
            numUnknown = 0
        return numUnknown
    
    #Updates memory to indicate a set of cards has been scored, removing them from play
    def memoryAddScore(self, number):
        for each in self.memory:
            each.numbers[number-1].data = [None, None, None]
    
    def updateOwnMemory(self):
        for i in range(len(self.memory)):
            if self.memory[i].player == self:
                break
        self.memory[i].knownDeck(self.deck)
        
    
    #returns player to ask and which card to ask for 
    def getPlay(self):
        self.deck.fix()
        wanted = self.deck.mostAbundant()
        
        try:
            wanted[3].remove(self.lastCard)
        except:
            wanted[3] = wanted[3]
        try:
            wanted[2].remove(self.lastCard)
        except:
            wanted[2] = wanted[2]
        try:
            wanted[1].remove(self.lastCard)
        except:
            wanted[1] = wanted[1]
        
        if self.mode == "Easy":
            if len(self.deck.cards) == 1:
                card = self.deck.cards[0].value
            else:
                if len(wanted[3]) != 0:
                    card = wanted[3][0] 
                elif len(wanted[2]) != 0:
                    card = wanted[2][0] 
                elif len(wanted[1]) != 0:
                    card = wanted[1][0]
                else:
                    card = randint(1,13)
            
            if len(self.otherPlayers) == 1:
                target = self.otherPlayers[0]
            else:
                target = self.otherPlayers[randint(0, len(self.otherPlayers)-1)]
            
            self.lastCard = card
            return target, card
            
        elif self.mode == "Med":
            return
        
        #mode == hard
        return 

class PlayerData():
    class NumberData():
        def __init__ (self, number):
            self.number = number
            self.data = [0.1, 0.1, 0.1]
        
    def __init__(self, player):
        self.player = player
        self.numbers = []
        for each in range(1, 14):
            self.numbers.append(self.NumberData(each))
    
    def update(self, card, probability):
        for each in self.numbers:
            if each.number == card:
                for i in range(0, 3):
                    if probability[i] != None:
                        each.data[i] = probability[i]
                        
    def knownDeck(self, deck):
        for each in self.numbers:
            each.data = [0, 0, 0]
        for card in deck.cards:
            for each in range(0, 3):
                if self.numbers[card.value-1].data[each] != 100:
                    self.numbers[card.value-1].data[each] = 100
                    break
                
                        
    def __str__(self):
        output = self.player.name
        for each in self.numbers:
            output += '\n'+str(each.number)+ ' ' + str(each.data)
        
        return output
        
        
        
gPlayers = []
cardsNotScored = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
cardsInDeck = 52

def main():
    #Intro to game
    print(">( o)3 Welcome to GO FISH!!! >( o)3\n")
    difficulty = ''
    while difficulty != 'Easy' and difficulty != 'Med' and difficulty != 'Hard':
        difficulty = input("Choose a difficulty(Easy / Med / Hard): ")
    numPlayers = 0
    
    while numPlayers <= 1 or numPlayers > 4:
        try:
            numPlayers = int(input("How many players would you like? (max 4) "))
        except ValueError:
            numPlayers = 0
            
    name = input("What is your name? ")
    print("\nHi "+name+"! The game is starting!\n")
    
    sea = Deck("Sea")
    sea.makeDefaultDeck()
    sea.shuffle()
    
    #Creating a deck for everyone
    decks = sea.deal(numPlayers, numPlayers*5)
    
    #Creating a dictionary of players with their decks
    decks[0].setName(name)
    players = [Player(name)]
    players[0].setDeck(decks[0])
    for i in range(1, numPlayers):
        p = Computer(difficulty)
        decks[i].setName(p.getName())
        p.setDeck(decks[i])
        players.append(p)
    
    #Where cards go after scored    
    discarded = Deck("Discard")
    goFish = False

    for each in players:
        if type(each) == Computer:
            each.setOtherPlayers(players)

    while discarded.getSize() < 52:    #Play the game while there are still cards to play 
        print("Player:\t\tScore:\tNumber of Cards:")
        print("-------\t\t------\t----------------")
        for p in players:
            print(p.name+"\t\t"+str(p.score)+"\t"+str(p.deck.getSize()))
        print('')

            
        for p in players:              #Give each player a turn
            goFish = False
            p.deck.fix()
            while not goFish:          #While still not told to go fish
                if discarded.getSize() >= 52: 
                    break
                
                if type(p) == Player:  #If human user's turn, not CPU
                    sleep(2)
                    print(p.deck)
                    
                    if numPlayers >= 3:#If the user needs to specify who they are asking
                        asked = input("Who would you like to ask for a card? ")
                        
                        #Get the CPU object based on the name inputed
                        for each in players:
                            if each.name == asked:
                                asked = each
                        
                        #If there is no CPU by that name, ask again        
                        if type(asked) == str:
                            print("That is not a player!")
                            continue
                    else: #There are only 2 people playing, the user does not need to specify who they are asking
                        #Determine who the one other player is
                        if p == players[1]:
                            asked = players[0]
                        else:
                            asked = players[1]
                            
                    askedFor = input("Which number would you like to ask for? ")
                    
                    #Make sure the user acutally inputed a number
                    try:
                        askedFor = int(askedFor)
                        if askedFor > 13 or askedFor < 1:
                            raise ValueError
                    except ValueError:
                        if askedFor == 'J':
                            askedFor = 11
                        elif askedFor == 'Q':
                            askedFor = 12
                        elif askedFor == 'K':
                            askedFor = 13
                        else:
                            print("That's not a number!")
                            continue
                        
                else: #It is the CPU's turn
                    play = p.getPlay()
                    asked = play[0]
                    askedFor = play[1]
                    print(p.name, "asks:")
                
                    
                result = asked.ask(asked.name, askedFor)
                if askedFor == 11:
                    askedForString = 'J'
                elif askedFor == 12:
                    askedForString = 'Q'
                elif askedFor == 13:
                    askedForString = 'K'
                else:
                    askedForString = askedFor
                    
                print(asked.name+", do you have any "+str(askedForString)+"\'s?")
                    
                if len(result) >= 1:  #If the CPU asked had what the user asked for
                    #Add the cards to the user's hand
                    print("Yes!\n")                     

                    for each in result:
                        p.deck.addCard(each)
                           
                else: # If the CPU did not have the card
                    goFish = True #End the player's turn
                    
                    print("Go Fish!\n")
                    p.deck.addCard(sea.draw())
                    global cardsInDeck
                    cardsInDeck = len(sea)
                
                scored = p.deck.hasFour()
                
                for person in players:
                    if type(person) == Computer:
                        person.updateMemories(p, askedFor, asked, len(result))
                        if goFish and person != p:
                            person.wentFish(p)
    
                if len(scored) > 1:
                    p.score += 1
                    global cardsNotScored
                    cardsNotScored.remove(scored[1].value)
                    for person in players:
                        if type(person) == Computer:
                            person.memoryAddScore(scored[1].value)
                        
                for each in scored:#Discard 4 of a kind once scored
                    discarded.addCard(each) 
                    
                sleep(1)
    
    #Once game is over 
    winner = ("name", 0)
    print("Player:\t\tScore:")
    print("-------\t\t------")        
    for p in players:
        print(p.name+"\t\t"+str(p.score)+"\t")
        if p.score > winner[1]:
            winner = (p.name, p.score)
    print("Winner is", winner[0],"!!!")
main()

#Changes to make:
#Med and Hard Modes
#record what was asked for in CPU's turn so that it can never ask for same card from same person in same turn
#make cards shorter                                                                                                   