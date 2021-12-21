#!/usr/bin/env gawk -f

function move(   i,m) {
  for (i=1;i<=3;i++) m+=++rolls
  return m
}

function part1(p1,p2,   s1,s2,m) {
  while (1) {
    m=move(); p1=(p1+m)%10; s1+=p1+1
    if (s1>=1000) {print s2*rolls; break}
    m=move(); p2=(p2+m)%10; s2+=p2+1
    if (s2>=1000) {print s1*rolls; break}
  }
}

# p1 is the current player
# p2 is the other player
# s1 is p1's score
# s2 is p2's score
# I couldn't get a solution with a current player flag to work...
function dirac(p1,p2,s1,s2,   k,w1,w2,d1,d2,d3,np1,ns1,r,ra) {
  if (s1>=21) return "1,0"
  if (s2>=21) return "0,1"
  k=p1 p2 s1 s2
  if (k in state) return state[k]
  for (d1=1;d1<=3;d1++) {
    for (d2=1;d2<=3;d2++) {
      for (d3=1;d3<=3;d3++) {
        np1=(p1+d1+d2+d3)%10
        ns1=s1+np1+1
        r=dirac(p2,np1,s2,ns1)
        split(r,ra,",")
        w1+=ra[2]
        w2+=ra[1]
      }
    }
  }
  state[k]=w1 "," w2
  return w1 "," w2
}

NR==1{P1=$NF-1}
NR==2{P2=$NF-1}

END{
  part1(P1,P2)
  wins=dirac(P1,P2,S1,S2)
  split(wins,sol,",")
  part2=sol[1]>sol[2]?sol[1]:sol[2]
  print part2
}
