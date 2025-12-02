#!/usr/bin/env gawk -f

BEGIN{RS=",";FS="-"}

{
  for(x=$1;x<=$2;x++){
      s=x"";l=length(s);
      if(l<2)continue;
      if(l%2==0&&substr(s,1,l/2)==substr(s,l/2+1))p1+=x;
      for(i=1;i<=l/2;i++)if(l%i==0&&substr(s,1,l-i)==substr(s,i+1)){p2+=x;break}
    }
}

END{print p1+0,p2+0}
