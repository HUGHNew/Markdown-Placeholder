from typing import Iterable
import re

import colors
from placer import Replacer

pattern = "(\\^\d+\\$)"

def load(input:str,charset:str="utf8",flat:bool=True):
    with open(input,"r",encoding=charset) as fd:
        lines = fd.readlines()
        return "".join(lines) if flat else lines

def loadList(input:str,charset:str="utf8")->Iterable[str]:
    return load(input,charset,False)

def loadStr(input:str,charset:str="utf8",flat:bool=True)->str:
    return load(input,charset,True)

def save(content:str,output:str,charset:str="utf8",suffix:str=""):
    with open(output,"w",encoding=charset) as fd:
        fd.write(content+suffix)

class Placeholder:
    """
    use flatten text only
    """
    def __init__(self,source:str,charset:str="utf8") -> None:
        self.__src=load(source,charset)
        self.__charset=charset
        self.__content=[] # Iterable[str]
        self.__holders=self.getHolders()
        self.rep=Replacer(self.__src)
    def getHolders(self)->set:
        match_list = [item for item in re.findall(pattern,self.__src)]
        # get matched into set
        return {*match_list} if len(match_list)!=0 else set()
    def substitute(self,content:str) -> list:
        if len(self.__holders) == 0:
            print(colors.Warning("No placeholder for substitution"))
        else:
            self.__content=[line[:-1] if line[-1]=='\n' else line 
                    for line in loadList(content,self.__charset)]
            self.showContents()
            self.rep.loadContent(self.__content)
            return self.rep.run(self.__holders)
    def showContents(self):
        for i in range(len(self.__content)):
            print(f"line {i+1}:{self.__content[i]}")