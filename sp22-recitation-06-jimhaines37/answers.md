# CMPS 2200 Reciation 6
## Answers

**Name:**_________________________


Place all written answers from `recitation-06.md` here for easier grading.

Perform two different comparisons: a comparison between sorting methods using random permutations of the specified sizes, and a comparison using already sorted permutations. How do the running times compare to the asymptotic bounds? How does changing the type of input list change the relative performance of these algorithms?

- **1b.**

Sorted:

|   n |   qsort-fixed-pivot |   qsort-random-pivot |
|-----|---------------------|----------------------|
|  10 |               0.075 |                0.086 |
| 100 |               4.164 |                0.464 |
| 200 |               4.553 |                0.877 |
| 300 |               9.590 |                1.308 |
| 400 |              17.621 |                1.994 |
| 500 |              26.731 |                2.461 |
| 600 |              40.732 |                2.808 |
| 700 |              52.291 |                3.470 |
| 800 |              75.920 |                4.029 |
| 900 |              89.697 |                6.902 |



Random Order: 

|   n |   qsort-fixed-pivot |   qsort-random-pivot |
|-----|---------------------|----------------------|
|  10 |               0.037 |                0.039 |
| 100 |               0.351 |                0.399 |
| 200 |               0.717 |                0.991 |
| 300 |               1.089 |                1.839 |
| 400 |               1.510 |                2.086 |
| 500 |               2.144 |                2.645 |
| 600 |               5.430 |                6.175 |
| 700 |               2.887 |                4.050 |
| 800 |               3.119 |                3.963 |
| 900 |               4.298 |                5.096 |


We can see that using a sorted list and a fixed pivot (the first value in the list) is very inefficient and takes up a lot of runtime as the input size increases.

When the list is randomized or the pivot value is randomized we experience much better runtimes. My sample sizes are relatively small so it is not easy to see the trend on how they increase, but they are all comparable in terms of runtime and have much lower runtime than the fixed pivot sorted list.







- **1c.**

Sorted:

|   n |   qsort-fixed-pivot |   qsort-random-pivot |   tim_sort |
|-----|---------------------|----------------------|------------|
|  10 |               0.087 |                0.049 |      0.003 |
| 100 |               1.291 |                0.474 |      0.004 |
| 200 |               9.001 |                2.249 |      0.008 |
| 300 |              10.227 |                1.592 |      0.007 |
| 400 |              18.561 |                1.979 |      0.008 |
| 500 |              29.431 |                2.326 |      0.009 |
| 600 |              40.288 |                2.926 |      0.010 |
| 700 |              54.617 |                3.464 |      0.010 |
| 800 |              79.534 |                4.356 |      0.013 |
| 900 |              97.409 |                4.767 |      0.011 |




Random Order:


|   n |   qsort-fixed-pivot |   qsort-random-pivot |   tim_sort |
|-----|---------------------|----------------------|------------|
|  10 |               0.060 |                0.074 |      0.004 |
| 100 |               0.600 |                2.497 |      0.015 |
| 200 |               1.191 |                1.036 |      0.024 |
| 300 |               1.119 |                1.383 |      0.036 |
| 400 |               1.514 |                1.939 |      0.041 |
| 500 |               1.943 |                2.396 |      0.052 |
| 600 |               2.224 |                2.877 |      0.066 |
| 700 |               2.855 |                3.386 |      0.079 |
| 800 |               3.232 |                4.518 |      0.120 |
| 900 |               3.792 |                4.640 |      0.102 |

Here, we experience similar results to 1b. The fixed pivot sorted list gives by far the worst runtimes because it is so inefficient. The other qsort functions still produce similar runtimes that are much lower than the sorted fixed pivor list. Tim_sort however provides by far the best runtimes for both sorted and randomized list, so we know our version of qsort still has some ineffiencies.
