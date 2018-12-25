import numpy as np
sample,spacing=np.linspace(1,10,retstep=True)
print(spacing)
sample,spacing=np.linspace(1,10,20,retstep=True)
print(spacing)
sample,spacing=np.linspace(1,10,20,endpoint=False,retstep=True)
print(spacing)

