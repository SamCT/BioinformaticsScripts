#############
# Sam Talbot
# 5/1/23
# 
# Convert Hard-masked genome to soft mask
#
##############


import argparse
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

def write_fasta(records, handle, line_width=80):
    """Write records with the line width of the original file."""
    for i, rec in enumerate(records):
        handle.write(">{}\n".format(rec.id))
        sequence = str(rec.seq)
        # Determine the line width from the first sequence
        if i == 0:
            for line in sequence.split("\n"):
                line_width = len(line)
                break
        # Write the sequence with the original line width
        for j in range(0, len(sequence), line_width):
            handle.write(sequence[j:j+line_width] + "\n")

# Setup command line arguments
parser = argparse.ArgumentParser(description='Replace Ns in the second fasta file with corresponding bases from the first fasta file.')
parser.add_argument('original', help='Original fasta file')
parser.add_argument('modified', help='Modified fasta file')
parser.add_argument('output', help='Output fasta file')

args = parser.parse_args()

# Parse the original and modified sequences
original_sequences = SeqIO.to_dict(SeqIO.parse(args.original, 'fasta'))
modified_sequences = SeqIO.to_dict(SeqIO.parse(args.modified, 'fasta'))

#for original, modified in zip(original_sequences, modified_sequences):
#	print(f"Length of original: {len(original.seq)}, Length of modified: {len(modified.seq)}")
#	assert len(original.seq) == len(modified.seq)

# Make sure the files contain the same number of sequences
assert len(original_sequences) == len(modified_sequences)

new_sequences = []
for seq_id in original_sequences:
    original = original_sequences[seq_id]
    modified = modified_sequences[seq_id]
#for original, modified in zip(original_sequences, modified_sequences):
    # Make sure the sequences are the same length
    assert len(original) == len(modified)

    # Create a new sequence by replacing 'N' with the corresponding original base (in lowercase)
    new_seq = ''
    for o, m in zip(str(original.seq), str(modified.seq)):
        if m == 'N':
            new_seq += o.lower()
#            print(f'Original: {o}, Modified: {m}')
        else:
            new_seq += m

    # Create a new sequence record with the new sequence and the original ID
    new_sequences.append(SeqRecord(Seq(new_seq), id=original.id))

# Write the new sequences to a fasta file with 80 characters per line
with open(args.output, 'w') as output_handle:
    write_fasta(new_sequences, output_handle, 80)
