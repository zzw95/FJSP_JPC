from collections import namedtuple
Jobshop = namedtuple('Jobshop', ['tag', 'n_orders', 'n_jobs', 'n_ops', 'n_machs', 'orders_vec', 'jobs_vec', 'ops_vec', 'vec_size', 'avail_machs', 'proc_times', 'jobs_prec'])
tag = 'inst5'
n_orders = 8
n_jobs = [6, 6, 6, 6, 6, 6, 6, 8]
n_ops = [[1,1,1,1,3,1], [1,1,1,1,3,1], [1,1,1,1,3,1], [1,1,1,1,3,1], [1,1,1,1,3,1], [1,1,1,2,3,1], [1,1,1,2,3,1], [1,1,1,1,3,2,2,1]]
n_machs = 7

orders_vec = [0,] *8 + [1, ]*8 + [2, ]*8 + [3, ]*8 + [4, ]*8 + [5, ]*9 + [6,]*9 + [7,] *12
jobs_vec= [0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5, 5, 6, 6, 7]

ops_vec = list(range(70))

vec_size = 70

avail_machs = [[4,5], [0,1], [4,5], [4,5], [0,1], [2,3], [2,3], [6],
               [4,5], [0,1], [4,5], [4,5], [0,1], [2,3], [2,3], [6],
               [4,5], [0,1], [4,5], [4,5], [0,1], [2,3], [2,3], [6],
               [4,5], [0,1], [4,5], [4,5], [0,1], [2,3], [2,3], [6],
               [4,5], [0,1], [4,5], [4,5], [0,1], [2,3], [2,3], [6],
               [4,5], [0,1], [4,5], [4,5], [6], [0,1], [2,3], [2,3], [6],
               [4,5], [0,1], [4,5], [4,5], [6], [0,1], [2,3], [2,3], [6],
               [4,5], [0,1], [4,5], [4,5], [0,1], [2,3], [6], [0,1], [4,5], [2,3], [4,5], [6]]

proc_times = [[108,116], [60,65], [125,135], [200,212], [122,138], [145,158], [152,166],[255],
              [256,278], [90,96], [175,188], [240,260], [300,320], [248,265], [275,290], [375],
              [182,196], [105,118], [200,220], [282,300], [282,300], [385,405], [303,322], [300],
              [250,250], [84,96], [125,135], [256,275], [135,145], [130,142], [125,132], [288],
              [285,300], [72,81], [152,166], [300,316], [340,352], [310,328], [250,275], [250],
              [172,180], [222,236], [175,191], [183,187], [246],[125,136], [122,135], [138,151], [176],
              [172, 180], [182,196], [204, 221], [168, 182], [196], [160, 165], [192, 205], [98, 106], [205],
              [99,109], [70,80], [174,180], [200,210], [160,165], [190,198], [272], [230,244], [165,178], [210,222], [175,190], [280]]

jobs_prec = [[None, None, None, [0,1], None, [0,1,2,3,4]],
             [None, None, None, [0,1], None, [0,1,2,3,4]],
             [None, None, [0,1], None, None, [0,1,2,3,4]],
             [None, None, [0,1], None, None, [0,1,2,3,4]],
             [None, None, None, [0,1], None, [0,1,2,3,4]],
             [None, None, None, [0,1,2], None, [0,1,2,3,4]],
             [None, None, None, [0,1,2], None, [0,1,2,3,4]],
             [None, None, None, [0,1,2], None, None, [0,1,2,3], [0,1,2,3,4,5,6]]]

jobshop = Jobshop(tag, n_orders, n_jobs, n_ops, n_machs, orders_vec, jobs_vec, ops_vec, vec_size, avail_machs, proc_times, jobs_prec)
