#!/usr/bin/env gawk -f

function s(p,_x,_y,_d,_s,_r) {
  for (;++_x<=a[NR];) {
    _s=0
    for (_y in a) {
      _d=_x-a[_y]
      _d=_d>0?_d:-_d
      _d=p?_d*(_d+1)/2:_d
      _s+=_d
    }
    if (!_r||_s<_r) _r=_s
  }
  return _r
}

BEGIN{RS=","}

{a[++i]=$0}

END{
  asort(a)
  print s()
  print s(2)
}
