#!/usr/bin/env gawk -f

function pv(v,  x) {
  for (x in v) {
    if (v[x]) printf "%s\n", x
  }
  printf "\n"
}

function count(str, e) {
  return gsub(e,"",str)
}

function small_caves_unique(visited,   visited_caves, node, current_cave, count) {
  split(visited,visited_caves,",")
  for (node in visited_caves) {
    current_cave=visited_caves[node]
    if (count[current_cave]++ && current_cave == tolower(current_cave)) return 0
  }
  return 1
}

function dfs(current, visited,   node) {
  visited=visited current ","
  if (current == "end") {
    all_paths[visited]++
    return
  }

  for (node in edges[current]) {
    if (!index(visited,node) || node != tolower(node)) {
      dfs(node,visited)
    }
  }
}

BEGIN{FS="-"}

{
  edges[$1][$2]++
  edges[$2][$1]++
}

END{
  # initialize an empty array
  split("",all_paths)
  dfs("start","")
  print length(all_paths)
}
