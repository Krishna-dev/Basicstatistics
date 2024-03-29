import pandas as pd
import numpy as np
from scipy import stats

n = int(input())
a = np.array(input().split())
a = a.astype(np.int32)

mean = np.mean(a)
sigma = np.std(a)
medi = np.median(a)
mod = stats.mode(a)
ci = stats.norm.interval(0.950004, loc=mean, scale=sigma/np.sqrt(n))
print("%.1f"%mean)
print("%.1f"%medi)
print("%.0f"%mod[0][0])
print("%.1f"%sigma)
print("%.1f %.1f"%(ci[0],ci[1]))
