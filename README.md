Application is located inside /dist directory as a onefile .exe

This is a text based application to keep track of different 
practice games for darts. Results are stored inside of a JSON 
file and can be read through the player history menu.

    Contents:
    Main Menu: This has the options available listed for the user to choose
        -Bulls: User indicates the amount of darts they will throw for the bull. Stats are compiled, shown to user and then written to file 
        -Doubles: User will indicate a hit or a miss on doubles from 1 to Bull. Stats are compiled, shown to user and then written to file
        -Triples: User will indicate a hit or a miss on doubles from 1 to 20. Stats are compiled, shown to user and then written to file
        -3 Out: A random number is generated for the user. They will have 3 darts to get an out and will indicate each hit for darts thrown
        -Until Out: A random number is generated for the user. They will throw darts until they can get an out and will indicate each hit for darts thrown
        -User History: This will direct user to the Player History menu

    Player History Menu: This will list the differnt practice types for the player to view past game stats on each if they choose
        -Practice games to view: Bulls, Doubles, Triples, Random Out (ALL)
        -Clear History (Choose File): This will direct the user to the Clear History Menu

    Clear History Menu
        -Practice games to clear: Bulls, Doubles, Triples, Random Out (ALL) 
        -or ALL History: This will clear all of the games in the JSON file


Created by:
Jake Robitaille

Using: Python 3, VSC Code, Pyinstaller

Current Version 1.02.03
5/21/2023

Version 1.01.01 on 4/22/2023
Version 1.02.01 on 5/6/2023
Version 1.02.02 on 5/11/2023