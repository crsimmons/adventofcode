#!/usr/bin/env gawk -f

function sum_result(   Letters, x) {
  for (x in Pairs) Letters[substr(x,1,1)]+=Pairs[x]
  # Last letter of original template is last letter of final template
  Letters[substr(Template,s,1)]++
  asort(Letters)
  print Letters[length(Letters)] - Letters[1]
}

function arrcpy(arr,   x) {
  delete Pairs
  for (x in arr) Pairs[x]=arr[x]
}

BEGIN{FS=" -> "}

/>/{Rules[$1]=$2; next}

/\S/{
  Template=$0
  for (s=1;s<length(Template);s++) Pairs[substr(Template,s,2)]++
}

END{
  for (;++i<=40;) {
    delete Pairs2
    for (p in Pairs) {
      split(p,pa,"")
      np=pa[1] Rules[p]
      Pairs2[np]+=Pairs[p]
      np=Rules[p] pa[2]
      Pairs2[np]+=Pairs[p]
    }
    arrcpy(Pairs2)
    if (i==10 || i==40) sum_result()
  }
}
