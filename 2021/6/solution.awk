#!/usr/bin/env gawk -f

# part 1: l=80
# part 2: l=256
BEGIN{RS=",";l=256}

{a[$0]++}

END{
  for (;d++<l;) {
    delete b
    for(x in a) {
      if (x==0) {
        b[6]+=a[x]
        b[8]=a[x]
      }
      else b[x-1]+=a[x]
    }
    delete a
    for (x in b) a[x]=b[x]
  }
  for (x in a) r+=a[x]
  print r
}
