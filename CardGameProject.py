from random import *

class Deck():
    def __init__(self, name):
        self.name = name
        self.cards = []
        
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
        
    def addCard(self, card):
        self.cards.append(card)
        return True
    
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
            matches[card.value].append(card)
            if len(matches[card.value]) == 4:
                for each in matches[card.value]:
                    removed.append(each)
                matches[card.value] = []
        for each in removed:
            self.removeCard(each)
        
        if len(removed) >= 1:
            print(self.name+" scored a set of "+str(removed[0].value)+"\'s")
            
        return removed
                
        
                
    def __str__(self):
        cardString = []
        for each in self.cards:
            cardString.append(str(each).split('\n'))
        
        output = ''
        for j in range (0, len(cardString[1])):
            for i in range(0, len(cardString)):
                output+= cardString[i][j]+ ' '
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
    
    def score(self):
        self.score+=1
    
    def getScore(self):
        return self.score
    
    def setDeck(self, deck):
        self.deck = deck
    
    def ask(self, name, card):
        result = []
        for each in self.deck.cards:
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
    
    def setOtherPlayers(self, players):
        for each in players:
            if self != each:
                self.otherPlayers.append(each)     
    
    #returns player to ask and which card to ask for 
    def getPlay(self):
        wanted = self.deck.mostAbundant()
        if self.mode == "Easy":
            if len(wanted[3]) != 0:
                card = wanted[3][0] 
            elif len(wanted[2]) != 0:
                card = wanted[2][0] 
            else:
                card = wanted[1][0]
            
            if len(self.otherPlayers) == 1:
                target = self.otherPlayers[0]
            else:
                target = self.otherPlayers[randint(0, len(self.otherPlayers)-1)]
            
            return target, card
            
        elif self.mode == "Med":
            return
        
        #mode == hard
        return 

class Memories:
    def __init__(self):
        self.memory = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[], 13:[]}
    
    def addMemory(self, asker, card):
        alreadyThere = False
        for each in self.memory[card]:
            if each == asker:
                alreadyThere = True
                break
        if not alreadyThere:
            self.memory[card].append(asker)
    
    def removeMemory(self, asker, card):
        if asker in self.memory[card]:
            self.memory[card].remove(asker)
    
    #Returns who asked for a certain value card
    def whoAsked(self, card):
        asked = self.memory[card]
        return asked
            
mem = Memories()
gPlayers = []

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
        print(each.name)
        print(each.deck)

    for each in players:
        if type(each) == Computer:
            each.setOtherPlayers(players)

    while discarded.getSize() < 52:    #Play the game while there are still cards to play 
        for p in players:              #Give each player a turn
            goFish = False
            while not goFish:          #While still not told to go fish
                if type(p) == Player:  #If human user's turn, not CPU
                    scored = p.deck.hasFour()
                    
                    for each in scored:#Discard 4 of a kind once scored
                        global mem
                        mem.removeMemory(p, each.value)
                        discarded.addCard(each)
                        
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
                        print("That's not a number!")
                        continue
                        
                else: #It is the CPU's turn
                    play = p.getPlay()
                    asked = play[0]
                    askedFor = play[1]
                
                global mem
                mem.addMemory(p, askedFor)
                    
                result = asked.ask(asked.name, askedFor)
                print(asked.name+", do you have any "+str(askedFor)+"\'s?")
                    
                if len(result) >= 1:  #If the CPU asked had what the user asked for
                    #Add the cards to the user's hand
                    print("Yes!\n")
                    for each in result:
                        p.deck.addCard(each)
                           
                else: # If the CPU did not have the card
                    goFish = True #End the player's turn
                    print("Go Fish!\n")
                    p.deck.addCard(sea.draw())                
                    
main()

#Changes to make:
#Med and Hard Modes
#Cannot ask for the same card back to back unless that is the only card they have
#organize cards, show score
# J, Q, K are numbers
#If CPU is out of cards, ask for random card
