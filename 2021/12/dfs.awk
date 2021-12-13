#!/usr/bin/env gawk -f

function count(str, e) {
  return gsub(e,"",str)
}

function dfs(current, visited, dupe,   node) {
  visited=visited current ","
  if (current == "end") {
    all_paths[visited]++
    return
  }

  for (node in edges[current]) {
    if (index(visited,node) && node==tolower(node)) {
      if (node!=dupe || count(visited,node)!=1) continue
    }
    dfs(node,visited,dupe)
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
  dfs("start","","")
  print length(all_paths)
  split("", all_paths)
  for (node in edges) {
    if (node==tolower(node) && node!="start" && node!="end") {
      dfs("start","",node)
    }
  }
  print length(all_paths)
}
