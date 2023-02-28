from ICommand import ICommand
import sys
sys.path.append("./")
from TCP import send
class PingCommand(ICommand):
    def __init__(self,conn,name:str) -> None:
        self.conn = conn
        self.name = name

    def execute(self):
        command = f'TRANSLATEPONG"{self.name}"'
        send(self.conn,command)
        