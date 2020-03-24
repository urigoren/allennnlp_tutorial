#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo "ERROR: Missing experiment name"
    exit
fi
EXP="experiments/$1.jsonnet"
if [ ! -f "$EXP" ]; then
    echo "ERROR: $EXP does not exist"
    exit
fi
mkdir target
rm -r "target/$1"
allennlp train "$EXP" -s "target/$1" --include-package src
