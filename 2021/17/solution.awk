#!/usr/bin/env gawk -f

function abs(k) {return k<0?-k:k}
function ceil(k){return (k==int(k))?k:int(k)+1}

BEGIN{FS=", "}

{
  gsub("target area: ","")
  split(substr($1,3),xa,".")
  split(substr($2,3),ya,".")
  LeftTarget=xa[1]; RightTarget=xa[3]
  BotTarget=ya[1]; TopTarget=ya[3]
}

END{
  # part 1 observations:
  # * max height is always reached at step n=initial y velocity
  # * max height is the triangle number of the step it is reached at (not sure how to prove this)
  # * height arrives at 0 with initial velocity (negated)
  # * last step therefore can have max velocity == the bottom of the target window (BotTarget)
  # * so max height = triangle number of BotTarget-1 = -1 * (BotTarget-1)/2 * (-1 * (BotTarget-1) + 1)
  #   = -BotTarget/2 * (-BotTarget - 1) = BotTarget/2 * (BotTarget + 1)

  print BotTarget*(BotTarget+1)/2

  # part 2 observations:
  # * the target x window in both the example and the input are postitve so we can discount
  #   negative x velocities since they will reach a max coordinate of 0
  # * max x distance reached after initial x velocity steps
  # * sum 0->n of x-n = -1/2 * (n + 1) * (n - 2x) but we actually start decrementing at n=1
  #   so n = n-1. Therefore distance travelled at step n = -1/2 * ((n-1)+1) * ((n-1)-2x)
  #   = -n/2 * (n-1-2x) where x is the absolute value of the starting x velocity
  # * by extension, the max x distance travelled with initial x velocity vx is where x=n=vx
  #   so -vx/2 * (vx-1-2vx) = -vx/2 * (-vx-1) = vx/2 * (vx + 1)
  # * So a good lower bound for vx is one that ulitmately reaches the target
  #   we're approaching from below so we want vx such that vx/2 * (vx + 1)=LeftTarget
  #   vx=1/2 * (±sqrt(8LeftTarget+1)-1) but we can discount the negative in ± as it will always
  #   result in a negative velocity which we ignore

  minx=ceil(0.5 * ((8*LeftTarget+1)**0.5)-1)

  # * max vx = RightTarget because otherwise you will overshoot the target on the first step

  maxx=RightTarget

  # * the whole y target window is negative for both the example and the input
  # * the maximum vy is the one that hits BotTarget on its first step below 0
  #   as seen in part 1 this means max vy = abs(BotTarget)-1

  maxy=abs(BotTarget)-1

  # * min vy is BotTarget as any lower would start below the target

  miny=BotTarget

  for (vx=minx;vx<=maxx;vx++) {
    for (vy=miny;vy<=maxy;vy++) {
      x=0;y=0
      for (n=1;n<=1000;n++) {
        x=n>vx?x:-1*(n/2)*(n-1-(2*vx))
        y=y+vy-n+1
        if (y<BotTarget) break
        if (x>=LeftTarget&&x<=RightTarget&&y<=TopTarget) {
          ++v
          break
        }
      }
    }
  }
  print v
}
