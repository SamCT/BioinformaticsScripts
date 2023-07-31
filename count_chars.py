#!/usr/bin/env python3

import argparse


def read_fasta(filename):
    sequences = {}
    current_header = ''
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                current_header = line[1:]
                sequences[current_header] = ''
            else:
                sequences[current_header] += line
    return sequences


def count_characters(sequences):
    lengths = {}
    for header, sequence in sequences.items():
        length = len(sequence)
        lengths[header] = length
    return lengths


def write_output(filename, lengths):
    with open(filename, 'w') as file:
        for header, length in lengths.items():
            file.write(f"{header}\t{length}\n")


def main():
    parser = argparse.ArgumentParser(description='FASTA sequence character counter')
    parser.add_argument('-i', '--input', required=True, help='Input FASTA file path')
    parser.add_argument('-o', '--output', required=True, help='Output file path')
    args = parser.parse_args()

    input_file = args.input
    output_file = args.output

    sequences = read_fasta(input_file)
    lengths = count_characters(sequences)
    write_output(output_file, lengths)


if __name__ == '__main__':
    main()
