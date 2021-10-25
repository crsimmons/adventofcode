function get_preamble(   j) {
  for (j = i; j <= pointer - 1; j++) {
    if (j > NR) break
    preamble[j] = values[j]
  }
}

function is_valid(val,   j) {
  for (x in preamble) {
    for (j = 1; j < preamble_length; j++) {
      if (preamble[x] + preamble[x + j] == val) {
        return 1
      }
    }
    delete preamble[x]
  }
  return 0
}

BEGIN{preamble_length = 25}

{values[++i] = $0}

END{
  for (i = 1; i <= NR; i++) {
    pointer = i + preamble_length
    delete preamble
    get_preamble()
    if (!is_valid(values[pointer])) {
      print values[pointer]
      break
    }
  }
}
