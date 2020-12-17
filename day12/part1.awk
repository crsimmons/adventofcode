function abs(  n) {return n < 0 ? -n : n}

function turn(  f,  ox) {
  ox=xinc
  if (f==1){xinc=(a=="R"?yinc:-yinc);yinc=(a=="R"?-ox:ox)}
  if (f==2){xinc=-ox;yinc=-yinc}
  if (f==3){xinc=(a=="R"?-yinc:yinc);yinc=(a=="R"?ox:-ox)}
}

BEGIN{xinc=1;yinc=0}

{
  a=substr($0,1,1); v=substr($0,2,length($0)-1);
  switch (a) {
    case "N":
      y+=v
      break
    case "E":
      x+=v
      break
    case "S":
      y-=v
      break
    case "W":
      x-=v
      break
    case "F":
      x+=xinc*v
      y+=yinc*v
      break
    default:
      turn((v/90)%4)
      break
  }
}


END{print abs(x)+abs(y)}
