import pgzrun

WIDTH=800
HEIGHT=500
TITLE = "Quiz Master"
lines = []
Game_over=False
timer=10

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
    if not Game_over: 
        screen.draw.filled_rect(marquee,"red")
        screen.draw.filled_rect(question_box,"orange")
        for box in optionboxes:
            screen.draw.filled_rect(box,"orange")
        screen.draw.filled_rect(timer_box,"orange")
        screen.draw.filled_rect(skip_box,"orange")
        screen.draw.textbox(current_question [0].strip(),question_box,color="red")
        screen.draw.textbox(current_question [1].strip(),option_box1,color="red")
        screen.draw.textbox(current_question [2].strip(),option_box2,color="red")
        screen.draw.textbox(current_question [3].strip(),option_box3,color="red")
        screen.draw.textbox(current_question [4].strip(),option_box4,color="red")
        screen.draw.textbox("SKIP",skip_box,color="red",angle=90)
        screen.draw.textbox(str(timer),timer_box,color="red")
    else:
        screen.draw.text("Game Over!",(400,250))


def read_question_file():
    file = open("questions.txt","r")
    for line in file:
        lines.append(line)
    file.close()
    #print(lines)

def read_next_question():
    global Game_over
    if lines:
        return lines.pop(0).split("|")
    else:
        Game_over=True


def skip():
   global current_question
   current_question = read_next_question()

def on_mouse_down(pos):
    if skip_box.collidepoint(pos):
        skip()


read_question_file()
current_question = read_next_question()
print (current_question)
pgzrun.go()





