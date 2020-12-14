{values[++i] = $0}

END{
  asort(values)
  for (x in values) {
    gaps[values[x] - prev]++
    prev = values[x]
  }
  print gaps[1] * (gaps[3] + 1)
}
