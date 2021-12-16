#!/usr/bin/env gawk -f

# I could probably clean this up but I can't be bothered
# AWK doesn't let you return multiple values from a function
# nor does it let you return an array from a function
# so in order to return both the remaining string and the literal value
# I add both to a global multidimensional array R[n][i] as i=1 and i=2 respectively
# while incrementing n. Then I return n so the caller can retrieve the values from R

# sorry...

# from day 3
function b2d(b,   l,k,e,d) {
  l=length(b)
  for(;++k<=l;){e=2**(l-k);d+=e*substr(b,k,1)}
  return d
}

function operate(v1,v2,o) {
  switch (o) {
    case 0:
      # sum
      return v1+v2
      break
    case 1:
      # product
      return v1*v2
      break
    case 2:
      # min
      return v1<v2?v1:v2
      break
    case 3:
      # max
      return v1>v2?v1:v2
      break
    case 5:
      # greater than
      return v1>v2?1:0
      break
    case 6:
      # less than
      return v1<v2?1:0
      break
    default:
      # equal
      return v1==v2?1:0
      break
  }
}

function get_literal(b,   l,b2) {
  part=substr(b,I,5)
  while(substr(part,1,1)==1){
    l=l substr(part,2,4)
    part=substr(b,I+=5,5)
  }
  I+=5
  return b2d(l substr(part,2,4))
}

function return_value(t,arr,   l,v,r) {
  l=length(arr)
  if (l==1) return arr[1]

  if (l==2) return operate(arr[1],arr[2],t)

  else {
    r=arr[1]
    for(v=2;v<=length(arr);v++) r=operate(r,arr[v],t)
    return r
  }
}

function eval_packet(b,   t,L,l,i,j,b2,payload,v,n,temp_values) {
  for (v in Packet_values) printf "P[%s]=%s\n", v, Packet_values[v]
  v=substr(b,1,3)
  t=b2d(substr(b,4,3))
  V[nV++]=b2d(v)

  if (t==4) {
    # literal value
    I=7
    n=get_literal(b)
    R[++nR][1]=n
    R[nR][2]=substr(b,I)
    return nR
  } else {
    # operator
    id=substr(b,7,1)
    if (id==0) {
      # subpackets by length
      L=b2d(substr(b,8,15))
      l=L
      i=23
      b2=b
      while (l>0) {
        payload=substr(b2,i,l)
        n=eval_packet(payload)
        b2=R[n][2]
        temp_values[++j]=R[n][1]
        l=length(b2)
        i=1
      }
      R[++nR][1]=return_value(t,temp_values)
      R[nR][2]=substr(b,L+23)
      return nR
    } else if (id==1) {
      # subpackets by number
      l=b2d(substr(b,8,11))
      I=19
      b2=b
      while (l>0) {
        i=I
        n=eval_packet(substr(b2,I))
        b2=R[n][2]
        temp_values[++j]=R[n][1]
        l--
        I=1
      }
      R[++nR][1]=return_value(t,temp_values)
      R[nR][2]=substr(b,length(b)-length(b2)+1)
      return nR
    }
  }
}

BEGIN{
  FS=""
  h2b["0"]="0000"
  h2b["1"]="0001"
  h2b["2"]="0010"
  h2b["3"]="0011"
  h2b["4"]="0100"
  h2b["5"]="0101"
  h2b["6"]="0110"
  h2b["7"]="0111"
  h2b["8"]="1000"
  h2b["9"]="1001"
  h2b["A"]="1010"
  h2b["B"]="1011"
  h2b["C"]="1100"
  h2b["D"]="1101"
  h2b["E"]="1110"
  h2b["F"]="1111"
}

{
  for (i=1;i<=NF;i++) B=B h2b[$i]
}

END{
  while (length(B)) {
    n=eval_packet(B)
    B=R[n][2]
  }
  for (v in V) p1+=V[v]
  print p1

  asort(R,R,"@ind_num_desc")
  print R[1][1]
}
