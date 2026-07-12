#Write a program that tracks a game score.


score = 0

def add_score():
    global score
    score+=10

def sub_score():
    global score
    score-=5

def display_score():
    print(score)

display_score()
add_score()
display_score()
add_score()
display_score()
sub_score()
display_score()