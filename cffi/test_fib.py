
pysetup = """
def fib(i):
  if i <= 2: return i
  else: return fib(i-1) + fib(i-2)
"""

import timeit

print timeit.timeit("fib(30)", setup=pysetup, number=1000)

csetup = '''
from cffi import FFI

ffi = FFI()

ffi.cdef("int fib(int i);")

lib = ffi.verify("""
int fib(int i) {
  if (i <= 2) return i;
  else return fib(i-1) + fib(i-2);
}
""")
'''

print timeit.timeit("lib.fib(30)", setup=csetup, number=1000)
