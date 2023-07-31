#!/bin/env bash

# check if the input file is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 inputfile"
    exit 1
fi

# assign argument to meaningful variable names
inputfile="$1"

# extract the identifiers from the 9th column, sort them, and write to a file
awk -F'[=;]' '{print $2}' $inputfile | sort -u > identifiers.txt

# create a sequence of numbers from 1 to 33506, prefix each with "Corav.Jeff.Hap1_g", sort it and write to a file
seq -f "Corav.Jeff.Hap1_g%.0f" 1 33506 | sort > all_identifiers.txt

# find the missing identifiers using comm
comm -23 all_identifiers.txt identifiers.txt > missing_identifiers.txt

# remove temporary files
rm identifiers.txt all_identifiers.txt
