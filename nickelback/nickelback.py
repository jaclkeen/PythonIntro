songs = {
    ('Nickelback', 'How You Remind Me'), 
    ('Will.i.am', 'That Power'),
    ('Miles Davis', 'Stella by Starlight'),
    ('Nickelback', 'Animals')
}

NickelbackSongs = {"Artist: " + key + "Song: " + value for(key, value) in songs if key=='Nickelback'}

print NickelbackSongs