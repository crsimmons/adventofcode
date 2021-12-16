#!/usr/bin/env gawk -f

# runs in 23-24s for both parts

function dijkstra(G, maxx, maxy,   finish, v, u, altg, xy, n, x, y, Q, gscore, fscore, seen) {
  finish=maxx SUBSEP maxy

  # gscore[v] = cost of currently known cheapest path from start to v
  for (v in G) gscore[v]=INFINITY
  gscore[START]=0
  Q[START]=1

  while (length(Q)) {
    # find vertex with min distance from start
    # this will be 0 for first iteration
    min=INFINITY
    u=""
    for (v in Q) {
      if (gscore[v] < min) {
        min=gscore[v]
        u=v
      }
    }

    # we can stop once we reach the end
    if (u==finish) break

    # remove min distance vertex from queue
    delete Q[u]

    # find all neighbours of u which are in the graph but haven't been seen yet
    # add them to the queue and update their distances
    split(u,xy,SUBSEP)
    for (n=1;n<5;n++) {
      x=xy[1]+DX[n]; y=xy[2]+DY[n]
      if (!(x SUBSEP y in G) || seen[x,y]) continue

      altg=gscore[u]+G[x,y]
      if (altg < gscore[x,y]) {
        seen[x,y]=1
        gscore[x,y]=altg
        if (!(x SUBSEP y in Q)) Q[x,y]=1
      }
    }
  }

  print gscore[finish]
}

BEGIN{
  FS=""
  INFINITY=9999999
  START="1"SUBSEP"1"
  DX[1]=0; DX[2]=-1; DX[3]=1; DX[4]=0
  DY[1]=-1; DY[2]=0; DY[4]=0; DY[4]=1
}

{
  for (i=1;i<=NF;i++) Graph[i,NR]=$i
}

END{
  dijkstra(Graph, NF, NR)

  for (xfill=0;xfill<5;xfill++) {
    for (yfill=0;yfill<5;yfill++) {
      for (x=1; x<=NR; x++) {
        for (y=1; y<=NR; y++) {
          Graph2[x+(NF*xfill),y+(NR*yfill)] = (Graph[x,y] + xfill + yfill - 1) % 9 + 1;
        }
      }
    }
  }

  dijkstra(Graph2, NF*5, NR*5)
}
