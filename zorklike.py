# Variables
playerin = ''
stageindex = 0
playername = ''

def check_stage(stageindex):
    if stageindex == 0:
        playername = input('what is your name?')
        stageindex += 1
        check_stage(stageindex)
    if stageindex == 1:
        print(playername + "? is this really your name?")
        input(playerin)
        if playerin.lower == 'y' or 'yes':
            stageindex += 1
            check_stage(stageindex)
        elif playerin.lower == 'n' or 'no':
            stageindex -= 1
            check_stage(stageindex)
    if stageindex == 2:
        print(playername)

check_stage(stageindex)