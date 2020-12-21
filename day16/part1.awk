BEGIN{RS=" |[a-z]|\n";FS="[,-]"}
/-/{for(i=$1;i<=$2;i++)v[i]++}
/,/&&++n>1{for(i=1;i<=NF;i++)s+=v[$i]?0:$i}
END{print s}
