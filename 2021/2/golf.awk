#!/usr/bin/env awk -f

/f/{h+=$2;d+=a*$2};/u/{a-=$2};/n/{a+=$2}END{print h*a,h*d}
