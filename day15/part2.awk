BEGIN{RS=","}

{spoken[$1]=NR}

END{
  turn=NR
  last=$1
  while (++turn<=30000000) {
    count=split(spoken[last],arr,",")
    last=(count-1?arr[count]-arr[count-1]:0)
    newCount=split(spoken[last],arr,",")
    spoken[last]=arr[newCount] (arr[newCount]?",":"") turn
  }
  print last
}
