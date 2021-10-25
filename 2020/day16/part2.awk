function validTicket() {
  for (field=1;field<=NF;field++) {
    if (!validValue[$field]) return 0
  }
  return 1
}

function determineValid() {
  for(i=$2;i<=$3;i++) {
    valid[$1][i]++
    validValue[i]++
  }
  for(i=$4;i<=$5;i++) {
    valid[$1][i]++
    validValue[i]++
  }
}

function nearbyTickets() {
  for (field=1;field<=NF;field++) {
    nearby[field][$field]++
    for (rule in valid) {
      if (!valid[rule][$field]) {
        bad[field][rule]++
      }
    }
  }
}

function findPossibleMappings() {
  for (field=1;field<=NF;field++) {
    for (rule in valid) {
      invalid = 0
      if (length(bad[field])) {
        for (badRule in bad[field]) {
          if (rule == badRule) {
            invalid++
            break
          }
        }
      }
      if (!invalid) {
        possibilities[field][rule]++
      }
    }
  }
}

function findMappings() {
  while (mapped < NF) {
    for (field=1;field<=NF;field++) {
      if (!mapping[field] && length(possibilities[field]) == 1) {
        for (rule in possibilities[field]) {
          mapping[field] = rule
        }
        for (otherField=1;otherField<=NF;otherField++) {
          if (otherField != field) {
            delete possibilities[otherField][rule]
          }
        }
        mapped++
      }
    }
  }
}

function findProduct() {
  product=1
  for (field in mapping) {
    if (mapping[field] ~ /^departure/) {
      product*=ownTicket[field]
    }
  }
  print product
}

BEGIN{FS="[,-]| or |: "}

/-/{determineValid()}
/,/ && !n++ {for(i=1;i<=NF;i++) ownTicket[i]=$i}
/,/ && n && validTicket() {nearbyTickets()}

END{
  findPossibleMappings()
  findMappings()
  findProduct()
}
