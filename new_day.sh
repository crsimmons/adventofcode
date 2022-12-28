#!/usr/bin/env bash

set -euo pipefail

if [[ ! $# -ge 1 ]]; then
  echo "usage is $0 <day number> <optional: year>"
  exit 1
fi

day=$1
year=${2:-2023}

dir="${year}/${day}"

if [[ -d "${dir}" ]]; then
  echo "$dir already exists - exiting"
fi

mkdir -p "${dir}"
cat << EOF > "${dir}/${day}.py"
#!/usr/bin/env python3
import sys

inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
data = open(inputfile)
lines = [l.strip() for l in data]

EOF
chmod +x "${dir}/${day}.py"

aocd "${day}" "${year}" > "${dir}/input.txt"
touch "${dir}/example.txt"
