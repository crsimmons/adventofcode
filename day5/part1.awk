function F(front,back){
  nback = back - rshift(back - front, 1)
  return nback
}

function B(front,back){
  nfront = front + rshift(back - front, 1)
  return nfront
}

function R(left,right) {
  nleft = left + rshift(right - left, 1)
  return nleft
}

function L(left,right) {
  nright = right - rshift(right - left, 1)
  return nright
}

function max(arr) {
  m = 0
  for (i in arr) {
    if (m <= arr[i]) {
      m = arr[i]
    }
  }
  return m
}

{
  split($0, chars, "")
  front = 0
  back = 128
  left = 0
  right = 8
  for (i in chars) {
    switch(chars[i]) {
      case "F":
        back = F(front,back)
        break
      case "B":
        front = B(front,back)
        break
      case "R":
        left = R(left,right)
        break
      case "L":
        right = L(left,right)
        break
      default:
        break;
    }
  }
  id = (front * 8) + left
  ids[NR]=id
  # printf "Row: %d, Column: %d, ID: %d\n---\n", front, left, id
}

END {
  print max(ids)
}
