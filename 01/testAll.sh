#!/bin/bash

for f in *.tst
do

    echo "$f: `HardwareSimulator.sh $f 2>&1`";
done