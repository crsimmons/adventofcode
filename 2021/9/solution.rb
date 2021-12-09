#!/usr/bin/env ruby

grid = ARGF.readlines.map { |x| x.strip.chars.map(&:to_i) }

maxY = grid.size - 1
maxX = grid[0].size - 1

basin = Hash.new(0)

grid.each_with_index do |row, y_start|
  row.each_with_index do |value, x_start|
    next if value == 9

    nextp = [y_start, x_start]
    while nextp
      y, x = nextp

      nextp = [[1, 0], [0, 1], [-1, 0], [0, -1]]
              .map { |dy, dx| [y + dy, x + dx] }
              .filter { |ny, nx| ny.between?(0, maxY) && nx.between?(0, maxX) }
              .filter { |ny, nx| grid[ny][nx] < grid[y][x] }
              .first
    end
    basin[[y, x]] += 1
  end
end

puts basin.keys.map { |y, x| grid[y][x] + 1 }.sum
puts basin.values.sort[-3..].reduce(:*)
