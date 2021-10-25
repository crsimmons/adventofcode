#!/usr/bin/env awk -f

function crabs(m,c,_x,_cur,_n,_d,_p1,_p2,_p3,_i,_t) {
  delete nex
  for(_x in a) {
    nex[a[_x]]=(_x+1>N)?a[1]:a[_x+1]
  }
  nex[0]=a[1]

  if (N<c) {
    nex[a[_x++]]=_x+1
  }

  for (;_x++<=c;) {
    nex[_x-1]=(_x>c)?a[1]:_x
  }

  _cur=0
  for (;_n++<m;) {
    _cur=nex[_cur]
    _d=(_cur!=1)?_cur-1:c
    _p1=nex[_cur]
    _p2=nex[_p1]
    _p3=nex[_p2]
    while (_d==_p1||_d==_p2||_d==_p3) {
      _d=(_d-1<1)?c:_d-1
    }
    if (_d<1) _d+=c
    _t=nex[_p3]
    nex[_p3]=nex[_d]
    nex[_d]=nex[_cur]
    nex[_cur]=_t
  }
  if (c < 10) {
    _i=nex[1]
    while (_i!=1) {
      printf("%s",_i)
      _i=nex[_i]
    }
    printf("\n")
  } else {
    print nex[1] * nex[nex[1]]
  }
}

{
  N=split($0,a,"")

  print "part1:"
  crabs(100,9)

  print "part2:"
  crabs(10000000,1000000)
}
