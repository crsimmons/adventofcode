#!/usr/bin/env ruby

$grid = ARGF.readlines.map { |x| x.strip.chars.map(&:to_i) }
$p1 = 0

def flash(r, c)
  $p1 += 1
  $grid[r][c] = -1
  [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]]
    .map { |dr, dc| [r + dr, c + dc] }
    .filter { |nr, nc| nr.between?(0, R - 1) && nc.between?(0, C - 1) }
    .each do |nr, nc|
    next unless $grid[nr][nc] != -1

    $grid[nr][nc] += 1
    flash(nr, nc) if $grid[nr][nc] >= 10
  end
end

R = $grid.size
C = $grid[0].size

p2 = 0
loop do
  p2 += 1

  $grid.each { |row| row.map! { |e| e += 1 } }

  (0...R).each do |r|
    (0...C).each do |c|
      flash(r, c) if $grid[r][c] >= 10
    end
  end
  (0...R).each do |r|
    (0...C).each do |c|
      $grid[r][c] = 0 if $grid[r][c] == -1
    end
  end
  puts $p1 if p2 == 100
  break if $grid.flatten.all? { |e| e == 0 }
end

puts p2
