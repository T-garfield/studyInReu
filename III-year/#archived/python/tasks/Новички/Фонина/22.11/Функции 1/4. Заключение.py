def repeat_stuff (stuff, num_repeats = 10):
    statement = stuff * num_repeats
    return statement
lyrics = repeat_stuff ("Row ", 3) + "Your boat \n"
song = repeat_stuff(lyrics)
print(song) 