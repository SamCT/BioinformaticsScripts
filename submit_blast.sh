#!/bin/bash

if [ "$#" -ne 1]; then
	echo "Usage: $0 <blast_command> <command2>"
	exit 1
fi

BLAST_COMMAND=$1

if [[ "$BLAST_COMMAND" != "blastp" && "$BLAST_COMMAND" != "blastx" && "$BLAST_COMMAND" != "blastn" ]]; then
	echo "error. Invalid blast command. Chose Blastp, blastx, or blastn"
	exit 1
fi

COUNTER=1
SUBJECT=braker.fa


for fa_file in *.fa; do
	
	FILENAME=$(basename "$fa_file" .fa)
	output_file="${FILENAME}_${BLAST_COMMAND}.txt"

	SGE_Batch -c "$BLAST_COMMAND -query $fa_file -subject $SUBJECT -max_hsps 1 -evalue 1e-5 -outfmt 6 > BM_$output_file" -q hoser -r blastjob2_${COUNTER}

	let COUNTER=COUNTER+1
done

echo "commands sent. Done."

