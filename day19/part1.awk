function resolve(name, r, _rule, _criteria) {
  _rule = rules[r]
  rules[r] = name
  # loop until all rule references in regex are resolved
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
  r = resolve("X", 0)
  r="^("r")$"
  next
}

$0 ~ r { m++; next }

END{
  print m
}
