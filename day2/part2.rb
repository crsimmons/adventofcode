#!/usr/bin/env ruby

input = File.read('input.txt')

valid = 0

input.each_line do |line|
  parts = line.split(' ')
  p1, p2 = parts[0].split('-').map!(&:to_i)
  letter = parts[1].delete_suffix(':')
  password = parts[2]

  valid += 1 if (password[p1-1] == letter) ^ (password[p2-1] == letter)
end

puts valid
