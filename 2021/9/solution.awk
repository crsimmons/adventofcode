#!/usr/bin/env gawk -f

function abs(k) {return k<0?-k:k}

function count(y,x,_e,_yy,_xx,_dy,_dx,_found) {
  if (checked[y][x]) return

  _e=a[y][x]

  size++
  checked[y][x]++

  _found=0
  for (_dy=-1;_dy<=1;_dy++) {
    for (_dx=-1;_dx<=1;_dx++) {
      # not diagonals
      if (abs(_dx)==abs(_dy)) continue
      _yy=y+_dy; _xx=x+_dx
      # within bounds of matrix and not a ridge
      if (_xx>=1&&_yy>=1&&_xx<=NF&&_yy<=NR&&a[_yy][_xx]!="9") {
        if (a[_yy][_xx]<=_e) _found++
        count(_yy,_xx)
      }
    }
  }
  if (!_found&&_e!="") p1+=_e+1
}

BEGIN{FS=""}

{for(i=0;++i<=NF;) a[NR][i]=$i}

END{
  for (y in a) {
    for (x in a[y]) {
      if (a[y][x]!=9) {
        size=0
        count(y,x)
        if (size) b[++n]=size
      }
    }
  }

  print p1

  p2=1
  asort(b)
  for (x=n-3;x++<n;) p2*=b[x]
  print p2
}
