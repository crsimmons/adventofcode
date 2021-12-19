#!/usr/bin/env gawk -f

function ceil(k){return (k==int(k))?k:int(k)+1}

function floor(k){return (k==int(k))?k:int(k)}

function arrcpy(arr1,arr2,   i) {
  delete arr1;
  for (i in arr2) {
    arr1[i]=arr2[i];
  }
}

function build_tree(t,   char,level,i) {
  for (char=1;char<=NF;char++) {
    if ($char=="[") level++
    else if ($char=="]") level--
    else if ($char!=",") t[++i]=$char "," level
  }
}

function add(tree1,tree2,output,   e,e2,arr) {
  for (e in tree1) {
    split(tree1[e],arr,",")
    output[e]=arr[1]","arr[2]+1
  }
  for (e2 in tree2) {
    split(tree2[e2],arr,",")
    output[++e]=arr[1]","arr[2]+1
  }
}

function explode(tree,   e,e2,vals,vals2,vals3) {
  for (e in tree) {
    split(tree[e],vals,",")
    if (vals[2]>=5) {
      # has a left neighbour
      if (e>1) {
        split(tree[e-1],vals2,",")
        tree[e-1]=vals2[1]+vals[1]","vals2[2]
      }
      # has a right neighbour
      if (e+2<=length(tree)) {
        split(tree[e+1],vals2,",")
        split(tree[e+2],vals3,",")
        tree[e+2]=vals3[1]+vals2[1]","vals3[2]
      }
      tree[e]=0","vals[2]-1
      for (e2=e+1;e2<length(tree);e2++) {
        tree[e2]=tree[e2+1]
      }
      delete tree[e2]
      return 1
    }
  }
  return 0
}

function splitnum(tree,   e,e2,vals) {
  for (e in tree) {
    split(tree[e],vals,",")
    if (vals[1]>=10) {
      for (e2=length(tree);e2>int(e);e2--) {
        tree[e2+1]=tree[e2]
      }
      tree[e]=floor(vals[1]/2)","vals[2]+1
      tree[e+1]=ceil(vals[1]/2)","vals[2]+1
      return 1
    }
  }
  return 0
}

function reduce(tree,   t,x,s) {
  while (1) {
    if (explode(tree)) continue
    if (splitnum(tree)) continue
    break
  }
}

function magnitude(tree,   e,e2,vals,vals2) {
  for (e=1;e<length(tree);e++) {
    split(tree[e],vals,",")
    split(tree[e+1],vals2,",")
    # depth of sequential numbers is same
    if (vals[2]==vals2[2]) {
      tree[e]=3*vals[1]+2*vals2[1]","vals[2]-1
      for (e2=e+1;e2<length(tree);e2++) {
        tree[e2]=tree[e2+1]
      }
      delete tree[e2]
    }
  }
}

function p2mag(a,b,   tree1,tree2,total,mag,result) {
  $0=a
  build_tree(tree1)
  $0=b
  build_tree(tree2)
  add(tree1, tree2, total)
  reduce(total)
  arrcpy(mag,total)
  l=0
  while (length(mag)>1) {
    magnitude(mag)
    if (l==length(mag)) break
    else l=length(mag)
  }
  split(mag[1],result,",")
  return result[1]
}

BEGIN{FS=""}

# don't parse empty lines
/^\s*$/ {next}

{
  rows[NR]=$0
}

NR==1{
  build_tree(total)
  next
}

{
  delete line
  delete tmp
  build_tree(line)
  add(total,line,tmp)
  arrcpy(total,tmp)
  reduce(total)
}

END{
  arrcpy(mag,total)
  l=0
  while (length(mag)>1) {
    magnitude(mag)
    # for some lines if you add them in reverse order you end up
    # with a reduced mag array with each element at a different
    # depth which causes this part to loop endlessly.
    # The following conditional breaks out of this
    if (l==length(mag)) break
    else l=length(mag)
  }

  split(mag[1],p1,",")
  print p1[1]

  for (i in rows) {
    for (j in rows) {
      if (i == j) continue
      newmag=p2mag(rows[i],rows[j])
      p2=newmag>p2?newmag:p2
    }
  }
  print p2
}
