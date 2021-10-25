function bags(graph, target,   graph_elements,   colour_count,   total) {
  _ = split(graph[target], graph_elements, ",");
  if (graph[target] == "")
    return 0
  for (graph_element in graph_elements) {
    split(graph_elements[graph_element], colour_count, "#");
    total += colour_count[2] + colour_count[2] * bags(graph, colour_count[1])
  }
  return total;
}

BEGIN{
  FS=","
}

{
  split($1, words, " ");
  outer = words[1] " " words[2]
  delete words
  for (i = 1; i <= NF; i++) {
    word_count = split($i, words, " ");
    inner = words[word_count - 2] " " words[word_count - 1];
    bag_count = words[word_count - 3];
    if (inner != "no other")
      graph[outer] = graph[outer] (graph[outer] ? "," : "") inner "#" bag_count;
  }
}

END{
  print bags(graph, "shiny gold")
}
