import wx


# Setting up the main window
class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        super(MainWindow, self).__init__(parent=None, title=title, size=(950, 600))
        self.Centre()
        self.CreateStatusBar()
        self.create_menu()

    def create_menu(self):
        # Creating the menu options on the main menu bar
        player = wx.Menu()
        games = wx.Menu()
        settings = wx.Menu()

        # PLAYER menu: LOGIN, PROFILE, STATS, LOGOUT
        player.Append(wx.ID_ANY, '&Login', 'Log into your player profile')
        player.AppendSeparator()
        player.Append(wx.ID_ANY, '&Profile', 'Access and change your profile information')
        player.AppendSeparator()
        player.Append(wx.ID_ANY, '&Stats', 'Access past and present season stats')
        player.AppendSeparator()
        player.Append(wx.ID_ANY, '&Logout', 'Log out of your player profile')

        # PLAY A GAME menu: PRACTICE, CRICKET, '01
        games.Append(wx.ID_ANY, '&Practice', 'Different types of practices to perfect your "g-aim"')
        games.AppendSeparator()
        games.Append(wx.ID_ANY, 'Cricket Game', 'Play a cricket game')
        games.AppendSeparator()
        games.Append(wx.ID_ANY, '\'01 Game', 'Play a \'01 game')

        # SETTINGS menu: ABOUT, SETTINGS, QUIT
        settings.Append(wx.ID_ABOUT, '&About', 'Information about the program')
        settings.AppendSeparator()
        settings.Append(wx.ID_ANY, '&Settings', 'Change program settings')
        settings.AppendSeparator()
        settings.Append(wx.ID_EXIT, '&Quit', 'Quit the program')

        # MENUBAR: PLAYER INFO, PLAY A GAME, SETTINGS
        menubar = wx.MenuBar()
        menubar.Append(player, 'Player Info')
        menubar.Append(games, 'Play a Game')
        menubar.Append(settings, 'Settings')
        self.SetMenuBar(menubar)
        self.Show(True)


# Main loop of the application
app = wx.App(False)
window = MainWindow(None, 'The Breakfast Club Dart Tracker')
app.MainLoop()
