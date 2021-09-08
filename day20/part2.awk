# heavily based on https://github.com/juntuu/advent_of_code_2020/blob/main/day_20/solution.awk

function side(n,_i,_t) {
  for(_i=1;_i<=NF;_i++){
    _t=_t substr($_i,n,1)
  }
  return _t
}

function reverse(s,_i,_o) {
  for(_i=length(s);_i!=0;_i--){
    _o=_o substr(s,_i,1)
  }
  return _o
}

function rotate(_i,_t,_a,_j) {
  # load each row into an array
  for(_i=1;_i<=NF;_i++){
    _t[_i]=$_i
    $_i=""
  }
  # convert rows into columns (rotate 90 degrees)
  for(_i=NF;_i>0;_i--){
    split(_t[_i],_a,"")
    for (_j in _a){
      $_j = $_j _a[_j]
    }
  }
}

function flip(_i) {
  for (_i = 1; _i <= NF; _i++)
    $_i = reverse($_i)
}

function remove_adjacent(x,y,t) {
  if ((x,y) in image) {
    gsub(image[x,y], "", Adjacent[t])
    gsub(t, "", Adjacent[image[x,y]])
  }
}

function common(s,_a,_b,_e) {
  split(s, _a)
  # traverse all input tile ids (_a) and return the
  # first one to appear more than once
  for(_e in _a){
    if(++_b[_a[_e]] > 1){
      return _a[_e]
    }
  }
}

function place(x,y,t) {
  # if tile is provided place it
  # otherwise find tile which is adjacent to the ones at
  # (x-1,y) and (x,y-1) and place it at (x,y)
  t = t ? 0+t : common(Adjacent[image[x-1,y]]" "Adjacent[image[x,y-1]])
  image[x,y] = t
  remove_adjacent(x-1, y, t)
  remove_adjacent(x, y-1, t)
}

function build(t,_o,_x,_i) {
  # place first corner
  place(1,1,t)
  split(Adjacent[t], _o)
  # place tiles adjacent to first corner
  place(2,1,_o[1])
  place(1,2,_o[2])
  # place tile diagonal from first corner (adjacent to above two tiles)
  place(2,2)
  # loop through remaining coordinates
  for(_x=3;_x<=N;_x++){
    # place tiles on first corner's side of diagonal
    place(_x, 1, Adjacent[image[_x-1,1]])
    place(1, _x, Adjacent[image[1,_x-1]])
    # place tiles on other side of diagonal
    for (_i = 2; _i < _x; _i++) {
      place(_x, _i)
      place(_i, _x)
    }
    # place tile on corner opposite to initial corner
    place(_x,_x)
  }
}

function rule(x,y) {
  return edges[image[x,y]]
}

function valid(x,y,_above,_below,_left,_right) {
  _above=($1 ~ rule(x, y-1))
  _below=($NF ~ rule(x, y+1))
  _left=(side(1) ~ rule(x-1, y))
  _right=(side(length($1)) ~ rule(x+1, y))
  return _above &&
    _below &&
    _left &&
    _right
}

function orient(x,y,_orientation) {
  $0 = tiles[image[x,y]]
  for(_orientation=1;_orientation<=8;_orientation++) {
    if(valid(x,y)){
      return tiles[image[x,y]] = $0
    }
    rotate()
    if(_orientation == 4) {
      flip()
    }
  }
}

function assemble(_s, _i, y, x) {
  for (y = 1; y <= N; y++) {
    # trim borders
    _i=2
    while(_i<=9){
      for (x = 1; x <= N; x++) {
        $0 = tiles[image[x,y]]
        gsub(/ /, "\n")
        _s = _s substr($_i, 2, 8)
      }
      _s = _s "\n"
      _i++
    }
  }
  return _s
}

function matches(str,regex,_offset) {
  delete RSTARTS
  # loop over each match of str with regex
  # for each one store the starting index of
  # the match relative to the original start of the line
  # (offset from the start + start of the match)
  # Then update the current pointer index
  # to be RSTART and the input string to be the remainder
  # of the string from RSTART to the end.
  while(match(str,regex)){
    RSTARTS[_offset + RSTART]
    _offset=RSTART
    str=substr(str,_offset+1)
  }
}

function join(a,_s,_i) {
  while (++_i in a){
    _s = _s a[_i]
  }
  return _s
}

function mark_monster(row,col,regex,_r,_regex,_i) {
  split($row,_r,"")
  split(regex,_regex,"")
  for(_i in _regex){
    # if the _i'th element of the monster string is '#' then
    # the corresponding element in the row is the start of
    # the match (col) + _i - 1 (since we're 1 indexed)
    if(_regex[_i]=="#"){
      _r[col+_i-1]="O"
    }
  }
  $row=join(_r)
}

function check_monsters(_row,_rs,_above,_below,_m) {
  for(_row=2;_row<NF;_row++){
    matches($_row,m[2])
    for(_rs in RSTARTS){
      _above=substr($(_row-1), _rs)
      _below=substr($(_row+1), _rs)
      if(_above ~ "^"m[1] && _below ~ "^"m[3]){
        mark_monster(_row-1, _rs, m[1])
        mark_monster(_row, _rs, m[2])
        mark_monster(_row+1, _rs, m[3])
        _m++
      }
    }
  }
  return _m
}

BEGIN{
  FS=RS
  RS=""
  m[1]="..................#."
  m[2]="#....##....##....###"
  m[3]=".#..#..#..#..#..#..."
}

{
  gsub(/\./, "~")
  id=substr($1,6,4)
  sub(/[^\n]*\n/,"")
  l=side(1)
  r=side(length($1))
  edges[id]=$1"|"reverse($1)"|"$NF"|"reverse($NF)"|"l"|"reverse(l)"|"r"|"reverse(r)
  tiles[id]=$0
}

END{
  FS=" "
  for(id in edges){
    for(j in edges){
      if(id!=j&&edges[j]~edges[id]){
        Adjacent[id]=Adjacent[id]" "j
      }
    }
    if(split(Adjacent[id],_)==2){
      corner=id
    }
  }
  N = sqrt(NR)
  build(corner)
  for(x=1;x<=N;x++){
    for(y=1;y<=N;y++){
      orient(x,y)
    }
  }
  $0 = assemble()
  # debug()
  for(orientation=0;orientation++<8 && !check_monsters();){
    rotate()
    if(orientation==4){
      flip()
    }
  }
  p2 = gsub(/#/, "")
  print p2
}
