
require 'json'
require 'stringio'

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c)
    i = 0
    jump = 0
    while i < c.length-1
        if i < c.length and c[i+2] != 1
          jump += 1
          i += 2
        else
          jump += 1
          i += 1
        end
    end
    return jump
end

n = gets.to_i

c = gets.rstrip.split(' ').map(&:to_i)

result = jumpingOnClouds c

print result
