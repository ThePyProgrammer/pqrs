#MUN Program

from time import sleep as s

def add_ppl(gslst):
    currname = input('Add to GSL: ')
    while len(currname):
        gslst.append(currname)
        currname = input('Add to GSL: ')
    print('\nThe GSL currently has the following people:', '________________________________', sep="\n")
    for i in gslst:
        print(i)
    print('________________________________')

def chtime():
    try:
        while True:
            time = int(input('Change time: '))
    except ValueError:
        print('\nThe GSL will now have a time limit of', time, 'seconds.')
        return time
    

def adjourn(times):
    print('This debate shall be adjourned.')
    timelst = list(times.items())
    timelst = sorted(timelst, key= lambda x: x[0])
    for j in timelst:
        print(j[1], 'came in with', j[0], 'of speaking time.')
    print('\n', timelst[-1][1], 'has won Best Delegate for overall contribution to this issue.')

def gslspeech(name, times, t):
    if not len(input(name+', please come forward for your speech ')):
        for k in range(t):
            try:
                s(1)
            except KeyboardInterrupt:
                yielding = input('\nYou have finished. How would you like to yield your time?: ')
                if yielding == 'POI':
                    timeleft = 59 - k
                    print('You have', timeleft, 'seconds left')
                    s(1)
                    continue
                if name not in times:
                    times[name] = k
                else:
                    times[name] = times[name] + k
                break
            else:
                if k == 59:
                    print('And your time is up!')
                    appending = k if name not in times else times[name] + k
                    times[name] = appending

def gsl(gslst=[], times={}, t=60):
    print("\nPlease add people for the General Speaker's list to commence")
    add_ppl(gslst)
    while True:
        while True:
            func = input('\nInput func: ')
            if not len(func):
                break
            if func == 'add':
                add_ppl(gslst)
            elif func == 'time':
                t = chtime()
            elif func == 'adj':
                adjourn(times)
                return []
        print('\nAre there any motions on the floor?')
        # unmod, time, name
        # mod, time, speaking_time, name
        motions = []
        ui = input('Enter Motion: ')
        while len(ui):
            motions.append(ui)
            ui = input('Enter Motion: ')
        if len(motions):
            return motions, gslst, times
        print('With no motions on the floor, the GSL has been reopened')
        print('\nMay the General Speaker\'s List begin.\n')
        gslspeech(gslst.pop(0), times, t)

def roll_call(args):
    statement_dict = dict()
    for i in args:
        statement_dict[i] = input(i+' : ')
    vals = list(statement_dict.values())
    num = vals.count('P&V')
    proced_vote = num//2 + 1
    sub_vote = round(2/3 * num)
    print('With', num, 'people present and voting, a procedural vote will be', proced_vote, 'and a substantiative vote will be', sub_vote)
    return (proced_vote, sub_vote)

def voteformotion(motions, proced_vote):
    maxy = 0
    for i in motions:
        num = input('Who votes for '+i)
        if num < proced_vote:
            print('With the vote count not passing the procedural vote count, this motion does not pass')
            continue
        if num > maxy:
            maxy, maxind = num, i
            print('This motion can pass')
            
    print('With the greatest amount of votes of', maxy, 'notes, the motion:', maxind, 'passes')
    return maxind

def unmodcauc(time, name):
    print('You may begin this unmoderated caucus of', time, 'minutes.')
    s(time*60)
    print('Your time is up. Delegate of ', name, ', please report summarise the unmoderated caucus in 1 minute or lesser', sep='')
    for i in range(60):
        try:
            s(1)
        except KeyboardInterrupt:
            print('Thank you delegate. Please be seated.')
        else:
            if i == 59:
                print('And you time is up.')

def modcauc(speaker_time, time, name):
    print('You may begin this moderated caucus of', time, 'minutes.')
    begend = bool(input('Will '+name+' start or end? ') == 'start')
    namelst = []
    currname = input('Add to Moderated Caucus: ')
    while len(currname):
        namelst.append(currname)
        currname = input('Add to Moderated Caucus: ')
    print('\nThe Moderated Caucus currently has the following people:', '________________________________', sep="\n")
    namelst = [name] + namelst if begend else namelst + [name]
    for i in namelst:
        print(i)
    print('________________________________')
    still_need = bool(len(namelst) != (time*60)//speaker_time)
    while len(namelst):
        currname = namelst.pop(0)
        print('\nDelegate of', currname, 'please arise.')
        for i in range(speaker_time):
            try:
                s(1)
            except KeyboardInterrupt:
                break
        if still_need and not(len(namelst)-2):
            currname = input('Add to Moderated Caucus: ')
            while len(currname) and len(namelst) != (time*60)//speaker_time:
                if begend:
                    namelst.append(currname)
                else:
                    namelst = namelst[:-1] + [currname, name]
                currname = input('Add to Moderated Caucus: ')

def actual_mun(*args):
    (proced_vote, sub_vote) = roll_call(args)
    while True:
        motions = gsl()
        if not len(motions):
            return 
        motion = voteformotion(motions, proced_vote)
        lst = motion.split(', ')
        if len(lst)-3:
            modcauc(int(lst[-2]), int(lst[1]), lst[-1])
        else:
            unmodcauc(int(lst[1]), lst[-1])
