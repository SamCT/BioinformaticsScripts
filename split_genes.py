#!/usr/bin/env python3

############
# Sam Talbot
# 5/8/23
# Take a list of gene IDs from (cat *.fasta | grep '>' > list_of_geneIDs.txt) and group them to create a split file
#
# ex. 
# gene1_t1; gene1_t2; gene1_t3;
# gene2_t1;
##########


import argparse

parser = argparse.ArgumentParser(description='Identify genes with multiple isoforms')
parser.add_argument('input_file', type=str, help='Name of input file')
parser.add_argument('output_file', type=str, help='Name of output file')
args = parser.parse_args()

with open(args.input_file) as f, open(args.output_file, 'w') as out:
    genes = {}
    for line in f:
        if line.startswith(">"):
            gene = line.strip()[1:]  # Remove '>' from the line
            gene_name = ".".join(gene.split(".")[:-1])
            if gene_name in genes:
                genes[gene_name].append(gene)
            else:
                genes[gene_name] = [gene]

    for gene_name, isoforms in genes.items():
        out.write(";".join(isoforms) + ";\n")
