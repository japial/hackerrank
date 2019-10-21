require 'json'
require 'stringio'

# Complete the countingValleys function below.
def countingValleys(n, s)
    steps = s.split('')
    sea = 0
    valley = 0
    steps.each do |item|
        if item == 'U'
            sea += 1
        else
            sea -= 1
        end

        if sea == 0 and item == 'U'
            valley += 1
        end
    end
    return valley
end

n = gets.to_i

s = gets.to_s.rstrip

result = countingValleys n, s

print result
