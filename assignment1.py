"""
Replace the contents of this module docstring with your own details.
"""
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
    return song_list


def display_song_list(song_list):
    count = 0
    for i in range(len(song_list)):
        if song_list[i][3] == "y":
            count += 1
            symbol = "*"
        else:
            symbol = " "
        song_list[i].pop(3)
        print(str(i)+".", symbol, "", end="")
        for j in range(len(song_list[i])):
            if j == 1:
                dash = "-"
            else:
                dash = ""
            print(dash, "{:30}".format(song_list[i][j]), end=" ")
        print()
    print(len(song_list) - count, "songs learned,", count, "songs still to learn")


def complete_a_song(song_list):
    song_number = input("enter the number of a song to mark as learned\n>>>")
    print(song_list)


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
    print(len(song_list), "songs loaded")
    menu_selection = menu()
    while menu_selection != "Q":
        if menu_selection == "L":
            display_song_list(song_list)
        elif menu_selection == "A":
            print("Add new song")
        else:
            complete_a_song(song_list)
        menu_selection = menu()
#if __name__ == '__main__':
main()
