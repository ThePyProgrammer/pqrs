def documentation(topic):
    topicdict = {
        'munprog': 'MUN Program',
        'games': 'Games',
        'plotting': 'Plotting',
        'pytools': 'PyTools',
        'utilities': 'Utilities'
        }
    topic = topicdict[topic]
    file = open(topic+'.txt')
    cont = file.read()
    print(cont)
    file.close()
    return
