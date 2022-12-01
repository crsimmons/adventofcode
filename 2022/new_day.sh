#!/usr/bin/env bash

set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "usage is $0 <day number>"
  exit 1
fi

day=$1

mkdir "$day"
cat << EOF > "${day}/${day}.py"
#!/usr/bin/env python3
import sys

from collections import defaultdict

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile)
lines = [l.strip() for l in data]

EOF
chmod +x "${day}/${day}.py"

aocd > "${day}/input.txt"
touch "${day}/example.txt"