function compare(  acc) {
  acc=0
  for (x in grid) {
    if (grid[x] != "" && grid[x]==output[x]) {
      acc++
    }
  }
  return acc
}

function replace() {
  delete grid
  for (x in output) {
    grid[x]=output[x]
  }
}

function count(  c) {
  for (x in grid) {
    while (sub("#","",grid[x])) c++
  }
  return c
}

function free(  x,  y) {
  if (x<=0 || y<=0 || x>maxx || y>NR || substr(grid[y],x,1) != "#") {
    return 1
  }
  return 0
}

function check_seats() {
  delete output
  for (y in grid) {
    for (x=1;x<=maxx;x++) {
      switch (substr(grid[y],x,1)) {
        case "L":
          sum=0
          for (i=-1;i<2;i++) {
            for (j=-1;j<2;j++) {
              if (i==0&&i==j) continue
              sum += free(x+i,y+j)
            }
          }
          output[y]=output[y] (sum==8 ? "#" : "L")
          break
        case "#":
          sum=0
          for (i=-1;i<2;i++) {
            for (j=-1;j<2;j++) {
              if (i==0&&i==j) continue
              sum += free(x+i,y+j)
            }
          }
          output[y]=output[y] (8-sum>=4 ? "L" : "#")
          break
        default:
          output[y]=output[y] substr(grid[y],x,1)
          break
      }
    }
  }
}

{grid[++i]=$0}

END{
  maxx=length(grid[1])
  while (1) {
    check_seats()
    if (compare() >= NR) break
    replace()
  }
  print count()
}
