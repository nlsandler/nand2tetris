#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import parse
import code
import symbol
import os
import sys
from typing import Union

def resolve_symbol(symbol: Union[int, str], table: symbol.SymbolTable) -> int:
    """convert symbol to corresponding address,
    and add to symbol table if needed"""
    if isinstance(symbol, str):
        if table.contains(symbol):
            return table.get_address(symbol)
        else:
            return table.add_entry(symbol)
    else:
        return symbol

def assemble_command(parser: parse.Parser, table: symbol.SymbolTable) -> str:
    """convert the current command into a binary string"""
    if parser.command_type() == parse.CmdType.A:
        symbol = parser.symbol()
        num = resolve_symbol(symbol, table)
        return "{:016b}".format(num)
    elif parser.command_type() == parse.CmdType.C: #C command
        op = "1"
        dest_sym = parser.dest()
        dest = code.dest(dest_sym)

        comp_sym = parser.comp()
        comp = code.comp(comp_sym)

        jump_sym = parser.jump()
        jump = code.jump(jump_sym)

        return "111{comp}{dest}{jump}".format(dest=dest, comp=comp, jump=jump)
    else:
        raise RuntimeError("Cannot assemble pseudo-command")


def assemble(filename:str ) -> None:
    #get output file name
    basename, _ = os.path.splitext(filename)
    outfile = basename+".hack"

    with open(filename, 'r') as infile, open(outfile, 'w') as out:
        #first pass: build symbol table
        parser = parse.Parser(infile)
        symbols = symbol.SymbolTable()
        address = 0
        while True:
            try:
                parser.advance()
                if parser.command_type() == parse.CmdType.L:
                    symbols.add_entry(parser.symbol(), address)
                else:
                    address += 1
            except StopIteration:
                break

        #second pass: generate assembly
        parser.reset()
        while True:
            try:
                parser.advance()
                if parser.command_type() != parse.CmdType.L:
                    cmd = assemble_command(parser, symbols)
                    print(cmd, file=out)
            except StopIteration:
                #end of file
                break

if __name__ == "__main__":
    filename = None
    try:
        filename = sys.argv[1]
    except IndexError:
        print("Enter name of .asm file")
        sys.exit(0)
    assemble(filename)

