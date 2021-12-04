#!/usr/bin/env gawk -f

function mark(n,_b,_x,_y) {
  for (_b in boards){
    for (_y in boards[_b]) {
      for (_x in boards[_b][_y]) {
        if (boards[_b][_y][_x]==n) boards[_b][_y][_x]=-1
      }
    }
  }
}

function has_won(b,_x,_y,_s) {
  for (_y=1;_y<=5;_y++) {
    _s=0
    for (_x=1;_x<=5;_x++) {
      _s+=b[_y][_x]
    }
    if (_s==-5) return 1
  }
  for (_x=1;_x<=5;_x++) {
    _s=0
    for (_y=1;_y<=5;_y++) {
      _s+=b[_y][_x]
    }
    if (_s==-5) return 1
  }
  return 0
}

function sum_unmarked(b,_x,_y,_s) {
  for (_y in b) {
    for (_x in b[_y]) {
      _s+=b[_y][_x]>0?b[_y][_x]:0
    }
  }
  return _s
}

BEGIN{RS="";F="[[:space:]]+"}

/,/{split($0,nums,",")}
/ /{
  for(row=1;row<=5;row++){
    for(col=1;col<=5;col++){
      boards[NR-1][row][col]=$(col+(row-1)*5)
    }
  }
}

END{
  for (num in nums) {
    mark(nums[num])
    for (board in boards) {
      if (has_won(boards[board])) {
        result=sum_unmarked(boards[board])*nums[num]
        if (++wins==1) printf "p1: %s\n", result
        else if (length(boards)==1) {printf "p2: %s\n", result; exit 1}
        else delete boards[board]
      }
    }
  }
}
