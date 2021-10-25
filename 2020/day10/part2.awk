{values[++i] = $0}

END{
  asort(values)
  a[1]=0; a[2]=0; a[3]=1; a[4]=1
  for (x in values) {
    n = values[x]
    a[n+3] = a[n] + a[n+1] + a[n+2]
  }
  print a[length(a)]
}
