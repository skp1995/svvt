import os
import sys
import math
import random

def insertionSort(array):
	for i in range(1, len(array)):
		tmp = 0
		tmp = array[i]
		position = i
		while position > 0 and array[position - 1] > tmp:
			array[position] = array[position - 1]
			position -= 1
		array[position] = tmp

def bucketsort( A ):
  # get hash codes
    code = hashing( A )
    buckets = [list() for _ in range( code[1] )]
  # distribute data into buckets: O(n)
    for i in A:
        x = re_hashing( i, code )
        buck = buckets[x]
        buck.append( i )
 
    for bucket in buckets:
        insertionSort( bucket )
 
    ndx = 0
  # merge the buckets: O(n)
    for b in range( len( buckets ) ):
        for v in buckets[b]:
            A[ndx] = v
            ndx += 1

    return A    
 
def hashing( A ):
    m = A[0]
    for i in range( 1, len( A ) ):
        if ( m < A[i] ):
            m = A[i]
    result = [m, int( math.sqrt( len( A ) ) )]
    return result
 
 
def re_hashing( i, code ):
    return int( i / code[0] * ( code[1] - 1 ) )

#testCaseInput1 = [5.5,1.1,2.2,9.9,3.3,10.1,4.4,7.7,8.8,6.6]
#print(bucketsort(testCaseInput1))

#testCaseInput2 = [1.7, -1.4, 1.2, 1.3, 1.1]
#print(bucketsort(testCaseInput2))

#testCaseInput3 = [8.8, 0, -2, -4.4, 6]
#print(bucketsort(testCaseInput3))

testCaseInput4 = [2,8,3,5,1,7]
print(bucketsort(testCaseInput4))