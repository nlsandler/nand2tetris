// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
//R2 = 0
//inc = 0
//while inc < R1:
//    R2 = R2 + R0

//zero R2
    @R2
    M=0
//zero inc counter
    @inc
    M=0
(LOOP)
    //jump to END if inc >= R1 (i.e. inc - R1 >= 0)
    @inc //M is @inc
    D=M //load value of @inc into D
    @R1 //M is @R1
    D=D-M //store inc - R1 in D
    @END //load value of @END into A
    D;JGE //jump to END if D >= 0

    //add R0 to R2, store result in R2
    @R0 //M is R0
    D=M //load value of R0 into D
    @R2 //M is R2
    M=D+M //store R0+R2 in R2

    //increment @i
    @inc //M is inc
    M=M+1

    //jump back to start of loop
    @LOOP
    0;JMP

(END)
    @END
    0;JMP //infinite loop
