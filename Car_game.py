# Car game
symbol=">"
while symbol!="Quit":
    symbol=input(">")
    if symbol=="start":
        print("Car started....Readey to go")
    elif symbol=="stop":
        print("Car Stopped")
    elif symbol=="helP":
        print('''
              start-to start the Car
              stop- to stop the Car
              quit- to exit 
              ''')
    elif symbol=="Quit":
        break
    else:
        print("I don't understand")
