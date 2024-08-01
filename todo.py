#__main__


import features as feat


tasks = {}
rerun = True

while rerun:
    print('\t MENU')
    print('1. Add new task \n2. List of unfinished tasks \n3. Mark a task done \n4. Exit')
    option = int(input('CHOOSE AN OPTION : '))

    if option == 1:
        feat.addtask(tasks)
    elif option == 2:
        feat.tasklist(tasks)
    elif option == 3:
        feat.marktask(tasks)
    elif option == 4:
        print('Exiting...')
        rerun = False
    else:
        print('oops!! wrong input! Try again')
