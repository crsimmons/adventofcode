function busDeparts(  o) {
  return $o == "x" || !((t + o - 1) % $o)
}

function getStreak(  streak) {
  for (i=1;i<=NF;i++) {
    if (!busDeparts(i)) {
      return streak
    }
    streak++
  }
  return streak
}

BEGIN{FS=","}

NR>1{
  step=1
  while(streak < NF) {
    t+=step
    streak=getStreak()
    streaks[streak]=streaks[streak] "," t
    if (split(streaks[streak], tmp, ",") >= 3) {
      step = tmp[3] - tmp[2]
    }
  }
  print t
}
