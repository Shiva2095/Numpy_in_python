import numpy as np
m=np.array([ [1,2,3,4],
             [5,6,7,8],
             [11,33,22,44],
             [22,33,44,55] ])
reverse=m[::-1,::-1]
print(m)
print(reverse)
print(m[1:-1,1:-1])
