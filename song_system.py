from song_functions import *

all_songs = {
   "12332": {
      "title": "Cardigan",
      "artist": "Taylor Swift",
      "length": "03:59",
      "album": "Folklore",
      "genre": ["folk", "indie rock"],
      "rating": 4,
      "released": "07/27/2020",
      "favorite": True,
      "uid" : 12332
   },
   "14567": {
      "title": "Soul Meets Body",
      "artist": "Death Cab for Cutie",
      "length": "",
      "album": "Plans",
      "genre": ["indie pop", "indie rock"],
      "rating": 5,
      "released": "07/16/2005",
      "favorite": True,
      "uid":14567
      },
   "78210": {
      "title": "Fake Love",
      "artist": "BTS",
      "length": "04:02",
      "album": "",
      "genre": ["hip hop", "electro pop", "Korean pop"],
      "rating": 3,
      "released": "05/18/2018",
      "favorite": False,
      "uid":78210
      },
    "99105": {
      "title": "Foil",
      "artist": "'Weird Al' Yankovic",
      "length": "02:22",
      "album": "Mandatory Fun",
      "genre": ["pop", "parody"],
      "rating": 5,
      "released": "07/15/2014",
      "favorite": True,
      "uid": 99105
      }
}

list_menu = {
    "A": "all songs - full",
    "B": "all songs - titles only",
    "F": "favorite songs",
    "G": "songs of a specific genre"
}

rating_map = {
    "1": "Hate",
    "2": "Dislike",
    "3": "Neutral",
    "4": "Like",
    "5": "Love!"
}


the_menu =  {"L" : "List",
    "A" : "Add",
    "E" : "Edit",
    "D" : "Delete",
    "M" : "Show statistical data on",
    "S" : "Save the data to file",
    "R" : "Restore data from file",
    "Q" : "Quit this program"}

opt = None

while True:
    print_main_menu(the_menu) 
    opt = input("::: Enter a menu option\n> ")
    opt = opt.upper() 

    if opt not in the_menu.keys(): 
        print(f"WARNING: {opt} is an invalid menu option.\n")
        continue

    print(f"You selected option {opt} to > {the_menu[opt]}.")

    if opt == 'Q': 
        print("Goodbye!\n")
        break
    elif opt == 'L':
        if all_songs == {}:
            print("WARNING: There is nothing to display!")
            # Pause before going back to the main menu
            input("::: Press Enter to continue")
            continue

        subopt = get_selection(the_menu[opt], list_menu)
        if subopt == 'A':
            print_songs(all_songs, rating_map, showid = True)
        elif subopt == 'B':
            print_songs(all_songs, rating_map, title_only = True)
        elif subopt == 'F':
            print_songs(all_songs, rating_map, fave = True)
        elif subopt == 'G':
            print_songs(all_songs, rating_map, get_genre = True)
     elif opt == 'D':
         continue_action = 'y'
         while continue_action == 'y':
             
             print_songs(all_songs, rating_map, title_only = True, show_id = True, fave = False, get_genre = False):
             print('Which song would you like to delete?')
             print('X - Delete all songs at once')
             print('::: OR Enter the number corresponding to the song ID')
             print("::: OR press 'M' to cancel and return to the main menu.")
             user_choice = input()
             if user_choice.isdigit() == False:
                 user_choice = user_choice.upper()
                 if user_choice == 'X':
                     print('::: WARNING! Are you sure you want to delete ALL songs?')
                     cont_delete = input('::: Type Yes to continue the deletion.\n')
                     if cont_delete == "Yes":
                         all_songs.clear()
                         print('Deleted all songs.')
                         input('::: Press Enter to continue\n')
                         break                      
                 elif user_choice == 'M':
                     break
             elif user_choice.isdigit() == True:
                 if delete_song(all_songs, user_choice) == 0:
                     print('WARNING: There is nothing to delete!')
                     break
                 elif delete_song(all_songs, user_choice) == -1:
                     print(f'WARNING: |{user_choice}| is an invalid song ID!')
                     wrong_choice = input("::: Would you like to delete another song? Enter 'y' to continue.")
                     if wrong_choice.lower() = 'y':
                        continue_action = 'y'
                     else:
                         break
                 else:
                     deleted_song = delete_song(all_songs, user_choice)
                     print('Success!')
                     print(f'Deleted the song |{deleted_song}|')
                     delete_again = input("::: Would you like to delete another song? Enter 'y' to continue.")
                     if delete_again.lower() == continue_action:
                         continue_action = 'y'
                     else:
                         break
    elif opt == 'A':
        continue_action = 'y'
        while continue_action == 'y':
            song_info = []
            print("::: Enter each required field:")
            # TODO: Get user inputs for all 9 song info fields (i.e. keys). 
            # Get *all* inputs as strings.
            title_input = input("Title: ")
            artist_input = input("Artist: ") 
            length_input = input("Length (00:00 format): ")
            album_input = input("Album: ")
            genres_input = input("Genres (separate them with commas): ")
            rating_input = input("Rating (1-5): ")
            release_input = input("Release Date (MM/DD/YYYY format): ")
            favorite_input = input("Favorite (T/F): ")
            uid_input = input("Unique ID: ")
            song_info = [title_input, artist_input, length_input, album_input, genres_input, rating_input, release_input, favorite_input, uid_input]
            key_list = all_songs.keys()

            result = get_new_song(song_info, rating_map, key_list) # TODO: attempt to create a new song
            if type(result) == dict:
                all_songs.update(result)
                print(f"Successfully added a new song!")
                print_song(result, rating_map, title_only = False, showid = False)
            elif type(result) == tuple:
                print(f"WARNING: invalid data!")
                print(f"Error: {result[0]}")

            print("::: Would you like to add another song?", end=" ")
            continue_action = input("Enter 'y' to continue.\n> ")
            continue_action = continue_action.lower() 
            # ----------------------------------------------------------------

    elif opt == 'S':
        continue_action = 'y'
        while continue_action == 'y':
            print("::: Enter the filename ending with '.csv'.")
            filename = input("> ")
            csv_result = save_to_csv(all_songs, file_name) # TODO: Call the function with appropriate inputs and capture the output
            if csv_result == -1: # TODO
                print(f"WARNING: |{filename}| is an invalid file name!") # TODO
                print("::: Would you like to try again?", end=" ")
                continue_action = input("Enter 'y' to try again.\n> ")
            else:
                print(f"Successfully stored all the songs to |{filename}|")
                continue_action = 'n'
    #--------------------------------------------------------------------------         
    elif opt == 'R':
        continue_action = 'y':
            while continue_action == 'y':
                print("::: Enter the filename ending with '.csv'.")
                filename_res = input("> ")
                csv_restore = load_from_csv(filename_res, all_songs, rating_map, key_list)
                if csv_restore == -1:
                    print ("WARNING: invalid input - must end with '.csv'")
                    print("::: Would you like to try again?", end=" ")
                    continue_action = input("Enter 'y' to try again.\n> ")   
                elif csv_restore == None:
                    print(f"WARNING: |{filename.res}| was not found!")
                    print("::: Would you like to try again?", end=" ")
                    continue_action = input("Enter 'y' to try again.\n> ")
                elif len(csv_restore) != 0:
                    print(f"WARNING: |{filename.res}| contains invalid data!")
                    print("The following rows from the file were not loaded:")
                    print(csv_restore)
                    print("::: Would you like to try again?", end=" ")
                    continue_action = input("Enter 'y' to try again.\n> ")
                else:
                    print(f"Successfully restored all songs from |{filename.res}|")
                    print("::: Would you like to try again?", end=" ")
                    continue_action = input("Enter 'y' to try again.\n> ")
    
                    
    elif opt == 'E':
        continue_action = 'y'
        while continue_action == 'y':
            if all_songs == {}: # TODO
                print("WARNING: There is nothing to edit!")
                break
            print("::: Song list:")
            print_songs(all_songs, rating_map, title_only = True, showid = True)
            print("::: Enter the song ID you wish to edit.")
            user_option = input("> ")
            if user_option in all_songs.keys(): # TODO - check to see if that ID is in the song dictionary
                subopt = get_selection("edit", all_songs[user_option], to_upper = False, go_back = True)
                if subopt == 'M': # if the user changed their mind
                    break
                print(f"::: Enter a new value for the field |{subopt}|") # TODO
                field_info = input("> ")
                key_list = all_songs.keys()
                result = edit_song(all_songs, user_option, rating_map, subopt, field_info, key_list) #TODO
                if type(result) == dict:
                    print(f"Successfully updated the field |{subopt}|:")  # TODO
                    print_song(result, rating_map, title_only = False, showid=False))  # TODO
                else: # edit_song() returned an error
                    print(f"WARNING: invalid information for the field |{subopt}|!")  # TODO
                    print(f"The song was not updated.")
            else: # song ID is incorrect/invalid
                print(f"WARNING: |{user_option}| is an invalid song ID!")  # TODO

            print("::: Would you like to edit another song?", end=" ")
            continue_action = input("Enter 'y' to continue.\n> ")
            continue_action = continue_action.lower()      
            # ----------------------------------------------------------------                    
                    
     elif opt =='M':
         continue_action = 'y'
         while continue_action == 'y':
             print('::: What would you like to show statistical data on?')
             print('A - Mean value of all song ratings')
             print('B - Median value of all song ratings')
             print('C - Standard Deviation value of all song ratings')
             print('D - Histogram of all song ratings')
             opt = input('::: Enter your selection \n> ')
             if opt.upper() == 'A':
                 print('You selected |A| to show statistical data on |mean value of all song ratings|.')
             if opt.upper() == 'B':
                 print('You selected |B| to show statistical data on |median value of all song ratings|.')
             if opt.upper() == 'C':
                 print('You selected |C| to show statistical data on |standard deviation value of all song ratings|.')
             if opt.upper() == 'D':
                 print('You selected |D| to show statistical data on |histogram of all song ratings|.'
             do_stats(all_songs, opt)
                 
                 
                 
                 
            
             continue_action = input("::: Would you like to get different statistics? Enter 'y' to continue. \n> ")
             
             
         
                
                     

    input("::: Press Enter to continue")

print("Have a nice day!")
