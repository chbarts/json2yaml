#!/usr/bin/env python3

import os
import sys
import json
import yaml
import argparse

def json2yaml(inf, outf):
    data = json.load(inf)
    yaml.dump(data, outf)

parser = argparse.ArgumentParser(description='Convert JSON to YAML')

parser.add_argument('-i', '--input', metavar='INFILE', type=str, nargs=1, default='', help='Specify INFILE as JSON input file, defaults to stdin')
parser.add_argument('-o', '--output', metavar='OUTFILE', type=str, nargs=1, default='', help='Specify OUTFILE as YAML output file, defaults to stdout')

args = parser.parse_args()

if (len(args.input) > 0) and (len(args.output) > 0):
    with open(args.input[0], 'r') as inf:
        with open(args.output[0], 'w') as outf:
            json2yaml(inf, outf)
    sys.exit(0)
elif len(args.input) > 0:
    with open(args.input[0], 'r') as inf:
        json2yaml(inf, sys.stdout)
    sys.exit(0)
elif len(args.output) > 0:
    with open(args.output[0], 'w') as outf:
        json2yaml(sys.stdin, outf)
    sys.exit(0)
else:
    json2yaml(sys.stdin, sys.stdout)
    sys.exit(0)
