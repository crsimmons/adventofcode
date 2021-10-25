#!/usr/bin/env awk -f

function parse(_i, _x, _y, _z, _d) {
  while ($++_i) {
    split(dir[$_i], _d)
    _x += _d[1]
    _y += _d[2]
    _z += _d[3]
  }
  return _x " " _y " " _z
}

function day(tiles, _tile, _coord, _k, _direction, _neighbours) {
  # tiles is an array of black tiles
  # build out coordinates of neighbouring tiles for each tile
  for (_tile in tiles) {
    split(_tile, _coord)
    for (_k in dir) {
      split(dir[_k], _direction)
      # 1=x,2=y,3=z
      _neighbours[_coord[1]+_direction[1],_coord[2]+_direction[2],_coord[3]+_direction[3]]++
    }
  }

  for (_tile in tiles) {
    # if a black tile has 0 or >2 black neighbours
    # flip to white (delete from tiles)
    if (!_neighbours[_tile] || _neighbours[_tile] > 2)
      delete tiles[_tile]
    # delete remaining neighbours of black tiles
    delete _neighbours[_tile]
  }
  for (_tile in _neighbours) {
    # each _tile in _neighbours is now a white tile
    # so _neighbours[_tile] == 2 is a white tile with
    # 2 adjacent black tiles
    if (_neighbours[_tile] == 2) tiles[_tile] = 1
  }
}

BEGIN {
  SUBSEP = FS
  # x y z
  # from https://www.redblobgames.com/grids/hexagons/
  dir["e"]  = "1 -1 0"
  dir["se"] = "0 -1 1"
  dir["sw"] = "-1 0 1"
  dir["w"]  = "-1 1 0"
  dir["nw"] = "0 1 -1"
  dir["ne"] = "1 0 -1"
}

# add space after 'e' or 'w'
# & is a special character for the whole match
{ gsub(/e|w/, "& ") }
# determine final vector of each set of instructions
{ k = parse($0) }
# if final vector appeared once before, flip it back
k in tile { delete tile[k]; next }
# mark final vector as black
{ tile[k] = 1 }

END {
  for (k in tile) part1++
  print "part1: " part1
  while (i++ < 100) day(tile)
  for (k in tile) part2++
  print "part2: " part2
}
