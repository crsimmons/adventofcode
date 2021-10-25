BEGIN {
  RS="\n\n"
}

{
  gsub("\n","")

  for (i = 1; i <= length($0); i++) {
    a[substr($0,i,1)] = 1
  }

  sum += length(a)

  delete a;
}

END {
  print sum
}
