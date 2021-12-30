#!/usr/bin/env gawk -f

function solve(solution,   i,r) {
  delete stack
  n=0; r=""
  for (i=1;i<=14;i++) {
    if (A[i]==1) stack[++n]=i
    else if (A[i]==26){
      j=stack[n--]
      solution[i]=solution[j]+B[i]+C[j]

      # if w_cur is greater than 9 then we want to reduce
      # w_prev by the amount that w_cur is above 9 which
      # therefore makes w_cur == 9
      if (solution[i] > 9) {
        solution[j]-=solution[i]-9
        solution[i]=9
      }

      # if w_cur is less than 1 then we increase w_prev
      # by the amount that w_cur is below 1 which
      # therefore makes w_cur == 1
      if (solution[i] < 1) {
        solution[j]+=1-solution[i]
        solution[i]=1
      }
    }
  }
  for (i=1;i<=14;i++) {
    r=r solution[i]
  }
  return r
}

BEGIN{r=1;RS="inp w"; FS="\n"}

NR>1{
  b=substr($6,7)
  a=b<0?26:1
  c=substr($16,7)

  A[++n]=a
  B[n]=b
  C[n]=c
}

END{
  for (i=1;i<=14;i++) {
    part1[i]=9
    part2[i]=1
  }

  print solve(part1)
  print solve(part2)
}
