#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import parse
from typing import IO

CMPS = {
    "not":"!",
    "neg":"-",
    "and":"&",
    "or":"|",
    "add":"+",
    "sub":"-",
    "gt":"JGT",
    "lt":"JLT",
    "eq":"JEQ"
}

#instructions to push D onto stack and increment SP
PUSH_D_INSTRUCTIONS = """
    @SP
    A=M
    M=D
    @SP
    M=M+1
"""

#instructions to pop top of stack into D and decrement SP

class Writer:

    def __init__(self, f: IO[str]) -> None:
        self.f = f
        self.label_ctr = 0

    def write_arithmetic(self, command: parse.Command) -> None:
        op = command.arg1
        comp = CMPS[op]
        if op in parse.UNARY_OPS:
            instructions = """//{op}
    @SP
    A=M-1
    M={cmp}M""".format(op=op, cmp=comp)
        elif op in parse.BINARY_OPS:
            instructions = """//{op}
    @SP
    AM=M-1
    D=M
    @SP
    A=M-1
    M=M{cmp}D""".format(op=op, cmp=comp)
        elif op in parse.CMP_OPS:
            instructions = """//{op}
//set result to -1 (true)
    @R13
    M=-1
//pop both values off the stack
    @SP
    AM=M-1
    D=M
    @SP
    A=M-1
//perform comparison
    D=M-D
    @label{ctr}
    D;{cmp}
//comparison was false, set result to 0
    @R13
    M=0
(label{ctr})
//add result to stack
    @R13
    D=M
    @SP
    A=M-1
    M=D""".format(op=op, cmp=comp, ctr=self.label_ctr)
            self.label_ctr += 1
        else:
            raise RuntimeError("Unknown op")

        #write the instruction
        self.f.write(instructions+"\n")


    def write_push_pop(self, command:  parse.Command) -> None:
        if command.arg1 == "constant":
            if command.cmd_type == parse.CmdType.PUSH:
                instructions = """//push constant {c}
    @{c}
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1""".format(c=command.arg2)
            else:
                raise RuntimeError("Cannot pop a constant")
        elif command.arg1 =="local":
            if command.cmd_type == parse.CmdType.PUSH:
                instructions = """//push local {index}
//store LCL+index in R13
@LCL
D=M //D holds base address of LCL
@{index}
A=D+A //A holds address of value we want to push
D=M //D holds value we want to push
@SP
A=M
M=D //put value on stack
//increment stack pointer
@SP
M=M+1""".format(index=command.arg2)

        else:
            raise NotImplementedError

        self.f.write(instructions+"\n")

