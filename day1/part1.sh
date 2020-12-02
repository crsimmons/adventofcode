#!/usr/bin/env bash

set -euo pipefail

jq -R -s 'split("\n") | .[:-1] | [combinations(2) | map(tonumber) | select(length == 2 and (.[0] + .[1] == 2020))][0] | reduce .[] as $i (1; . * $i)' < input.txt
