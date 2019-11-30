from collections import namedtuple
Jobshop = namedtuple('Jobshop', ['tag', 'n_orders', 'n_jobs', 'n_ops', 'n_machs', 'orders_vec', 'jobs_vec', 'ops_vec', 'vec_size', 'avail_machs', 'proc_times', 'jobs_prec'])
tag = 'inst1'
n_orders = 4
n_jobs = [6,6,6,6]
n_ops = [[1,1,3,1,1,1], [1,1,1,1,3,1], [1,1,3,1,1,1], [1,1,1,1,3,1]]
n_machs =5

orders_vec = [0,] *8 + [1, ]*8 + [2, ]*8 + [3, ]*8
jobs_vec= [0, 1, 2, 2, 2, 3, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 2, 2, 3, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5]
ops_vec = list(range(32))

vec_size =32

avail_machs = [[0,1], [2,3], [0,1], [0,1], [2,3], [2,3], [2,3], [4],
               [0,1], [2,3], [2,3], [2,3], [0,1], [0,1], [2,3], [4],
               [0,1], [2,3], [0,1], [0,1], [2,3], [2,3], [2,3], [4],
               [0,1], [2,3], [2,3], [2,3], [0,1], [0,1], [2,3], [4]]

proc_times = [[100, 110], [250,275], [150,164], [235, 252], [242, 260], [251, 270], [400, 440], [750],
              [50, 55], [150, 162], [75, 88], [150, 165], [204, 222], [174, 188], [225, 240], [225],
              [60, 65], [300, 322], [300, 322], [410, 420], [300, 328], [170, 184], [280,300], [300],
              [70, 78], [250, 272], [125, 138], [238, 250], [375, 390], [365, 382], [245, 262], [375]]

jobs_prec = [[None, None, None, None, [0,1], [0,1,2,3,4]],
             [None, None, None, [0,1], None, [0,1,2,3,4]],
             [None, None, None, None, [0,1], [0,1,2,3,4]],
             [None, None, None, [0,1], None, [0,1,2,3,4]]]

jobshop = Jobshop(tag, n_orders, n_jobs, n_ops, n_machs, orders_vec, jobs_vec, ops_vec, vec_size, avail_machs, proc_times, jobs_prec)


