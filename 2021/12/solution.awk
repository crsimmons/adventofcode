#!/usr/bin/env gawk -f

function count(path,node) {
  return gsub(node,"",path)
}

function contains(arr,e,   x) {
  for (x in arr) if (arr[x]==e) return 1
  return 0
}

function small_caves_unique(path,   caves_in_path, node, current_cave, count) {
  split(path,caves_in_path,",")
  for (node in caves_in_path) {
    current_cave=caves_in_path[node]
    if (count[current_cave]++ && current_cave == tolower(current_cave)) return 0
  }
  return 1
}

function find_paths(neighbours, paths, path, node, part,   caves_in_path, neighbour) {

  if (part==1) {
    split(path,caves_in_path,",")
    if (node==tolower(node) && contains(caves_in_path,node)) return
  }

  path=path node ","

  for (neighbour in neighbours[node]) {
    if (neighbour == "start") continue
    if (neighbour == "end") {
      paths[length(paths)+1]=path "end"
      continue
    }
    # if neighbour is lowercase, appears in the path, and the path already has non-unique small caves, then skip
    if (part==2 && neighbour==tolower(neighbour) && count(path,neighbour)>0 && !small_caves_unique(path)) continue
    find_paths(neighbours,paths,path,neighbour,part)
  }
}

BEGIN{FS="-"}

{
  neighbours[$1][$2]++
  neighbours[$2][$1]++
}

END{
  # initialize an empty array
  split("",paths)
  find_paths(neighbours,paths,"","start",2)
  print length(paths)
}
