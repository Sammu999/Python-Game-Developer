import pgzrun
WIDTH = 800
HEIGHT = 800
game_state = "launch"
galaga = Actor ("galaga")
galaga.pos = (WIDTH/2, HEIGHT-50)


def draw():
    screen.fill ("cyan")
    if game_state == "launch":
        screen.draw.text("Welcome to the Galaga Game",center = (WIDTH/2,HEIGHT/2), color="black", fontsize=50)
        screen.draw.text("Press any key to continue",center = (WIDTH/2 , HEIGHT/2+50), color = "black" , fontsize = 25)
    
    elif game_state == "start":
        galaga.draw()
       

    


def update():
    if keyboard.A and galaga.x >= 0:
        galaga.x -= 10

    if keyboard.D and galaga.x <= WIDTH:
        galaga.x += 10
    

def on_key_down(key):
    global game_state

    if game_state == "launch":
        game_state = "start"

    



pgzrun.go()