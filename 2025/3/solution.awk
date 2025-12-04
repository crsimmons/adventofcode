#!/usr/bin/env gawk -f

function P(a,i,n){return(r=match(a,i".{"n+1"}"))?i P(substr(a,r+1),9x,n-1):i?P(a,--i,n):m}

{A+=P(b=P($0,9x,10),9x,0);B+=b}

END{print A,B}
