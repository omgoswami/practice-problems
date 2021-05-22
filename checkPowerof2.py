# take an integer as input and return whether it is a power of 2
# this implementation uses bits -- if the number is a power of 2, the bit representation will be a leading 1 and then all 0s
# for example, 16 (2^4) is 10000, and 1 less than that, 15, is 01111 --> because there are no common digits in any place value, 16 & 15 == 0
# the n!= 0 is just a fail-safe, because 0 & 0 = 1
class Solution:
  def solve(self, n):
    return (n & (n-1) == 0) and n != 0
