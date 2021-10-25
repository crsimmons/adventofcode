function follow(line, total,   visited) {
  while (!visited[line] && line <= NR) {
    visited[line] = 1
    if (cmd[line] == "acc") {
      total += val[line]
    }
    if (cmd[line] == "jmp") {
      line += val[line] - 1
    }
    line++
  }
  if (line > NR) print total
}

{
  cmd[++i] = $1
  val[i] = $2
  if ($1 == "jmp") jmp[i] = $2
  if ($1 == "nop") nop[i] = $2
}

END{
  for (line in nop) {
    cmd[line] = "jmp"
    follow(1, 0)
    cmd[line] = "nop"
  }
  for (line in jmp) {
    cmd[line] = "nop"
    follow(1, 0)
    cmd[line] = "jmp"
  }
}
