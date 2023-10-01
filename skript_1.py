'''
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Pavel Šalanda
email: pavel.salanda@gmail.com
discord: pavelsalanda
'''
from itertools import combinations


def plaing_area (edge):
    '''
    The function parametrically defines the size of the playing field.
    The playing field is always a square with a side length equal to the "EDGE" parameter.
    The function defines the visual of each row of the playing field.
    The first line is always statically in the "Lines" variable of the list type, 
    Other list series are added dynamically according to the size of the playing field.
    The individual lists are then combined into one "separate_lines", 
    where the fastener is the character "n" for line breaks for printing.
    Subsequently, the entire list of "separate_lines" is decomposed 
    Character-by-character to the "Disintegration" list. 
    The output of the function is a list of "disintegration".
    To print the playing field, it is necessary to use the "join" method, 
    where the connecting element will be "" and set the Print "SEP" parameter to "".
    '''
    lines = [edge * '----' + '-']
    for i in range(edge):
        lines.append('|' + edge * '   |')
        lines.append(edge * '----' + '-')
    separate_lines = '\n'.join(lines)
    disintegration = [i for i in separate_lines]
    return(disintegration)

def number_series (edge):
    '''
    The purpose of the function is to define winning series of numbers from the playing field.
    Winning lines are always three numbers.. There are nested functions in a function,
    which define number sequences in rows, columns and diagonals.
    The output from nested functions is combined into a single "merget_rows" list.
    The output of the function is a list of "merget_rows".
    '''
    def correct_rows (edge):
        '''
        The function defines the winning lines in the lines of the playing field.
        The function in the "wrong_numbers" variable defines a field from which winning streaks cannot be calculated.
        The field from which winning streaks cannot be counted are the last two columns of the playing field.
        The calculation of winning streaks is determined in such a way that in the "part_of_rows" 
        defines a range of consecutive numbers with the length of the "edge" parameter. 
        If the series begins with a number from the "wrong_numbers", it is discarded. 
        From these series, the first three numbers are selected and added to the "rows".
        "rows" is the output of the function.
        '''
        row = list(range(0,(edge * edge) + 1))
        wrong_numbers_1 = [edge * i for i in range(1, edge + 1)] 
        wrong_numbers_2 = [i - 1 for i in wrong_numbers_1]
        wrong_numbers= wrong_numbers_1 + wrong_numbers_2
        rows = []
        for i in range(1,edge * edge):
            part_of_rows = row[i:i + edge]
            if len(part_of_rows) > 2 and i not in wrong_numbers:
                rows.append(part_of_rows[:3])
        return(rows)

    def correct_collumns (edge):
        '''
        The purpose of the function is to define winning lines in the columns of the playing field.
        The function in the "wrong_numbers" variable defines a field from which winning streaks cannot be calculated.
        The field from which the winning streak cannot be counted is the last two rows of the playing field.
        The calculation of winning lines is calculated by adding a number equal to the "edge" parameter to each number. 
        If the series begins with a number from the "wrong_numbers", it is discarded. 
        From these series, the first three numbers are selected and added to the "rows".
        "rows" is the output of the function.
        '''
        collumn = list(range(1,(edge * edge) + 1)) 
        wrong_numbers = list(range((edge * edge) - (edge * 2) + 1,(edge * edge) + 1))
        rows = []
        for i in range(0,edge * edge):
            part_or_rows = collumn[i - (edge * edge):i + (edge * edge):edge]
            if i not in wrong_numbers and len(part_or_rows) > 2:
                rows.append(part_or_rows[:3])
        return(rows)

    def left_diagonal (edge):
        '''
        The purpose of the function is to define winning lines in diagonals going from left to right of the playing field.
        The function in the "wrong_numbers" variable defines a field from which winning streaks cannot be calculated.
        The field from which winning streaks cannot be counted are the last two columns of the playing field.
        The calculation of winning series is calculated by adding to each number a number equal to the parameter "edge" + 1. 
        If the series begins with a number from the "wrong_numbers" it is discarded. 
        From these series, the first three numbers are selected and added to the "rows".
        "rows" is the output of the function.
        '''
        row = list(range(0,(edge * edge) + 1)) 
        rows = []
        wrong_numbers_1 = [edge * i for i in range(1, edge + 1)]
        wrong_numbers_2 = [i - 1 for i in wrong_numbers_1]
        wrong_numbers= wrong_numbers_1 + wrong_numbers_2
        for i in range(1,edge * edge):
            part_of_rows = row[i:i + (edge * edge):edge + 1]
            if len(part_of_rows) > 2 and i not in wrong_numbers:
                rows.append(part_of_rows[:3])
        return(rows)

    def right_diagonal (edge):
        '''
        The purpose of the function is to define winning lines in diagonals going from the right to the left of the playing field.
        The function in the "wrong_numbers" variable defines a field from which winning streaks cannot be calculated.
        The field from which winning lines cannot be counted are the first two columns of the playing field.
        The calculation of winning series is calculated by adding to the individual numbers a number equal to the parameter "edge" - 1. 
        If the series begins with a number from the "wrong_numbers" it is discarded. 
        From these series, the first three numbers are selected and added to the "rows".
        "rows" is the output of the function.
        '''
        row = list(range(0,(edge * edge) + 1)) 
        rows = []
        wrong_numbers_1 = list(range(1,edge * edge,edge))
        wrong_numbers_2 = [i + 1 for i in wrong_numbers_1]
        wrong_numbers= wrong_numbers_1 + wrong_numbers_2
        for i in range(1,edge * edge):
            part_of_rows = row[i:i + (edge * edge):edge - 1]
            if len(part_of_rows) > 2 and i not in wrong_numbers:
                rows.append(part_of_rows[:3])
        return(rows)
    merged_rows = []
    merged_rows.extend(correct_rows(edge))
    merged_rows.extend(correct_collumns(edge))
    merged_rows.extend(left_diagonal(edge))
    merged_rows.extend(right_diagonal(edge))
    return(merged_rows) 

def introduction ():
    # přeložit docstring
    '''
    The purpose of the function is to display the introductory text and the rules of the game.
    '''
    greeating = 'Welcome to Tic Tac Toe'
    rules = '''GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
===========================================
Let's start the game'''
    all_text = (greeating, separator,rules)
    conected_all_text = '\n'.join(all_text)
    return(conected_all_text)

def plaing_fields(field):
    # přeložit docstring
    '''
    The function defines the indexes of the playing field into which the player marks "o" or "x" will be inserted. 
    The field where the player mark appears consists of three spaces. 
    The middle space is for the player marks "o" or "x". Thus, the space for player marks "o" or "x" is always even.
    The loop that specifies the indexes selects all spaces whose index is even, and 
    Index adds to the variable "index_field" that is output by the function.
    '''
    index_field = []
    for index, value in enumerate(field):
        if value == ' ' and index % 2 == 0:
            index_field.append(index)  
    return(index_field)

def input_verifikacion_o (fields, used_numbers):
    '''
    The purpose of the function is to request input from player "o" and evaluate it.
    The function verifies: 
    Whether the input is a number 
    whether the entered number is in the correct range according to the playing field,
    whether the number has not already been used.
    The output of the function is a verified number from player "o".
    '''
    while True:
        try:
            user_input = input(f'{separator}\nPlayer o | Please enter your move number: ')
            print(separator)
            player_input = int(user_input)
            if player_input < 1 or player_input > len(fields):
                print(f'This number in not between 1 and {len(fields)}')
                continue  
            if player_input in used_numbers:
                print('This number has already been used!')
                continue  
            break
        except ValueError:
            print('This number is not valid!')
    return(player_input) 

def game_avaluation(numbers, winning_numbers, edge, used_number): 
        '''
        The function evaluates the state of the game after entering and verifying the player's input.
        The function sorts all user input.
        The function creates possible combinations of numbers of three.
        The function verifies whether the player has a winning line or if all playing fields are filled,
        If so, it exits the game and prints the game state if no the code continues.
        '''
        sorting_numbers = sorted(numbers)
        all_combinations = list(combinations(sorting_numbers, 3))
        all_combinations_to_list = [list(t) for t in all_combinations]
        for i in all_combinations_to_list:
            if i in winning_numbers:
                game_status = 'game_over'
                return(game_status) 
            elif len(used_number) == (edge * edge):
                game_status = 'draw'
                return(game_status)

def input_verifikacion_x (fields, used_number):
    '''
    The purpose of the function is to request input from player "x" and evaluate it.
    The function verifies: 
    Whether the input is a number 
    whether the entered number is in the correct range according to the playing field,
    whether the number has not already been used.
    The output of the function is a verified number from player "x".
    '''
    while True:
        try:
            user_input = input(f'{separator}\nPlayer x | Please enter your move number: ') 
            print(separator)
            player_input = int(user_input)
            if player_input < 1 or player_input > len(fields):
                print(f'This number in not between 1 and {len(fields)}')
                continue  
            if player_input in used_number:
                print('This number has already been used!')
                continue  
            break
        except ValueError:
            print('This number is not valid!')
    return(player_input)

separator = '==========================================='


def main ():
    '''
    The function defines the necessary variables for creating the playing field, running the called functions.
    The size of the playing field can be generated dynamically according to the "plaing_edge" variable.
    The playing field is always a square with the edge of the variable "plaing_edge".
    By default, "plaing_edge" is set to 3. 
    Variables needed to run the program:
    winning_streak - winning series of numbers, used to compare inputs from players
    game_area - defines the playing field
    game_fields - defines the indexes into which player marks are inserted
    game_result, game_state - variables for running while loops
    numbers_used - defines a list of all numbers entered and verified by players
    numbers_player_o - list of entered and verified numbers of player "o"
    numbers_player_x - list of entered and verified numbers of player "x"
    The basis of a function is a while loop that uses function calls 
    It will request authenticated user input and evaluate the current state of the game. 
    The while loop interrupt is outside the while loop based on the call result 
    "game_avaluation" function. 
    If the condition evaluates the state and using "break" and
    "Continue" terminates or lets the loop continue.
    '''
    plaing_edge = 3
    winning_streak = (number_series(plaing_edge))
    game_area = (plaing_area(plaing_edge))
    print(introduction(),'\n', ''.join(plaing_area(plaing_edge)),sep = '')
    game_fields = plaing_fields(game_area)
    game_result = ['game_run']
    game_state = ['game_run']
    numbers_used = []
    numbers_player_o = []
    numbers_player_x = []

    while game_result == game_state:  
        player_input_o = input_verifikacion_o(game_fields, numbers_used)  
        game_area[game_fields[player_input_o - 1]] = 'o'
        numbers_used.append(player_input_o)
        numbers_player_o.append(player_input_o)
        print(''.join(game_area))    
        current_staus = (game_avaluation(numbers_player_o,winning_streak, plaing_edge, numbers_used)) 
        if current_staus == 'game_over':
            print(f'{separator}\nCongratulations, the player o WON!\n{separator}')
            break
        elif current_staus == 'draw':
            print('The game ended in a draw.')
            break     
        player_input_x = input_verifikacion_x(game_fields, numbers_used)  
        game_area[game_fields[player_input_x - 1]] = 'x'
        numbers_used.append(player_input_x)
        numbers_player_x.append(player_input_x)
        print(''.join(game_area))  
        current_staus = (game_avaluation(numbers_player_x, winning_streak, plaing_edge, numbers_used)) 
        if current_staus == 'game_over':
            print(f'{separator}\nCongratulations, the player x WON!\n{separator}')
            break
        elif current_staus == 'draw':
            print('The game ended in a draw.')
            break
        else:
            continue

if __name__ == "__main__":
    main()





