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

function find_chair(  x,  y,  xinc,  yinc,  val) {
  while (1) {
    x+=xinc; y+=yinc
    if (x<=0 || y<=0 || x>maxx || y>NR) return "."
    val = substr(grid[y], x, 1)
    if (val != ".") return val
  }
}

function free_chairs(  x,  y,  c,  t) {
  c = find_chair(x,y,0,-1) find_chair(x,y,1,-1) find_chair(x,y,1,0) find_chair(x,y,1,1) find_chair(x,y,0,1) find_chair(x,y,-1,1) find_chair(x,y,-1,0) find_chair(x,y,-1,-1)
  while (sub("#","",c)) t++
  return 8-t
}

function check_seats() {
  delete output
  for (y in grid) {
    for (x=1;x<=maxx;x++) {
      switch (substr(grid[y],x,1)) {
        case "L":
          sum = free_chairs(x,y)
          output[y]=output[y] (sum==8 ? "#" : "L")
          break
        case "#":
          sum = free_chairs(x,y)
          output[y]=output[y] (sum<=3 ? "L" : "#")
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
