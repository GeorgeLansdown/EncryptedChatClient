'''
tkinter class for user interface
George Lansdown 13/08/16
'''

from Tkinter import *           #DEPENDANCIES
import networkInterface, __init__, time         

class Application(Frame):
        def __init__(self, master=None):        #CONSTRUCTOR FOR USER INTERFACE CLASS
                Frame.__init__(self, master)
                self.pack()
                self.createWidgets()
        
        def createWidgets(self):        #CREATES USER INTERFACE ELEMENTS
                #Labels
                self.ipEntryLabel = Label(master=self, text="IP").grid(row=0, column=0)
                self.portEntryLabel = Label(master=self, text="PORT").grid(row=0, column=2)
                self.ipLabel = Label(master=self, text="Your IP address is: "+__init__.IP)
                self.ipLabel.grid(row=1, column=0)
                self.portLabel = Label(master=self, text="Your port is: "+str(__init__.PORT))
                self.portLabel.grid(row=1, column=2)

                #Entry elements
                self.ipEntry = Entry(master=self)
                self.ipEntry.insert(0, __init__.IP)
                self.ipEntry.grid(row=0, column=1)
                self.portEntry = Entry(master=self)
                self.portEntry.insert(0, __init__.PORT)
                self.portEntry.grid(row=0, column=3)
                self.messageEntry = Entry(master=self, width=70)
                self.messageEntry.bind("<Return>", lambda event: self.changeMessage(self.messageEntry.get()))
                self.messageEntry.grid(row=3, columnspan=4)

                #Listbox
                self.scrollbar = Scrollbar(master=self, orient="vertical")
                self.messageLog = Listbox(master=self, width=100, yscrollcommand=self.scrollbar.set)
                self.scrollbar.config(command=lambda *args: apply(self.messageLog.yview, args))
                self.scrollbar.grid(column=6, row=2, rowspan=1, sticky="NS")
                self.messageLog.grid(row=2, columnspan=6)

                #Buttons
                self.connect = Button(master=self, text="connect", command=lambda: self.changeIPandPORT(self.ipEntry.get(), self.portEntry.get()))
                self.connect.grid(row=0, column=4)
                self.send= Button(master=self, text="send", command=lambda: self.changeMessage(self.messageEntry.get()))
                self.send.grid(row=3, column=4)
                self.clientButton = Radiobutton(master=self, text="Client", value="CLIENT", indicatoron=0, command=lambda: self.changeMode("CLIENT"))
                self.clientButton.grid(row=0, column=5)
                self.serverButton = Radiobutton(master=self, text="Server", value="SERVER", indicatoron=0, command=lambda: self.changeMode("SERVER"))
                self.serverButton.grid(row=1, column=5)
                
        def changeIPandPORT(self, x, y):        #METHOD FOR CHANGING IP AND PORT VARAIBLES IN __INIT__
                if __init__.connected:
                        __init__.connected = False
                        __init__.mode = None
                        __init__.messages.append([(time.strftime("%H:%M:%S", time.gmtime())),"[DEBUG] Disconnected from server"])
                else:
                        if __init__.validateIPandPort(x, y):
                                __init__.IP = x
                                __init__.PORT = y
                                __init__.connected = True
                        else:
                                __init__.messages.append([(time.strftime("%H:%M:%S", time.gmtime())),"[DEBUG] Invalid form for IP and Port, must be in the form XXX.XXX.XXX.XXX XXXX where X is Integer"])
        def changeMessage(self, x):             #METHOD FOR CHANGING THE CURRENT MESSAGE VARIABLE IN __INIT__
                __init__.currentMessage = x
        def changeMode(self, x):                #METHOD FOR CHANGING THE MODE BETWEEN CLIENT AND SERVER
                __init__.mode = x
                
