'''
NETWORKINTERFACE.PY
GEORGE LANSDOWN
DEALS WITH COMMUNICATIONS BETWEEN TWO COMPUTERS


__init__.messages.append([(time.strftime("%H:%M:%S", time.gmtime())),"[DEBUG] Switched to client mode"])
LINES WITH THIS ARE USED FOR APPENDING TIMESTAMPED MESSAGES IN __INIT__.MESSAGES TO SHOW USER
!!!!!THIS USES 2D ARRAYS!!!!!

'''
import __init__, socket, threading, time        #DEPENDANCIES

class connection(object):       #CONNECTION CLASS WITH TWO MODES
        def __init__(self):     #CONSTRUCTOR
            self.currentMessage = None #CREATES LOCAL CURRENTMESSAGE VARIABLE TO COMPARE TO __INIT__ ONE
	
        def client(self):       #CLIENT MODE
            self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #CREATES SOCKET CONNECTION
            __init__.messages.append([(time.strftime("%H:%M:%S", time.gmtime())),"[DEBUG] Switched to client mode"]) #WRITES TIMESTAMPED MESSAGE ABOUT CLIENT MODE
            while __init__.mode == "CLIENT":
                if __init__.connected:
                        try:    #ERROR HANDLING
                                            self.connection.connect((__init__.IP, int(__init__.PORT)))
                                            __init__.messages.append([(time.strftime("%H:%M:%S", time.gmtime())),"[DEBUG] Connected to "+str(__init__.IP)])
                                            __init__.connected = True
                                            while __init__.connected:
                                                if self.currentMessage != __init__.currentMessage and __init__.currentMessage != "":
                                                        self.currentMessage = __init__.currentMessage
                                                        self.connection.send(__init__.encrypt(self.currentMessage))     #SENDS ENCRYPTED MESSAGE
                                                        __init__.messages.append([(socket.gethostbyname(socket.gethostname()), time.strftime("%H:%M:%S", time.gmtime())),self.currentMessage])
                                                else:
                                                        self.connection.send("@]32[/")  #RANDOM STRING SENT TO SIGNIFY BLANK MESSAGE TO AVOID ISSUES WITH EMPTY PACKETS
                                                self.data = self.connection.recv(1024)
                                                if self.data and self.data.split("/")[0] != "@]32[":    #ENSURES MESSAGE ISNT 'BLANK'
                                                        __init__.messages.append([(__init__.IP, time.strftime("%H:%M:%S", time.gmtime())),__init__.encrypt(self.data)]) 
                        except socket.error:    #ACCEPT ERROR ABOUT SERVER REFUSING CONNECTION
                                            __init__.messages.append([(time.strftime("%H:%M:%S", time.gmtime())), "[DEBUG] Socket error, cannot connect"]) 
                        finally:        #ENSURES CONNECTIONS ARE CLOSED PROPERLY
                                            __init__.connected = False
                                            __init__.mode = None
                                            self.connection.close();
                        

        def server(self):       #SERVER MODE
            self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            __init__.messages.append([(time.strftime("%H:%M:%S", time.gmtime())),"[DEBUG] Switched to server mode"])
            self.connection.bind((socket.gethostbyname(socket.gethostname()), int(__init__.PORT)))
            __init__.messages.append([(time.strftime("%H:%M:%S", time.gmtime())),"[DEBUG] Hosting on "+socket.gethostbyname(socket.gethostname())])
            self.connection.listen(1)
            self.conn, self.addr = self.connection.accept()
            __init__.messages.append([(time.strftime("%H:%M:%S", time.gmtime())),"[DEBUG] Connection from "+str(self.addr[0])])
            try:
                while self.conn and __init__.mode == "SERVER":
                        if self.currentMessage != __init__.currentMessage and __init__.currentMessage != "":
                                self.currentMessage=__init__.currentMessage
                                self.conn.send(__init__.encrypt(self.currentMessage))
                                __init__.messages.append([(__init__.IP, time.strftime("%H:%M:%S", time.gmtime())),self.currentMessage])
                        else:
                                self.conn.send("@]32[/")        #RANDOM STRING SENT TO SIGNIFY BLANK MESSAGE TO AVOID ISSUES WITH EMPTY PACKETS
                        self.data = self.conn.recv(1024)
                        if self.data and self.data.split("/")[0] != "@]32[":    #ENSURES MESSAGE ISNT 'BLANK'
                                __init__.messages.append([(str(self.addr[0]), time.strftime("%H:%M:%S", time.gmtime())),__init__.encrypt(self.data)])
            except socket.error:        #ACCEPT ERROR FOR BROKEN PIPE
                __init__.messages.append([(time.strftime("%H:%M:%S", time.gmtime())),"[DEBUG] Server lost connection"])             
            finally:    #ENSURES CONNECTIONS ARE CLOSED PROPERLY
                self.connection.close()
                __init__.mode = None
                
        def __del__(self):      #DESTRUCTOR TO ENSURE CONNECTION IS CLOSED
            __init__.messages.append([(time.strftime("%H:%M:%S", time.gmtime())),"[DEBUG] Shutting down object"])
            self.connection.close()
