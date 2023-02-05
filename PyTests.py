player_tuple = [(1, '&Login', 'Log into your player profile'), (2, '&Profile', 'Access and change '
                'your profile information'), (3, '&Stats', 'Access past and present season stats'),
                (4, '&Logout', 'Log out of your player profile')]
playgame_tuple = [(1, '&Practice', 'Different types of practices to perfect your "g-aim"'), (2,
                  'Cricket Game', 'Play a cricket game'), (3, '\'01 Game', 'Play a \'01 game')]
settings_tuple = [(1, '&About', 'Information about the program'), (2, '&Settings',
                  'Change program settings'), (3, '&Quit', 'Quit the program')]


# Loop through to create menu elements
def menu_items(menu, elements):
    for element in elements:
        print(f"{menu}.Append({element[0]}, '{element[1]}', '{element[2]}')")


menu_items('player', player_tuple)
menu_items('games', playgame_tuple)
menu_items('settings', settings_tuple)
