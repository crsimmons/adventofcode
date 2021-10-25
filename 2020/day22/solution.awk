#!/usr/bin/env awk -f

function score(c,n,_a,_s) {
  split(c,_a," ")
  for(_i=n;_i>0;_i--) {
    _s+=_a[_i]*(n-_i+1)
  }
  return _s
}

function draw(cards,n,_o) {
  match(cards, "^([0-9]+ ?){"n"}")
  _o=substr(cards, 1, RLENGTH)
  sub(/ $/,"",_o)
  return _o
}

function max(cards, _a, _k,_o) {
	split(cards, _a)
	for (_k in _a) {
    cards = _a[_k]
    if (_a[_k] > _o) {
      _o=_a[_k]
    }
  }
	return _o
}

function combat(a,b,an,bn,r,_s,_a,_b,_w) {
  if (r > 1 && max(a) > max(b)) {
    return 1
  }
  while(an && bn) {
    if(r&&_s[a,b]++) {
      return 1
    }
    _a = +a
    _b = +b
    sub(/^[0-9]+ ?/,"",a)
    sub(/^[0-9]+ ?/,"",b)
    an--
    bn--
    _w=_a>_b
    if (r&&an>=_a&&bn>=_b) {
      _w=combat(draw(a,_a),draw(b,_b),_a,_b,2)
    }
    if(_w) {
      a=a" "_a" "_b
      an+=2
    } else {
      b=b" "_b" "_a
      bn+=2
    }
  }
  return r>1?_w:score(a b,an+bn)
}

BEGIN{
  RS=""
}

{
  N=gsub(/Player .:.|\n/," ")
  gsub(/^ /,"")
}

NR==1 {A=$0;AN=N}
NR==2 {B=$0;BN=N}

END{
  print "part1: "combat(A,B,AN,BN)
  print "part2: "combat(A,B,AN,BN,1)
}
