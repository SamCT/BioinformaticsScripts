#!/usr/bin/env python3

import argparse
import os
import glob

def sort(input_file, output_file):

	sort_1 = f"sort -k2,2 -k12,12gr -k11,11g -k3,3gr {input_file}"

	sort_1_out = os.popen(sort_1).read()

	with open("temp_file_s1.txt", "w") as temp_file:
		temp_file.write(sort_1_out)

	sort_2 = f"sort -u -k2,2 --merge temp_file_s1.txt"

	final_sort_output = os.popen(sort_2).read()
	
	with open(output_file, "w") as out_file:
		out_file.write(final_sort_output)

	os.remove("temp_file_s1.txt")



def main():
	parser = argparse.ArgumentParser(description="sort blast .txt file outfmt 6")
	parser.add_argument("--input_file", type=str, default=None, help="input blast.txt outfmt 6")
	parser.add_argument("--output_file", type=str, default=None, help="output name.txt")
	parser.add_argument("--all", action="store_true", help="sort all .txt files in current directory")

	args = parser.parse_args()

	if args.all:
		for file in glob.glob("*.txt"):
			output_name = f"{os.path.splitext(file)[0]}_sorted.txt"
			sort(file, output_name)

	else:
		if not args.input_file or not args.output_file:
			print("Provide input file or output file names, or use --all flag")
			return
	
		sort(args.input_file, args.output_file)



if __name__ == "__main__":
	main()
