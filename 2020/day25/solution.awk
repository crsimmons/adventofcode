#!/usr/bin/env awk -f

function mod_pow(x, exponent, mod, _result, _base) {
  if (exponent < 0) {
    print "negative exponent"
    exit
  }
  _result = 1
  _base = x % mod
  while (exponent > 0) {
    if (exponent % 2) _result = (_result * _base) % mod
    exponent = rshift(exponent, 1)
    _base = (_base ** 2) % mod
  }
  return _result
}

NR==1{a=$0}
NR==2{b=$0}

END {
  mod = 20201227
  other[a] = b
  other[b] = a
  for (n = 1; n != a && n != b; loop_size++) {
    n = (n * 7) % mod
  }
  print mod_pow(other[n], loop_size, mod)
}
