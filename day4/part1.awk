BEGIN {
  RS="\n\n"
  split("byr ecl eyr hcl hgt iyr pid", valid)
  gsub("\n"," ")
}
{
  split($0, arr)
  asort(arr)
  for (i in arr) {}
  switch(i) {
    case 8:
      sum +=1
      break
    case 7:
      for (j=1; j<=i; j++) {
        if (substr(arr[j],1,3) != valid[j]) {
          next
        }
      }
      sum +=1
      break
    default:
      break
  }
}
END {
  print sum
}
