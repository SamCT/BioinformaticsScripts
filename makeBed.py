#!/usr/bin/env python3

##########
# Sam Talbot
#
# Function: Make bed file from gff file
#
################


import argparse

def main(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            if line.startswith("#"):
                continue
            cols = line.strip().split('\t')
            if len(cols) >= 9:
                # Extract ID value
                info_parts = cols[8].split(';')
                id_value = ''
                for part in info_parts:
                    if part.startswith('ID='):
                        id_value = part[3:]
                        break
                # Write to output file
                f_out.write(f'{cols[0]}\t{cols[3]}\t{cols[4]}\t{id_value}\n')
            else:
                print(f'Skipped line with fewer than 9 columns: {line}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert file to BED format.')
    parser.add_argument('-i', '--input', help='Input file name', required=True)
    parser.add_argument('-o', '--output', help='Output file name', required=True)
    args = parser.parse_args()

    main(args.input, args.output)
