function get_path(graph, outer, target, path,   graph_elements,   path_elements,   graph_element) {
  path = path (path ? "," : "") outer;
  if (outer == target) {
    return path
  }
  split(graph[outer], graph_elements, ",");
  split(path, path_elements, ",");
  for (graph_element in graph_elements) {
    if (!(graph_elements[graph_element] in path_elements)) {
      next_path = get_path(graph, graph_elements[graph_element], target, path);
      if (next_path != "")
        return next_path;
    }
  }
}

BEGIN{
  FS=","
}

{
  split($1, words, " ")
  outer = words[1] " " words[2]
  delete words
  for (i = 1; i <= NF; i++) {
    word_count = split($i, words, " ");
    inner = words[word_count - 2] " " words[word_count - 1]
    if (inner != "no other") {
      graph[outer] = graph[outer] (graph[outer] ? "," : "") inner;
    }
  }
}

END{
  for (outer in graph) {
    if (get_path(graph, outer, "shiny gold", "")) {
      t++
    }
  }
  print t - 1
}
