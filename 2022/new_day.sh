#!/usr/bin/env bash

set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "usage is $0 <day number>"
  exit 1
fi

day=$1

mkdir "$day"
cat << EOF > "${day}/solution.py"
#!/usr/bin/python3
import sys

from aocd import data
from aocd import lines
from aocd import numbers

from collections import defaultdict

exampledata = sys.argv[1] if len(sys.argv)>1 else 'example.txt'
data = exampledata
EOF
chmod +x "${day}/solution.py"

aocd > input.txt
touch "${day}/example.txt"
