#!/bin/bash

for i in **/*.asm
do
    base="${i%.*}" #we output .hack in current directory
    hackfile=$base".hack"
    expected=$base".expected"

    #run reference assembler
    ../../tools/Assembler.sh $i >/dev/null
    mv $hackfile $expected

    #run our assembler
    ./assembler/assembler.py $i

    #compare outputs
    if [[ $(diff $hackfile $expected) ]]; then
        echo $base": FAIL"
    else
        echo $base": OK"
    fi

    rm $hackfile
    rm $expected
done



