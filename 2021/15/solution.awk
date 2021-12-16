#!/usr/bin/env gawk -f

# my original solution - works for part 1 but takes presumably hours for part 2

function pd(   x) {
  for (x in Dist) {
    printf "Dist[%s]=%s\n", x, Dist[x]
  }
}

function abs(k) {return k<0?-k:k}

function create_graph(G,   x,y,dx,dy,xx,yy) {
  for (x=1;x<=MAXX;x++) {
    for (y=1;y<=MAXY;y++) {
      Vertices[x,y]=1
      for (dy=-1;dy<=1;dy++) {
        for (dx=-1;dx<=1;dx++) {
          # not diagonals
          if (abs(dx)==abs(dy)) continue
            yy=y+dy; xx=x+dx
          # within bounds of grid
          if (xx>=1&&yy>=1&&xx<=MAXX&&yy<=MAXY) {
            Edges[x,y][xx,yy]=G[xx][yy]
          }
        }
      }
    }
  }
}

function isEdge(v1,v2) {
  return (v1 in Edges) && (v2 in Edges[v1])
}

function dijkstra(   v, u, alt) {
  for (v in Vertices) {
    Q[v]=1
    if (v == START) {
      Dist[v]=0
    } else if (isEdge(START,v)) {
      Dist[v]=Edges[START][v]
    } else {
      Dist[v]=INFINITY
    }
  }

  while (length(Q) > 0) {
    print length(Q)
    u = find_min_weight_vertex()

    if (u==FINISH) break

    delete Q[u]

    for (v in Q) {
      if (isEdge(u,v)) {
        alt=Dist[u]+Edges[u][v]
        if (alt < Dist[v]) {
          Dist[v]=alt
          Prev[v]=u
        }
      }
    }
  }
  print Dist[FINISH]
}

function find_min_weight_vertex(   min, minVert, v) {
  min=INFINITY
  minVertex=""

  for (v in Q) {
    if (Dist[v] < min) {
      minVertex=v
      min=Dist[v]
    }
  }
  return minVertex
}

BEGIN{
  FS=""
  INFINITY=9999999
  START="1"SUBSEP"1"
}

{
  for (i=1;i<=NF;i++) grid[i][NR]=$i
}

END{
  MAXX=NF
  MAXY=NR
  FINISH=MAXX SUBSEP MAXY
  # create_graph(grid)

  # dijkstra()

  delete Edges
  delete Vertices

  for (xfill=0;xfill<5;xfill++) {
    for (yfill=0;yfill<5;yfill++) {
      for (x=1; x<=NR; x++) {
        for (y=1; y<=NR; y++) {
          grid2[x+(NF*yfill)][y+(NR*xfill)] = (grid[x][y] + xfill + yfill - 1) % 9 + 1;
        }
      }
    }
  }

  MAXX=NF*5
  MAXY=NR*5
  FINISH=MAXX SUBSEP MAXY

  create_graph(grid2,NF*5,NR*5)

  dijkstra()
}
