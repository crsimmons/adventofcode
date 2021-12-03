#!/usr/bin/env awk -f

function c(a,b,p,_x,_s,_n,_k,_r) {
  q=p?0:1
  if(length(a)==1||b>NF) return b2d(a[1])
  for(_x in a){_s+=substr(a[_x],b,1)}
  _s=_s>=length(a)/2?p:q
  for(_x in a)if(substr(a[_x],b,1)==_s)_n[++_k]=a[_x]
  return c(_n,++b,p)
}

function b2d(b,_k,_e,_d) {
  for(;++_k<=NF;){_e=2**(NF-_k);_d+=_e*substr(b,_k,1)}
  return _d
}

BEGIN{FS=""}

{for(i=0;i<=NF;i++)s[i]+=$i}
{a[++j]=$0}

END{
  for(;++k<=NF;){b=2**(NF-k);v=s[k]>NR/2?1:0;n=v?0:1;g+=b*v;e+=b*n}
  printf "p1: %d\np2: %d\n", g*e, c(a,1,1)*c(a,1,0)
}
