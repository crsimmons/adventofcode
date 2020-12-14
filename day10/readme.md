# Part 2 - My head hurts

`a[n] = k` is read as "there are `k` possible combinations to reach `n` jolts"

If `n - (n-1) == 1` then the adapter `n` can extend the totals of all the combinations currently ending at `n-1`, `n-2`, and `n-3`. Thus the total number of combinations to reach `n+3` increases by the sum of the cobinations to those totals.

If `n - (n-1) == 3` then the adapter `n` can only extend the total of the combination currently ending at `n-3`. Thus the total number of combinations stays the same.
