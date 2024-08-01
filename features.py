#__module__

def addtask(tasks):
    try:
        no = int(input('Number of entries: '))
        if no < 1:
            raise ValueError("Number shouldn't be less than 1.")
        for i in range(no):
            taskname = input('Enter the task: ')
            tasks[taskname] = 'not done'
        print('Task added successfully!!')
    except ValueError:
        print('Invalid input!Enter a number.')
    except Exception as e:
        print(f'Error : {e}')

def tasklist(tasks):
    try:    
        j = 1
        for i in tasks:
            if tasks[i].lower() == 'not done':
                print(j, '. ', i)
                j += 1
    except Exception as e:
        print("Error: ", e)

def marktask(tasks):
    try:
        j = 1
        for i in tasks:
            if tasks[i].lower() == 'not done':
                print(j, '. ', i)
                j += 1
        
        uinput = input('Enter the name of the task you want to mark as done: ')
        for i in tasks:
            if i.lower() == uinput.lower():
                tasks.pop(i)
                print('Task marked done successfully')
                return
        print("Task not found!!")
    except ValueError:
        print("Invalid Input! Enter a number!")
    except Exception as e:
        print("Error: ", e)
