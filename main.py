import os
from tkinter import *
from itertools import count
import pymysql
global user_name
global pass_word
LARGE_FONT = ("Verdana", 12)

def login():
    global screen2
    screen2 = Tk()
    screen2.title("Login")
    screen2.geometry("300x350")
    Label(screen2, text="Enter Local Host Credentials").pack()
    Label(screen2, text="").pack()

    global user_name
    global pass_word
    global username_verify
    global password_verify
    global username_entry1
    global password_entry1
    username_verify = StringVar()
    password_verify = StringVar()


    Label(screen2, text="Username :").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    username_entry1.bind('<Return>', login_verify) #
    Label(screen2, text="").pack()
    Label(screen2, text="Password :").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify, show="*")
    password_entry1.pack()
    password_entry1.bind('<Return>', login_verify) #
    Label(screen2, text="").pack()
    btn = Button(screen2, text="Login", width=10, height=1) #
    btn.bind('<Button-1>', login_verify) #
    btn.pack() #

    screen2.mainloop()

def login_verify(event):
    global invalid_label
    try:
        invalid_label.pack_forget()
    except:
        invalid_label = Label(screen2, text="")
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    global user_name
    global pass_word
    user_name = username1
    pass_word = password1
    try:
        cnx = pymysql.connect(host='localhost', user=user_name, password=pass_word, db='music_stats',
                              charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        login_success()
    except:
        invalid_label = Label(screen2, text="Invalid Credentials")
        invalid_label.pack()




def login_success():
    screen2.destroy()
    session()

def session():
    global screen8
    screen8 = Tk()
    screen8.title("My Music Database")
    screen8.geometry("400x400")
    Label(screen8, text="Welcome to Music Stats").pack()
    Button(screen8, text="Add or Delete", command=add_update).pack()
    Button(screen8, text="Search Music", command=view_stats).pack()
    Button(screen8, text="Log Out", command=log_out).pack()

    screen8.mainloop()

def view_stats():
    global screen10
    global song_entry1
    global searches
    searches = []
    screen10 = Toplevel(screen8)
    screen10.title("Add, Update, or Delete")
    screen10.geometry("400x400")
    search = StringVar()
    Label(screen10, text="Look Up Music ").pack()
    Label(screen10, text="").pack()
    song_entry1 = Entry(screen10, textvariable=search)
    song_entry1.bind('<Return>', search_for) #
    song_entry1.pack()
    Label(screen10, text="").pack()
    btn = Button(screen10, text="Search") # 
    btn.bind('<Button-1>', search_for) #
    btn.pack() #
    Label(screen10, text="").pack()
    Button(screen10, text="Return to Menu", command=return_to_menu_view).pack()


def search_for(event):
    no_artists = False
    no_songs = False
    no_albums = False
    for i in searches:
        i.destroy()
    search = song_entry1.get()
    try:
        cnx = pymysql.connect(host='localhost', user=user_name, password=pass_word, db='music_stats', charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor)
    except FileNotFoundError:
        print('didnt connect')

    cur = cnx.cursor()
    # stmt_select = "select * from song where song_name=" + "'" + search + "' or album_name = '" + search + "'"
    stmt_select = f"select * from song where song_name = {search} or album_name = {search}"
    print(stmt_select)
    try:
        cur.execute(stmt_select)
        for row in cur:
            label1 = Label(screen10, text="")
            label1.pack()
            searches.append(label1)
            label2 = Label(screen10, text=str(row).replace("'song_name':", "").replace("'album_name':", "")
                           .replace("'artist_name':", "").replace("'song_id':", "").replace("'genre_name':", "")
                           .replace("{", "").replace("}", "")[3:] + "  SONG")
            label2.pack()
            searches.append(label2)
    finally:
        no_songs = True

    print(searches)
    cur.close()
    cur = cnx.cursor()
    # stmt_select = "select * from album where album_name=" + "'" + search + "'"
    stmt_select = f"select * from album where album_name = {search}"
    try:
        cur.execute(stmt_select)
        for row in cur:
            label3 = Label(screen10, text="")
            label3.pack()
            searches.append(label3)
            label4 = Label(screen10, text=str(row).replace("'song_name':", "").replace("'album_name':", "")
                           .replace("'artist_name':", "").replace("'genre_name':", "").replace("'song_id':", "")
                           .replace("{", "").replace("}", "")[1:] + "  ALBUM")
            label4.pack()
            searches.append(label4)
    finally:
        no_albums = True

    cur.close()

    cur = cnx.cursor()
    # stmt_select = "select * from artist where artist_name=" + "'" + search + "'"
    stmt_select = f"select * from artist where artist_name = {search}"
    print(stmt_select)
    try:
        cur.execute(stmt_select)
        for row in cur:
            label5 = Label(screen10, text="")
            label5.pack()
            searches.append(label5)
            label6 = Label(screen10, text=str(row).replace("'song_name':", "").replace("'album_name':", "")
                           .replace("'artist_name':", "").replace("'genre_name':", "").replace("'song_id':", "")
                           .replace("{", "").replace("}", "")[1:] + "  ARTIST")
            label6.pack()
            searches.append(label6)
    finally:
        if no_artists or no_albums:
            label5 = Label(screen10, text="")
            label5.pack()
            searches.append(label5)
            label6 = Label(screen10, text="No more music from this search")
            label6.pack()
            searches.append(label6)
    print(searches)
    cur.close()



def return_to_menu_view():
    screen10.destroy()

def add_update():
    global screen9
    global song_entry
    global artist_entry
    global album_entry
    global genre_entry
    global song_entry_delete
    global artist_entry_delete
    global album_entry_delete
    global genre_entry_delete
    global song_entry_update_from
    global artist_entry_update_from
    global album_entry_update_from
    global genre_entry_update_from
    global song_entry_update_to
    global artist_entry_update_to
    global album_entry_update_to
    global genre_entry_update_to

    screen9 = Toplevel(screen8)
    screen9.title("Add, Update, or Delete")
    screen9.geometry("500x450")
    song = StringVar()
    album = StringVar()
    artist = StringVar()
    genre = StringVar()
    song_delete = StringVar()
    album_delete = StringVar()
    artist_delete = StringVar()
    genre_delete = StringVar()
    song_entry_from = StringVar()
    album_entry_from = StringVar()
    artist_entry_from = StringVar()
    genre_entry_from = StringVar()
    song_entry_to = StringVar()
    album_entry_to = StringVar()
    artist_entry_to = StringVar()
    genre_entry_to = StringVar()
    
    Label(screen9, text="Add to, Remove from, or Modify Stored Songs").pack()
    f0 = Frame(screen9)
    f0.pack()
    
    f1 = Frame(f0)
    f1.pack(side = LEFT, expand = 1)
    Label(f1, text="Add a Song ").pack()
    Label(f1, text="Song title: ").pack()
    song_entry = Entry(f1, textvariable=song)
    song_entry.pack()
    Label(f1, text="Artist: ").pack()
    artist_entry = Entry(f1, textvariable=artist)
    artist_entry.pack()
    Label(f1, text="Album: ").pack()
    album_entry = Entry(f1, textvariable=album)
    album_entry.pack()
    Label(f1, text="Genre: ").pack()
    genre_entry = Entry(f1, textvariable=genre)
    genre_entry.pack()
    Button(f1, text="Add Song", command=add_entry).pack()
    
    f2 = Frame(f0)
    f2.pack(side = LEFT, expand = 1)
    Label(f2, text="Delete a Song ").pack()
    Label(f2, text="Song title: ").pack()
    song_entry_delete = Entry(f2, textvariable=song_delete)
    song_entry_delete.pack()
    Label(f2, text="Artist: ").pack()
    artist_entry_delete = Entry(f2, textvariable=artist_delete)
    artist_entry_delete.pack()
    Label(f2, text="Album: ").pack()
    album_entry_delete = Entry(f2, textvariable=album_delete)
    album_entry_delete.pack()
    Label(f2, text="Genre: ").pack()
    genre_entry_delete = Entry(f2, textvariable=genre_delete)
    genre_entry_delete.pack()
    Button(f2, text="Delete Song", command=delete_entry).pack()
    
    f3 = Frame(f0)
    f3.pack(side = LEFT, expand = 1)
    Label(f3, text="Update a Song ").pack()
    Label(f3, text="Old Song title: ").pack()
    song_entry_update_from = Entry(f3, textvariable=song_entry_from)
    song_entry_update_from.pack()
    Label(f3, text="New Song title: ").pack()
    song_entry_update_to = Entry(f3, textvariable=song_entry_to)
    song_entry_update_to.pack()
    Label(f3, text="Old Artist: ").pack()
    artist_entry_update_from = Entry(f3, textvariable=artist_entry_from)
    artist_entry_update_from.pack()
    Label(f3, text="New Artist: ").pack()
    artist_entry_update_to = Entry(f3, textvariable=artist_entry_to)
    artist_entry_update_to.pack()
    Label(f3, text="Old Album: ").pack()
    album_entry_update_from = Entry(f3, textvariable=album_entry_from)
    album_entry_update_from.pack()
    Label(f3, text="New Album: ").pack()
    album_entry_update_to = Entry(f3, textvariable=album_entry_to)
    album_entry_update_to.pack()
    Label(f3, text="Old Genre: ").pack()
    genre_entry_update_from = Entry(f3, textvariable=genre_entry_from)
    genre_entry_update_from.pack()
    Label(f3, text="New Genre: ").pack()
    genre_entry_update_to = Entry(f3, textvariable=genre_entry_to)
    genre_entry_update_to.pack()
    Button(f3, text="Update Song", command=update_entry).pack()
    Label(f3, text="").pack()

    Button(screen9, text="Return to Menu", command=return_to_menu_add).pack()

def clean_entry(entry):
    return "'" + entry.get().replace("'", "") + "'"

def add_entry():

    song_entry_ = clean_entry(song_entry)
    artist_entry_ = clean_entry(artist_entry)
    album_entry_ = clean_entry(album_entry)
    genre_entry_ = clean_entry(genre_entry)
    
    try:
        cnx = pymysql.connect(host='localhost', user=user_name, password=pass_word,
                              db='music_stats', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    except FileNotFoundError:
        print('didnt connect')

    cur = cnx.cursor()
    stmt_select = "select max(entry_id) from song_entry"
    cur.execute(stmt_select)
    rows = cur.fetchall()
    try:
        for row in rows:
            count = int(str(row)[17:-1])
            print(count) #TEST
    except:
        count = 0

    cnx.commit()
    cur.close()

    cur = cnx.cursor()
    # stmt_select = "insert into song_entry (entry_id, song_name, artist_name, album_name, genre_name) " \
    #               "values (" + str(count + 1) + "," +"'" +song_entry_+"', '"+artist_entry_ + "', '" \
    #               + album_entry_ + "', '" + genre_entry_ + "')"
    stmt_select = "insert into song_entry (entry_id, song_name, artist_name, album_name, genre_name) " \
        f"values ({str(count + 1)}, {song_entry_}, {artist_entry_}, {album_entry_}, {genre_entry_})" 
    cur.execute(stmt_select)

    print(stmt_select)
    cnx.commit()
    cur.close()





    cur = cnx.cursor()
    # stmt_select = "insert into genre (genre_name) values ('" + genre_entry_ + "')"
    stmt_select = f"insert into genre (genre_name) values ({genre_entry_})" 

    try:
        cur.execute(stmt_select)
    except:
        print("this genre is found!")
    print(stmt_select)
    cnx.commit()
    cur.close()

    cur = cnx.cursor()
    # stmt_select = "insert into artist (artist_name) values ('" + artist_entry_ + "')"
    stmt_select = f"insert into artist (artist_name) values ({artist_entry_})" 

    try:
        cur.execute(stmt_select)
    except:
        print("this artist is found!")
    print(stmt_select)
    cnx.commit()
    cur.close()


    cur = cnx.cursor()
    # stmt_select = "insert into album (album_name, artist_name) values ('" + album_entry_ + "', '" + artist_entry_ + "')"
    stmt_select = f"insert into album (album_name, artist_name) values ({album_entry_}, {artist_entry_})" 
    try:
        cur.execute(stmt_select)
    except:
        print("this album is found!")
    print(stmt_select)
    cnx.commit()
    cur.close()





    cur = cnx.cursor()
    stmt_select = "select max(song_id) from song"
    cur.execute(stmt_select)
    rows = cur.fetchall()
    try:
        for row in rows:
            count2 = int(str(row)[16:-1])
    except:
        count2 = 0
    cnx.commit()
    cur.close()

    cur = cnx.cursor()
    # stmt_select = f"insert into song (song_id, song_name, artist_name, album_name, genre_name) " \
    #               "values ('" + str(count2 + 1) + "', '" + song_entry_ + "', '" + artist_entry_ + "', '" \
    #               + album_entry_ + "', '" + genre_entry_ + "')"
    stmt_select = f"insert into song (song_id, song_name, artist_name, album_name, genre_name) " \
        f"values ({str(count2 + 1)}, {song_entry_}, {artist_entry_}, {album_entry_}, {genre_entry_})" 
    
    cur.execute(stmt_select)
    cnx.commit()
    cur.close()

def delete_entry():
    song_entry_ = clean_entry(song_entry_delete) #
    artist_entry_ = clean_entry(artist_entry_delete) #
    album_entry_ = clean_entry(album_entry_delete) #
    genre_entry_ = clean_entry(genre_entry_delete) #
    try:
        cnx = pymysql.connect(host='localhost', user=user_name, password=pass_word,
                              db='music_stats', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    except FileNotFoundError:
        print('didnt connect')


    cur = cnx.cursor()
    # stmt_select = "delete from song_entry where (song_name = '" + song_entry_ + \
    #               "' and  artist_name = '" + artist_entry_ + "' and album_name = '"\
    #               + album_entry_ + "' and genre_name = '" + genre_entry_ + "')"
    stmt_select = f"call delete_entry_proc({song_entry_}, {artist_entry_}, {album_entry_}, {genre_entry_})"
    print(stmt_select)
    cur.execute(stmt_select)
    cnx.commit()
    cur.close()


    # cur = cnx.cursor()
    # stmt_select = "delete from song where (song_name = '" + song_entry_ + \
    #               "' and  artist_name = '" + artist_entry_ + "' and album_name = '"\
    #               + album_entry_ + "' and genre_name = '" + genre_entry_ + "')"
    
    # cur.execute(stmt_select)
    # cnx.commit()
    # cur.close()

def update_entry():
    song_entry_ = clean_entry(song_entry_update_from)
    artist_entry_ = clean_entry(artist_entry_update_from)
    album_entry_ = clean_entry(album_entry_update_from)
    genre_entry_ = clean_entry(genre_entry_update_from)
    song_entry_to = clean_entry(song_entry_update_to)
    artist_entry_to = clean_entry(artist_entry_update_to)
    album_entry_to = clean_entry(album_entry_update_to)
    genre_entry_to = clean_entry(genre_entry_update_to)
    try:
        cnx = pymysql.connect(host='localhost', user=user_name, password=pass_word,
                              db='music_stats', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    except FileNotFoundError:
        print('didnt connect')

    cur = cnx.cursor()

    cnx.commit()
    cur.close()

    cur = cnx.cursor()
    # stmt_select = "update song_entry set song_name = '" + song_entry_to + "', artist_name = '" + artist_entry_to + \
    #               "', album_name = '" + album_entry_to + "', genre_name = '" + genre_entry_to + \
    #               "' where song_name = '" + song_entry_ +"' and artist_name = '" + artist_entry_ +  "' and album_name = '" + \
    #               album_entry_ + "' and genre_name = '" + genre_entry_ + "'"
    stmt_select = f"update song_entry set song_name = {song_entry_to}, artist_name = {artist_entry_to}, " \
        f"album_name = {album_entry_to}, genre_name = {genre_entry_to} where song_name = {song_entry_}, " \
        f"and artist_name = {artist_entry_}, and album_name = {album_entry_}, and genre_name = {genre_entry_}"

    print(stmt_select)
    cur.execute(stmt_select)
    cnx.commit()
    cur.close()

    cur = cnx.cursor()
    # stmt_select = "insert into genre (genre_name) values ('" + genre_entry_to + "')"
    stmt_select = f"insert into genre (genre_name) values ({genre_entry_to})"
    try:
        cur.execute(stmt_select)
    except:
        print("this genre is found!")
    print(stmt_select)
    cnx.commit()
    cur.close()

    cur = cnx.cursor()
    # stmt_select = "insert into artist (artist_name) values ('" + artist_entry_to + "')"
    stmt_select = f"insert into artist (artist_name) values ({artist_entry_to})"
    try:
        cur.execute(stmt_select)
    except:
        print("this artist is found!")
    print(stmt_select)
    cnx.commit()
    cur.close()

    cur = cnx.cursor()
    # stmt_select = "insert into album (album_name, artist_name) values ('" + album_entry_to + "', '" + artist_entry_to + "')"
    stmt_select = f"insert into album (album_name, artist_name) values ({album_entry_to}, {artist_entry_to})"

    try:
        cur.execute(stmt_select)
    except:
        print("this album is found!")
    print(stmt_select)
    cnx.commit()
    cur.close()

    cur = cnx.cursor()
    stmt_select = "select max(song_id) from song"
    cur.execute(stmt_select)
    rows = cur.fetchall()
    try:
        for row in rows:
            count2 = int(str(row)[16:-1])
    except:
        count2 = 0
    cnx.commit()
    cur.close()

    cur = cnx.cursor()
    # stmt_select = "insert into song (song_id, song_name, artist_name, album_name, genre_name) " \
    #               "values ('" + str(count2 + 1) + "', '" + song_entry_to + "', '" + artist_entry_to + "', '" \
    #               + album_entry_to + "', '" + genre_entry_to + "')"
    stmt_select = f"insert into song (song_id, song_name, artist_name, album_name, genre_name) " \
                  "values ({str(count2 + 1)}, {song_entry_to}, {artist_entry_to}, {album_entry_to}, {genre_entry_to})"

    cur.execute(stmt_select)
    cnx.commit()
    cur.close()





def return_to_menu_add():
    screen9.destroy()

def log_out():
    screen8.destroy()
    login()




login()

