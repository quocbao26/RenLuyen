"""
Viết chương trình in tất cả các hoán vị của [1,2,3].
"""
import itertools
lst = [1,2,3]
lst1 = list(itertools.permutations(lst))
print(lst1)
