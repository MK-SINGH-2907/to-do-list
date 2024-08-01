#__main__


import features as feat


tasks = {}

while True:
    try:
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
            exit()
        else:
            print('oops!! wrong input! Try again')
    except ValueError:
        print('Invalid input! Enter a number.')
    except Exception as e:
        print(f'Error: {e}')
