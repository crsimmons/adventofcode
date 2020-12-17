function abs(  n) {return n < 0 ? -n : n}

function turn(  f,  ox) {
  ox=wx
  if (f==1){wx=(a=="R"?wy:-wy);wy=(a=="R"?-ox:ox)}
  if (f==2){wx=-ox;wy=-wy}
  if (f==3){wx=(a=="R"?-wy:wy);wy=(a=="R"?ox:-ox)}
}

BEGIN{wx=10;wy=1}

{
  a=substr($0,1,1); v=substr($0,2,length($0)-1);
  switch (a) {
    case "N":
      wy+=v
      break
    case "E":
      wx+=v
      break
    case "S":
      wy-=v
      break
    case "W":
      wx-=v
      break
    case "F":
      sx+=wx*v
      sy+=wy*v
      break
    default:
      turn((v/90)%4)
      break
  }
}


END{print abs(sx)+abs(sy)}
