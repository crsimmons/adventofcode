#!/usr/bin/env gawk -f

function step(a,   x,y,z) {
  for(x=$2;x<=$3;x++) for(y=$4;y<=$5;y++) for(z=$6;z<=$7;z++) grid[x][y][z]=a?1:0
}

BEGIN{
  FS="[onfxyz ,]+=|\\.\\."
}

NR>20{next}

/on/ {
  step(1)
}

/off/ {
  step(0)
}

END{
  for (x=-50;x<=50;x++) for (y=-50;y<=50;y++) for (z=-50;z<=50;z++) s+=grid[x][y][z]
  print s
}
