function sumNeighbours(w,z,y,x, _sum) {
  for (dw=-1;dw<=1;dw++) {
    for (dz=-1;dz<=1;dz++) {
      for (dy=-1;dy<=1;dy++) {
        for (dx=-1;dx<=1;dx++) {
          if (dw==0&&dz==0&&dy==0&&dx==0) continue
          _sum+=grid[w+dw][z+dz][y+dy][x+dx]
        }
      }
    }
  }
  return _sum
}

function sumAll(_sum) {
  for (w in grid) {
    for (z in grid[w]) {
      for (y in grid[w][z]) {
        for (x in grid[w][z][y])
          _sum += grid[w][z][y][x]
      }
    }
  }
  return _sum
}

BEGIN{FS="";c=6;offset=13}

{
  for (x=1;x<=length($0);x++) {
    grid[offset][offset][NR+offset][x+offset]=($x=="#"?1:0)
  }
}

END{
  for (w=1;w<=2*offset;w++) {
    for (z=1;z<=2*offset;z++) {
      for (y=1;y<=2*offset;y++) {
        for (x=1;x<=2*offset;x++) {
          if (!grid[w][z][y][x]) grid[w][z][y][x]=0
        }
      }
    }
  }

  while (c--) {
    delete new
    for (w=1;w<=2*offset;w++) {
      for (z=1;z<=2*offset;z++) {
        for (y=1;y<=2*offset;y++) {
          for (x=1;x<=2*offset;x++) {
            s=sumNeighbours(w,z,y,x)
            new[w][z][y][x]=grid[w][z][y][x]
            if (grid[w][z][y][x]==0 && s==3) new[w][z][y][x]=1
            else if (grid[w][z][y][x]==1 && s<2) new[w][z][y][x]=0
            else if (grid[w][z][y][x]==1 && s>3) new[w][z][y][x]=0
          }
        }
      }
    }
    for (w=1;w<=2*offset;w++) {
      for (z=1;z<=2*offset;z++) {
        for (y=1;y<=2*offset;y++) {
          for (x=1;x<=2*offset;x++) {
            grid[w][z][y][x]=new[w][z][y][x]
          }
        }
      }
    }
  }
  print sumAll()
}
