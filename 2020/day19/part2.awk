function resolve(name, r, _rule, _criteria) {
  _rule = rules[r]
  rules[r] = name
  while (split(_rule, _criteria, /[^0-9]+/) > 2) {
    for (e in _criteria) {
      gsub(" "_criteria[e]" ", " ("rules[_criteria[e]]") ", _rule)
    }
  }
  gsub(/ /, "", _rule)
  return _rule
}

BEGIN{FS=": "}

NF==2 {
  gsub(/"/,"")
  # " (fixes syntax highlighting)
  rules[$1]=" "$2" "
  next
}

NF==0 {
  A = resolve("A", 42)
  B = resolve("B", 31)
  C = resolve("C", 8)
  D = resolve("D", 11)
  r1 = r2 = resolve("X", 0)
  gsub(/C/, C, r1)
  gsub(/D/, D, r1)
  gsub(/A/, A, r1)
  gsub(/B/, B, r1)
  r1="^("r1")$"

  for (i = 0; i < 3; i++) {
    gsub(/D/, "(("A")("B")|("A")D("B"))", r2)
  }
  gsub(/D/, "(("A")("B"))", r2)
  gsub(/C/, "("A")+", r2)
  r2 = "^("r2")$"
  next
}

$0 ~ r1 { match1++; next }
$0 ~ r2 { match2++ }

END{
  print match1 + match2
}
