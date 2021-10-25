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
      invalid = values[pointer]
      break
    }
  }

  left = 1
  right = 2
  sum = values[1]
  while (right <= NR) {
    sum += values[right]
    if (sum == invalid) {
      break
    }
    else if (sum < invalid) {
      right++
    }
    else {
      left++
      sum = values[left]
      right = left + 1
    }
  }

  min = values[left]
  max = values[left]
  for (i = left + 1; i <= right; i++) {
    if (values[i] < min) min = values[i]
    if (values[i] > max) max = values[i]
  }
  print min + max
}
