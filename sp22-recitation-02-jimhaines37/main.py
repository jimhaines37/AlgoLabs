"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
###

def simple_work_calc(n, a, b):
  if n == 1: 
    return 1 
  else if n == 0:
    return 0
  else: 
    return a*simple_work_calc(n//b, a, b) + n 
pass

	"""Compute the value of the recurrence $W(n) = aW(n/b) + n

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor

	Returns: the value of W(n).
	"""
	# TODO
  #a = number of child nodes 
  #where b is the work of each node
  #go until last nodes are equal to 1??
  #use // for floor devision
  # return a * simple_work_calc(n//b, a, b) + f(n)??\
  #if n//b = 1, return 1, so stop the recursion 
  #also account for case where value of last node is 0, should return 0
  

def test_simple_work():
	""" done. """
	assert work_calc(10, 2, 2) == 36
  	assert work_calc(12, 4, 2) == 148
	assert work_calc(20, 3, 2) == 230
	assert work_calc(30, 4, 2) == 650
  	assert work_calc(40, 2, 4) == 68

def work_calc(n, a, b, f):
  if n == 1:
    return 1
  elif n == 0:
    return 0
  else: return a*work_calc(n//b, a, b, f) + f(n)
pass
  
	"""Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	
	

def span_calc(n, a, b, f):
  if n == 1:
    return 1
  elif n == 0:
    return 0
  else: return work_calc(n//b, a, b, f) + f(n)
pass

	"""Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""


def test_work():
	""" done. """
	assert work_calc(10, 2, 2,lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300
  	assert work_calc(40, 2, 3, lambda n: n) == 90
  	assert work_calc(50, 3, 4, lambda n: n) == 113
  	assert work_calc(40, 2, 3, lambda n: 3*n) == 254
  #lambda x : x^2, just an easier way to define a function 

def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
  result = []
	for n in sizes:
		result.append((
			n,
			work_fn1(n),
			work_fn2(n)
			))
	return result

  """
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
  
	

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_work(sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
  result = []

  work_fn1 = lambda n: work_calc(n, 4, 2, lambda n: n)
  work_fn2 = lambda n: work_calc(n, 4, 2, lambda n: n*n)
    
  res = compare_work(work_fn1, work_fn2)
	print_results(res)

	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work
    
	# create work_fn1
	# create work_fn2
  #Dont need assert statements, just make sure the work outputs are corrcet when printed

  

def compare_span(span_fn1, span_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
  result = []
	for n in sizes:
		result.append((
			n,
			span_fn1(n),
			span_fn2(n)
			))
	return result


def test_compare_span():
  result = []

  span_fn1 = lambda n: span_calc(n, 4, 2, lambda n: n)
  span_fn2 = lambda n: span_calc(n, 4, 2, lambda n: n*n)
    
  res = compare_span(span_fn1, span_fn2)
	print_results(res)
