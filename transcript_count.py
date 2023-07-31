#!/usr/bin/env python3

####
# Sam Talbot 7/31/23
# 
# Usage: transcript_count.py my_extracted transcripts.gff output.txt
# Function: Count number of transcripts in gff file
# 
# Requires GFF file that is just transcripts
#   ie. awk '{if ($3=="transcript")print$0}'
#
#
# Output: 2 column file, col1 = genes with N transcripts, col2 = Number of genes, col3 = % of total
#
############

import re
import argparse
from collections import defaultdict

## requires GFF file that is just transcripts
# ie. awk '{if ($3=="transcript")print$0}'


#Create dict
gene_counts = {}

#create arg parse object
parser = argparse.ArgumentParser(description="Count number of genes with number of transcripts for each GENEID")

parser.add_argument("filename", help="Name of file to process")
parser.add_argument("outputfile", help="Name of output file")
parser.add_argument("-format", choices=["tab", "csv"], default="tab", help="Optional: 'tab' (default) or 'csv' for comma-separated.")

args = parser.parse_args()


with open (args.filename, 'r') as file:
	for line in file:
		line = line.strip()
		line_parts = line.split('\t')
		
		id_string = line_parts[8]

		gene_id = re.search('Parent=([^;]+)', id_string).group(1)
		gene_counts[gene_id] = gene_counts.get(gene_id, 0) + 1
		#if gene_id in gene_counts:
		#	gene_counts[gene_id] = 1

		#else:
		#	gene_counts[gene_id] = 1

transcript_counts = {}

for count in gene_counts.values():
	if count in transcript_counts:
		transcript_counts[count] = transcript_counts.get(count, 0) + 1
	else:
		transcript_counts[count] = 1
total = sum(transcript_counts.values())

delimiter = "," if args.format== "csv" else "\t"

with open(args.outputfile, 'w') as output:
	output.write(f'Transcripts{delimiter}Count{delimiter}Percent\n')

	for transcripts, count in transcript_counts.items():
		percentage = (count / total) * 100
		output.write(f'{transcripts}{delimiter}{count}{delimiter}{percentage:.2f}%\n')
	
	
	output.write(f'\nTotal{delimiter}{total}\n')
