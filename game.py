"""
 *****************************************************************************
   FILE:            game.py

   AUTHOR:          Truong

   ASSIGNMENT:      Project 10: Game: Boggle

   DATE:            11/14/18

   DESCRIPTION:     The program create a version of the Boggle board game. It
                    is different from the orginal version because on of the 
                    rule -- if two players submitted the same word, then the 
                    word will be cancel -- is not implemented. The program 
                    borrows the codes from the cs110graphics to display the 
                    board game as well as allow users to interact with the
                    program. The program also support to unlimited amount of
                    players and unlimited rounds of play. Each play of the
                    game will last for a minutes. At the end of the play,
                    the program is going to declare the winner of the game,
                    or if the game is tied.

 *****************************************************************************
"""

import random
from cs110graphics import *

def no_newlines(strings):
    """ Make a list of words, in which the word
        are not placed in the row style. """

    # Cite: Alistair Campbell
    # Desc: The code for editing a text file

    result = []
    for item in strings:
        result.append(item[:-1])
    return result

def uppercase_all(strings):
    """ Make all letters of a word uppercased, and do
        it for every word. """

    # Cite: Alistair Campbell
    # Desc: The code for editing a text file

    result = []
    for item in strings:
        result.append(item.upper())
    return result

def get_dictionary():
    """ Open the text profile, and edit it to make it
        usable for the game. """

    # Cite: Alistair Campbell
    # Desc: The code for editing a text file

    file = open("dictionary.txt")
    lines = file.readlines()
    file.close()
    lines = no_newlines(lines)
    return lines

class Player:
    """ A class representing the player in the game, building a
        player and its properties and characteristics. """

    def __init__(self, win, register):
        """ Define and construct characteristics and properties 
            of the player. """

        self._win = win           # The window in which the game is drawn
        self._status = False      # Use to check if the player is playing
        self._player = register   # Use to check which player is playing

    def activate(self):
        """ Activate the player so the player
            can play the game. """

        # Change the called player's status to active.
        self._status = True

    def deactivate(self):
        """ Deactivate the player so the player
            can play the game. """

        # Change the called player's status 
        # to not-active.
        self._status = False

    def get_status(self):
        """ Check the current state of the player,
            whether the player is active or not. """

        # Return the current state of the player.
        return self._status

    def identify(self):
        """ Identify the number that was registered to
            the called player. """

        # Return the value that was registered
        # to the called player.
        return self._player

class Interaction(EventHandler):
    """ A class for handling events for the Boggle program. """

    def __init__(self, clicked_box, game):
        """ Define and construct events that will occur when
        the user is playing with the program Boggle. """

        # Used to check the event that user 
        # make from the keyboard or the mouse.
        EventHandler.__init__(self)
        self._clicked_box = clicked_box  # The box that user click on
        self._game = game                # The master class that run 
                                         # the game

    def handle_mouse_enter(self, event):
        """ Change color of the border of either special
            buttons or tiles when user drag the mouse to 
            the button or tile. """

        self._clicked_box.change_border_color("#ffffff")

    def handle_mouse_leave(self, event):
        """ Return the orginal color of the border of 
            either special buttons or tiles when user s
            drag the mouse away from the button or tile. """

        self._clicked_box.change_border_color("#000000")

    def handle_key_press(self, event):
        """ Add the new selected word into a list of chosen words
            everytime the player hit the key "Enter" on the keyboard. """

        # If the key "Enter" is hit, add the new word to the playing
        # player's personal word list.
        if event.get_key() == "Return":
            self._game.record_selection()

    def handle_mouse_press(self, event):
        """ Create events when the user clicks either
            special buttons or tile. """

        # If the user hit the Boggle button, shuffle the dice faces, 
        # start the game, and run the clock.
        if self._clicked_box.get_location() == (245, 350) \
        and self._clicked_box.get_status() is True:
            if self._game.get_turn() < self._game.get_total_players():
                self._game.boggle()
                self._game.update_turn()
            else:
                self._game.show_winner()

        # If the user hit the Clear button, clear the current selected
        # letters, and allow user to chose new letters.
        if self._clicked_box.get_location() == (245, 520) \
        and self._clicked_box.get_status() is True:
            self._game.delete_selection()

        # If the user hit the tile, highlight the tile, deactivate the tile
        # so that the player cannot chose the same tile again
        if self._clicked_box.get_location() not in [(245, 520), (245, 350),
                                                    (708, 560), (849, 560)] \
        and self._clicked_box.get_status() is True:
            if self._game.neighbor_only(self._clicked_box) is True:
                self._clicked_box.change_fill_color("#e3cf57")
                self._clicked_box.update_status(False)
                self._game.update_tile_selection_order()

        # If user hit the yes button, reset the game and all of the
        # tool and program that's used to keep track of the game
        if self._clicked_box.get_location() == (708, 560) \
        and self._clicked_box.get_status() is True:
            self._game.play_again()

        # If user hit the no button, shut down the game and move
        # to a farewell screen
        if self._clicked_box.get_location() == (849, 560) \
        and self._clicked_box.get_status() is True:
            self._game.end_game()

class GameButton:
    """ A class representing all the special button in Boggle game
        board, building the buttons, and creating characteristic and
        properties for each button. """

    def __init__(self, win, width, height, center, text):
        """ Define and construct characteristics and properties 
            of all special buttons that allow user user to interact
            with the program Boggle. """

        self._win = win        # The windown that the button is drawn on
        self._width = width    # Use to adjust the width of the button
        self._height = height  # Use to adjust the height of the button
        self._center = center  # Use to adjust the location of the button
        self._text = text      # The text appears on the button
        self._status = True    # Use to keep track if the button is selected 
                               # or not

        # Make the button, set it to a specific color and
        # specific location, then make viewable on the gameboard
        self._button = Rectangle(self._win, self._width, 
                                 self._height, self._center)
        self._button.set_fill_color("#d6ba8b")
        self._button.set_border_color("#000000")
        self._button.set_depth(1)

        # Add the name of the button to the center of the button
        self._face = self.add_text(self._text, self._center)
        self._face.set_depth(0)

        # The properties and characteristics of the button
        self._parts = [self._button, self._face]

    def add_handler(self, handler):
        """ Provide call-back function for user interaction. """

        # Add handler for the button, user can interacter with it
        for part in self._parts:
            part.add_handler(handler)

    def add_text(self, text, location):
        """ Add a graphical text to the called button. """

        return Text(self._win, text, 24, location)

    def add_to_window(self):
        """ Add all the parts of the game special buttons
            (characteristics and properties) to the windown. """

        for part in self._parts:
            self._win.add(part)

    def change_border_color(self, color):
        """ Change the border color of the button to a
            desired color. """

        self._button.set_border_color(color)

    def change_fill_color(self, color):
        """ Change the color of the button 
            to a desired color. """

        self._button.set_fill_color(color)

    def change_face(self, face):
        """ Change the button face to the another face
            for all all possible purposes after all players
            are played. """

        self._face.set_text(face)
        self._face.set_depth(0)

    def get_location(self):
        """ Return the location (in pixel) 
            of the called button. """

        return self._center

    def get_status(self):
        """ Check if the called button 
            is clicked by the user. """

        return self._status

    def remove_from_window(self):
        """ Remove all the parts of the game special buttons
            (characteristics and properties) from the windown. """

        for part in self._parts:
            self._win.remove(part) 

    def update_status(self, status):
        """ Update the status (if the button is clicked by
            the user or not) of the button. """

        self._status = status

class Tile:
    """ A class representing all the lettered dice in the 
        Boggle game board, building each die, and creating 
        characteristic and properties for each die. """

    def __init__(self, win, width, height, center, nth_cube):
        """ Define and construct characteristics and properties 
            of the dice in the Boggle. """

        self._win = win          # The window that tile is drawn on
        self._width = width      # Use to adjust the width of the tile
        self._height = height    # Use to adjust the height of the tile
        self._center = center    # Use to adjust the location of the tile
        self._loc = nth_cube     # Use to find the location of the tile
                                 # within the grid
        self._text = ""          # The text that appeared on the tile
        self._status = False     # Use to check if the tile is selected
        self._selecting_order = 0   # Use to keep track how long had the
                                    # tile been selected in a selection

        # Tile have a square shape and is colored with the similar color
        # to all the game button
        self._tile = Square(self._win, self._width, self._center)
        self._tile.set_fill_color("#d6ba8b")
        self._tile.set_border_color("#000000")
        self._tile.set_depth(1)

        # Add a letter to the center of the tile
        self._face = self.add_face(self._center)
        self._face.set_depth(5)

        # The tile characteristics
        self._parts = [self._tile, self._face]

    def add_face(self, location):
        """ Put a text on the called tile. """

        return Text(self._win, self.random_text(), 24, location)

    def add_handler(self, handler):
        """ Provide call-back function for user interaction. """

        for part in self._parts:
            part.add_handler(handler)

    def add_to_window(self):
        """ Add all the parts of the game dice (characteristics
            and properties) to the windown. """

        for part in self._parts:
            self._win.add(part)
    
    def change_fill_color(self, color):
        """ Change the color of the tile to a desired color. """

        self._tile.set_fill_color(color)

    def change_border_color(self, color):
        """ Change the border color of the tile to a 
            desired color. """

        self._tile.set_border_color(color)

    def clear_selecting_order(self):
        """ Reset the selecting count of all tile
            to prepare for another submission. """

        self._selecting_order = 0

    def get_center(self):
        """ Return the location (in pixel) 
            of the called tile. """

        return self._center

    def get_face(self):
        """ Return the letter that is shown 
            on the called tile. """

        return self._text

    def get_location(self):
        """ Return the location of the called tile 
            in the grid of tiles. """

        return self._loc

    def get_selecting_order(self):
        """ Return the selecting count of a tile. """
        
        return self._selecting_order

    def get_status(self):
        """ Check if the called tile is clicked by the user. """

        return self._status

    def random_text(self):
        """ Giving out a random letter when the 
            user wants to letter to a tile """

        faces = ["Q", "W", "E", "E", "R", 
                 "T", "Y", "U", "U", "I", 
                 "I", "O", "O", "P", "A", 
                 "A", "S", "D", "F", "G", 
                 "H", "J", "K", "L", "Z", 
                 "X", "C", "V", "B", "N", 
                 "M", "QU"]

        # The text that appeared on the tile is
        # being chosen randomly
        self._text = random.choice(faces)
        return self._text

    def remove_from_window(self):
        """ Remove all the parts of the game special buttons
            (characteristics and properties) from the windown. """

        for part in self._parts:
            self._win.remove(part)

    def restart(self):
        """ Reset all the settings and characteristics 
            of the tile that the program used to keep 
            track of the game. """

        # Make the status, color of the tile become normal,
        # along with adding a new text to the tile.
        self.update_status(False)
        self.change_fill_color("#d6ba8b")
        self._face.set_text(self.random_text())
        self._face.set_depth(5)

    def shuffle(self):
        """ Remove the old texts on the tiles 
            and put the new ones on. """

        # Change the tile back to its normal color, but turn it
        # on so user can select it, and also change the appeared text
        self.update_status(True)
        self.change_fill_color("#d6ba8b")
        self._face.set_text(self.random_text())
        self._face.set_depth(0)

    def update_selection_order(self):
        """ Update how many time the tile 
            had been chose in one submission. """

        self._selecting_order += 1

    def update_status(self, status):
        """ Update the status (if the button is clicked by
            the user or not) of the tile. """

        self._status = status

class GameTimer:
    """ A class representing the timer in the Boggle game board, 
        building the parts of the timer, and creating 
        characteristic and properties for the timer. """

    def __init__(self, win, center, player):
        """ Define and construct characteristics 
            and properties of the timer. """

        self._win = win                # The window that timer is drawn
        self._center = center          # Use to adjust the location of the timer
        self._playing_player = player  # Use to check which player is playing

        # Make a sign that help players to know what to do to start the game
        self._sign = Text(self._win, "Click Boggle To Begin!",
                          30, (645, 100))
        self._sign.set_depth(0)

        # The body of the timer (an hourglass): divided to multiple
        # parts for aesthetic purposes

        # Make the top of the hourglass
        self._timer_ttop = Polygon(self._win, [(126, 98), (243, 145), 
                                               (359, 98)])

        self._timer_btop = Polygon(self._win, [(126, 98), (220, 180), 
                                               (270, 180), (359, 98), 
                                               (243, 145)])

        # Make the top of the hourglass blank
        self._timer_ttop.set_fill_color("#ffffff") 
        self._timer_ttop.set_border_color("#ffffff")
        self._timer_ttop.set_depth(0)
        self._timer_btop.set_fill_color("#ffffff") 
        self._timer_btop.set_border_color("#ffffff")
        self._timer_btop.set_depth(0)

        # Make the bottom of the hourglass
        self._timer_tbottom = Polygon(self._win, [(126, 260), (220, 180), 
                                                  (270, 180), (359, 260), 
                                                  (243, 213)])
        self._timer_bbottom = Polygon(self._win, [(126, 260), (243, 213), 
                                                  (359, 260)])

        # Make the bottom of the hourglass filled with color
        self._timer_tbottom.set_fill_color("#2c9c91") 
        self._timer_tbottom.set_border_color("#2c9c91")
        self._timer_tbottom.set_depth(0)
        self._timer_bbottom.set_fill_color("#2c9c91") 
        self._timer_bbottom.set_border_color("#2c9c91")
        self._timer_bbottom.set_depth(0)

        # All the parts of the timer, which include the sign and the hourglass
        self._parts = [self._sign, self._timer_ttop, self._timer_btop,
                       self._timer_tbottom, self._timer_bbottom]

    def add_to_window(self):
        """ Add all the parts of the timer (characteristics
            and properties) to the windown. """

        for part in self._parts:
            self._win.add(part)

    def remove_from_window(self):
        """ Remove all the parts of the game special buttons
            (characteristics and properties) from the windown. """

        for part in self._parts:
            self._win.remove(part)

    def update_sign(self, player):
        """ Change the sign to tell which player is playing. """

        self._sign.set_text("Player %d's Turn!" % player)

    def tik_tok(self):
        """ Make the hourglass change its filling through certain
            points of time, to make it looks (started with the top of 
            the hour glass is filled, and end with the bottom is filled). """

        # Make the top of the hourglass filled with color 
        # while the bottom is not
        self._timer_ttop.set_fill_color("#2c9c91") 
        self._timer_ttop.set_border_color("#2c9c91")
        self._timer_btop.set_fill_color("#2c9c91") 
        self._timer_btop.set_border_color("#2c9c91")
        self._timer_tbottom.set_fill_color("#ffffff") 
        self._timer_tbottom.set_border_color("#ffffff")
        self._timer_bbottom.set_fill_color("#ffffff") 
        self._timer_bbottom.set_border_color("#ffffff")
        yield 20000

        # Make half of the top and half of the bottom of the hourglass filled
        # because the falling of sand in the hourglass, marking half of the
        # period is gone.
        self._timer_ttop.set_fill_color("#ffffff") 
        self._timer_ttop.set_border_color("#ffffff")
        self._timer_btop.set_fill_color("#39c9bb") 
        self._timer_btop.set_border_color("#39c9bb")
        self._timer_tbottom.set_fill_color("#ffffff") 
        self._timer_tbottom.set_border_color("#ffffff")
        self._timer_bbottom.set_fill_color("#39c9bb")
        self._timer_bbottom.set_border_color("#39c9bb")
        yield 20000

        # Make the whole bottom of the hourglass filled while the top is blank
        # because the sand would have fall almost complete.
        self._timer_ttop.set_fill_color("#ffffff") 
        self._timer_ttop.set_border_color("#ffffff")
        self._timer_btop.set_fill_color("#ffffff") 
        self._timer_btop.set_border_color("#ffffff")
        self._timer_tbottom.set_fill_color("#2c9c91") 
        self._timer_tbottom.set_border_color("#2c9c91")
        self._timer_bbottom.set_fill_color("#2c9c91") 
        self._timer_bbottom.set_border_color("#2c9c91")
        yield 20000

class Game:
    """ A class representing the Boggle board game, building a
        Boggle board game and all the dice and special buttons. """

    def __init__(self, win, width, center, total_players):
        """ Define and construct characteristics and properties 
            of the Boggle game board. """

        self._win = win           # The window that the game is played          
        self._width = width       # Use to adjust all the elements of the board
        self._center = center     # Use to get the location of dice and buttons
        self._current_player = 0  # Use to track the playing player
        self._turn_count = 0      # Use to track the current round of the game
        self._players = []        # A list to get all players, and their info
        self._neighbors = []      # A list to get neighbors of selected tile
        self._word_bank = []      # A list to get the player's chosen words
        self._winners = []        # A list to get players with the highest score
        self._score_board = []    # A score board that tell which player won
        self._submitted = {}      # A database to check all players' chosen 
                                  # words and scores.

        self._total_players = total_players # Use to check how many rounds
                                            # the game will be played
        self._dictionary = get_dictionary() # The dictionary that will be use
                                            # to check the players' chosen words

        # The button that allow user to choose if they want to play again                                    
        self._yes_button = GameButton(self._win, self._width // 8,
                                      self._width // 8, (708, 560), "Yes")
        self._yes_button.change_fill_color("#d6ba8b")

        # The button that allow user to end the game after all rounds are played
        self._no_button = GameButton(self._win, self._width // 8,
                                     self._width // 8, (849, 560), "No")
        self._no_button.change_fill_color("#d6ba8b")

        # Create starting information and tools for each player so the game
        # can track the players' actions.
        for order in range(1, self._total_players + 1):
            self._players.append(Player(self._win, order))

        # Make the board of the Boggle game board
        self._board = Rectangle(self._win, self._width, self._width - 300, 
                                self._center)
        self._board.set_fill_color("#b22222")
        self._board.set_depth(2)

        # A game button that allows user to starts and shuffles the tiles
        self._boggle_button = GameButton(self._win, self._width // 3 - 50,
                                         self._width // 4 - 60, 
                                         (245, 350), "Boggle!!!")

        # A game button that allows user to clear their selected words, if
        # they accidently choose the wrong letters.
        self._delete_button = GameButton(self._win, self._width // 3 - 50,
                                         self._width // 4 - 60, 
                                         (245, 520), "Delete Selection")

        # Game timer to gives each players a specific amount of time to
        # play the game
        self._timer = GameTimer(self._win, (245, 180), self._current_player)

        # All the tiles that is going to be used for the purpose of the game
        # The tiles are arranged in a 4x4 dimension
        self._tiles = []
        for x in range(4):
            x_loc = (x * 120 + self._center[0] - 30)
            for y in range(4):
                y_loc = (y * 120 + self._center[1] - 155)
                self._tiles.append(Tile(self._win, self._width // 8, 
                                        self._width // 8, (x_loc, y_loc), 
                                        (x, y)))

    def activate_current(self):
        """ Activate the current player by using the 
            index from the new going-to-play player """

        # Cite: Alistair Campbell
        # Desc: The code for activate the current player

        # Deactivate all player, then only activate the
        # player that is found the current player's index
        for player in self._players:
            player.deactivate()
        self._players[self._current_player].activate()

    def boggle(self):
        """ Start the game by shuffle the die, and assign
            a player to play. """

        # Find the another new player, shuffle the dice (then
        # disable the shuffle command), and start the game that 
        # will last a minute.
        self._boggle_button.update_status(False)
        self.activate_current()
        self._timer.update_sign(self._current_player + 1)
        for tile in self._tiles:
            tile.shuffle()
        self._neighbors = []

        # Run the program with delay: this component of the
        # CS110Graphics package allow the program to built
        # a timer.
        RunWithYieldDelay(self._win, self.start_game())

    def display(self):
        """ Adding properties of the Boggle board game (tiles and 
            buttons) to window. """

        # Add all the dice and buttons in the boggle dice to window.  
        self._win.add(self._board)
        for tile in self._tiles:
            tile.add_to_window()
        self._timer.add_to_window()
        self._boggle_button.add_to_window()
        self._delete_button.add_to_window()

        # Add the each property of the board game to the handler,
        # to check behavior of each property when a button or tile
        # is clicked.
        for tile in self._tiles:
            tile.add_handler(Interaction(tile, self))
        self._boggle_button.add_handler(Interaction(self._boggle_button, self))
        self._delete_button.add_handler(Interaction(self._delete_button, self))

    def get_total_players(self):
        """ Return the total registered players. """

        return self._total_players

    def update_turn(self):
        """ Record how many times the game had played. """

        self._turn_count += 1

    def get_turn(self):
        """ Return the number that indicate the total
            times the game had played. """

        return self._turn_count

    def start_game(self):
        """ Givign a certain time for a player to play their turn
            before the program shut down. """

        # Cite: Chiara Bondi
        # Desc: The idea of the timming of the game and the choosing
        # words can be run seperately; and the idea of calling a
        # self.method in another self.method

        # Run the sand timmer, while delay the processing of 
        # the program for a minute
        RunWithYieldDelay(self._win, self._timer.tik_tok())
        yield 60000

        # Conclude the game, shut the program down, after a minute
        self.end_turn()

    def end_turn(self):
        """ Record all the words of a specific player and store
            the achievement of that player into a Master list.
            Then empty the list of words, then change turn for 
            a new player to play. """

        # Cite: Chiara Bondi
        # Desc: The idea of storing the list of words and the player
        # identity together to make the future process easier.

        # Find the current player and store their identity with their
        # founded words into a Master list.
        for player in self._players:
            if player.get_status() is True:
                self._submitted[player.identify()] = self.get_word_bank()
        self.evaluate_performance()

        # Reset all the settings and tools of the game to
        # give the new player a fresh start out.
        for tile in self._tiles:
            tile.restart()
        self.empty_word_bank()
        self.change_turn()
        self._boggle_button.update_status(True)

        # When all the round are played, change the description
        # of the Boggle button to direct the user's next actions.
        if self.get_turn() == self.get_total_players():
            self._boggle_button.change_face("Show Winner")

    def neighbor_only(self, recent):
        """ Check if the new selected tile is a neighbor
            of the previous selected tile. """

        # Cite: Lucas Barusek
        # Desc: The idea of looking for neighbor by 
        # comparing the location of the new selected
        # tile to the previous tile's neighbors' locations

        # If the list of neighbors is empty (often because of 
        # fisrt letter), record all the neighbors of the first letter
        if self._neighbors == []:
            self.find_neighbors(recent.get_location())
            return True

        # If the list of neighbor is not empty, check if the clicked
        # was a neighbor of the previous letter. If so, find the 
        # neighbors of the clicked of button.
        for neighbor in self._neighbors:
            if recent.get_location() == neighbor:
                self.find_neighbors(recent.get_location())
                return True
        return False

    def find_neighbors(self, location):
        """ Find the neigbor locations of a given location. """

        directions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                      (1, 0), (1, -1), (0, -1), (-1, -1)]

        # For each called location, find 
        # all neighbors of that location
        self._neighbors = []
        for dr in directions:
            self._neighbors.append((dr[0] + location[0], 
                                    dr[1] + location[1]))

    def delete_selection(self):
        """ Delete the selected word, and reset the settings and 
            tools that the program used to keep track of the game. """

        for tile in self._tiles:
            tile.change_fill_color("#d6ba8b")
            tile.update_status(True)
            tile.clear_selecting_order()
        self._neighbors = []

    def update_tile_selection_order(self):
        """ Record the order of select of each selected tile. """

        # For each tile that is selected for each round of selection
        # update how many times the tile had been selected before 
        # the user submit the entire selection
        for tile in self._tiles:
            if tile.get_status() is False:
                tile.update_selection_order()

    def get_word_bank(self):
        """ Return the player's personal word list. """

        return self._word_bank

    def empty_word_bank(self):
        """ Empty player's personal word bank for the
            new player to add their new founded words. """

        # Turn word bank into a new empty list
        self._word_bank = []

    def record_selection(self):
        """ Put the selected letters together to make a word
            then record that word into the player's personal
            wordlist. """

        # Make a list of all selected tile
        chosen = []
        for tile in self._tiles:
            tile.change_fill_color("#d6ba8b")
            tile.update_status(True)
            if tile.get_selecting_order() > 0:
                chosen.append(tile.get_selecting_order())

        # Cited: Python: How to Sort a List? (The Right Way) - Afternerd
        # URL: https://www.afternerd.com/blog/python-sort-list/
        # Desc: The way to sort a numerical list in a descending order
        
        # Make a list of all selected tile in the order that 
        # the tiles were selected. Then find the letter on each 
        # tile and put them together into a word; then add the 
        # into the player's personal word list
        word = ""
        if len(chosen) > 2:    
            chosen.sort(reverse=True)
            for i in chosen:
                for tile in self._tiles:
                    if tile.get_selecting_order() == i:
                        word += tile.get_face()
            if word not in self._word_bank:
                self._word_bank.append(word)

        # The selecting order so that the next selection 
        # will not be confused with the previous selection
        self._neighbors = []
        for tile in self._tiles:
            tile.clear_selecting_order()

    def change_turn(self):
        """ Switch the played player to another player. """

        # Cite: Alistair Campbell
        # Desc: The code for switching player

        # Change the index of the current player.
        self._current_player += 1
        self._current_player = self._current_player % len(self._players)

    def evaluate_performance(self):
        """ Check if the word found by users matches
            with a word in the dictionary. """

        # Cite: Boggle - Fun With Words
        # URL: http://www.fun-with-words.com/play_boggle.html
        # Desc: Citing for the scoring rules of the game Boggle

        score = 0
        scored_word = []
        for word in self._submitted[self._current_player + 1]:
            if word in self._dictionary:
                if len(word) < 5:
                    score += 1
                if len(word) == 5:
                    score += 2
                if len(word) == 6:
                    score += 3
                if  len(word) == 7:
                    score += 4
                if len(word) > 7:
                    score += 11
                scored_word.append(word)

        # Update the playing player's submission with scored
        # points and the list of all real words
        self._submitted[self._current_player + 1] = \
                       (score, scored_word)

    def remove_game_board(self):
        """ Remove the Boggle board game and its properties (game buttons,
            game dice, game timer, and game sign) off the window. """

        self._win.remove(self._board)
        for tile in self._tiles:
            tile.remove_from_window()
        self._timer.remove_from_window()
        self._boggle_button.remove_from_window()
        self._delete_button.remove_from_window()

    def show_winner(self):
        """ Make a Score Board that will show the winner of the game,
            their scores and submitted words, as well as the option 
            if the user want to play the game again. """

        # Remove the game board away and find the winner of the game to get
        # ready for the Score Board.
        self.remove_game_board()
        self.find_winners()
        self._boggle_button.update_status(False)

        # Make the board of the Score Board
        scored_word = []
        score_board = Rectangle(self._win, self._width, self._width - 300, 
                                self._center)
        score_board.set_fill_color("#194392")
        score_board.set_depth(1)
        self._win.add(score_board)

        # Put up declaration of whether the game is tied or there is a winner
        # according the amount of players with the highest score.
        if len(self._winners) > 1:
            declaration = Text(self._win, "OH NO! THE GAME IS TIED!!!",
                               40, (500, 350))
            declaration.set_depth(0)
            self._win.add(declaration)
            score_declaration = Text(self._win, "", 40, (200, 200))
            for i in range(4):
                scored_word.append(Text(self._win, "", 40, (200, 200)))
            winning_word = Text(self._win, "", 40, (200, 200))
            self._win.add(winning_word)
        else:
            declaration = Text(self._win, "The Winner is:" +
                               " Player #%d" % (self._winners[0]), 
                               40, (500, 170))
            declaration.set_depth(0)
            self._win.add(declaration)

            # Check if the Winner win by the score that is higher than 1 points
            # and exactly 1 points
            if self._submitted[self._winners[0]][0] > 1:
                score_declaration = Text(self._win, "Score: %d Points" % \
                                         self._submitted[self._winners[0]][0],
                                         40, (580, 230))
                score_declaration.set_depth(0)
                self._win.add(score_declaration)
            else:
                score_declaration = Text(self._win, "Score: %d Point" % \
                                         self._submitted[self._winners[0]][0],
                                         40, (580, 230))
                score_declaration.set_depth(0)
                self._win.add(score_declaration)

            # Show the words that winning player found -- only shows up to 
            # four words out of all submitted words due to limited space on 
            # the score board
            winning_word = Text(self._win, "Winning Words:", 40, (361, 290))
            winning_word.set_depth(0)
            self._win.add(winning_word)
            for i in range(len(self._submitted[self._winners[0]][1])):
                if i < 4:
                    word = Text(self._win, self._submitted[self._winners[0]] \
                                [1][i].capitalize(), 40, 
                                (657, (i + 1) * 50 + 240))
                    scored_word.append(word)
                    word.set_depth(0)
                    self._win.add(word)

        # Properties of the Score Board
        self._score_board = [score_board, winning_word, scored_word,
                             declaration, score_declaration]

        self.ask_play_again()

    def find_winners(self):
        """ Find the highest score and all players that scored the 
            highest score. """

        # Find the highest score from all the scores of each players
        winning_score = 0
        for i in range(len(self._submitted)):
            if self._submitted[i + 1][0] > winning_score:
                winning_score = self._submitted[i + 1][0]

        # Find all players that have the highest score, and make list
        # out of these players.
        self._winners = []
        for i in range(len(self._submitted)):
            if self._submitted[i + 1][0] == winning_score:
                self._winners.append(i + 1)

    def ask_play_again(self):
        """ Add button for user to choose if they want to play again. """

        # Add game buttons and texts to direct user's
        # next actions after the game is player
        self._yes_button.add_to_window()
        self._no_button.add_to_window()
        self._yes_button.add_handler(Interaction(self._yes_button, self))
        self._no_button.add_handler(Interaction(self._no_button, self))
        question = Text(self._win, "Do you want to play again?", 35, 
                        (350, 560))
        question.set_depth(0)
        self._score_board.append(question)
        self._win.add(question)

    def play_again(self):
        """ Add button for user to choose if they want to play again. """

        # If the users wanted to play again, remove the score board, and 
        # reset the status of the game buttons, timer, and the tiles.
        self._boggle_button.update_status(True)
        self._yes_button.remove_from_window()
        self._no_button.remove_from_window()
        for part in self._score_board:
            if isinstance(part, list) is True:
                for stuff in part:
                    self._win.remove(stuff)
            else:
                self._win.remove(part)

        # Calling the reset method to reset the game
        self.reset()

    def reset(self):
        """ Reset all the tools and settings that allow the program to
            keep track of the game as well as the players' information. """

        self._current_player = 0  # Reset the current player
        self._turn_count = 0      # Reset the counting of round
        self._players = []        # Reset the information of player
        self._neighbors = []      # Reset the information of tiles' neighbors
        self._word_bank = []      # Reset the players' chosen words list
        self._submitted = {}      # Reset players' submission
        self._winners = []        # Reset list of players with the highest score

        # Change the Boggle button description to its original
        # version to direct user's next actions
        for order in range(1, self._total_players + 1):
            self._players.append(Player(self._win, order))
        self._boggle_button.change_face("Boggle!!!")
        
        # Display the game board again for the player to play another
        # rounds of Boggle
        self.display()

    def end_game(self):
        """ Make a farewell board. """

        # Remove the score board, the last graphical
        # object after the game is played
        self._boggle_button.update_status(False)
        self._yes_button.remove_from_window()
        self._no_button.remove_from_window()
        for part in self._score_board:
            if isinstance(part, list) is True:
                for stuff in part:
                    self._win.remove(stuff)
            else:
                self._win.remove(part)

        # Make a farewell statement and add to window, to make it visible
        farewell = Text(self._win, "Good Game!", 40, (500, 360))
        farewell.set_depth(0)
        self._win.add(farewell)

def program(win):
    """ Set up the graphics in the window. """

    # Welcome sign, as well as asking for number of players
    print("Welcome to Boggle!!!")

    # Cite: Notify user if wrong data type entered (Python 3) - Stack Overflow
    # Url: https://stackoverflow.com/questions/44347556/notify-user
    #      -if-wrong-data-type-entered-python-3
    # Desc: How to prevent user from entering letter and not integer.

    # Prevent user from entering letter and not integer.
    while True:
        try:
            total_players = int(input("Enter the total number of players: "))
            break
        except ValueError:
            print("Invalid value! Please, try again!")

    # Boggle required two or more people to play
    if total_players < 2:
        print("Please, add more players!")
        total_players = int(input("Enter the total number of players: "))

    # Cite: Chiara Bondi
    # Desc: The idea of getting the amount of players before making 
    # making the board game. 

    # If total player is more than one, create the game board and 
    # add to window
    if total_players > 1:
        boggle = Game(win, 900, (500, 350), total_players)
        boggle.display()

def main():
    """ The main program. """

    StartGraphicsSystem(program, 1000, 1000)

if __name__ == "__main__":
    main()