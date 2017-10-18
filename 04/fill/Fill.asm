// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

//while true:
//  if key is pressed, blackend pix
//  else, clear pix
//  pix++ (looping if needed)

//@pix variable loops from beginning to end of screen
    @SCREEN //A is address of screen start
    D=A //D contains address of screen start
    @pix //M points to pix
    M=D //pix points to start of screen
//@maxpix represents lower right corner
    @8192 //size of screen in words
    D=A //save it to D
    @SCREEN //A is start of screen
    D=D+A //D is address of screen end
    @maxpix //M is @maxpix
    M=D
(LOOP)
    //set @val (what we'll write to screen) to 0
    @val
    M=0
    @KBD //M is @kbd
    D=M //load value of @KBD into D
    @UPDATEPIX //load address of CLEAR into A
    D;JEQ //jump over 'blacken' keyboard is 0 (no key pressed)
(BLACKEN)
    @val //M is val (which is zero)
    M=!M //bitwise not Ms so it'll be all 1s


(UPDATEPIX)
    @val
    D=M //store all 1s or all 0s to D
    @pix //M contains *address* of current pix
    A=M //now M points to screen itself
    M=D //update all those pixels 
    @pix //M points to address again
    M=M+1 //increment pix

    //now see if we need to loop back to beginning of screen
    D=M //D contains @pix
    @maxpix //M contains @maxpix
    D=D-M //store difference to D
    @CONT
    D;JLT //if we're not at end of screen, jump to end of loop,
    //otherwise continue to loop back to end of screen

    @SCREEN //A is address of screen start
    D=A //D contains address of screen start
    @pix //M points to pix
    M=D //pix points to start of screen

(CONT)
    //loop forever
    @LOOP
    0;JMP