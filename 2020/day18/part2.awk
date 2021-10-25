{e=sprintf("awk \"BEGIN {printf(" sprintf("(%s)", gensub("*",")*(","g")) ")}\""); e | getline o;close(e); s+=o}
END{print s}
