#!/usr/bin/env bash

set -euo pipefail

# jq -R -s '[split("\n") | .[:-1] | (.[0] | length) as $width | to_entries[] | select(.value[(.key * 3) % $width:(.key * 3) % $width +1] == "#")] | length' < input.txt

awk '{if(substr($0,((NR-1)*3)%(length($0))+1,1)=="#")sum+=1}END{print sum}' input.txt
