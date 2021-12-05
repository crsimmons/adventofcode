#!/usr/bin/env gawk -f

BEGIN{FS=" -> "}

{
  split($1,p1,",")
  split($2,p2,",")

  # uncomment for part 1
  # if (p1[1]!=p2[1]&&p1[2]!=p2[2]) next

  segments[++i][1]=p1[1]
  segments[i][2]=p1[2]
  segments[i][3]=p2[1]
  segments[i][4]=p2[2]
}

END{
  for (line in segments) {
    x1=segments[line][1]
    y1=segments[line][2]
    x2=segments[line][3]
    y2=segments[line][4]
    x=x1
    y=y1
    while (1) {
      grid[x][y]++
      if (x==x2&&y==y2) break
      if (x2>x1) x++
      else if (x2<x1) x--
      if (y2>y1) y++
      else if (y2<y1) y--
    }
  }

  for (x in grid) for (y in grid[x]) if(grid[x][y]>1) sum++
  print sum
}
