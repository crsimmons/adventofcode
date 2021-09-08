function S(n,_i,_t) {
  for(_i=1;_i<=NF;_i++){
    _t=_t substr($_i,n,1)
  }
  return _t
}

function R(s,_i,_o) {
  for(_i=length(s);_i!=0;_i--){
    _o=_o substr(s,_i,1)
  }
  return _o
}

BEGIN{
  FS=RS
  RS=""
}

{
  gsub(/\./, "~")
  id=substr($1,6,4)
  sub(/[^\n]*\n/,"")
  l=S(1)
  r=S(length($1))
  e[id]=$1"|"R($1)"|"$NF"|"R($NF)"|"l"|"R(l)"|"r"|"R(r)
}

END{
  FS=" "
  p1=1
  for(id in e){
    for(j in e){
      if(id!=j&&e[j]~e[id]){
        # printf("j: %s, id: %s\ne[j]:  %s\ne[id]: %s\n", j, id, e[j], e[id])
        O[id]=O[id]" "j
        # printf("O[id]: %s, split: %s\n",O[id],split(O[id],_))
      }
    }
    if(split(O[id],_)==2){
      p1*=id
    }
  }
  printf("part1: %s\n",p1)
}
