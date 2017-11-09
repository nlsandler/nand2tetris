#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
import gen
import parse

def translate(vmcode):
    #vmcode can be a file or a directory
    vmfiles = []
    if os.path.isfile(vmcode):
        vmfiles.append(vmcode)
        out_filename = os.path.splitext(vmcode)[0] + ".asm"
    else: 
        #it's a directory, add all .vm files in it
        vmfiles.extend([f for f in os.listdir(vmcode) if isfile(f) and os.path.splitext(f)[1] == "vm"])
        out_filename = vmcode.strip("/")+".asm"

    with open(out_filename, 'w') as out_file:
        writer = gen.Writer(out_file)
        for in_filename in vmfiles:
            with open(in_filename, 'r') as in_file:
                parser = parse.Parser(in_file)
                writer.in_filename = in_filename

                while True:
                    try:
                        parser.advance()
                        cmd = parser.cmd
                        if cmd.cmd_type == parse.CmdType.ARITH:
                            writer.write_arithmetic(cmd)
                        else:
                            writer.write_push_pop(cmd)
                    except StopIteration:
                        #end of file
                        break                    

if __name__ == "__main__":
    vmcode = None
    try:
        vmcode = sys.argv[1]
    except IndexError:
        print("Enter name of .vm file")
        sys.exit(0)
    translate(vmcode)