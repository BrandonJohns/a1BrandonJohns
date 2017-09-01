"""
Brandon Johns
Student ID: 13438272
01/09/2017
This program is an interactive song list that allows a user to add songs
they wish to learn and songs the have learned.
Git hub: https://github.com/BrandonJohns/a1BrandonJohns
"""
from operator import itemgetter

FILE_NAME = "songs.csv"
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


# load_songs function opens the songs file and writes them to song_list a
# list of lists
def load_songs():
    song_list = []
    in_file = open(FILE_NAME, 'r')
    for line in in_file:
        line = line.strip("\n")
        song_artist_year_list = line.split(",")
        song_list.append(song_artist_year_list)
    in_file.close()
    return song_list


# display_song_list function prints a formatted table of songs from song_list
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


"""
complete_a_song(song_list)
    song_number = get_integer("song number: ")
    song_list[song_number][3] = "n"
    print song_list[song_number][0]+"by"+song_list[song_number][1]+"learned"
    return song_list
"""


# complete_a_song function gets a song number input from the user and marks the song
# as complete
def complete_a_song(song_list):
    song_number = get_integer("enter the number of a song to mark as learned\n>>>")
    if song_list[song_number][3] == "n":
        print("You have already learned", song_list[song_number][0])
    else:
        song_list[song_number][3] = "n"
        print(song_list[song_number][0], "by", song_list[song_number][1], "learned")
        return song_list


# song_adder function gets song details input from the user and adds it to the song_list
def song_adder():
    new_song = []
    title = get_string("Title: ")
    artist = get_string("Artist: ")
    year = str(get_integer("Year: "))
    new_song.append(title)
    new_song.append(artist)
    new_song.append(year)
    new_song.append("y")
    print(title, "by", artist, "({:4})".format(year), "added to song list")
    return new_song


# get_integer function gets an integer input from the user and checks that it is valid
def get_integer(prompt):
    valid = False
    while not valid:
        try:
            integer_input = int(input(prompt))
            if integer_input < 0:
                print("Number must be >= 0")
            else:
                return integer_input
        except ValueError:
            print("Invalid input; enter a valid number")


# get_string function gets a string input from the user and checks it is valid
def get_string(prompt):
    string_input = input(prompt)
    while len(string_input) == 0:
        print("Input can not be blank")
        string_input = input(prompt)
    return string_input.title()


# menu function displays the menu and gets menu selection input from the user
def menu():
    menu_prompt = "Menu:\nL - List songs\nA - Add new song\nC - Complete a song\nQ - Quit\n>>>"
    menu_selection = input(menu_prompt).upper()
    while menu_selection not in list("LACQ"):
        print("Invalid menu choice")
        menu_selection = input(menu_prompt).upper()
    return menu_selection


# save_songs function writes the song_list to a csv file
def save_songs(song_list):
    out_file = open(FILE_NAME, 'w')
    for i in range(len(song_list)):
        if i != 0:
            print("\n", end="", file=out_file)
        for j in range(len(song_list[i])):
            out_file.write(song_list[i][j])
            if j != 3:
                print(",", end="", file=out_file)
    out_file.close()


# main function brings all the other functions together
def main():
    print("Songs To Learn 1.0 - by Brandon Johns")
    song_list = load_songs()
    print(len(song_list), "songs loaded")
    menu_selection = menu()
    while menu_selection != "Q":
        song_list.sort(key=itemgetter(1, 0))
        if menu_selection == "L":
            display_song_list(song_list)
        elif menu_selection == "A":
            song_list.append(song_adder())
        else:
            complete_a_song(song_list)
        menu_selection = menu()
    save_songs(song_list)
    print(len(song_list), "songs saved to", FILE_NAME, "\nHave a nice day :)")


if __name__ == '__main__':
    main()
