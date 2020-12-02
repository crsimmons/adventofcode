#!/usr/bin/env ruby

input = File.read('input.txt')

valid = 0

input.each_line do |line|
  parts = line.split(' ')
  min, max = parts[0].split('-').map!(&:to_i)
  letter = parts[1].delete_suffix(':')
  password = parts[2]

  valid += 1 if password.count(letter).between?(min, max)
end

puts valid
