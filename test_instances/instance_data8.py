from collections import namedtuple
Jobshop = namedtuple('Jobshop', ['tag', 'n_orders', 'n_jobs', 'n_ops', 'n_machs', 'orders_vec', 'jobs_vec', 'ops_vec', 'vec_size', 'avail_machs', 'proc_times', 'jobs_prec'])
tag = 'inst8'
n_orders = 12
n_jobs = [6, 6, 6, 6, 6, 6, 6, 6, 8, 8, 8, 8]
n_ops = [[1,1,1,1,3,1],
         [1,1,1,1,3,1],
         [1,1,1,1,3,1],
         [1,1,1,1,3,1],
         [1,1,1,1,3,1],
         [1,1,1,1,3,1],
         [1,1,1,1,3,1],
         [1,1,1,1,3,1],
         [1,1,1,1,2,2,1,1],
         [1,1,1,1,2,2,1,1],
         [1,1,1,1,2,2,1,1],
         [1,1,1,1,2,2,1,1]]

n_machs = 9

orders_vec = [0,] *8 + [1, ]*8 + [2, ]*8 + [3, ]*8 + [4, ]*8 + [5, ]*8 + [6,]*8 + [7,] *8 + [8,]*10 + [9,]*10 + [10,]*10 + [11,]*10

jobs_vec= [0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 5, 5, 6, 7,
           0, 1, 2, 3, 4, 4, 5, 5, 6, 7,
           0, 1, 2, 3, 4, 4, 5, 5, 6, 7,
           0, 1, 2, 3, 4, 4, 5, 5, 6, 7,]

ops_vec = list(range(104))

vec_size = 104

avail_machs = [[2,3], [0,1], [6,7], [6,7], [0,1], [2,3], [4,5], [8],
               [2,3], [0,1], [6,7], [6,7], [0,1], [2,3], [4,5], [8],
               [2,3], [0,1], [6,7], [6,7], [0,1], [2,3], [4,5], [8],
               [6,7], [0,1], [6,7], [4,5], [0,1], [2,3], [4,5], [8],
               [6,7], [0,1], [6,7], [4,5], [0,1], [2,3], [4,5], [8],
               [4,5], [0,1], [6,7], [2,3], [0,1], [2,3], [4,5], [8],
               [6,7], [0,1], [2,3], [6,7], [0,1], [2,3], [4,5], [8],
               [6,7], [0,1], [2,3], [6,7], [0,1], [2,3], [4,5], [8],
               [0,1], [2,3], [4,5], [6,7], [0,1], [4,5], [6,7], [4,5], [2,3], [8],
               [0,1], [2,3], [4,5], [6,7], [0,1], [4,5], [6,7], [4,5], [2,3], [8],
               [0,1], [2,3], [4,5], [6,7], [0,1], [4,5], [2,3], [6,7], [4,5], [8],
               [0,1], [2,3], [4,5], [6,7], [0,1], [4,5], [2,3], [6,7], [4,5], [8],
             ]
proc_times = [[218,230], [175,195], [195,217], [208,210], [282,290], [222,233], [265,281], [333],
              [165,179], [135,148], [244,262], [125,135], [105,114], [285,303], [136,150], [218],
              [108, 116], [250, 272], [125, 138], [250, 266], [211, 228], [119, 128], [138, 154], [250],
              [204, 213], [108, 113], [212,229], [189,200], [125,135], [144,158], [220,228], [272],
              [141,152], [178,185], [190,203], [241,253], [166,181], [173,187], [195,203], [285],
              [114,125], [171,187], [233,244], [272,286], [187,199], [143,157], [186,194], [256],
              [98,109], [144,160], [162,176], [177,191], [223,238], [162,178], [207,209], [338],
              [138,151], [235,250], [175,188], [228,240], [178,192], [270,286], [178,192], [185],
              [99,108], [170,183], [174,186], [201,212], [161,165], [190,198], [230,244], [163,174], [210,222], [190],
              [255,272], [153,167], [197,213],  [178,183], [279,294], [300,319], [138,154], [350,372], [205,218], [308],
              [155,174], [216,232], [266,282],[147,151], [172,185], [208,222], [165,178], [243,260], [193,212], [322],
              [177,189], [112,125], [175,190], [198,207], [320,340], [233,242], [314,333], [172,190], [194,213], [250]]

jobs_prec = [[None, None, None, [0,1], None, [0,1,2,3,4]],
             [None, None, None, [0,1], None, [0,1,2,3,4]],
             [None, None, None, [0,1], None, [0,1,2,3,4]],
             [None, None, [0,1], None, None, [0,1,2,3,4]],
             [None, None, [0,1], None, None, [0,1,2,3,4]],
             [None, None, [0,1], None, None, [0,1,2,3,4]],
             [None, None, None, [0,1,2], None, [0,1,2,3,4]],
             [None, None, None, [0,1,2], None, [0,1,2,3,4]],
             [None, None, None, [0,1,2], None, None, [4,5], [0,1,2,3,4,5,6]],
             [None, None, None, [0,1,2], None, None, [4,5], [0,1,2,3,4,5,6]],
             [None, None, None, [0, 1, 2], None, None, [4, 5], [0, 1, 2, 3, 4, 5, 6]],
             [None, None, None, [0, 1, 2], None, None, [4, 5], [0, 1, 2, 3, 4, 5, 6]],
             ]

jobshop = Jobshop(tag, n_orders, n_jobs, n_ops, n_machs, orders_vec, jobs_vec, ops_vec, vec_size, avail_machs, proc_times, jobs_prec)

