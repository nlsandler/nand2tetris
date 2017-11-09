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

BASE_PTRS = {
    "local": "LCL",
    "this": "THIS",
    "that": "THAT",
    "argument": "ARG"
}

BASE_VALS = {
    "pointer": "3",
    "temp": "5"
}

#instructions to push D onto stack and increment SP
PUSH_D_INSTRUCTIONS = """
    @SP
    A=M
    M=D
    @SP
    M=M+1
"""

#instructions to load value at segment[index] into D
#for directly memory-mapped segments (pointer, temp), {reg} is A
#for segments where we only store base ptr (local, argument, this, that),
#we need to dereference that pointer, so {reg} is M 
LOAD_INTO_D_INSTRUCTIONS = """
//push {segment} {index}
    @{base}
    D={reg} //D holds base address of segment
    @{index}
    A=D+A //A holds address of value we want to push
    D=M //D holds value we want to push"""

#instructions to pop value into segment[index]
#for directly memory-mapped segments (pointer, temp), {reg} is A
#for segments where we only store base ptr (local, argument, this, that),
#we need to dereference that pointer, so {reg} is M 
POP_INSTRUCTIONS = """
//pop {segment} {index}

//calculate value we want to pop to, store in R13
    @{base}
    D={reg} //D holds base address of segment
    @{index}
    D=D+A //D holds address we want to write to
    @R13
    M=D //store address to write to in R13

//pop top of stack into D
    @SP
    AM=M-1
    D=M //D holds top value on stack

//write D to address stored in R13
    @R13
    A=M
    M=D"""

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


    def write_push(self, command: parse.Command) -> None:
        #first generate code to get value into D

        if command.arg1 == "constant":
            instructions = """//push constant {c}
    @{c}
    D=A""".format(c=command.arg2)
        elif command.arg1 in BASE_PTRS:
            base = BASE_PTRS[command.arg1]
            instructions = LOAD_INTO_D_INSTRUCTIONS.format(index=command.arg2, 
                                                                segment=command.arg1, 
                                                                base=base, reg="M")
        elif command.arg1 in BASE_VALS:
            base = BASE_VALS[command.arg1]
            instructions = LOAD_INTO_D_INSTRUCTIONS.format(index=command.arg2, 
                                                                segment=command.arg1, 
                                                                base=base, reg="A")
        #Now push value in D onto stack
        instructions += PUSH_D_INSTRUCTIONS

        self.f.write(instructions+"\n")

    def write_pop(self, command: parse.Command) -> None:
        if command.arg1 in BASE_PTRS:
            base = BASE_PTRS[command.arg1]
            instructions = POP_INSTRUCTIONS.format(index=command.arg2,
                                                        segment=command.arg1,
                                                        base=base, reg="M")

        elif command.arg1 in BASE_VALS:
            base = BASE_VALS[command.arg1]
            instructions = POP_INSTRUCTIONS.format(index=command.arg2,
                                                        segment=command.arg1,
                                                        base=base, reg="A") 

        elif command.arg1 == "constant":
            raise RuntimeError("Cannot pop a constant")              

        else:
            raise NotImplementedError("segment {}".format(command.arg1))

        self.f.write(instructions+"\n")           

    def write_push_pop(self, command:  parse.Command) -> None:
        if command.cmd_type == parse.CmdType.PUSH:
            self.write_push(command)


        elif command.cmd_type == parse.CmdType.POP:
            self.write_pop(command)

        else:
            raise RuntimeError("Expected command type push or pop, got {}".format(command.cmd_type))

