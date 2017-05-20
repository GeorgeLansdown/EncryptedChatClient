'''_
__INIT__.PY
GEORGE LANSDOWN
CONTAINS VARIALES AND FUNCTIONS THAT NEED TO BE ACCESSED BY ALL OTHER PARTS
'''
import socket, time #DEPENDANCIES


IP = socket.gethostbyname(socket.gethostname())     #SETS IP ADDRESS TO MACHINES CURRENT IP ADDRESS
PORT = 6969 #SETS PORT TO 6969
mode = None   
messages = []   #USED FOR STORING ALL USER SIDE INFORMATION, GETS DUMPED TO CHATLOG WHEN PROGRAM IS CLOSED
currentMessage = None   #USED FOR SENDING MESSAGES
connected = False   #VARIABLE FOR STATUS OF CLIENT CONNECTIONS

chatlog = open("CHATLOG "+time.strftime("%d-%b-%Y %H.%M.%S", time.gmtime())+".txt", "w")    #!!!!!!!!!FILE OPERATIONS!!!!!!!!    OPENS CHATLOG FILE WITH TIME STAMP


def validateIPandPort(ip, port):    #FUNCTION FOR VALIDATING IP AND PORT PAIR
    if ip != "" and port != "":
        try:
            IPsplit = ip.split(".") #SPLITS IP INTO LIST WITH INTEGER VALUES
            for each in IPsplit: 
                if int(each) < 0 or int(each) > 255:    #ENSURES THAT INTEGER VALUES EXIST WITHIN 0 TO (2^8-1)
                    return False
            if len(IPsplit) == 4:   #ENSURES THAT ONLY 4 COMPONENTS EXIST x.x.x.x is valid but x.x.x is not
                if int(port) > 0 and int(port) < 65536: #ENSURES PORT EXISTS IN RANGE
                    return True
        except ValueError:
            return False

def encrypt(x):     #FAIRLY UNIMPRESSIVE ENCRYPTION ALGORITHM - ROT13 + INVERTING UPPERCASE AND LOWERCASE - BLUE BECOMES oyhr
    alphabet = {"a":"n","b":"o","c":"p","d":"q","e":"r","f":"s","g":"t","h":"u","i":"v","j":"w","k":"x","l":"y","m":"z","n":"a","o":"b","p":"c","q":"d","r":"e","s":"f","t":"g","u":"h","v":"i","w":"j","x":"k","y":"l", "z":"m"} #DICTIONARY OF LETTER SHIFTS TO ENSURE THAT CORRECT CHARACTERS ARE USED   
    newstring = ""  #EMPTY NEW STRING
    for f in x:
        try:
            if f.isupper(): newstring += alphabet[f.lower()]
            else: newstring += alphabet[f].upper()
        except KeyError: #WHEN CHARACTER ISN'T IN DICTIONARY KEYERROR IS RAISED
            newstring += f #IGNORES SHIFT
    return newstring