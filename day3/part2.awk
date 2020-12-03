function trees(r,m){
  (substr($0,((m)*r)%(length($0))+1,1)=="#") ? s=1 : s=0
  return s
}

{
  s1 += trees(1,NR-1);
  s2 += trees(3,NR-1);
  s3 += trees(5,NR-1);
  s4 += trees(7,NR-1);
  if ((NR % 2) == 1) {
    s5 += trees(1,int(NR/2));
  }
}

END {
  print s1 * s2 * s3 * s4 * s5
}
