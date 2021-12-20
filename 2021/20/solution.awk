#!/usr/bin/env gawk -f

# from day 3
function b2d(b,   l,k,e,d) {
  l=length(b)
  for(;++k<=l;){e=2**(l-k);d+=e*substr(b,k,1)}
  return d
}

function arrcpy(arr1,arr2,   x,y) {
  delete arr1;
  for (x in arr2) {
    for (y in arr2[x]) {
      arr1[x][y]=arr2[x][y];
    }
  }
}

function new_pixel(step,x0,y0,   x,y,b) {
  for (y=y0-1;y<=y0+1;y++) {
    for (x=x0-1;x<=x0+1;x++) {
      # The infinite region outside of the image alternates between
      # all 1s and all 0s because algo[0]=1 and algo[511]=0.
      # This is not the case with the example where the first and last
      # characters in algo are switched.
      # So we assume all points are 0 extending to infinity but on
      # odd steps (first step is 0) we change points outside the current
      # window to 1 before adding it to the binary value.
      if (y<miny || y>maxy || x<minx || x>maxx) {
        if (algo[0] && step%2) {
          image[x][y]=1
        }
      }
      b=b image[x][y]+0
    }
  }
  return algo[b2d(b)]
}

function enhance(step,image_in,image_out,   x,y,c) {
  for (y=miny-1;y<=maxy+1;y++) {
    for (x=minx-1;x<=maxx+1;x++) {
      image_out[x][y]=new_pixel(step,x,y)
      if (image_out[x][y]) c++
    }
  }
  return c
}

BEGIN{FS=""; y=0; STEPS=50}

NR==1{
  for (i=1;i<=NF;i++) algo[i-1]=$i=="#"?1:0
  next
}

{
  for (i=1;i<=NF;i++) {
    image[i-1][y]=$i=="#"?1:0
  }
  y++
}


END{
  minx=0; maxx=NF-1; miny=0; maxy=y-1
  for (s=0;s<STEPS;s++) {
    sum=enhance(s,image,image2)
    arrcpy(image,image2)
    delete image2
    minx--; miny--; maxx++; maxy++
    if (s==1) print sum
  }
  print sum
}
