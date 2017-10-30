#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import code
import enum
from typing import Union, Iterator, Optional, IO
from collections import deque

class CmdType(enum.Enum):
    A = enum.auto()
    C = enum.auto()
    L = enum.auto()

valid_regex = re.compile(r'[_.$:A-Za-z][_.$:\w]*')
def valid_symbol(symbol: str) -> bool:
    return (re.match(valid_regex, symbol) is not None)

class Command:

    @classmethod
    def from_string(cls, cmd_str):
        if cmd_str[0] == "(":
            return LCommand(cmd_str)
        elif cmd_str[0] == "@":
            return ACommand(cmd_str)
        else:
            return CCommand(cmd_str)               


class LCommand(Command):
    def __init__(self, cmd_str: str) -> None:
        assert (cmd_str[0] == "(" and cmd_str[-1] == ")"), "Invalid L command {}".format(cmd_str)

        self.symbol: str = cmd_str[1:-1]
        if not valid_symbol(self.symbol):
            raise ValueError("Invalid symbol for L command: {}".format(self.symbol))

    @property
    def cmd_type(self) -> CmdType:
        return CmdType.L


class ACommand(Command):
    def __init__(self, cmd_str: str) -> None:
        assert cmd_str[0] == "@", "Invalid A command {}".format(cmd_str)
        
        symbol_str = cmd_str[1:]

        #parse as a constant if possible - if not, treat as symbol
        try:
            self.symbol: Union[int, str] = int(symbol_str)
        except ValueError:
            self.symbol = symbol_str
            if not valid_symbol(self.symbol):
                raise ValueError("Invalid symbol for A command: {}".format(self.symbol))

    @property
    def cmd_type(self) -> CmdType:
        return CmdType.A


class CCommand(Command):
    def __init__(self, cmd_str: str) -> None:

        #parse fields one at a time
        #use deque b/c popleft() is more readable here
        try:
            self.dest,rest = cmd_str.split("=")
        except ValueError:
            #no dest
            rest = cmd_str
            self.dest = "null"

        try:
            self.comp,self.jump = rest.split(";")
        except ValueError:
            self.comp = rest
            self.jump = "null"

        #make sure that comp and jump are valid (already check dest above),
        #and there aren't leftover fields
        if not(self.dest in code.dests):
            raise ValueError("Unknown dest {} in {}".format(self.dest, cmd_str))            
        if not(self.comp in code.comps):
            raise ValueError("Unknown comp {} in {}".format(self.comp, cmd_str))
        if not(self.jump in code.jumps):
            raise ValueError("Unknown jump {} in {}".format(self.dest, cmd_str))

    @property
    def cmd_type(self) -> CmdType:
        return CmdType.C


class Parser:
    def __init__(self, file: IO[str]) -> None:
        self.file: Iterator[str] = file

    def reset(self):
        #jump back to start of file
        self.file.seek(0)
        self.cmd = None

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

        self.cmd: Command = Command.from_string(cmd_str)

    def command_type(self):
        return self.cmd.cmd_type

    def symbol(self):
        return self.cmd.symbol

    def dest(self):
        return self.cmd.dest

    def comp(self):
        return self.cmd.comp

    def jump(self):
        return self.cmd.jump


