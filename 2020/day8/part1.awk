{
  cmd[++i] = $1
  val[i] = $2
}

END{
  while(++line) {
    if (visited[line]) {
      print total
      break
    }
    visited[line] = 1
    if (cmd[line] == "acc") {
      total += val[line]
    }
    if (cmd[line] == "jmp") {
      line += --val[line]
    }
  }
}
