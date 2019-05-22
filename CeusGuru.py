import os, time, webbrowser
def functions(pg = 0):
    print(pg)
def lesson():
    os.chdir(os.getcwd() + '\Documentation')
    print('Well do you like this tutorial? Do you like learning here')
    time.sleep(0.5)
    if input('Tell me would you like some videos? (Y/N)') == 'Y':
        print('You will not regret this choice.(Check your web browser)')
        webbrowser.open_new('https://www.youtube.com/playlist?list=PLWKjhJtqVAbnqBxcdjVGgT3uVR10bzTEB')
        return None
    else:
        print('Oh well...\n')
    while True:
        try:
            file = open('Modules.txt')
            print('\n' + file.read())
            file.close()
            module = input('What module do you choose? ')
            print('\n')
            os.chdir(os.getcwd() + '\Module ' + str(module)) #Directing to Module file
        except: #If no such module
            print('Please enter valid a module number.')
            continue
        try:
            file = open('List.txt')
            print(file.read(), '\n')
            file.close()
            lesson = input('What lesson will you choose? ')
            print('=======================Starting Lesson=========================')
            time.sleep(0.2)
            file = open('Lesson ' + lesson + '.txt')
            lines = file.readlines()
            lines, Question, Answer = lines[:lines.index("Question:\n")],lines[lines.index("Question:\n") : -1], lines[-1]
            content = ''
            for line in lines:
                time.sleep(0.1)
                print(line[:-1])
            Q = ''
            for line in Question:
                Q += line
            User_ans = ''
            while True:
                for count in range(2):
                    print(Q)
                    User_ans = input('>>>')
                    if User_ans != Answer[5:]:
                        if count == 1:
                            print('Wrong Answer. Let\'s read through the lesson again\n')
                        else:
                            print("Wrong Answer, Try again!\n")
                    else:
                        print('Congrats, You got it right!!!\n')
                        os.chdir('C:\\Users\\yuanx\\Desktop\\Hackathon')
                        return None
                for line in lines:
                    time.sleep(0.1)
                    print(line[:-1])
        except: #If lesson is invalid or the user want to change module or selected quiz
            if lesson == 'Quiz':
                os.chdir(os.getcwd() + '\Quiz')
                for question in range(1, 6):
                    file = open(str(question) + '.txt')
                    lines = file.readlines()
                    for count in range(2):
                        for line in lines[:-1]:
                            print(line, end = '')
                        User_ans = input('>>>')
                        if User_ans == lines[-1]:
                            print('Good Job, you got it right!\n')
                            break
                        elif count == 1:
                            print('Look at the module again, Try again next time.')
                            return None
                print('You finished the Quiz and got everything right. YAY!')
                return None
            if lesson == 'back':
                continue
            print('Please enter a valid lesson name.')
            continuex
