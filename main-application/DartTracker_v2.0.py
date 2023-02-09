import wx

player_tuple = [(wx.ID_ANY, '&Login', 'Log into your player profile'), (wx.ID_ANY, '&Profile', 'Access and change '
                'your profile information'), (wx.ID_ANY, '&Stats', 'Access past and present season stats'),
                (wx.ID_ANY, '&Logout', 'Log out of your player profile')]
playgame_tuple = [(wx.ID_ANY, '&Practice', 'Different types of practices to perfect your "g-aim"'), (wx.ID_ANY,
                  'Cricket Game', 'Play a cricket game'), (wx.ID_ANY, '\'01 Game', 'Play a \'01 game')]
settings_tuple = [(wx.ID_ABOUT, '&About', 'Information about the program'), (wx.ID_ANY, '&Settings',
                  'Change program settings'), (wx.ID_EXIT, '&Quit', 'Quit the program')]

teamname = 'The Breakfast Club'


# Setting up the main window
class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        super(MainWindow, self).__init__(parent, title=title, size=(950, 600))
        self.Centre()
        self.CreateStatusBar()
        self.create_menu()

    # Loop through to create menu elements
    def menu_items(self, menu, elements):
        for element in elements:
            menu.Append(element[0], element[1], element[2])
            self.Bind(wx.EVT_LEFT_DOWN, btn_click, menu)
    
    def create_menu(self):
        # Creating the menu options on the main menu bar
        player = wx.Menu()
        games = wx.Menu()
        settings = wx.Menu()

        # PLAYER menu: LOGIN, PROFILE, STATS, LOGOUT
        self.menu_items(player, player_tuple)

        # PLAY A GAME menu: PRACTICE, CRICKET, '01
        self.menu_items(games, playgame_tuple)

        # SETTINGS menu: ABOUT, SETTINGS, QUIT
        self.menu_items(settings, settings_tuple)

        # MENUBAR: PLAYER INFO, PLAY A GAME, SETTINGS
        menubar = wx.MenuBar()
        menubar.Append(wx.Menu(), 'Home')
        menubar.Append(player, 'Player Info')
        menubar.Append(games, 'Play a Game')
        menubar.Append(settings, 'Settings')
        self.SetMenuBar(menubar)
        self.Show()


def btn_click(clicked):
    if clicked == '&Quit':
        window.Close()

# Main loop of the application
app = wx.App(False)
window = MainWindow(None, f"{teamname} Dart Tracker")
app.MainLoop()
