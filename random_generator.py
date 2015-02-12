#!/usr/bin/env python3

import argparse
import random

def generate_random_integers(num_integers, filename):
    with open(filename, 'w') as file:
        for count in range(0,num_integers):
            random.seed(count)
            file.write(str(random.randint(0,num_integers))+"\n")
    file.close()    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Random Integers Generator')
    parser.add_argument('-n', '--num-integers', type=int,
                   help='How many integer you want to generate')
    parser.add_argument('-o', '--output', type=str,
                   help='Output file')

    args = parser.parse_args()
    num_integers = args.num_integers
    out_file = args.output

    if not (num_integers and out_file):
        parser.print_help()
    else:
        generate_random_integers(num_integers, out_file)
