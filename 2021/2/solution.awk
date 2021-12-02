#!/usr/bin/env awk -f

/forward/ {h+=$2;d2+=d*$2}
/down/ {d+=$2}
/up/ {d-=$2}

END{
  printf "p1: %d\np2: %d\n", h*d, h*d2
}
