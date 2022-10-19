from multiprocessing import Process



def print_func(continent='Asia'):# Python 3.4+

    print ('The name of continentis : ' , continent)
if __name__ == '__main__':
    names = ['Ameica' , 'Europe' , 'Africa']
    procs = []
    proc = Process(target=print_func)
    procs.append(proc)
    proc.start()

     # instantiating process with arguments
    for name in names:
        # print(name)
        proc = Process(target=print_func, args=(name,))
        procs.append(proc)
        proc.start()

    #Complete the processes

    for proc in procs:
        proc.join()