function lPad(v) {if (length(v) < 36){return lPad(0 v)}return v}
function d2b(d,  b) {while(d) {b=d%2b;d=int(d/2)}return(lPad(b))}
function b2d(b,  d) {for(i=1;i<=length(b);i++){d+=substr(b,i,1)*(2^(length(b)-i))}return(d)}

function applyMask(v,  o) {
  for (i=1;i<=36;i++) {
    n=substr(v,i,1)
    m=substr(mask,i,1)
    o=o (m=="0"?n:m)
  }
  return o
}

function floating(v,  l) {
  if (!index(v, "X"))
    return v;
  tmp = v;
  sub(/X/,0,tmp);
  l=l (l?",":"") floating(tmp);
  sub(/X/,1,v);
  l=l (l?",":"") floating(v);
  return l;
}

BEGIN{FS=" = "}

{
  if ($1=="mask") {mask=$2}
  else {
    addr=substr($1,5,length($1)-5)
    maskedAddr=applyMask(lPad(d2b(addr)))
    floatingAddrs=floating(maskedAddr)
    split(floatingAddrs,addrs,",")
    for (a in addrs) {
      mem[addrs[a]]=$2
    }
  }
}

END {
  for (a in mem) {sum += mem[a]}
  print sum
}
