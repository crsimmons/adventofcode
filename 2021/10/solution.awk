#!/usr/bin/env gawk -f

BEGIN{
  p="\\(\\)|\\[\\]|{}|<>"
  c="\\)|\\]|}|>"
  s[")"]=3;s["]"]=57;s["}"]=1197;s[">"]=25137
  s2["("]=1;s2["["]=2;s2["{"]=3;s2["<"]=4
}

{
  line=$0;r=0
  while(line~p) gsub(p,"",line)
  m=match(line,c)
  if (m) {p1+=s[substr(line,m,1)];next}
  for (i=length(line);i>0;i--) r=(r*5)+s2[substr(line,i,1)]
  p2[++n]=r
}

END{
  print p1
  asort(p2)
  print p2[int(length(p2)/2)+1]
}
