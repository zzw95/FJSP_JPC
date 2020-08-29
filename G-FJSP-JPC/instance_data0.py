from collections import namedtuple
Jobshop = namedtuple('Jobshop', ['tag','n_orders', 'n_jobs', 'n_ops', 'n_machs', 'orders_vec', 'jobs_vec', 'ops_vec', 'vec_size', 'avail_machs', 'proc_times', 'jobs_prec'])
tag = 'inst0'
n_orders = 2
n_jobs = [5,3]
n_ops = [[2,2,2,3,1], [1,2,3]]
n_machs =6

orders_vec = [0,] *10 + [1, ]*6
jobs_vec= [0, 0, 1, 1, 2, 2, 3, 3, 3, 4,
           0, 1, 1, 2, 2, 2]

ops_vec = list(range(16))

vec_size =16

avail_machs = [[2,3], [0,1], [2,3], [0,1], [0,1], [4,5], [0,1], [2,3], [4,5], [4,5],
               [4,5], [4,5], [2,3], [0,1], [2,3], [4,5]]

proc_times = [[[3,5],[4,6]], [[2,3],[3,4]],
              [[2,3],[3,4]], [[3,4], [4,6]],
              [[2,3],[3,4]], [[3,4],[4,5]],
              [[3,4],[4,5]], [[2,3], [3,5]], [[4,6], [5,6]],
              [[4,5],[5,7]],
              [[3,5],[4,5]],
              [[2,4],[3,5]], [[3,4],[4,6]],
              [[3,5],[4,5]],[[2,3],[3,4]], [[2,3],[3,4]]]

jobs_prec = [[None, None, [0,1], None, [0,1,2,3]],
             [None, None, [0,1]]]

jobshop = Jobshop(tag, n_orders, n_jobs, n_ops, n_machs, orders_vec, jobs_vec, ops_vec, vec_size, avail_machs, proc_times, jobs_prec)


