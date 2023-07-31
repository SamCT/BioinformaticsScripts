#!/usr/bin/env python3
import argparse
import csv

def main():
    parser = argparse.ArgumentParser(description='Merge two tab-delimited files.')
    parser.add_argument('-i', '--input_file', type=str, required=True, help='2-column description.txt file.')
    parser.add_argument('-m', '--merge_file', type=str, required=True, help='Gff file to merge')
    parser.add_argument('-o', '--output_file', type=str, required=True, help='Output file.')

    args = parser.parse_args()
    merge_files(args.input_file, args.merge_file, args.output_file)

def merge_files(input_file, merge_file, output_file):
    # Load descriptions from input file into a dictionary
    descriptions = {}
    with open(input_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            identifier = row[0].split('=')[1]  # Extract the identifier from the first column
            descriptions[identifier] = row[1]

    # Open the merge file and the output file
    with open(merge_file, 'r', encoding='utf-8') as in_file, open(output_file, 'w') as out_file:
        reader = csv.reader(in_file, delimiter='\t')
        writer = csv.writer(out_file, delimiter='\t')

        # Process each line
        for row in reader:
            if row[0].startswith("##"):
                # Write comment lines as is
                writer.writerow(row)
            else:
                identifier = row[8].split('=')[1]  # Extract the identifier from the 9th column (ID attribute)
                if identifier in descriptions:
                    # Add the description to the 9th column
                    row[8] += f';description={descriptions[identifier]}'
                # Write the row to the output file
                writer.writerow(row)
