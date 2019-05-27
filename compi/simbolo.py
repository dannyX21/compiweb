class Simbolo:
    def __init__(self, lexema, token):
        self.Lexema = lexema
        self.Token = token

    def __repr__(self):
        return ("Lexema: " + self.Lexema).ljust(20) + ("Token: " +
    str(self.Token)).rjust(12)

TOKENS = {
    'BOOL': 256,
    'CALL': 257,
    'CHAR': 258,
    'CONST_CHAR': 259,
    'CONST_STRING' : 260,
    'DIF' : 261,
    'DO' : 262,
    'ELSE' : 263,
    'FLOAT' : 264,
    'FOR' : 265,
    'FUNCTION' : 266,
    'ID' : 267,
    'IF' : 268,
    'IGU' : 269,
    'INT' : 270,
    'MAI' : 271,
    'MAIN' : 272,
    'MAY' : 273,
    'MEI' : 274,
    'MEN' : 275,
    'NUM' : 276,
    'NUMF' : 277,
    'READ' : 278,
    'RETURN' : 279,
    'STRING' : 280,
    'THEN' : 281,
    'TO' : 282,
    'VOID' : 283,
    'WHILE' : 284,
    'WRITE' : 285,
    'FALSE' : 286,
    'TRUE' : 287
    }

CONST_TOKENS = {}
for key,value in TOKENS.items():
    CONST_TOKENS[value]=key
