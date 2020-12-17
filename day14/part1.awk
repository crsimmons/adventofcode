function lPad(v) {if (length(v) < 36){return lPad(0 v)}return v}
function d2b(d,  b) {while(d) {b=d%2b;d=int(d/2)}return(lPad(b))}
function b2d(b,  d) {for(i=1;i<=length(b);i++){d+=substr(b,i,1)*(2^(length(b)-i))}return(d)}

function applyMask(v,  o) {
  for (i=1;i<=36;i++) {
    n=substr(v,i,1)
    m=substr(mask,i,1)
    o=o (m=="X"?n:m)
  }
  return o
}

BEGIN{FS=" = "}

{
  if ($1=="mask") {mask=$2}
  else {
    mem[substr($1,5,length($1)-5)]=b2d(applyMask(d2b($2)))
  }
}

END {
  for (a in mem) {sum += mem[a]}
  print sum
}
