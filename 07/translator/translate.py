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
        os.chdir(vmcode)
        vmfiles.extend([f for f in os.listdir(".") if os.path.isfile(f) and os.path.splitext(f)[1] == ".vm"])
        out_filename = os.path.basename(vmcode.strip("/"))+".asm"

    with open(out_filename, 'w') as out_file:
        writer = gen.Writer(out_file)
        writer.write_init()
        for in_filename in vmfiles:
            with open(in_filename, 'r') as in_file:
                parser = parse.Parser(in_file)
                base_infile = os.path.basename(in_filename)
                base_infile = os.path.splitext(base_infile)[0]
                writer.in_filename = base_infile

                while True:
                    try:
                        parser.advance()
                        cmd = parser.cmd
                        if cmd.cmd_type == parse.CmdType.ARITH:
                            writer.write_arithmetic(cmd)
                        elif cmd.cmd_type == parse.CmdType.LABEL:
                            writer.write_label(cmd)
                        elif cmd.cmd_type == parse.CmdType.GOTO:
                            writer.write_goto(cmd)
                        elif cmd.cmd_type == parse.CmdType.IF:
                            writer.write_if(cmd)
                        elif cmd.cmd_type == parse.CmdType.CALL:
                            writer.write_call(cmd)
                        elif cmd.cmd_type == parse.CmdType.FUNCTION:
                            writer.write_function(cmd)
                        elif cmd.cmd_type == parse.CmdType.RET:
                            writer.write_return(cmd)
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