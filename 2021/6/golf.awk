#!/usr/bin/env gawk -f

# part 1: l=80
# part 2: l=256
BEGIN{RS=",";l=256}{a[$0]++}END{for (;++d<l;)a[(d+7)%9]+=a[d%9];for (x in a)r+=a[x];print r}

# I got this solution from the reddit thread. It took a while to grok
# Basically instead of mutating the array you mutate the index while the array
# acts as a sliding window on the 0-8 (7 day) age range of the fish

# In the example we start with (sorted)
# 1,2,3,3,4
# which in dictionary form is:
# 0,1,1,2,1,0,0,0,0 (0 0th day fish, 1 1st day fish, 2 3rd day fish, etc)

# In my original part 2 solution I manipulate the array where each time some fish
# reach 0 on their timer they get added to the number of fish with 6 day timers
# and they also spawn one 8 day timer fish each. Otherwise all timers are decremented.
# So the first two iterations are:

# 1,1,2,1,0,0,0,0,0 - decrement timers
# 1,2,1,0,0,0,1,0,1 - the 1 fish at 0 moves to 6 and spawns a fish at 8

# This approach requires modifying the whole array (especially in awk) on each iteration

# The reddit magic approach instead opts to do one index operation per iteration.

# Starting with our initial dictionary taking note of which index represents the 0th day fish:
# 0,1,1,2,1,0,0,0,0
# ^

# On the first day there are no fish with timer 0 so no new fish are spawned. We don't change
# the array but rather move the index indicating the 0th day fish:
# 0,1,1,2,1,0,0,0,0
#   ^
# Effectively the 0th day fish have become the 8th day fish as the window has moved

# On the second day there is one fish that will spawn a new fish. Using our array manipulation
# rules in addition to the sliding window the next dicitonary representation is:
# 0,1,1,2,1,0,0,0,1
#     ^

# This array now reads left to right as:
# - 0 7th day fish
# - 1 8th day fish
# - 1 0th day fish
# - 2 1st day fish
# etc

# Or, written with the original window: 1,2,1,0,0,0,1,0,1 which matches our second iteration above.

# So the question is how do we achieve these numbers through only index manipulation?

# By incorporating the day (d) into our index calculations that will take care of shifting the
# window by one each iteration.

# Let's look at the magic line: a[(d+7)%9]+=a[d%9]
# a is the dictionary
# d is the iterator in the loop representing the number of days that have passed

# In the first iteration d=0 and a=[0,1,1,2,1,0,0,0,0]
# The calculation tells us to add the value at index d%9=0%9=0 to the value at (d+7)%9=7%9=7
# This means we set a[7]=a[7]+a[0]=0+0=0
# Note that a[0] is the location of our 0th day fish index at the start of this iteration
# We added 0 to 0 so no numbers in the dictionary changed

# Moving on to the second iteration we now have d=1 and a=[0,1,1,2,1,0,0,0,0]
# Now we do a[(d+7)%9]=a[(d+7)%9]+a[d%9] -> a[8%9]=a[8%9]+a[1%9] -> a[8]=a[8]+a[1]=0+1
# After this operation we have a=[0,1,1,2,1,0,0,0,1]

# By shifting the window every iteration we effectively get the 0 -> 8 spawning for free
# since day 0 in one cycle becomes day 8 in the next
# This means the modulo operation is taking care of the 0th fish resetting to 6th fish
# d%9 will always be the location of the 0th day fish index
# (d+7)%9 is the location of the 6th day fish
# It's +7 because we do the array operation then the window slides over effectively decrementing
# the index that we just wrote to before it gets fed into the next iteration.
