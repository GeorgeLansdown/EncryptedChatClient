'''
__MAIN__.PY
GEORGE LANSDOWN
COMBINES ALL OTHER ELEMENTS OF PROGRAM
'''

import __init__, userInterface, networkInterface, socket, threading, time       #DEPENDANCIES
from Tkinter import *


def network():              #NETWORK INTERFACE THREAD
        connection = networkInterface.connection()      #CREATES NETWORK INTERFACE OBJECT
        while True:
            if __init__.mode == "CLIENT":       #PUTS INTO CLIENT MODE
                connection.client()
            elif __init__.mode  == "SERVER":    #PUTS INTO SERVER MODE
                connection.server()
                
                
def user():              #USER INTERFACE THREAD - SETS UP INTERFACE
        root = Tk()
        root.wm_title("Network Chat Client")
        root.resizable(width=False, height=False)
        app = userInterface.Application(master=root)
        q = threading.Thread(target=interactions, args=[app])   #CREATE INTERACTIONS THREAD WITH ACCESS TO USER INTERFACE ELEMENTS
        root.after(50, q.start) #STARTS INTERACTIONS THREAD AFTER 50ms
        app.mainloop() #STARTS USER INTERFACE

def interactions(x):            #DATA DISPLAY THREAD    USES RECURRSION
        
        if __init__.mode == None:                       #UPDATES STATUS OF MODE BUTTONS
                x.connect["state"] = DISABLED
                x.ipEntry["state"] = DISABLED
                x.portEntry["state"] = DISABLED
                x.clientButton.deselect()
                x.serverButton.deselect()
        elif __init__.mode == "CLIENT":
                x.connect["state"] = "normal"
                x.ipEntry["state"] = "normal"
                x.portEntry["state"] = "normal"
        elif __init__.mode == "SERVER":
                x.connect["state"] = DISABLED
                x.ipEntry["state"] = DISABLED
                x.portEntry["state"] = DISABLED
        else:
                x.connect["state"] = DISABLED
                x.ipEntry["state"] = DISABLED
                x.portEntry["state"] = DISABLED
         
        if __init__.connected:                          #CHANGES VALUE OF CONNECT BUTTON WHEN IT IS CONNECTED TO A SERVER
                x.connect["text"] = "Disconnect"
        else:
                x.connect["text"] = "Connect"
        
        for f in range(x.messageLog.size(), len(__init__.messages)):            #UPDATES USER INTERFACE MESSAGE LOG AND CHAT LOG FILE WHEN THE __INIT__.MESSAGES LIST CHANGES
                x.messageLog.insert(END, str(__init__.messages[f][0])+"    "+__init__.messages[f][1])
                __init__.chatlog.write(str(__init__.messages[f][0])+"    "+__init__.messages[f][1]+"\n")
                
        time.sleep(0.5) #TIME DELAY SO FEWER PROCESSES ARE USED WHEN NOT REQUIRED
        
        
        if s.isAlive():         #IF USER INTERFACE THREAD STILL ALIVE
                interactions(x)         #RECURRSION TO MEET REQUIREMENTS                !!!!!!!!!!RECURSION!!!!!!!!!!
        else: 
                __init__.chatlog.close()        #OTHERWISE CLOSE CHATLOG FILE AS NO CHANGES WILL BE MADE


        
if __name__ == "__main__":      #IF BEING EXECUTED AS MAIN FILE
        t = threading.Thread(target=network)    #CREATE THREADS
        s = threading.Thread(target=user)       
        
        s.start()       #ACTIVATE THREADS
        t.start()
                