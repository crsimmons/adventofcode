#!/usr/bin/env gawk -f

function min(a, b) { return (a < b) ? a : b; }
function max(a, b) { return (a > b) ? a : b; }

BEGIN { FS = "-" }

/-/ { if (!($1 in ranges) || ranges[$1]+0 < $2+0) ranges[$1] = $2; }
/^[0-9]+$/ { for (start in ranges) if (start+0 <= $0 && ranges[start]+0 >= $0) { part1++; break; } }

END {
  n=asorti(ranges,keys,"@ind_num_asc")
  if(n){
    delete newranges
    s=keys[1]+0; e=ranges[keys[1]]+0
    for(i=2;i<=n;i++){
      t=keys[i]+0; u=ranges[keys[i]]+0
      if(t<=e){ if(u>e) e=u } else { newranges[s]=e; s=t; e=u }
    }
    newranges[s]=e
    delete ranges
    for(k in newranges) ranges[k]=newranges[k]
  }
  for (r in ranges) part2 += (ranges[r] + 1 - r);
  printf "part1: %s\npart2: %s\n", part1, part2;
}
