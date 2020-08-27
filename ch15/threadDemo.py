import threading, time

print('Start of program')

def take_nap():
    time.sleep(5)
    print('Wake up!')

thread_obj = threading.Thread(target=take_nap)
thread_obj.start()

print('End of program')