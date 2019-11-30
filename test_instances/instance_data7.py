from collections import namedtuple
Jobshop = namedtuple('Jobshop', ['tag', 'n_orders', 'n_jobs', 'n_ops', 'n_machs', 'orders_vec', 'jobs_vec', 'ops_vec', 'vec_size', 'avail_machs', 'proc_times', 'jobs_prec'])
tag = 'inst7'
n_orders = 10
n_jobs = [6, 6, 6, 6, 6, 6, 8, 8, 8, 8]
n_ops = [[1,1,1,1,3,1],
         [1,1,1,1,3,1],
         [1,1,1,1,3,1],
         [1,1,1,1,3,1],
         [1,1,1,2,3,1],
         [1,1,1,2,3,1],
         [1,1,1,1,2,2,1,1],
         [1,1,1,1,2,2,1,1],
         [1,1,1,2,2,2,1,1],
         [1,1,1,2,2,2,1,1]]

n_machs = 8

orders_vec = [0,] *8 + [1, ]*8 + [2, ]*8 + [3, ]*8 + [4, ]*9 + [5, ]*9 + [6,]*10 + [7,] *10 + [8,]*11 + [9,]*11

jobs_vec= [0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 5, 5, 6, 7,
           0, 1, 2, 3, 4, 4, 5, 5, 6, 7,
           0, 1, 2, 3, 3, 4, 4, 5, 5, 6, 7,
           0, 1, 2, 3, 3, 4, 4, 5, 5, 6, 7]

ops_vec = list(range(92))

vec_size = 92

avail_machs = [[6,7], [0,1], [6,7], [6,7], [0,1], [2,3], [4,5], [6,7],
               [6,7], [0,1], [6,7], [6,7], [0,1], [2,3], [4,5], [6,7],
               [6,7], [0,1], [6,7], [6,7], [0,1], [2,3], [4,5], [6,7],
               [6,7], [0,1], [6,7], [6,7], [0,1], [2,3], [4,5], [6,7],
               [6,7], [0,1], [6,7], [2,3], [6,7], [0,1], [2,3], [4,5], [6,7],
               [6,7], [0,1], [6,7], [2,3], [6,7], [0,1], [2,3], [4,5], [6,7],
               [2,3], [2,3], [2,3], [6,7], [0,1], [4,5], [0,1], [4,5], [4,5], [6,7],
               [2,3], [2,3], [2,3], [6,7], [0,1], [4,5], [0,1], [4,5], [4,5], [6,7],
               [0,1], [0,1], [6,7], [0,1], [2,3], [0,1], [2,3], [0,1], [2,3], [4,5], [6,7],
               [0,1], [0,1], [6,7], [0,1], [2,3], [0,1], [2,3], [0,1], [2,3], [4,5], [6,7],
             ]
proc_times = [[135,148], [165,174], [140,152], [125,136], [105,114], [185,202], [136,150], [300,318],
              [142,156], [178,185], [190,203], [241,253], [166,181], [173,187], [293,309], [385,400],
              [98,109], [144,160], [162,176], [177,191], [223,238], [261,278], [167,179], [325,342],
              [94,105], [171,187], [233,244], [272,286], [187,199], [143,157], [186,194], [272,288],
              [106,112], [208,220], [251,266], [304,320], [154,166], [174,186], [335,350], [200,210], [288, 300],
              [82,90], [318,328], [192,206], [215,226], [192,208], [185,197], [325,340], [110,118], [121,144],
              [125,138], [235,250], [75,88], [228,240], [178,192], [270,286], [178,192], [185,202], [255,272], [125,138],
              [116,129], [189,200], [125,135], [144,158], [220,228], [216,230], [175,195], [195,217], [290,310], [250,266],
              [108,116],[250,272], [125,138], [250,266], [211,228], [119,128], [138,154], [350,372], [205,218], [308,320], [267,283],
              [190,205], [282,290], [322,333], [265,277], [322,344], [238,256], [278,295], [279,294],[278,295], [300,319], [194,213]]

jobs_prec = [[None, None, None, [0,1], None, [0,1,2,3,4]],
             [None, None, None, [0,1], None, [0,1,2,3,4]],
             [None, None, [0,1], None, None, [0,1,2,3,4]],
             [None, None, [0,1], None, None, [0,1,2,3,4]],
             [None, None, [0,1], None, None, [0,1,2,3,4]],
             [None, None, [0,1], None, None, [0,1,2,3,4]],
             [None, None, None, [0,1,2], None, None, [4,5], [0,1,2,3,4,5,6]],
             [None, None, None, [0,1,2], None, None, [4,5], [0,1,2,3,4,5,6]],
             [None, None, [0,1], None, None, None, [3,4,5], [0,1,2,3,4,5,6]],
             [None, None, [0,1], None, None, None, [3,4,5], [0,1,2,3,4,5,6]]
             ]

jobshop = Jobshop(tag, n_orders, n_jobs, n_ops, n_machs, orders_vec, jobs_vec, ops_vec, vec_size, avail_machs, proc_times, jobs_prec)

