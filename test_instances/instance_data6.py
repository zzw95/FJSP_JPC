from collections import namedtuple
Jobshop = namedtuple('Jobshop', ['tag', 'n_orders', 'n_jobs', 'n_ops', 'n_machs', 'orders_vec', 'jobs_vec', 'ops_vec', 'vec_size', 'avail_machs', 'proc_times', 'jobs_prec'])
tag = 'inst6'
n_orders = 10
n_jobs = [3, 6, 6, 6, 6, 6, 6, 8, 8, 8]
n_ops = [[1,1,1],
         [1,1,1,1,3,1],
         [1,1,1,1,3,1],
         [1,1,1,1,3,1],
         [1,1,1,1,3,1],
         [1,1,1,1,3,1],
         [1,1,1,1,3,1],
         [1,1,1,1,2,2,1,1],
         [1,1,1,1,2,2,1,1],
         [1,1,1,1,2,2,1,1]]

n_machs = 8

orders_vec = [0,] *3 + [1, ]*8 + [2, ]*8 + [3, ]*8 + [4, ]*8 + [5, ]*8 + [6,]*8 + [7,] *10 + [8,]*10 + [9,]*10

jobs_vec= [0, 1, 2,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 5, 5, 6, 7,
           0, 1, 2, 3, 4, 4, 5, 5, 6, 7,
           0, 1, 2, 3, 4, 4, 5, 5, 6, 7]

ops_vec = list(range(81))

vec_size = 81

avail_machs = [[0,1], [0,1], [6,7],
               [0,1], [4,5], [6,7], [2,3], [0,1], [2,3], [4,5], [6,7],
               [0,1], [4,5], [2,3], [6,7], [0,1], [2,3], [4,5], [6,7],
               [0,1], [2,3], [4,5], [6,7], [0,1], [2,3], [4,5], [6,7],
               [0,1], [2,3], [4,5], [6,7], [0,1], [2,3], [4,5], [6,7],
               [0, 1], [4, 5], [6, 7], [2, 3], [0, 1], [2, 3], [4, 5], [6, 7],
               [0, 1], [4, 5], [2, 3], [6, 7], [0, 1], [2, 3], [4, 5], [6, 7],
               [0,1], [2,3], [4,5], [6,7], [0,1], [4,5], [2,3], [4,5], [0,1], [6,7],
               [0,1], [2,3], [4,5], [6,7], [0,1], [4,5], [2,3], [4,5], [0,1], [6,7],
               [0,1], [2,3], [4,5], [6,7], [0,1], [4,5], [2,3], [4,5], [2,3], [6,7]]

proc_times = [[120,132], [125,136], [205,214],
              [132,146], [178,185], [150,163], [221,233], [166,181], [170,180], [293,300], [385,400],
              [78,88], [244,260], [172,186], [178,190], [325,338], [360,378], [267,279], [325,342],
              [94,102], [175,184], [230,244], [270,288], [182,195], [242,258], [186,194], [272,288],
              [66,75], [250,262], [125,135], [244,258], [120,128], [116,130], [175,195], [295,318],
              [108,116], [211,228], [119,128], [138,154], [350,372], [205,218], [308,320], [300,319],
              [125,138], [235,250], [75,88], [228,240], [178,192], [270,286], [185,202], [255,272],
              [116,129], [189,200], [190,205], [282,290], [322,333], [265,277], [322,344], [238,256], [278,295], [279,294],
              [155,174], [212,225], [175,190], [285,298], [320,340], [333,352], [290,310], [314,333], [267,283], [300,322],
              [135,147], [172,185], [165,182], [165,178], [243,260], [193,212], [172,190], [194,213], [232,250], [283,302]]

jobs_prec = [[None, None, [0,1]],
             [None, None, [0,1], None, None, [0,1,2,3,4]],
             [None, None, None, [0,1], None, [0,1,2,3,4]],
             [None, None, None, [0,1,2], None, [0,1,2,3,4]],
             [None, None, None, [0,1,2], None, [0,1,2,3,4]],
             [None, None, [0,1], None, None, [0,1,2,3,4]],
             [None, None, None, [0,1], None, [0,1,2,3,4]],
             [None, None, None, [0,1,2], None, None, None, [0,1,2,3,4,5,6]],
             [None, None, None, [0,1,2], None, None, None, [0,1,2,3,4,5,6]],
             [None, None, None, [0,1,2], None, None, [4,5], [0,1,2,3,4,5,6]]]

jobshop = Jobshop(tag, n_orders, n_jobs, n_ops, n_machs, orders_vec, jobs_vec, ops_vec, vec_size, avail_machs, proc_times, jobs_prec)


