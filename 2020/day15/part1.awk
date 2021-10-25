BEGIN{RS=","}

{spoken[$1]=NR}

END{
  turn=NR
  last=$1
  while (++turn<=2020) {
    count=split(spoken[last],arr,",")
    last=(count-1?arr[count]-arr[count-1]:0)
    spoken[last]=spoken[last] (spoken[last]?",":"") turn
  }
  print last
}
