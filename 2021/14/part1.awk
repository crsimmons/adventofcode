#!/usr/bin/env gawk -f

BEGIN{FS=" -> "}

/>/{D[$1]=$2;next}
/\S/{S=$0}

END{
  for (;++i<=40;) {
    S2=""
    for (s=1;s<length(S);s++) {
      p=substr(S,s,2)
      split(p,pa,"")
      r=pa[1] D[p]
      if (s+1==length(S)) r=r pa[2]
      S2=S2 r
    }
    S=S2
  }

  for (s=1;s<=length(S);s++) {
    N[substr(S,s,1)]++
  }
  asort(N)
  print N[length(N)] - N[1]
}
