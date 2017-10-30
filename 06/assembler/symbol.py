class SymbolTable:
    def __init__(self):
        #initialize with predefined symbols
        self.table = {
            "SP":       0,
            "LCL":      1,
            "ARG":      2,
            "THIS":     3,
            "THAT":     4,
            "SCREEN":   16384
        }

        #add virtual registers 0-15
        for i in range(16):
            reg_name = "R"+str(i)
            self.table[reg_name] = i

    def add_entry(self, symbol: string, address: int) -> None:
        self.table[symbol] = address

    def contains(self, symbol: string) -> bool:
        return symbol in self.table

    def get_address(self, symbol: string) -> int:
        return self.table[symbol]