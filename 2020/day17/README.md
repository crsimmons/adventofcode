# Day17

`awk` doesn't initialize arrays with anything so I needed to create an array of dots large enough to contain the permuations but not so large as to take forever to calculate. I basically brute forced the correct offset value by incrementing it until the sum stopped increasing.

[This](https://rosettacode.org/wiki/Conway%27s_Game_of_Life#AWK) was pretty helpful.
