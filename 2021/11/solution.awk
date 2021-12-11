#!/usr/bin/env gawk -f

function z(_r) {
  _r=1
  for (r in grid) for (c in grid[r]) if (grid[r][c]!=0) _r=0
  return _r
}

function flash(r,c,_dr,_dc,_nr,_nc) {
  p1++
  grid[r][c]=-1
  for (_dr=-1;_dr<=1;_dr++) {
    for (_dc=-1;_dc<=1;_dc++) {
      _nr=r+_dr;_nc=c+_dc
      if (_nr>0&&_nr<=R&&_nc>0&&_nc<=C&&grid[_nr][_nc]!=-1) grid[_nr][_nc]++
    }
  }
  # awk goes into the recursion too early if this is in the first loop
  for (_nr in grid) for (_nc in grid[_nr]) if (grid[_nr][_nc]>=10) flash(_nr,_nc)
}

BEGIN{FS=""}

{for(i=0;++i<=NF;) grid[NR][i]=$i}

END{
  R=length(grid)
  C=length(grid[1])

  while (1) {
    p2++
    for (r in grid) for (c in grid[r]) grid[r][c]++
    for (r in grid) for (c in grid[r]) if (grid[r][c]>=10) flash(r,c)
    for (r in grid) for (c in grid[r]) if (grid[r][c]<0) grid[r][c]=0
    if (p2==100) print p1
    if (z()) break
  }
  print p2
}
