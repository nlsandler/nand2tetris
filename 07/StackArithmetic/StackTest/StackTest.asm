//push constant 17
    @17
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
//push constant 17
    @17
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
//eq
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
    @label0
    D;JEQ
//comparison was false, set result to 0
    @R13
    M=0
(label0)
//add result to stack
    @R13
    D=M
    @SP
    A=M-1
    M=D
//push constant 17
    @17
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
//push constant 16
    @16
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
//eq
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
    @label1
    D;JEQ
//comparison was false, set result to 0
    @R13
    M=0
(label1)
//add result to stack
    @R13
    D=M
    @SP
    A=M-1
    M=D
//push constant 16
    @16
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
//push constant 17
    @17
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
//eq
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
    @label2
    D;JEQ
//comparison was false, set result to 0
    @R13
    M=0
(label2)
//add result to stack
    @R13
    D=M
    @SP
    A=M-1
    M=D
//push constant 892
    @892
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
//push constant 891
    @891
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
//lt
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
    @label3
    D;JLT
//comparison was false, set result to 0
    @R13
    M=0
(label3)
//add result to stack
    @R13
    D=M
    @SP
    A=M-1
    M=D
//push constant 891
    @891
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
//push constant 892
    @892
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
//lt
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
    @label4
    D;JLT
//comparison was false, set result to 0
    @R13
    M=0
(label4)
//add result to stack
    @R13
    D=M
    @SP
    A=M-1
    M=D
//push constant 891
    @891
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
//push constant 891
    @891
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
//lt
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
    @label5
    D;JLT
//comparison was false, set result to 0
    @R13
    M=0
(label5)
//add result to stack
    @R13
    D=M
    @SP
    A=M-1
    M=D
//push constant 32767
    @32767
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
//push constant 32766
    @32766
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
//gt
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
    @label6
    D;JGT
//comparison was false, set result to 0
    @R13
    M=0
(label6)
//add result to stack
    @R13
    D=M
    @SP
    A=M-1
    M=D
//push constant 32766
    @32766
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
//push constant 32767
    @32767
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
//gt
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
    @label7
    D;JGT
//comparison was false, set result to 0
    @R13
    M=0
(label7)
//add result to stack
    @R13
    D=M
    @SP
    A=M-1
    M=D
//push constant 32766
    @32766
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
//push constant 32766
    @32766
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
//gt
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
    @label8
    D;JGT
//comparison was false, set result to 0
    @R13
    M=0
(label8)
//add result to stack
    @R13
    D=M
    @SP
    A=M-1
    M=D
//push constant 57
    @57
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
//push constant 31
    @31
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
//push constant 53
    @53
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
//add
    @SP
    AM=M-1
    D=M
    @SP
    A=M-1
    M=M+D
//push constant 112
    @112
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
//sub
    @SP
    AM=M-1
    D=M
    @SP
    A=M-1
    M=M-D
//neg
    @SP
    A=M-1
    M=-M
//and
    @SP
    AM=M-1
    D=M
    @SP
    A=M-1
    M=M&D
//push constant 82
    @82
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
//or
    @SP
    AM=M-1
    D=M
    @SP
    A=M-1
    M=M|D
//not
    @SP
    A=M-1
    M=!M
