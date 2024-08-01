#__module__

def addtask(tasks):
    no = int(input('Number of entries: '))
    for i in range(no):
        taskname = input('Enter the task: ')
        tasks[taskname] = 'not done'
    print('Task added successfully!!')

def tasklist(tasks):
    j = 1
    for i in tasks:
        if tasks[i].lower() == 'not done':
            print(j, '. ', i)
            j += 1

def marktask(tasks):
    j = 1
    for i in tasks:
        if tasks[i].lower() == 'not done':
            print(j, '. ', i)
            j += 1
    
    uinput = input('Enter the name of the task you want to mark as done: ')
    for i in tasks:
        if i.lower() == uinput.lower():
            tasks[i] = 'done'
    print('Task marked done successfully')
