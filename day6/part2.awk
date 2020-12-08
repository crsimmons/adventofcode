BEGIN {
  RS="\n\n"
}

{
  gsub(/\n$/,"")
  split($0, group_answers, "\n");

  for (group_member in group_answers) {
    individual_answers = group_answers[group_member]

    if (group_member == 1) {
      output = individual_answers
      continue
    }

    for (i = 1; i <= length(output); i++) {
      letter = substr(output,i,1)
      if (match(individual_answers,letter) == 0) {
        sub(letter,"",output)
        i--
      }
    }
  }
  sum += length(output)
}

END {
  print sum
}
