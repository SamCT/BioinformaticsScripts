#!/usr/bin/env python3

import argparse
from Bio import SeqIO
import re

def extract_sequences(fasta_file, id_file, output_file):
    # Extract IDs from id_file
    with open(id_file, 'r') as f:
        ids = [line.strip() for line in f]

    # Extract the matching sequences from the fasta file
    with open(fasta_file, 'r') as f:
        sequences = SeqIO.parse(f, 'fasta')
        extracted_sequences = []
        for seq in sequences:
            # Extract the number after the "g" in the fasta header
            match = re.search(r'g(\d+)', seq.id)
            if match and match.group(1) in ids:
                extracted_sequences.append(seq)

    # Write the extracted sequences to the output file
    SeqIO.write(extracted_sequences, output_file, 'fasta')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract sequences from a fasta file using a list of IDs.')
    parser.add_argument('fasta_file', help='Path to the input fasta file.')
    parser.add_argument('id_file', help='Path to the txt file containing the IDs.')
    parser.add_argument('output_file', help='Path to the output fasta file.')

    args = parser.parse_args()

    extract_sequences(args.fasta_file, args.id_file, args.output_file)
