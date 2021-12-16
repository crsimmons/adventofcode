#!/usr/bin/env gawk -f

# attempt at A* - runs both parts in 24s
# seemed the same or slightly slower than dijkstra so I moved it to its own file

function abs(k) {return k<0?-k:k}

function max(a,b) {return a>b?a:b}

function min(a,b) {return a<b?a:b}

function min3(a,b,c,   t) {
  t=min(a,b)
  return min(t,c)
}

function astar(G, maxx, maxy,   finish, v, u, altg, xy, n, x, y, Q, gscore, fscore, seen, d, diag, hdist, t1, t2, this_estimate) {
  finish=maxx SUBSEP maxy

  # some crazy heuristic from reddit (https://github.com/Kateba72/advent_of_code/blob/main/2021/15.rb)
  for (d=maxx+maxy;d>0;d--) {
    diag=INFINITY
    for (y=max(0,d-maxy);c<=min(maxx,d);c++) {
      x=d-c
      t1=hdist[x+1,y]?hdist[x+1,y]:INFINITY
      t2=hdist[x,y+1]?hdist[x,y+1]:INFINITY
      hdist[x,y]=min3(t1,t2,diag+2) + G[x,y]
      this_estimate=hdist[x,y]
      diag=diag+2<this_estimate?diag+2:this_estimate
    }
    diag=INFINITY
    for (y=max(0,d-maxy);c<=min(maxx,d);c++) {
      x=d-c
      hdist[x,y]=min(hdist[x,y],diag+2+G[x,y])
      this_estimate=hdist[x,y]
      diag=diag+2<this_estimate?diag+2:this_estimate
    }
  }

  # gscore[v] = cost of currently known cheapest path from start to v
  # fscore[v] = gscore[v] + h(v) = current best guess of shortest path from start to finish through v
  for (v in G) {
    gscore[v]=INFINITY
    fscore[v]=INFINITY
  }
  gscore[START]=0
  fscore[START]=hdist[START]

  Q[START]=1

  while (length(Q)) {
    # find vertex with min distance from start
    # this will be 0 for first iteration
    minimum=INFINITY
    u=""
    for (v in Q) {
      if (fscore[v] < minimum) {
        minimum=fscore[v]
        u=v
      }
    }

    # we can stop once we reach the end
    if (u==finish) break

    # remove minimum distance vertex from queue
    delete Q[u]

    # find all neighbours of u which are in the graph but haven't been seen yet
    # add them to the queue and update their distances
    split(u,xy,SUBSEP)
    for (n in DX) {
      x=xy[1]+DX[n]; y=xy[2]+DY[n]
      if (!(x SUBSEP y in G) || seen[x,y]) continue

      altg=gscore[u]+G[x,y]
      if (altg < gscore[x,y]) {
        seen[x,y]=1
        gscore[x,y]=altg
        fscore[x,y]=altg+hdist[START]
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
  astar(Graph, NF, NR)

  for (xfill=0;xfill<5;xfill++) {
    for (yfill=0;yfill<5;yfill++) {
      for (x=1; x<=NR; x++) {
        for (y=1; y<=NR; y++) {
          Graph2[x+(NF*xfill),y+(NR*yfill)] = (Graph[x,y] + xfill + yfill - 1) % 9 + 1;
        }
      }
    }
  }

  astar(Graph2, NF*5, NR*5)
}
