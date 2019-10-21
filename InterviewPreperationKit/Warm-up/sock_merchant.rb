require 'json'
require 'stringio'

# Complete the sockMerchant function below.
def sockMerchant(n, ar)
    group_by = ar.group_by(&:itself)
    trans_form = group_by.transform_values{ |v| v.size / 2 }
    pairs = trans_form.values.sum
end

n = gets.to_i

ar = gets.rstrip.split(' ').map(&:to_i)

result = sockMerchant n, ar

print result
