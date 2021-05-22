#take an integer as input and return the base 3 notation of that integer
def solve(n):
  s = ''
  while n >= 3:
    s = str(n%3) + s
    n = n//3
  return str(n)+s
