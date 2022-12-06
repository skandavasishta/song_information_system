from song_functions import *

swiftie = {
      "title": "Cardigan",
      "artist": "Taylor Swift",
      "length": "03:59",
      "album": "Folklore",
      "genre": ["folk", "indie rock"],
      "rating": 4,
      "released": "07/27/2020",
      "favorite": True,
      "uid" : 12332
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
empty_dict = {}

song_info = ["Gooba", "Tekashi 6ix9ine", "04:09", "Snitches", "Rap, pop rap", "1", "06/09/2020", 'F', '69696']
song_info1 = ["Gooba", "Tekashi 6ix9ine", "04:09", "Snitches", "Rap, pop rap", 1, "06/09/2020", 'F', '69696']
key_list = all_songs.keys()

assert get_written_date(['12', '31', '2004']) == 'December 31, 2004'
assert get_written_date(['01', '01', '1990']) == 'January 1, 1990'

assert is_valid_date('12/31/2004') == True
assert is_valid_date('21/31/2004') == False
assert is_valid_date('12/32/2004') == False
assert is_valid_date('02/30/2004') == False
assert is_valid_date('12/31') == False
assert is_valid_date('12/31/') == False
assert is_valid_date('12/31/04') == False
assert is_valid_date('123/31/2004') == False
assert is_valid_date('12/31/2004/') == False


assert is_valid_title('Skanda') == True
assert is_valid_title('S') == False
assert is_valid_title(10) == False
assert is_valid_title('S'*41) == False

assert is_valid_time("1:00") == False
assert is_valid_time("01:00") == True
assert is_valid_time("1A:00") == False

assert is_valid_uid('69696', key_list) == True
assert is_valid_uid('696966', key_list) == False
assert is_valid_uid('12332', key_list) == False

assert is_valid_addlist(song_info) == True
assert is_valid_addlist([])== False
assert is_valid_addlist(song_info1) == False

assert delete_song({}, '12332') == 0
assert delete_song(all_songs, '12331') == -1
assert delete_song(all_songs, '12332') == 'Cardigan'



assert get_new_song(song_info, rating_map, key_list)== {'title': 'Gooba', 'artist': 'Tekashi 6ix9ine', 'length': '04:09', 'album': 'Snitches', 'genre': ['Rap', ' pop rap'], 'rating': 1, 'released': '06/09/2020', 'favorite': False, 'uid': 69696}
assert get_new_song(["Tekashi 6ix9ine", "04:09", "Snitches", "Rap, pop rap", "1", "06/09/2020", 'F', '69696'] , rating_map, key_list) == ("Bad list. Found non-string, or bad length", 0)
assert get_new_song(["G", "Tekashi 6ix9ine", "04:09", "Snitches", "Rap, pop rap", "1", "06/09/2020", 'F', '69696'] , rating_map, key_list) == ("Bad Title length", -1)
assert get_new_song(["Gooba", "Tekashi 6ix9ine", "4:09", "Snitches", "Rap, pop rap", "1", "06/09/2020", 'F', '69696'] , rating_map, key_list) == ("Invalid time format for Length", -2)
assert get_new_song(["Gooba", "Tekashi 6ix9ine", "04:09", "Snitches", "Rap, pop rap", "1", "16/09/2020", 'F', '69696'] , rating_map, key_list) == ("Invalid date format for Release Date", -4)
assert get_new_song(["Gooba", "Tekashi 6ix9ine", "04:09", "Snitches", "Rap, pop rap", "6", "06/09/2020", 'F', '69696'] , rating_map, key_list) == ("Invalid Rating value", -3)
assert get_new_song(["Gooba", "Tekashi 6ix9ine", "04:09", "Snitches", "Rap, pop rap", "1", "06/09/2020", 'L', '69696'] , rating_map, key_list) ==("Invalid value for Favorite", -5)
assert get_new_song(["Gooba", "Tekashi 6ix9ine", "04:09", "Snitches", "Rap, pop rap", "1", "06/09/2020", 'F', '696969'] , rating_map, key_list) == ("Unique ID is invalid or non-unique", -6)


assert edit_song({}, '12332', rating_map, 'title', 'Cardigan', key_list) == 0
assert edit_song(all_songs, '12332', rating_map, 1, 'Cardigan', key_list) == -1
assert edit_song(all_songs, '12332', rating_map, 'title', 'C', key_list) == 'title'
assert edit_song(all_songs, '12332', rating_map, 'length', '4:00', key_list) == 'length'
assert edit_song(all_songs, '12332', rating_map, 'released', '16/20/2000', key_list) == 'released'
assert edit_song(all_songs, '12332', rating_map, 'rating', '6', key_list) == 'rating'
assert edit_song(all_songs, '12332', rating_map, 'favorite', 'Good', key_list) == 'favorite'


assert save_to_csv(all_songs, 'skanda.txt') == -1
assert save_to_csv(all_songs, 'filename.csv') == None

assert load_from_csv('skanda.txt', all_songs, rating_map, key_list) == -1
assert load_from_csv('skanda.csv', all_songs, rating_map, key_list) == None

#assert load_from_csv('some_bad.csv', all_songs, rating_map, key_list) == [1,3]
#assert load_from_csv('matni_songs_allgood.csv', all_songs, rating_map, key_list) == []
