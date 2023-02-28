from ICommand import ICommand
import sys
sys.path.append("./")
from TCP import send

class TranslateLocal(ICommand):
    def __init__(self,conn,word,dict) -> None:
        self.conn = conn
        self.word = word
        self.dict = dict

    def execute(self) -> None:
      try:
        diction = self.dict[self.word]
        command = f'TRANSLATEDSUC"{diction}"'
        send(self.conn,command)
      except:
          command = f'TRANSLATEDERR"error"'
          send(self.conn,command)



    

