import random, time
import tabulate


def qsort(a, pivot_fn):
    if len(a) == 0:
      return a 
    else:
      #lambda a: a[0]
      #lambda a: random.choice(a)
      p = pivot_fn(a)
      l = list(filter(lambda x: x < p, a))
      r = list(filter(lambda x: x > p, a))
      left = qsort(l, pivot_fn)
      right = qsort(r, pivot_fn)

    return left + [p] + right 

def randomize(a):
  return random.choice(a)

def fixed(a): 
  return a[0]
    
def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###

def compare_sort(sizes=[10, 100, 200, 300, 400, 500, 600, 700, 800, 900]):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """

    qsort_fixed_pivot = lambda x: qsort(x, fixed) #returns fixed version of qsort
    qsort_random_pivot = lambda x: qsort(x, randomize) #returns randomize version of qsort
    tim_sort = sorted
    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        # shuffles list if needed
        #random.shuffle(mylist)
        result.append([
            len(mylist),
            time_search(qsort_fixed_pivot, mylist),
            time_search(qsort_random_pivot, mylist),
            time_search(tim_sort, mylist)
        ])
    return result
    ###

def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot', 'tim_sort'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
    print_results(compare_sort())

random.seed()
test_print()
