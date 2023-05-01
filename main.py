import threading
import queue
from time import sleep
import random


class MyClass:
    def __init__(self):
        self.Qin = queue.Queue()
        self.q2=queue.Queue()
        self.ll=[]
        self.cm=False
        self.orderid=''
        t1 = threading.Thread(target=self.qfill)
        t2 = threading.Thread(target=self.function2)
        t3 = threading.Thread(target=self.run)
        t1.start()
        t2.start()
        t3.start()
        self.back()
        

    def qfill(self):
        while True:
            number=random.randint(1,15)
            # y=(f"{number}_not")
            # y=()
            if number ==(5 or 7):
                self.cm=False
                self.Qin.put((number,"done"))
            else:
                self.Qin.put((number,"not"))
            sleep(2)

    def run(self):
        while True:
            try:
                data=self.q2.get()
                if data is not None:
                        self.orderid=data[0]
                        if data[1]=="done":
                            self.cm=True
            except:
                pass
    def back(self):
        while True:
            if self.cm==True:
                print("--TRUE--")
                self.cm=False


    def function2(self):
        # This is the second function to run in a separate thread
        print("Function 2 started")
        # Get items from the queue and print them
        while True:
            try:
                data=self.Qin.get_nowait()
                print(data)
                if data[1]=="done":
                    self.q2.put(data)
                    # self.ll.append(data)
                    
                # if self.cm==False:
                #     print("Yes... Working",data)
                    
                #     sleep(1)

                #     self.cm=True
            except:
                pass
            
            # item = self.q.get()
            # if item is None:
            #     break
            # print("Item:", item)
            # self.q.task_done()
        # print("Function 2 finished")

# Create an object of the class
my_object = MyClass()

'''
qwertyuiasdfghjk pill mee   addmid more by develop


'''

# Wait for the queue to be empty before exiting the program
# my_object.q.join()
# my_object.Q
