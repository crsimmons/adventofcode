#!/usr/bin/env gawk -f

function max(a,b) {return a>b?a:b}
function min(a,b) {return a<b?a:b}

BEGIN{FS="[onfxyz ,]+=|\\.\\."}

{
  new_val=$0~/on/?1:-1
  nminx=$2; nmaxx=$3
  nminy=$4; nmaxy=$5
  nminz=$6; nmaxz=$7

  delete updates

  for (c in cubes) {
    split(c,arr,",")
    cube_val=cubes[c]
    cminx=arr[1]; cmaxx=arr[2]
    cminy=arr[3]; cmaxy=arr[4]
    cminz=arr[5]; cmaxz=arr[6]

    # Intersections
    # If there are any intersections they will fall between the highest
    # min and lowest max for each dimension.
    i_minx=max(nminx,cminx); i_maxx=min(nmaxx,cmaxx)
    i_miny=max(nminy,cminy); i_maxy=min(nmaxy,cmaxy)
    i_minz=max(nminz,cminz); i_maxz=min(nmaxz,cmaxz)

    # If the highest min is less than the lowest max then there is an intersection
    # on that axis. If this is true on all axes then there is an intersection of
    # the cuboids so we create a new cuboid (or update it if it exists) for these
    # intersection coordinates by subtracting the original value for this cuboid.
    #
    # For example if the original value of the current cuboid (c) is 1 (on) and we've
    # just found an intersection cuboid with the current action then before evaluating
    # the new instruction we first create a new cuboid in the intersection space
    # where all the cubes are cancelled (off).
    # This prevents double counting and we can do it regardless of whether this action
    # is to turn cubes on or off. In the former case we add a cuboid turning these off
    # now then they get turned back on in the final tally by adding the new cuboid in
    # the next step. In the latter case these cubes will be turned off after accounting
    # for the new action anyway.
    #
    # In the inverse case where c is actually off (-1) we still cancel its value for
    # the intersection (subtract -1) but then there isn't a subsequent step for it
    # so they stay cancelled in the final tally.
    if (i_minx<=i_maxx && i_miny<=i_maxy && i_minz<=i_maxz) {
      updates[i_minx "," i_maxx "," i_miny "," i_maxy "," i_minz "," i_maxz]-=cube_val
    }
  }

  # If the latest action is to turn the cube on then we add 1 to every
  # cube in the new cuboid. We don't need to evaluate the off case because
  # we've turned off intersecting cubes already and the default cube state is off
  if (new_val>0) {
    updates[nminx "," nmaxx "," nminy "," nmaxy "," nminz "," nmaxz]+=new_val
  }

  # Update the total list of cubes with the updates from this new action
  for (u in updates) {
    cubes[u]+=updates[u]
  }
}

END{
  # Volume of a cuboid is just L * B * H
  # For example if we had a cuboid defined by:
  # x=0..3, y=3..5, z=1..2
  # Then L=3-0+1, B=5-3+1, H=2-1+1
  # the '+1' is needed for some reason but my brain is too fried to figure it out
  # Once we have the volume of each cuboid we multiply it by it's sign which will
  # either be -1 (off), 0 (cancelled), or 1 (on)
  # Summing across these volumes results in the total number of cubes that are on.
  for (c in cubes) {
    split(c,arr,",")
    s+=((arr[2]-arr[1]+1) * (arr[4]-arr[3]+1) * (arr[6]-arr[5]+1) * cubes[c])
  }
  print s
}
