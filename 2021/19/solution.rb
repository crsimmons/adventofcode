#!/usr/bin/env ruby

require 'set'

# Combine two transformations into one
def compose(t1, t2)
  transform = []
  (0..2).each do |i|
    row = []
    (0..2).each do |j|
      row.push(
        t1[i][0] * t2[0][j] +
        t1[i][1] * t2[1][j] +
        t1[i][2] * t2[2][j]
      )
    end
    transform.push(row)
  end
  transform
end

# https://en.wikipedia.org/wiki/Determinant
def determinant(arr)
  arr[0][0] * (arr[1][1] * arr[2][2] - arr[1][2] * arr[2][1]) +
    arr[0][1] * (arr[1][2] * arr[2][0] - arr[1][0] * arr[2][2]) +
    arr[0][2] * (arr[1][0] * arr[2][1] - arr[1][1] * arr[2][0])
end

# Create 3x3 matrices for coordinate remaps
def build_remaps
  remaps = []
  [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]].each do |permute|
    remap = []
    (0..2).each do |i|
      row = [0, 0, 0]
      row[permute[i]] = 1
      remap.push(row)
    end
    remaps.push(remap)
  end
  remaps
end

# Create 3x3 matrices for coordinate negations
def build_negations
  negations = []
  (-1..1).each do |i|
    (-1..1).each do |j|
      (-1..1).each do |k|
        negations.push([[i, 0, 0], [0, j, 0], [0, 0, k]])
      end
    end
  end
  negations
end

# Create 3x3 matrices for all 24 possible transformations
# this is the 6 remaps combined with sign-flipping each coordinate
# 6*2*2*2=48 but half have the wrong "handedness" or chirality so
# we take the ones with a determinant of 1
# https://docs.microsoft.com/en-us/windows/win32/direct3d9/coordinate-systems
def build_transformations(remaps, negations)
  transformations = []
  remaps.each do |remap|
    negations.each do |negation|
      composed = compose(remap, negation)
      transformations.push(composed) if determinant(composed) == 1
    end
  end
  transformations
end

# Apply the transformation to the coordinate
def transform_coord(coord, transformation)
  result = []
  (0..2).each do |i|
    result.push(coord[0] * transformation[i][0] + coord[1] * transformation[i][1] + coord[2] * transformation[i][2])
  end
  result
end

# Apply the transformation to the scanner
def transform(scanner, transformation)
  result = []
  scanner.each do |coord|
    result.push(transform_coord(coord, transformation))
  end
  result
end

# Compare two scanners by calculating the difference between
# each beacon's coordinates. This difference shows the position
# of the second scanner relative to the first based on a common
# beacon. If we find the requisite 12 common beacons we return
# the correlation vector else nil.
def check_correlation(scanner1, scanner2)
  freqs = Hash.new 0
  scanner1.each do |coord1|
    scanner2.each do |coord2|
      diff = [coord2[0] - coord1[0], coord2[1] - coord1[1], coord2[2] - coord1[2]]
      freqs[diff.to_s] += 1
      next unless freqs[diff.to_s] == 12

      return diff
    end
  end
  nil
end

# Modify the provided scanner according to the correlation vector.
# This orients the scanner's beacon list so it aligns with the one
# with which it is correlated.
def normalise(scanner, correlation)
  scanner.map do |beacon|
    beacon[0] -= correlation[0]
    beacon[1] -= correlation[1]
    beacon[2] -= correlation[2]
  end
  scanner
end

# Now that all scanners have been normalised we can take the
# coordinates of each beacon seen by each scanner and compute
# the number of unique ones.
def part1(scanners)
  unique = Set.new
  scanners.each do |scanner|
    scanner.each do |beacon|
      unique.add(beacon.to_s)
    end
  end
  puts unique.length
end

# The correlation vector is the position of each scanner relative
# to the one at [0,0,0] (scanner 0). So we calculate the Manhattan
# distance of each one relative to each other and print the largest one
def part2(correlation)
  max_distance = -1
  (0..correlation.length - 1).each do |i|
    (i + 1..correlation.length - 1).each do |j|
      dist = (correlation[i][0] - correlation[j][0]).abs +
             (correlation[i][1] - correlation[j][1]).abs +
             (correlation[i][2] - correlation[j][2]).abs
      max_distance = dist > max_distance ? dist : max_distance
    end
  end
  puts max_distance
end

data = ARGF.read.strip.split("\n\n")

scanners = []
data.each do |scanner|
  beacon = []
  scanner.split("\n").each do |line|
    line = line.strip
    next if line.start_with?('--')

    x, y, z = line.split(',').map(&:to_i)
    beacon.push([x, y, z])
  end
  scanners.push(beacon)
end

remaps = build_remaps
negations = build_negations
transformations = build_transformations(remaps, negations)

diff_from_0 = Array.new(scanners.length)
diff_from_0[0] = [0, 0, 0]

queue = [0]

until queue.empty?
  queue_index = queue.pop
  base = scanners[queue_index]
  scanners.each_with_index do |scanner, j|
    next unless diff_from_0[j].nil?

    transformations.each do |transformation|
      transformed = transform(scanner, transformation)
      correlation = check_correlation(base, transformed)
      next if correlation.nil?

      puts "Found correlation of scanner #{queue_index} with scanner #{j} = #{correlation}"
      scanners[j] = normalise(transformed, correlation)
      diff_from_0[j] = correlation
      queue.push(j)
    end
  end
end

part1(scanners)
part2(diff_from_0)
