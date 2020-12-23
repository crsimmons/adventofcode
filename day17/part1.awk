function sumNeighbours(z,y,x, _sum) {
  for (dz=-1;dz<=1;dz++) {
    for (dy=-1;dy<=1;dy++) {
      for (dx=-1;dx<=1;dx++) {
        if (dz==0&&dy==0&&dx==0) continue
        _sum+=grid[z+dz][y+dy][x+dx]
      }
    }
  }
  return _sum
}

function sumAll(_sum) {
  for (z in grid) {
    for (y in grid[z]) {
      for (x in grid[z][y])
        _sum += grid[z][y][x]
    }
  }
  return _sum
}

BEGIN{FS="";c=6;offset=13}

{
  for (x=1;x<=length($0);x++) {
    grid[offset][NR+offset][x+offset]=($x=="#"?1:0)
  }
}

END{
  for (z=1;z<=2*offset;z++) {
    for (y=1;y<=2*offset;y++) {
      for (x=1;x<=2*offset;x++) {
        if (!grid[z][y][x]) grid[z][y][x]=0
      }
    }
  }

  while (c--) {
    delete new
    for (z=1;z<=2*offset;z++) {
      for (y=1;y<=2*offset;y++) {
        for (x=1;x<=2*offset;x++) {
          s=sumNeighbours(z,y,x)
          new[z][y][x]=grid[z][y][x]
          if (grid[z][y][x]==0 && s==3) new[z][y][x]=1
          else if (grid[z][y][x]==1 && s<2) new[z][y][x]=0
          else if (grid[z][y][x]==1 && s>3) new[z][y][x]=0
        }
      }
    }
    for (z=1;z<=2*offset;z++) {
      for (y=1;y<=2*offset;y++) {
        for (x=1;x<=2*offset;x++) {
          grid[z][y][x]=new[z][y][x]
        }
      }
    }
  }
  print sumAll()
}
