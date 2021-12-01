#!/usr/bin/env awk -f

{$1<p?"":s1++;p=$1}
{a[++i]=$1}

END{
  for (x in a) {
    a[x]<a[x+3]?s2++:""
  }
  printf "p1: %d\np2: %d\n", s1-1, s2
}
