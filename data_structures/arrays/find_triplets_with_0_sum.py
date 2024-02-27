"""
Given a list of integers, return elements a, b, c such that a + b + c = 0.
Args:
    nums: list of integers
Returns:
    list of lists of integers where sum(each_list) == 0
Examples:
    >>> find_triplets_with_0_sum([-1, 0, 1, 2, -1, -4])
    [[-1, -1, 2], [-1, 0, 1]]
    >>> find_triplets_with_0_sum([])
    []
    >>> find_triplets_with_0_sum([0, 0, 0])
    [[0, 0, 0]]
    >>> find_triplets_with_0_sum([1, 2, 3, 0, -1, -2, -3])
    [[-3, 0, 3], [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
"""

'''
方法一：三层循环https://github.com/TheAlgorithms/Python/blob/master/data_structures/arrays/find_triplets_with_0_sum.py
'''

'''
方法一：利用Hashing的过程来得到结果，在O(n2），涉及遍历数组。对于每个元素 arr[i]，找到总和为“-arr[i]”的对。
这个问题可以简化为对和，并且可以使用散列在 O(n) 时间内解决。

算法： 
1.创建一个 hashmap 来存储一个键值对。
2.运行一个包含两个循环的嵌套循环，外循环从 0 到 n-2，内循环从 i + 1 到 n-1
3.检查第 i 个和第 j 个元素的总和乘以 -1 是否存在于 hashmap 中
4.如果元素存在于哈希图中，则打印三元组，否则将第 j 个元素插入哈希图中。
复杂性分析： 
•时间复杂度： O(n2)。由于需要两个嵌套循环，所以时间复杂度为O(n2)。
•空间复杂度： O(n)。由于需要 hashmap，所以空间复杂度是线性的。
'''



'''
方法3： 该方法使用Sorting得到正确的结果，在O(n2)时间内求解。方法需要额外的空间。对于每个元素，检查是否存在一对其和等于该元素的负值。
算法： 
1.按升序对数组进行排序。
2.从头到尾遍历数组。
3.对于每个索引 i，创建两个变量 l = i + 1 和 r = n – 1
1.如果 array[i]、array[l] 和 array[r] 之和为零，则运行一个循环直到 l 小于 r，然后打印三元组并中断循环
2.如果总和小于零，则增加 l 的值，通过增加 l 的值，总和将随着数组的排序而增加，所以 array[l + 1] > array [l] 
3.如果总和大于零，则减少 r 的值，通过增加 l 的值，总和将随着数组的排序而减少，所以 array[r-1] < array [r].



'''
