function format() {
  field = 1
  # If the special character ‘&’ appears in replacement, it stands for the precise substring that was matched by regexp.
  gsub(/\(/, "& ")
  gsub(/\)/, " &")
}

function eval(_sum) {
  _sum = partial()
  while ($field == "+" || $field == "*")
    _sum = $(field++) == "+" ? _sum + partial() : _sum * partial()
  return _sum
}

function partial(_partialSum) {
  if ($field ~ /^[0-9]+$/) {
    return $(field++)
  } else {
    field++
    _partialSum = eval()
    field++
    return _partialSum
  }
}

{
  format()
  sum += eval()
}

END { print sum }
