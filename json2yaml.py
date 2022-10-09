#!/usr/bin/env python3

import os
import sys
import json
import yaml

def json2yaml(inf, outf):
    data = json.load(inf)
    yaml.dump(data, outf)

if ((len(sys.argv) == 2) and ((sys.argv[1] == '-h') or (sys.argv[1] == '--help'))) or (len(sys.argv) > 3):
    print("Usage: json2yaml [input.json] [output.yaml]")
    print("With no arguments, defaults to stdin and stdout")
    print("With one argument, reads from named file and writes to stdout")
    sys.exit(0)

if len(sys.argv) == 1:
    json2yaml(sys.stdin, sys.stdout)
    sys.exit(0)

if len(sys.argv) == 2:
    with open(sys.argv[1], 'r') as inf:
        json2yaml(inf, sys.stdout)
    sys.exit(0)

if len(sys.argv) == 3:
    with open(sys.argv[1], 'r') as inf:
        with open(sys.argv[2], 'w') as outf:
            json2yaml(inf, outf)
    sys.exit(0)
