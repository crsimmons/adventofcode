#!/usr/bin/env bash

set -euo pipefail

if [[ ! $# -ge 1 ]]; then
  echo "usage is $0 <day number> <optional: year>"
  exit 1
fi

day=$1
year=${2:-2024}

dir="${REPO_DIR}/${year}/${day}"

aocd "${day}" "${year}" > "${dir}/input.txt"

# initial setup

# while read -r i; do
#   dir="${REPO_DIR}/2024"
#   mkdir -p "${dir}/$i"
#   touch "${dir}/$i/example.txt"

#   cp "${REPO_DIR}/template.py" "${dir}/$i/solution.py"
#   chmod +x "${dir}/$i/solution.py"
# done <<< "$(seq 1 25)"
