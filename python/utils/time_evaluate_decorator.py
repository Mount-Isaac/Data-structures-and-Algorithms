#decorator function which is used to measure the Tn of each algorithm
import time

def time_it(func):
  def wrapper(*args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    print(f'{func.__name__} took {str((end-start) * 1000)} milliseconds')
    return result
  return wrapper
