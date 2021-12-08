#!/usr/bin/env gawk -f

function contains(v1,v2,m,_s,_x,_r) {
  if (v2=="") return 0
  split(v2,_s,"")
  for (_x in _s) if (index(v1,_s[_x])) _r++
  if (m) return _r==m
  return _r==length(v2)
}

function pop_len(arr,_x,_l) {
  for (_x in arr) if (arr[_x]!="") _l++
  return _l
}

BEGIN{FS=" \\| "}

{sequence[++i]=$1;outputs[i]=$2}

END{
  # PART 1
  for (x in outputs) {
    split(outputs[x],d," ")
    for (y in d) {
      l=length(d[y])
      if (l~/2|4|3|7/) p1++
    }
  }

  # PART 2
  for (record in sequence) {
    output=""
    delete cypher
    delete a
    split(sequence[record],elements," ")
    for (y in elements) a[elements[y]]=length(elements[y])
    while (pop_len(cypher)<length(a)) {
      for (val in a) {
        len=a[val]
        if (len==2) cypher[1]=val
        else if (len==3) cypher[7]=val
        else if (len==4) cypher[4]=val
        else if (len==7) cypher[8]=val
        else if (len==5 && contains(val,cypher[1])) cypher[3]=val
        else if (contains(val,cypher[3]) && contains(val,cypher[4])) cypher[9]=val
        else if (len==6 && contains(val,cypher[1]) && !contains(val,cypher[9])) cypher[0]=val
        else if (len==6 && !contains(val,cypher[1])) cypher[6]=val
        else if (len==5 && contains(val,cypher[6],5)) cypher[5]=val
        else if (len==5 && cypher[5] && !contains(val,cypher[5])) cypher[2]=val
      }
    }
    split(outputs[record],elements," ")
    for (e in elements) {
      for (c in cypher) {
        if (contains(elements[e],cypher[c])&&contains(cypher[c],elements[e])) {
          output=output c
          break
        }
      }
    }
    p2+=output
  }

  print p1
  print p2
}
