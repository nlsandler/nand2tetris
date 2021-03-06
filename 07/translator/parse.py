#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import enum
from typing import Iterator, IO

UNARY_OPS = ["neg","not"]
BINARY_OPS = ["add","sub","and","or"]
CMP_OPS = ["gt","lt","eq"]
ARITHMETIC_OPS = UNARY_OPS + BINARY_OPS + CMP_OPS

class CmdType(enum.Enum):
    ARITH = enum.auto()
    PUSH = enum.auto()
    POP = enum.auto()
    LABEL = enum.auto()
    GOTO = enum.auto()
    IF = enum.auto()
    FUNCTION = enum.auto()
    RET = enum.auto()
    CALL = enum.auto()

# expected # of args, including command itself
# default is 2 for all commands not listed here
EXPECTED_ARGS = {
    CmdType.ARITH: 1,
    CmdType.PUSH: 3,
    CmdType.POP: 3,
    CmdType.FUNCTION: 3,
    CmdType.CALL: 3,
    CmdType.RET: 1,
    CmdType.IF: 2,
    CmdType.LABEL: 2,
    CmdType.GOTO: 2
}

class Command:

    def __init__(self, cmd_str: str) -> None:
        self.args = cmd_str.split()
        cmd = self.args[0]
        if cmd in ARITHMETIC_OPS:
            self.cmd_type = CmdType.ARITH
        elif cmd == "push":
            self.cmd_type = CmdType.PUSH
        elif cmd == "pop":
            self.cmd_type = CmdType.POP
        elif cmd == "label":
            self.cmd_type = CmdType.LABEL
        elif cmd == "goto":
            self.cmd_type = CmdType.GOTO
        elif cmd == "if-goto":
            self.cmd_type = CmdType.IF
        elif cmd == "function":
            self.cmd_type = CmdType.FUNCTION
        elif cmd == "call":
            self.cmd_type = CmdType.CALL
        elif cmd == "return":
            self.cmd_type = CmdType.RET
        else:
            raise ValueError("Unrecognized command {}".format(cmd))

        #make sure we have the right number of arguments
        if len(self.args) != EXPECTED_ARGS[self.cmd_type]:
            raise ValueError("Expected {} arguments in command {}, but got {}".format(EXPECTED_ARGS[self.cmd_type], cmd_str, len(self.args)))

    @property
    def arg1(self) -> str:
        if self.cmd_type == CmdType.ARITH:
            return self.args[0]
        elif self.cmd_type == CmdType.RET:
            raise RuntimeError("RET command does not have arguments")
        else:
            return self.args[1]

    @property
    def arg2(self) -> str:
        if (self.cmd_type == CmdType.PUSH or
            self.cmd_type == CmdType.POP or
            self.cmd_type == CmdType.FUNCTION or
            self.cmd_type == CmdType.CALL):
            return self.args[2]
        else:
            raise RuntimeError("{} command does not have two arguments".format(self.cmd_type))           



class Parser:
    def __init__(self, file: IO[str]) -> None:
        self.file: Iterator[str] = file

    def advance(self) -> None:
        cmd_str = next(self.file).strip()

        #skip comments and empty lines
        while (not cmd_str) or cmd_str.startswith("//"):
            cmd_str = next(self.file).strip()

        #remove end of line comment if there is one
        try:
            cmd_str, _ = cmd_str.split("//")
            cmd_str = cmd_str.strip()
        except ValueError:
            #no comment to remove
            pass

        self.cmd: Command = Command(cmd_str)