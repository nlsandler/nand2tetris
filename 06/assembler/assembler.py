#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import parse
import code
import os
import sys

def assemble_command(parser: parse.Parser) -> str:
    """convert the current command into a binary string"""
    if parser.command_type() == parse.CmdType.L:
        return None #pseudo-command
    elif parser.command_type() == parse.CmdType.A:
        symbol = parser.symbol()
        return "{:016b}".format(symbol)
    else: #C command
        op = "1"
        dest_sym = parser.dest()
        dest = code.dest(dest_sym)

        comp_sym = parser.comp()
        comp = code.comp(comp_sym)

        jump_sym = parser.jump()
        jump = code.jump(jump_sym)

        return "111{comp}{dest}{jump}".format(dest=dest, comp=comp, jump=jump)


def assemble(filename:str ) -> None:
    parser = parse.Parser(filename)

    #get output file name
    basename, _ = os.path.splitext(os.path.basename(filename))
    outfile = basename+".hack"

    with open(outfile, 'w') as out:
        while True:
            try:
                parser.advance()
                cmd = assemble_command(parser)
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

