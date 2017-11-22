for i in ../*/*/*.vm
do
    ./translate.py $i #translate it
    testfile="${i%.*}".tst #get name of
    echo -n $i"    "
    CPUEmulator.sh $testfile
done

for i in ../../08/*/*/
do
    ./translate.py $i #translate whole directory
    testfile=`basename $i`'.tst'
    echo -n $testfile"    "
    CPUEmulator.sh $i$testfile
done