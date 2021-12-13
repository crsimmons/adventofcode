#!/usr/bin/env gawk -f

function arrcpy(arr) {
  delete grid
  for (x=0;x<=maxX;x++) {
    for (y=0;y<=maxY;y++) {
      grid[x][y]=arr[x][y]
    }
  }
}

function fold(axis,line,   x,y,v,grid2) {
  for (x in grid) {
    for (y in grid[x]) {
      # awk arrays be weird
      if (!grid[x][y]) continue
      if (axis == "y") {
        # multiplying by 1 forces numerical comparison
        # (y-line) is distance from y to the reflection line (upwards)
        # line-x is the line that is distance x from the reflection line (upwards)
        # go up from the line however far you were down from the line
        v=y*1<line*1?y:line-(y-line)
        grid2[x][v]="#"
        maxY=line-1
      }
      else if (axis == "x") {
        v=x*1<line*1?x:line-(x-line)
        grid2[v][y]="#"
        maxX=line-1
      }
    }
  }
  arrcpy(grid2)
}

function count(   r) {
  for (y=0;y<=maxY;y++) for (x=0;x<=maxX;x++) if (grid[x][y]=="#") r++
  return r
}

BEGIN{FS=",| "}

/,/{
  grid[$1][$2]="#"
  if($1>maxX) maxX=$1
  if($2>maxY) maxY=$2
}

/fold/{
  split($3,a,"=")
  fold(a[1],a[2])
  if (!f++) print count()
}

END{
  for (y=0;y<=maxY;y++) {
    for (x=0;x<=maxX;x++) printf "%s ", grid[x][y]?"█":" "
    printf "\n"
  }
}
