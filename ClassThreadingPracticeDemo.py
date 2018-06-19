#Class demo 6/19/2018
#threading
#import pygame
import threading
import time

#lock delay for timing control
lock = threading.Lock()

def f():
    global lock
    #time.sleep(0.01)
    lock.aquire(True)
    print "this is running in a thread {}".format(n)
    print "threads are good for running things in the background"
    lock.release()
    r.r = r.n * 2
    #suggested thread graphics?
    #suggested thread online stuff
    
class R(object):
    def __init__(self, n):
        self.n = n

r0 = R(0)
r1 = R(1)
r2 = R(2)
r3 = R(3)
#t = threading.Thread(target=f)# or kwargs={target, f}
#target, args=(1,2,etc) kwargs=None 

t0 = threading.Thread(target=f, args=(r0,))
t1 = threading.Thread(target=f, args=(r1,))
t2 = threading.Thread(target=f, args=(r2,))
t3 = threading.Thread(target=f, args=(r3,))


#t.start()
t0.start()
t1.start()
t2.start()
t3.start()
lock.aquire(True)
print "threads are started"
lock.release()
#t.join()
t0.join()
t1.join()
t2.join()
t3.join()

print r0.r, r1.r, r2.r, r3.r

#locks can stop a thread until lock is released


pygame.init()
screen = pygame.display.set_mode((800,600))
run = True
def quit(e): #optional event registration method
    global run
    run = False
events.register(pygame.QUIT, quit)

clock = pygame.Clock()

while run:
    clock.tick(30)#30 FPS

    #Events First
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    #Physics Second

    #Rendering Third
    
    

pygame.quit()
