#!/bin/bash

# check if both input files are supplied
if [[ $# -ne 3 ]]; then
    echo "Usage: ./script.sh <fasta_file> <txt_file> <output.txt>"
    exit 1
fi

fasta_file=$1
txt_file=$2
output_file=$3

# process the fasta file
while IFS= read -r id
do
    awk -v RS=">" -v id="$id" 'index($0, id){print ">" $0}' "$fasta_file"
done < "$txt_file" | grep -v '^$' > "$output_file"
