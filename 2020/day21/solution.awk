#!/usr/bin/env gawk -f

# Converts a space-separated list of elements
# into a set with the element as keys and the
# number of occurences of each element in the
# input list as values
function Set(s,o,_a,_e) {
  delete o
  split(s,_a,/ /)
  for(_e in _a) {
    o[_a[_e]]++
  }
}

# Coverts set/array into space-separated list
function join(l,_e,_o) {
  for(_e in l) {
    _o=_o" "_e
  }
  gsub(/^ /,"",_o)
  return _o
}

# Returns a space-separated list of unique elements
# which are common between space-separated input a
# and input set b
function intersection(a,b,_a,_e) {
  if(!a) return join(b)
  Set(a,_a)
  for(_e in _a) {
    if(!(_e in b)) {
      delete _a[_e]
    }
  }
  return join(_a)
}

function single(arr,_o,_a) {
  for(_o in arr) {
    split(arr[_o],_a," ")
    if(length(_a)==1) {
      return _o
    }
  }
}

# Remove elements in a from b then return the remaining
# elements as a space-separated list
function remove(a,b,_a,_b,_e) {
  Set(a,_a)
  Set(b,_b)
  for(_e in _a) {
    delete _b[_e]
  }
  return join(_b)
}

function dupe(a,b,_e) {
  for(_e in a) {
    b[_e]=a[_e]
  }
}

BEGIN{
  FS=" .contains |, "
}

{
  gsub(/\)/,"")
  Set($1,ingregient_counts)
  for(e in ingregient_counts) {
    ingredients[e]+=ingregient_counts[e]
  }
  for(e=1;e++<NF;) {
    allergens[$e]=intersection(allergens[$e],ingregient_counts)
  }
}

END{
  # delete ingredients which are allergens
  for(x in allergens) {
    Set(allergens[x],allergen_counts)
    for(e in allergen_counts) {
      delete ingredients[e]
    }
  }
  # count number of ingredients which aren't
  # allergens
  for(i in ingredients) {
    part1 += ingredients[i]
  }
  print "part1: "part1
  # for each allergen associated with a
  # single allergen add it to a final array
  # then remove that ingredient from the
  # ingredient lists of all other allergens
  while(x = single(allergens)) {
    final[x]=allergens[x]
    delete allergens[x]
    for(e in allergens){
      allergens[e]=remove(final[x],allergens[e])
    }
  }
  dupe(final,sorted_allergens)
  asorti(sorted_allergens)
  for(x in sorted_allergens) {
    part2=part2","final[sorted_allergens[x]]
  }
  gsub(/^,/,"",part2)
  print "part2: "part2
}
