#!/usr/bin/env bash

set -euo pipefail

if [[ ! $# -ge 1 ]]; then
  echo "usage is $0 <day number> <optional: year>"
  exit 1
fi

day=$1
year=${2:-2023}

dir="${REPO_DIR}/${year}/${day}"

# dir="${REPO_DIR}/2023"

# if [[ -d "${dir}" ]]; then
#   echo "$dir already exists - exiting"
#   exit
# fi

# while read -r i; do
#   mkdir -p "${dir}/$i"
#   touch "${dir}/$i/example.txt"

#   cat << EOF > "${dir}/$i/solution.py"
# #!/usr/bin/env python3
# import sys

# inputfile = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
# data = open(inputfile)
# lines = [l.strip() for l in data]


# EOF
# done <<< "$(seq 3 25)"

chmod +x "${dir}/solution.py"

aocd "${day}" "${year}" > "${dir}/input.txt"
# touch "${dir}/example.txt"
