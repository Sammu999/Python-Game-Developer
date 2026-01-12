import pgzrun

WIDTH=800
HEIGHT=500
TITLE = "Quiz Master"
lines = []

marquee = Rect(0,0,800,65)
question_box = Rect (5,75,600,150)
option_box1= Rect (5,235,295,120)
option_box2= Rect (305,235,295,120)
option_box3= Rect (5,365,295,120)
option_box4= Rect (305,365,295,120)
timer_box = Rect (615,75,180,150)
skip_box = Rect (615,235,180,250)

optionboxes = [option_box1,option_box2,option_box3,option_box4]

def draw():
    screen.fill("blue")
    screen.draw.filled_rect(marquee,"red")
    screen.draw.filled_rect(question_box,"orange")
    for box in optionboxes:
        screen.draw.filled_rect(box,"orange")
    screen.draw.filled_rect(timer_box,"orange")
    screen.draw.filled_rect(skip_box,"orange")

def read_question_file():
    file = open("questions.txt","r")
    for line in file:
        lines.append(line)
    file.close()
    print(lines)

read_question_file()
pgzrun.go()





