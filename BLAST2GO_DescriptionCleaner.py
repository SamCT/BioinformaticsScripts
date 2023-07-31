#!/usr/bin/env python3

#############
# Sam Talbot 
# 6/9/23
#
# Description: given a 2 column .txt file, exported from BLAST2GO, with SeqID in first column and Description in second column
#              remove the gene ID identifier (from a blast result) from the description column 2
#
# Example of a 2-column tab delimitted input .txt file: Gene123      XP_041005370.1protein FATTY ACID EXPORT 2, chloroplastic-like
#
# Example of output: Gene123      protein FATTY ACID EXPORT 2, chloroplastic-like
#
# Usage: python3 Description_remover.py -i blast2go_output.txt -o blast2go_output_cleaned.txt 
###############


import re
import argparse

def clean_description(description):
    # Split the description at the first alphanumeric sequence followed by a period and digits
    parts = re.split(r"[A-Za-z0-9_]+\.[0-9]*", description, 1)
    if len(parts) > 1:
        return parts[1].lstrip() # If an identifier was found and removed, return the second part
    return description # If no identifier was found, return the original description

def process_file(input_filename, output_filename):
    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        for line in input_file:
            parts = line.split('\t', 1) # split by first tab only
            if len(parts) > 1:
                parts[1] = clean_description(parts[1].rstrip()) + '\n' # strip trailing newlines and whitespaces then add back newline
            output_file.write('\t'.join(parts))

def main():
    parser = argparse.ArgumentParser(description='Clean a text file.')
    parser.add_argument('-i', '--input_file', type=str, required=True, help='The name of the input file.')
    parser.add_argument('-o', '--output_file', type=str, required=True, help='The name of the output file.')

    args = parser.parse_args()
    process_file(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
