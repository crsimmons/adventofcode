#!/usr/bin/env gawk -f

BEGIN { p=50 }

{ split($0,a,/[LR]/,s); d=s[1]=="L"?-1:1; while(a[2]--) {p=(p+d)%100; if (p==0) p2++} if (p==0) p1++ }

END { print p1, p2 }
