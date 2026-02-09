import pgzrun


WIDTH=800
HEIGHT=500
TITLE = "Quiz Master"
lines = []
Game_over=False
timer=10
score=0
totalquestions=0
question_number=0

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
        screen.draw.textbox(f"Welcome to Quiz Master. This is Q {question_number} out of {totalquestions}",marquee,color="blue")
    else:
        screen.draw.text("Game Over!",center=(WIDTH//2,HEIGHT//2))
        screen.draw.text(f"Your final score is {score} out of {totalquestions}",center=(WIDTH//2,HEIGHT//2+50))

    
def update():
    marquee.x-=3
    if marquee.right<0:
        marquee.left=WIDTH


def read_question_file():
    global totalquestions
    file = open("questions.txt","r")
    for line in file:
        lines.append(line)
    file.close()
    totalquestions=len(lines)
    #print(lines)

def read_next_question():
    global Game_over, timer,question_number
    timer=10
    if lines:
        question_number+=1
        return lines.pop(0).split("|")
    else:
        Game_over=True
    


def skip():
   global current_question
   current_question = read_next_question()

def on_mouse_down(pos):
    if skip_box.collidepoint(pos):
        skip()

    for box in optionboxes:
        global score
        if box.collidepoint(pos):
            if optionboxes.index(box)+1== int(current_question[5]):
                score = score+1

            skip()


def update_time():
    global timer
    if timer > 0:
        timer=timer-1
    else:
        skip()
    


read_question_file()
current_question = read_next_question()
print (current_question)

clock.schedule_interval(update_time,1)
pgzrun.go()





