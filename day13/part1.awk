BEGIN{FS=","}

{
  if (NR==1) {t=$0}
  else {
    for(i=1;i<NF;i++) {
      if ($i != "x") {arr[i]=$i}
    }
  }
}

END{
  for (x in arr) {
    v=arr[x]-(t%arr[x])
    if (m==0){m=v;b=arr[x]}
    else if (v<m){m=v;b=arr[x]}
  }
  print m * b
}
