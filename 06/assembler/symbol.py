from typing import Dict

class SymbolTable:
    def __init__(self):
        #initialize with predefined symbols
        self.table : Dict[str, int] = {
            "SP":       0,
            "LCL":      1,
            "ARG":      2,
            "THIS":     3,
            "THAT":     4,
            "SCREEN":   16384,
            "KBD":      24576
        }

        #add virtual registers 0-15
        for i in range(16):
            reg_name = "R"+str(i)
            self.table[reg_name] = i

        self.next_available = 16

    def add_entry(self, symbol: str, address: int=None) -> int:
        if symbol in self.table:
            raise ValueError("Symbol {} already in table!".format(symbol))

        #caller should set address for instruction labels, use next_available for RAM labels
        if not address:
            address = self.next_available #note: no error handling if we've allocated up to SCREEN

        self.table[symbol] = address
        self.next_available += 1
        return self.table[symbol]

    def contains(self, symbol: str) -> bool:
        return symbol in self.table

    def get_address(self, symbol: str) -> int:
        return self.table[symbol]