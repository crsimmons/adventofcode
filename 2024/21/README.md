# 21

The downstream bots (away from the numeric pad) always have to return to the A button. This effectively resets their position, so we can chunk the solve.

For any two buttons on a pad, there's a specific shortest path that is always best with respect to the downstream bots.

- First, always prefer the path with the fewest turns. For going from 9 to 1 on the numeric pad, for example, prefer `<<vv` to something like `<v<v`. The path length at this level is the same, but it incurs extra movement for the downstream bots.

  - `<` is rather expensive for downstream bots since they also need to go < to reach it and it's the furthest away key. Once a bot has reached the < key, the only moves that it needs to make to hit any other key are > and ^, both of which are right next to the A key for the downstream bot keeping the downstream bot's sequence shorter.

    For example, let's say you're comparing `v<A` vs `<vA`. Both of them move the same amount, but the cost will change a lot for downstream bots!

    `v<A` starts "closer" to A and moves out. To do that, the downstream bot needs to output a < in two separate groups. For example: `v<A<A>>^A`. Compare that to `<vA` (starting "further" from A and moving in) which can be achieved with the < moves grouped together: `v<<A>A>^A`. These paths are the same length, but since it takes 3 moves to reach the < key but only one to reach either > or ^, the bundling of < moves is more important!

    Let's go another level: If we expand the "in to out" group we might see `v<A<A>>^Av<<A>>^AvAA<^A>A`, 25 keypresses. If we expand the "out to in" group then we might see `v<A<AA>>^AvA^AvA^<A>A`, 21 keypresses. It takes a couple levels but making a downstream bot go to the `<` key repeatedly will eventually blow up!

- All else being the same, prioritize moving < over ^ over v over >. I found this through trial and error.
- Given the existence of an always optimal route, we don't need to try different paths DFS style.
