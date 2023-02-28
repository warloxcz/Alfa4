import socket
import sys
from threading import Thread
from Dictionary import Dictionary
from Log import Log
from TCP import receive,send,parse_message
import ipaddress
sys.path.append("./Command")
from Command.PingCommand import PingCommand
from Command.TranslateLocal import TranslateLocal
from Command.TranslateScan import TranslateScan
from Log import Log


class Server():

    def __init__(self,address,port:int,dict:Dictionary,port_range,ip_range) -> None:
        self.dict = dict
        self.port_range = port_range
        self.ip_range = ip_range
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((address,port))
        self.socket.listen()
        while True:
            conn, addr = self.socket.accept()
            t = Thread(target=self.accept_client,args=(conn,))
            t.start()

    def accept_client(self,conn):
            i = 0
            while True:
                try:
                   message = receive(conn)
                   parsed = parse_message(message)
                   Log.out(parsed)
                except TimeoutError as t:
                   Log.out("Timeout")
                   conn.close()
                   break
                except Exception as e:
                   Log.out("Error")
                   Log.out(e)
                   i += 1
                   if i == 20:
                       conn.close()
                       break
                   continue
                try:
                    if parsed[0] == "TRANSLATEPING":
                        PingCommand(conn,self.dict.name).execute()
                    elif parsed[0] == "TRANSLATELOCL":
                        TranslateLocal(conn,parsed[1],self.dict.word_dict).execute()  
                    elif parsed[0] == "TRANSLATESCAN":
                        TranslateScan(conn,parsed[1],self.dict,ipaddress.ip_network(self.ip_range),self.port_range).execute()  
                    else:
                        send(conn,'TRANSLATEDERR"uknown command"')
                    
                except Exception as e:
                    pass
                
    
    



