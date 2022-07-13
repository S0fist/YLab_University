# Запоминает и выводит значения.
def memoize(function):
  memo = {}
  def wrapper(*args):
    if args in memo:
      return f'{memo[args]} кэш'
    else:
      rv = function(*args)
      memo[args] = rv
      return f'{rv} запись в кэш'
  return wrapper

@memoize
def multiplier(number: int):
    return number * 2


if __name__ == "__main__":
    print(f'{multiplier(2)}')
    print(f'{multiplier(2)}')
    print(f'{multiplier(2)}')
    print(f'{multiplier(2)}')
