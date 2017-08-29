"""
Replace the contents of this module docstring with your own details.
"""
from operator import itemgetter

"""
load songs
    song_list = list
    in_file = open songs.csv (read)
    for line in in_file
        remove newline character
        song_artist_year_list = split line for ","
        song_list = append song_artist_year_list
    return songlist
"""


def load_songs():
    song_list = []
    in_file = open("songs.csv", 'r')
    for line in in_file:
        line = line.strip("\n")
        song_artist_year_list = line.split(",")
        song_list.append(song_artist_year_list)
    in_file.close()
    return song_list


def display_song_list(song_list):
    count = 0
    for i in range(len(song_list)):
        if song_list[i][3] == "y":
            count += 1
            symbol = "*"
        else:
            symbol = " "
        print(str(i) + ".", symbol, "", end="")
        for j in range(len(song_list[i]) - 2):
            if j == 1:
                dash = "-"
            else:
                dash = ""
            print(dash, "{:30}".format(song_list[i][j]), end=" ")
        print("({:4})".format(song_list[i][-2]))
    print(len(song_list) - count, "songs learned,", count, "songs still to learn")


def complete_a_song(song_list):
    song_number = input("enter the number of a song to mark as learned\n>>>")
    # if song_number


def song_adder():
    title = input("Title: ")
    string_error_checker(title, "Title: ")
    artist = input("Artist: ")
    string_error_checker(artist, "Artist: ")
    year = int(input("Year: "))
    integer_error_checker(year, "Year: ")


def integer_error_checker(user_input, prompt):
    while user_input <= 0:
        print("Number must be >= 0")
        user_input = int(input(prompt))


def string_error_checker(user_input, prompt):
    while len(user_input) == 0:
        print("Input can not be blank")
        user_input = input(prompt)


def menu():
    menu_prompt = "Menu:\nL - List songs\nA - Add new song\nC - Complete a song\nQ - Quit\n>>>"
    menu_selection = input(menu_prompt).upper()
    while menu_selection not in list("LACQ"):
        print("Invalid menu choice")
        menu_selection = input(menu_prompt).upper()
    return menu_selection


def main():
    print("Songs To Learn 1.0 - by Brandon Johns")
    song_list = load_songs()
    song_list.sort(key=itemgetter(1, 0))
    print(len(song_list), "songs loaded")
    menu_selection = menu()
    while menu_selection != "Q":
        if menu_selection == "L":
            display_song_list(song_list)
        elif menu_selection == "A":
            song_adder()
        else:
            complete_a_song(song_list)
        menu_selection = menu()


if __name__ == '__main__':
    main()
