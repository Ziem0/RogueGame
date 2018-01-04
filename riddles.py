question_1 = {'You are participating in a race. You overtake the second person. What position are you in?: ': 'second'}
question_2 = {'What kind of cheese is made backwards: ' : 'edam'}
question_3 = {'Poor people have it. Rich people need it. What is it?: ' : 'nothing'}

def ask_riddles(question, delay_print, handles_first_level, handles_second_level):
    answer = input(*question.keys()).lower()
    for key, value in question.items():
        if answer == value:
            delay_print("Yes, that's right!")
            handles_second_level()
        else:
            delay_print("Uuu, you're wrong!")
            handles_first_level()
            

