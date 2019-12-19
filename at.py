def at():
    import time
    import subprocess as sp

    def inpu(z, anz):
        comalist = []

        for i in range(anz):
            print('add a command')
            comma = input('> ')
            comalist.append(comma)

        tim(z, comalist, anz)


    def tim(z, kom, anz):
        min = z * 60
        try:
            min = int(min)
        except:
            print('the time have to be at least a secound, start the programm again')
        print("time:", min ,'sec')
        time.sleep(min)
        if anz == 1:
            com(kom)
        else:
            com(kom)


    def com(kom):
        if anz == 1:
            sp.run(kom, shell = True)
        else:
            for kom in kom:
                print('to execute: ', kom)
                sp.run(kom, shell = True)


    print('x        |')
    print('   ----   |')
    print('x        |')
    print('at command with timer')
    while True:
        print("time in minutes (from now)")
        z = input('> ')
        try:
            z = float(z)
            break
        except:
            print("Input Mistake")
            print("try it again")
            time.sleep(1)
            continue

    while True:
        print("how many (int) default: 1")
        ma = input('> ')
        if ma == "":
            anz = 1
            break
        else:
            try:
                anz = int(ma)
                break
            except:
                print('Input Mistake')
                print("try it again")
                time.sleep(1)
                continue

    if anz == 1:
        print('bash command which will be executed (default: shutdown)')
        kom = input('> ')
        if kom == "":
            kom = "shutdown now"
        print('command: ', kom ,'in: ', z ,'min')
        tim(z, kom, anz)
    else:
        kom = False
        inpu(z, anz)
