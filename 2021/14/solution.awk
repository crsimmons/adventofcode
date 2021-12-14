#!/usr/bin/env gawk -f

function sum_result(   L, x) {
  for (x in P) L[substr(x,1,1)]+=P[x]
  L[substr(S,s,1)]++
  asort(L)
  print L[length(L)] - L[1]
}

function arrcpy(arr,   x) {
  delete P
  for (x in arr) P[x]=arr[x]
}

BEGIN{FS=" -> "}

/>/{D[$1]=$2; next}

/\S/{
  S=$0
  for (s=1;s<length(S);s++) P[substr(S,s,2)]++
}

END{
  for (;++i<=40;) {
    delete P2
    for (p in P) {
      split(p,pa,"")
      np=pa[1] D[p]
      P2[np]+=P[p]
      np=D[p] pa[2]
      P2[np]+=P[p]
    }
    arrcpy(P2)
    if (i==10 || i==40) sum_result()
  }
}
