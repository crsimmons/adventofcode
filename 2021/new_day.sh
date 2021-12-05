#!/usr/bin/env bash

set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "usage is $0 <day number>"
  exit 1
fi

day=$1

mkdir "$day"
echo "#!/usr/bin/env gawk -f" > "$day/solution.awk"
chmod +x "$day/solution.awk"
touch "$day/input.txt"
touch "$day/example.txt"
