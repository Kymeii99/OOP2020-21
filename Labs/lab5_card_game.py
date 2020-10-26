# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: B. Schoen-Phelan
# date: Oct 2020
# purpose: Lab 5 - GUI and card game using queue

from tkinter import *

# to use the queue FIFO
from queue import Queue

# to use the shuffle for shuffling the cards
from random import shuffle


class CardGame():

    # initialises the application
    def __init__(self):
        # set up game logic here:
        # shuffle the cards before first use
        # variable for holding the score
        self.player_score = 0
        self.the_cards = self.load_cards()
        self.init_window()

    # used by __init__
    # initialises the GUI window
    def init_window(self):
        root = Tk()
        root.geometry("300x200")
        root.title("Card Game")

        master_frame = Frame(master=root)
        master_frame.pack(expand=True)

        # frames hold the elements of the window
        # grid arranges the elements in a tabular manner
        # see mock-up screen in lab sheet for the layout design
        cards_frame = LabelFrame(master=master_frame)
        cards_frame.grid(row=0, column=0)
        button_frame = LabelFrame(master=master_frame)
        button_frame.grid(row=0, column=1)
        score_frame = LabelFrame(master=master_frame)
        score_frame.grid(row=1, column=0, columnspan=2)

        # add elements into the frames
        rand_card = self.the_cards.get()
        self.open_card = Button(cards_frame)
        the_card = PhotoImage(file='cards/' + rand_card + '.gif')  # need to be changed
        self.open_card.config(image=the_card)
        self.open_card.grid(row=0, column=0, padx=2, pady=2)
        self.open_card.photo = the_card

        closed_deck = Button(cards_frame)
        closed_card = PhotoImage(file='cards/closed_deck.gif')
        closed_deck.config(image=closed_card)
        closed_deck.grid(row=0, column=1, padx=2, pady=2)
        closed_deck.photo = closed_card

        done_button = Button(button_frame, text="I'm done!")
        done_button.grid(row=0, column=0, pady=12)
        new_game_button = Button(button_frame, text="New Game")
        new_game_button.grid(row=1, column=0, pady=13)
        exit_button = Button(button_frame, text="Exit", command=self.game_exit)
        exit_button.grid(row=2, column=0, pady=13)

        self.score_label = Label(score_frame, text="Your score: " + str(self.player_score), justify=LEFT)
        self.score_label.pack()

        root.mainloop()

    # called by the exit_button Button
    # ends the GUI application
    def game_exit(self):
        exit()

    # helper function to load the cards
    # puts everything in a list first as it needs to be shuffled
    # returns a queue
    def load_cards(self):
        cards = Queue(maxsize=52)  # change this if you want to use a different data structure
        suits = ("hearts", "diamonds", "spades", "clubs")
        people = ("queen", "jack", "king")
        card_list = []

        # your code goes here:
        # carddict = {'T': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'queen': 10,'jack': 10, 'king': 10}
        # dc = carddict.copy()
        #
        # Queue.put(dc)

        for suit in suits:
            for card in range(1, 11):  # number cards from 1 to 10
                card_list.append(str(card) + '_' + suit)

            for card in people:
                card_list.append(card + '_' + suit)

        shuffle(card_list)

        # your code goes here:
        for i in range(len(card_list)):
            cards.put(card_list[i])

        print(card_list)
        return cards
 
    # called when clicking on the closed deck of cards
    # picks a new card from the card FIFO
    # updates the display
    # updates the score
    def pick_card(self):
        # next_card = Queue.pop(0)
        # Queue.append(next_card)
        #
        # self.open_card.config(image=next_card[1])
        # self.open_card.photo = next_card[1]

        return next_card

        # pass  # replace this line by your code

    # contains the logic to compare if the score
    # is smaller, greater or equal to 21
    # sets a label
    def check_scores(self):
        # if self.player_score > 21:
        #     self.score_label.config(text="You're Busted!")
        #     self.game_exit()
        # elif self.player_score < 21:
        #     self.score_label.config(text="You can continue!")
        #
        # # pass  # replace this line by your code
        # self.score_label.update_idletasks()
        pass

    # calculates the new score
    # takes a card argument of type
    def update_score(self, card):
        # self.score_label.update_idletasks()
        pass

    # this method is called when the "Done" button is clicked
    # it means that the game is over and we check the score
    # but we don't allow any further game play. When clicking
    # on the closed deck after this button is pressed, nothing
    # should happen. Only options are to ask for a new game or
    # exit the program after this button was pressed.
    def done_playing(self):
        pass  # replace this line by your code

    # this method is called when the "New Game" button is clicked
    # resets all variables
    # sets the game's cards to the initial stage, with a freshly
    # shuffled card deck
    def reset_game(self):
        pass  # replace this line by your code


# object creation here:

app = CardGame()
