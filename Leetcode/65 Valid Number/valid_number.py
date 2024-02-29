import re


class Solution:
    def isNumber(self, s: str) -> bool:
        number = re.compile(
            r"[+,-]?([0,1,2,3,4,5,6,7,8,9]+|[0,1,2,3,4,5,6,7,8,9]+\.[0,1,2,3,4,5,6,7,8,9]*|[0,1,2,3,4,5,6,7,8,9]*\.[0,1,2,3,4,5,6,7,8,9]+)([e,E][+,-]?[0,1,2,3,4,5,6,7,8,9]+)?")
        if number.fullmatch(s):
            return True
        return False
