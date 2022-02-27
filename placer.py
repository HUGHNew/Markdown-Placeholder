from typing import Iterable
import colors
class Replacer():
    def __init__(self,source:str="",content:Iterable[str]=[]) -> None:
        self.source=source
        self.content=content
    def loadContent(self,content:Iterable[str])->None:
        self.content=content
    def run(self,holders:set)->str:
        # ^0$ -> 0
        # stubs = set(map(lambda x:x[1:-1],holders))
        result=self.source
        for holder in holders:
            idx = int(holder[1:-1])
            if idx >= len(self.content):
                print(colors.Warning(f"{holder} is out of range!"))
            else:
                print(f"holder:{holder};cont:{self.content[idx]}")
                result=result.replace(holder,self.content[idx])
        return result
