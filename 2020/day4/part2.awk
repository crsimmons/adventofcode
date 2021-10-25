BEGIN {
  RS="\n\n";
  split("byr ecl eyr hcl hgt iyr pid", valid)
  gsub("\n"," ")
}
{
  split($0, arr);
  asort(arr);
  for (i in arr) {
    k = substr(arr[i],1,3)
    v = substr(arr[i],5)
    switch(k) {
      case "byr":
        if (length(v) != 4 || v < 1920 || v > 2002) {
          next
        }
        break
      case "iyr":
        if (length(v) != 4 || v < 2010 || v > 2020) {
          next
        }
        break
      case "eyr":
        if (length(v) != 4 || v < 2020 || v > 2030) {
          next
        }
        break
      case "hgt":
        unit=substr(v,length(v)-1)
        value=substr(v,1,length(v)-2)
        if ((unit == "cm" && (value < 150 || value > 193)) || (unit == "in" && (value < 59 || value > 76)) || unit !~ /cm|in/) {
          next
        }
        break
      case "hcl":
        if (v !~ /^#[0-9a-f]{6}$/) {
          next
        }
        break
      case "ecl":
        if (v !~ /^amb$|^blu$|^brn$|^gry$|^grn$|^hzl$|^oth$/) {
          next
        }
        break
      case "pid":
        if (v !~ /^[0-9]{9}$/) {
          next
        }
        break
      default:
        break
    }
  }
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
