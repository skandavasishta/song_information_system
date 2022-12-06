

def print_main_menu(menu):
    """prints the menu """
    print(menu)

def get_selection(action, suboptions, to_upper = True, go_back = False):
    """
    param: action (string) - the action that the user
            would like to perform; printed as part of
            the function prompt
    param: suboptions (dictionary) - contains suboptions
            that are listed underneath the function prompt.
    param: to_upper (Boolean) - by default, set to True, so
            the user selection is converted to upper-case.
            If set to False, then the user input is used
            as-is.
    param: go_back (Boolean) - by default, set to False.
            If set to True, then allows the user to select the
            option M to return back to the main menu

    The function displays a submenu for the user to choose from. 
    Asks the user to select an option using the input() function. 
    Re-prints the submenu if an invalid option is given.
    Prints the confirmation of the selection by retrieving the
    description of the option from the suboptions dictionary.

    returns: the option selection (by default, an upper-case string).
            The selection be a valid key in the suboptions
            or a letter M, if go_back is True.
    """
    selection = None
    if go_back:
        if 'm' in suboptions or 'M' in suboptions:
            print("Invalid submenu, which contains M as a key.")
            return None

    while selection not in suboptions:
        print(f"::: What would you like to {action.lower()}?")
        for key in suboptions:
            print(f"{key} - {suboptions[key]}")
        if go_back == True:
            selection = input(f"::: Enter your selection "
                              f"or press 'm' to return to the main menu\n> ")
        else:
            selection = input("::: Enter your selection\n> ")
        if to_upper:
            selection = selection.upper() # to allow us to input lower- or upper-case letters
        if go_back and selection.upper() == 'M':
            return 'M'

    if to_upper:    
        print(f"You selected |{selection}| to",
              f"{action.lower()} |{suboptions[selection].lower()}|.")
    else:
        print(f"You selected |{selection}| to",
          f"{action.lower()} |{suboptions[selection]}|.")
    return selection

def get_written_date(date_list):
    """turns a date entered as MM/DD/YYYY into Month Day, Year format by taking
        in a date in the original format as a parameter"""
    new_list = []
    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
    for num in date_list:
        #loop creates new list with each value being an integer instead of
        #string
        num = int(num)
        new_list.append(num)
    month = month_names[new_list[0]]
    day = new_list[1]
    year = new_list[2]
    return (f'{month} {day}, {year}')

def print_song(song, rating_map, title_only = False, showid=False):
    """
    param: song (dict) - a single song dictionary
    param: rating_map (dict) - a dictionary object that is expected
            to have the string keys that correspond to the "rating"
            integer values stored in the song; the stored value is displayed for the
            rating field, instead of the numeric value.
    param: title_only (Boolean) - by default, set to False.
            If True, then only the name of the song is printed.
            Otherwise, displays the formatted song fields.
    param: show_id (Boolean) - by default, set to False.
            If False, then the id number of the song is not displayed.
            Otherwise, displays the id number.

    returns: None; only prints the song values

    Helper functions:
    - get_written_date() to display the 'released' field
        You created a similar function in a previous lab.
    """
    date = song['released']
    if len(date) !=0:
        real_date = get_written_date(date.split("/")) #list with 3 items: mm, dd, yyyy
    else:
        real_date = '' #returns an empty string if no date provided
    num_rating = str(song['rating'])
    rating = rating_map[num_rating]
    genre_list = song['genre']
    genre_string = ''
    for gen in genre_list:
        new_gen = gen.title()
        if gen == genre_list[-1]:
            genre_string += new_gen
        else:
            genre_string+=new_gen + ", "        
    if (title_only == False) and (showid == False):#everything except ID at top shown
        for key in song.keys():
            if key == "uid":
                continue
            elif key == "rating":
                print(f'{key.upper():>8}: {rating}')
            elif key == "released":
                if len(real_date) == 0:
                    continue
                else:
                    print(f'{key.upper():>8}: {real_date}')
            elif key == 'genre':
                if len(real_date) == 0:
                    continue
                else:
                    print(f'{key.upper():>8}: {genre_string}')
            elif key == 'length' and len(song['length'])==0:
                continue
            elif key == 'album' and len(song['album'])==0:
                continue
            else:
                print(f'{key.upper():>8}: {song[key]}')
        print('******************************************')
        
    elif (title_only == True) and (showid == True):#only title and ID at top shown
        print(f'{"ID:":>9} {song["uid"]} |{"TITLE:":>9} {song["title"]}')
    elif (title_only == False) and (showid == True):#everything shown
        for key in song.keys():
            if key == "uid":
                continue
            elif key == "rating":
                print(f'{key.upper():>8}: {rating}')
            elif key == "released":
                print(f'{key.upper():>8}: {real_date}')
            elif key == 'genre':   
                print(f'{key.upper():>8}: {genre_string}')
            elif key == "title":
                print(f'{"ID:":>9} {song["uid"]} |{"TITLE:":>9} {song["title"]}')
            else:
                print(f'{key.upper():>8}: {song[key]}')
        print('******************************************')
    elif (title_only == True) and (showid == False):#only title shown at top
        print(f'{"TITLE":>8}: {song["title"]}')
        
        
        

    

def print_songs(song_dict, rating_map, title_only = False, show_id = False, fave = False, get_genre = False):
    """
    param: song_dict (dict) - a dictionary containing dictionaries with
            the song data
    param: rating_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "rating"
            integer values stored in the song; the stored value is displayed 
            for the rating field, instead of the numeric value.
    param: title_only (Boolean) - by default, set to False.
            If True, then only the title of the song is printed.
            Otherwise, displays the formatted song fields.
    param: showid (Boolean) - by default, set to False.
            If False, then the key (unique ID number) of the song is not displayed.
            Otherwise, displays the id number.
    param: fave (Boolean) - by default, set to False, and prints all songs.
            Otherwise, if it is set to True, prints only the songs marked as favorite.
            This parameter is meant to be used exclusive of get_genre
            (i.e. if fave=True, then get_genre should be False, and vice versa).
    param: get_genre (Boolean) - by default, set to False, and prints all songs.
            If set to True, then the function should ask the user for a
            genre keyword (string) and print only those songs that contain that string in its genre value.
            This parameter is meant to be used exclusive of fave (i.e. if fave=True, then get_genre should be False, and vice versa).
            NOTE: If a song has multiple instances of that genre keyword, you should only print the song once.

    returns: None; only prints the song values from the song_list

    Helper functions:
    - print_song() to print individual songs
    """
    print("*"*42)
    # Check to see if get_genre is True, so that you can ask for the genre keyword
    if get_genre == True:
        genre_input = str(input('Enter genre:: '))
   # Go through all the songs in the song dictionary:
   
    for songs, vals in song_dict.items(): 
        # if not asking for favorites or specific genres: print everything
        if fave == False and get_genre == False :
            print_song(vals, rating_map, title_only, show_id)
        # otherwise: if asking for favorites, print just those:
        elif (fave == True) and (get_genre == False) :
            if vals['favorite'] == True:
                print_song(vals, rating_map, title_only, show_id)
            else:
                continue
        # otherwise: if asking for a specific genre, print just those:
        elif get_genre:
            # search all the songs' genres for the genre keyword
            # and print only those songs where that keyword appears in the genre value
            # NOTE: You should only print a song *once* 
            # even if the genre keyword appears more than once in it
            genre_list = vals['genre']
            genre_string = ''
            for gen in genre_list:
                genre_string += gen.title()
            if genre_input.upper() in genre_string.upper():
                print_song(vals, rating_map, title_only, show_id)
            else:
                continue

    
def delete_song(song_dict, songid):
    """
    param: song_dict - a dictionary of songs (dict of dict)
    param: songid (str) - a string that is expected to
            contain the key to a song dictionary (i.e. same as its unique ID)

    The function first checks if the dictionary of songs is empty.
    The function then validates the song ID to verify
    that the provided ID key can access an element from song_dict
    On success, the function saves the item's "title" from song_dict
    and returns that string ("title" value)
    after the item is deleted from song_dict.

    returns:
    If the input list is empty, return 0.
    If the ID is not valid (i.e. not found in the song_dict), return -1.
    Otherwise, on success, the entire song is removed from song_dict
    and the function returns the title of the deleted song.
    """
    if song_dict == {}: #if dictionary is empty, cant delete anything
        return 0
    elif songid not in song_dict.keys(): #if an invalid ID is being attempted to delete
        return -1
    elif songid in song_dict.keys():
        saved_title = song_dict[songid]['title']
        del song_dict[songid]
        return saved_title

def get_new_song(input_list, rating_map, key_list):
    """
    Once validation is taken care of, then the values passed into get_new_song() through
    its list parameter, must be added as values to a new dictionary with the 9 song keys
    (i.e. "title", "artist", "length", etc…)

    Important: make sure when you add these values that they are added as the correct data type.
    The new dictionary gets returned at the conclusion of this process.
    """
    new_dict = {}
    #below are different validations that, if false, return corresponding strings
    if is_valid_addlist(input_list) == False:
        addlist_tuple = ("Bad list. Found non-string, or bad length", 0)
        return addlist_tuple
    if is_valid_time(input_list[2]) == False:
        time_tuple = ("Invalid time format for Length", -2)
        return time_tuple
    if is_valid_date(input_list[6]) == False:
        date_tuple = ("Invalid date format for Release Date", -4)
        return date_tuple
    if str(input_list[5]) not in rating_map.keys():
        rating_tuple = ("Invalid Rating value", -3)
        return rating_tuple
    if input_list[7][0] not in ["T", "t", "F", "f"]:
        fav_tuple = ("Invalid value for Favorite", -5)
        return fav_tuple
    if is_valid_uid(input_list[8], key_list) == False:
        uid_tuple = ("Unique ID is invalid or non-unique", -6)
        return uid_tuple
    if is_valid_title(input_list[0]) == False:
        title_tuple = ("Bad Title length", -1)
        return title_tuple
    
    new_dict['title'] = input_list[0] #add corresponding key, value for title
    new_dict['artist'] = input_list[1] #add corresponding key, value for artist
    new_dict['length'] = input_list[2] #add corresponding key, value for song length
    new_dict['album'] = input_list[3] #add corresponding key, value for album
    new_dict['genre']  = input_list[4].split(",") #add corresponding key, value for genre; split at comma to create new list
    new_dict['rating'] = int(input_list[5]) #add corresponding key, value for rating. value is an int
    new_dict['released'] = input_list[6] #add corresponding key, value for date of release
    if input_list[7][0].upper() == 'T': #depending on if the given input is true or false, add corresponding key, value for favorite (boolean value)
        new_dict['favorite'] = True
    else:
        new_dict['favorite'] = False
    new_dict['uid'] = int(input_list[8])
    return new_dict
                    
        

def is_valid_addlist(input_list):
    """
    The entire input list has to be made up of strings.
    The function calls the helper function is_valid_addlist() to check this.
    This helper function returns a Boolean value.
    If the value is invalid, then get_new_song() has to return a tuple containing
    the message string "Bad list. Found non-string, or bad length" and the integer 0."""
    
    for input_string in (input_list):
        if type(input_string) == str: #each item in list must be a string
            pass
        else:
            return False
    if len(input_list) == 9: #length of list must be 9
        return True
    else:
        return False
    

def is_valid_title(title):
    """
    This helper function returns a Boolean value.
    If the value is invalid, then get_new_song() has to return a tuple containing the message
    string "Bad Title length" and the integer -1. """
    if type(title) == str and 2<= len(title) <=40: #title must be a string and between 2 and 40 characters
        return True
    else:
        return False
def is_valid_time(time):
    """
    The "length" value has to be in 00:00 format, that is, it's a string that has
    2 digits, followed by a colon, followed by 2 digits. The function calls the helper
    function is_valid_time() to check this."""
    if len(time) == 5 and (time[0]).isdigit() == True and (time[1]).isdigit() == True and time[2] == ':' and (time[3]).isdigit() == True and (time[4]).isdigit() == True:
        return True
    else:
        return False
        
                
def is_valid_date(date):
    """
    This helper function returns a Boolean value.
    If the value is invalid, then get_new_song() has to return a tuple containing the
    message string "Bad Title length" and the integer -1."""
    num_days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    if date.count("/") == 2: #must be two '/' in a valid date
        date_list = date.split("/") #creates list of [mm, dd, yyyy]
        for num in date_list:
            if num.isdigit() !=True: #iterates through each value in list to ensure they are only digits
                return False
        if len(date_list) == 3 and len(date_list[0]) == 2 and len(date_list[1]) == 2 and len(date_list[2]) == 4: #checks length specifications
            month = date_list[0]
            year = date_list[2]
            if (1<=int(month)<=12) and int(year)>1000: #checks month and year are valid numbers
                month = int(date_list[0])
                day = int(date_list[1])
                if month in num_days.keys():  
                    month_days = num_days[month] #assigns appropriate month to given numerical counterpart
                    if day<=month_days:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
                        
                
             
            
  
def is_valid_uid(uid, key_list):

    """ 
    The "uid" value is a string that has to be made up of exactly 5 digits.
    The range of these digits can only be "10000" to "99999". Additionally, this value has
    to be unique to any other uid value in the current song dictionary (all_songs). The function
    calls the helper function is_valid_uid(str, key_list) to check this. The key_list parameter
    is a list of all the keys in the song dictionary (hint: you can use the .key() method to
    obtain these). This helper function returns a Boolean value.If the value is invalid,
    then get_new_song() has to return a tuple containing the message string "Unique ID is
    invalid or non-unique" and the integer -6"""
    if uid.isdigit()==True and len(uid) == 5 and (10000 <= int(uid) <= 99999) and str(uid) not in key_list:
        return True
    else:
        return False
        
    
       
def save_to_csv(song_dict, filename):
    """
    param: song_dict(dict of dict) - The dictionary of songs stored 
    param: filename (str) - A string that ends with '.csv' which represents
               the name of the file to which to save the songs. This file will
               be created if it is not present, otherwise, it will be overwritten.

    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv` as well as `import os`.

    The function will use the `with` statement to open the file `filename`.
    After creating a csv writer object, the function uses a `for` loop
    to loop over every song in the dictionary and creates a new list
    containing only strings - this list is saved into the file by the csv writer
    object. The order of the elements in the dictionary is:

    * title
    * artist
    * length
    * album
    * genre (all element in the original list are converted to string
        joined with commas separating)
    * rating (converted to string)
    * released (written as string, i.e, "06/06/2022", NOT "June 6, 2022")
    * favorite (converted to string)
    * uid

    returns:
    -1 if the last 4 characters in `filename` are not '.csv'
    None if we are able to successfully write into `filename`
    """
    import csv
    import os
    
    if filename[-4:] == '.csv': #checks if last four characters of inputted filename are '.csv'
        with open('filename.csv', 'w') as songs_file: #opens file to write
            songs_writer = csv.writer(songs_file)     
            for key, value in song_dict.items():
                if type(value) == list:
                    value = ",".join(value) #converts list to string separated by commas to facilitate csv writing'
                elif type(value) == bool:
                    value = str(value) #converts boolean to string
                    value = value.upper()
                song_info_list = []
                value = str(value)
                song_info_list.append(value)
                songs_writer.writerow(song_info_list) #dictionary file written as CSV
    else:
        return -1
                
                
                
def load_from_csv(filename, in_dict, rating_map, allkeys):
    """
    param: filename (str) - A string variable which represents the
            name of the file from which to read the contents.
    param: in_dict (dict of dict) - A dictionary of songs (dictionary objects) to which
            the songs read from the provided filename are added to.
            If in_dict is not empty, the existing songs are not dropped.
    param: rating_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "rating"
            integer values stored in the song; the stored value is displayed 
            for the rating field, instead of the numeric value.
    param: allkeys (key_list) - a key_list of all keys in the song dictionary

    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv` and `import os`.

    If the file exists, the function will use the `with` statement to open the
    `filename` in read mode. For each row in the csv file, the function will
    proceed to create a new song using the `get_new_song()` function.
    - If the function `get_new_song()` returns a valid song object,
    it gets added to `in_dict`.
    - If the `get_new_song()` function returns an error, the 1-based
    row index gets recorded and added to the NEW list that is returned.
    E.g., if the file has a single row, and that row has invalid song data,
    the function would return [1] to indicate that the first row caused an
    error; in this case, the `in_dict` would not be modified.
    If there is more than one invalid row, they get excluded from the
    in_dict and their indices will be appended to the new list that's
    returned.

    returns:
    * -1, if the last 4 characters in `filename` are not '.csv'
    * None, if `filename` does not exist.
    * A new empty list, if the entire file is successfully read from `in_dict`.
    * A list that records the 1-based index of invalid rows detected when
      calling get_new_song().

    Helper functions:
    - get_new_song()
    
    """
    import csv
    import os
    if filename[-4:] == ".csv": #checks if last four characters of inputted filename are '.csv'
        if os.path.exists(filename): #checks if the file exists
            failurelist = [] #list that will keep record of 1 based index
            count = 1 #increment for 1 based index that is later appended to list
            with open(filename, 'r') as f: #inputted file is opened for reading               
               row_reader = csv.reader(f)
               for row in row_reader:
                   result = get_new_song(row,rating_map,allkeys) #get_new_song will either return a dictionary for valid rows or a tuple for invalid rows                  
                   if type(result) != dict: #get_new_song fails validation, leading to updated failurelist
                       failurelist.append(count) 
                   else:
                       in_dict[str(result["uid"])] = result #dictionary added to all_songs dictionary
                   count+=1
               return failurelist
        else:
            return None
    else:
        # does not exist
        return -1
        
                
                    
def edit_song(song_dict, songid, rating_map, field_key, field_info, allkeys):
    """
    param: song_dict (dict) - dictionary of all songs
    param: songid (str) - a string that is expected to contain the key of
            a song dictionary (same value as its unique id)
    param: rating_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "rating"
            integer values stored in the song; the stored value is displayed 
            for the rating field, instead of the numeric value.
    param: field_key (string) - a text expected to contain the name
            of a key in the song dictionary whose value needs to 
            be updated with the value from field_info
    param: field_info (string) - a text expected to contain the value
            to validate and with which to update the dictionary field
            song_dict[field_key]. The string gets stripped of the
            whitespace and gets converted to the correct type, depending
            on the expected type of the field_key.
    param: allkeys (key_list) - a key_list of all keys in the song dictionary.

    The function first calls some of its helper functions
    to validate the provided field.
    If validation succeeds, the function proceeds with the edit.

    return:
    If song_dict is empty, return 0.
    If the field_key is not a string, return -1.
    If the remainder of the validation passes, return the dictionary song_dict[songid].
    Otherwise, return the field_key.

    Helper functions:
    The function calls the following helper functions depending on the field_key:
    - is_valid_title()
    - is_valid_time()
    - is_valid_date()
    - is_valid_uid()
    """
    songid = str(songid)
    if song_dict == {}: #dictionary can't be updated if empty
        return 0
    if type(field_key) != str: #field_key parameter must be a string
        return -1
    if field_key.lower() == 'title':
        if is_valid_title(field_info) != True: #checks if title is valid
            return field_key
    if field_key.lower() == 'length':
        if is_valid_time(field_info) != True: #checks if song length is valid
            return field_key
    if field_key.lower() == 'released':
        if is_valid_date(field_info) != True: #checks if release date is valid
            return field_key
    if field_key.lower() == 'uid':
        if is_valid_uid(field_info, allkeys) != True: #checks if uid is valid
            return field_key
    if field_key.lower() == 'rating':
        if str(field_info) not in rating_map.keys(): #checks if rating is valid
            return field_key
    if field_key.lower() == 'favorite':
        if field_info[0] not in ["T", "t", "F", "f"]: #checks if favorite is valid
            return field_key
    else:
        field_key = field_key.lower()
        if type(field_info) == str: 
            song_dict[songid][field_key] = str(field_info).strip() #removes whitespace if  astring needs to be updated
            if field_key == 'favorite': #returns boolean depending on user input for favorite
                if field_info[0].upper() == 'F':
                    song_dict[songid][field_key] = False
                elif field_info[0].upper() == 'T':
                    song_dict[songid][field_key] = True
        if type(field_info) == list:
            song_dict[songid][field_key] = ','.join(field_info) #converts list to string
        if type(field_info) == int:
            song_dict[songid][field_key] = int(field_info)
    return song_dict[songid]
    
    
        
def do_stats(song_dict, opt):
    """
    param: song_dict - a dictionary of songs (dict of dict)
    param: opt (str) - an option from the menu
    to do one of the following statistical calculations:
        "A" - find the mean (average) of all song ratings values
        "B" - find the median of all song ratings values
        "C" - find the standard deviation of all song ratings values
        "D" - print out a histogram of all song ratings values

    Helpful hint: see example on top of page in
    zyBook Ch. 8.4 to see how to do mean and stddev calculations.

    returns: Nothing! This function only PRINTS out results.    
    """
    rating_list = []
    for value in song_dict.values(): #returns a list of ratings
        rating = value['rating']
        rating_list.append(rating)
    sum_list = sum(rating_list) #sum of ratings
    amount_items = len(rating_list) #amount of ratings
    mean = sum_list/amount_items
    sorted_list = sorted(rating_list)
    
    if opt.upper() == 'A':
        #find mean
        print(f'The mean value of all ratings is: {mean:.2f}')   
            
    if opt.upper() == 'B':
        #find median
        if len(sorted_list)%2 != 0:
            median = int((len(sorted_list)+1)/2 -1)
            print('The median value of all ratings is:', sorted_list[median])
        else:
            med1 = int((len(sorted_list))/2 -1)
            med2 = int((len(sorted_list))/2)
            new_med = (sorted_list[med1] + sorted_list[med2])/2
            print(f'The median value of all ratings is: {new_med:.2f}')
    if opt.upper() == 'C':
        #find standard deviation
        x = 0
        for r in rating_list:
            x += (r - mean )**2
        std_dev = (x/len(rating_list))**0.5
        print(f'The standard deviation value of all ratings is: {std_dev:.2f}')
    if opt.upper() == 'D':
        #print histogram
        x1 = 0
        x2 = 0
        x3 = 0
        x4 = 0
        x5 = 0
        star = '*'
        for num in rating_list:
            if num == 1:
                x1 +=1
            elif num == 2:
                x2 +=1
            elif num == 3:
                x3 +=1
            elif num == 4:
                x4 +=1
            elif num == 5:
                x5 +=1
        
        print("1", star*x1)
        print("2", star*x2)
        print("3", star*x3)
        print("4", star*x4)
        print("5", star*x5)
            
                

                    
                
            
            
        
        
    
            
    
    
    
        
    
        
