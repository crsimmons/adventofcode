#!/usr/bin/env gawk -f

function arrcpy(arr1,arr2,   x,y) {
  delete arr1;
  for (x in arr2) {
    for (y in arr2[x]) {
      arr1[x][y]=arr2[x][y];
    }
  }
}

BEGIN{FS=""}

{
  for (i=1;i<=NF;i++) {
    grid[i][NR]=$i=="."?0:$i
  }
}

END{
  maxx=NF
  maxy=NR

  m=1
  while (m) {
    m=0
    part1++
    arrcpy(ngrid,grid)

    for (x=1;x<=maxx;x++) {
      for (y=1;y<=maxy;y++) {
        if (grid[x][y]==">") {
          nx=x+1>maxx?1:x+1
          if (!grid[nx][y]) {
            ngrid[nx][y]=">"
            ngrid[x][y]=0
            m++
          }
        }
      }
    }
    arrcpy(grid,ngrid)

    for (x=1;x<=maxx;x++) {
      for (y=1;y<=maxy;y++) {
        if (grid[x][y]=="v") {
          ny=y+1>maxy?1:y+1
          if (!grid[x][ny]) {
            ngrid[x][ny]="v"
            ngrid[x][y]=0
            m++
          }
        }
      }
    }
    arrcpy(grid,ngrid)
  }
  print part1
}
