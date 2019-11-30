from collections import namedtuple
Jobshop = namedtuple('Jobshop', ['tag', 'n_orders', 'n_jobs', 'n_ops', 'n_machs', 'orders_vec', 'jobs_vec', 'ops_vec', 'vec_size', 'avail_machs', 'proc_times', 'jobs_prec'])
tag = 'inst12'
n_orders = 16
n_jobs = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8, 8, 8, 8, 8, 8]
n_ops = [[1,1,1,1,3,1],
         [1,1,1,1,3,1],
         [1,1,1,1,3,1],
         [1,1,1,1,3,1],
         [1,1,1,1,3,1],
         [1,1,1,2,3,1],
         [1,1,1,2,3,1],
         [1,1,1,2,3,1],
         [1,1,1,2,3,1],
         [1,1,1,2,3,1],
         [1,1,1,1,3,3,1,1],
         [1,1,1,1,3,3,1,1],
         [1,1,1,1,3,2,2,1],
         [1,1,1,1,3,2,2,1],
         [1,1,1,1,2,2,2,1],
         [1,1,1,1,2,2,2,1]]

n_machs = 11

orders_vec = [0,] *8 + [1, ]*8 + [2, ]*8 + [3, ]*8 + [4, ]*8 + [5, ]*9 + [6,]*9 + [7,] *9 + [8,]*9 + [9,]*9 \
             + [10,]*12 + [11,]*12 + [12,]*12 + [13,]*12 + [14,]*11 + [15,] *11

jobs_vec= [0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5, 5, 5, 6, 7,
           0, 1, 2, 3, 4, 4, 4, 5, 5, 5, 6, 7,
           0, 1, 2, 3, 4, 4, 4, 5, 5, 6, 6, 7,
           0, 1, 2, 3, 4, 4, 4, 5, 5, 6, 6, 7,
           0, 1, 2, 3, 4, 4, 5, 5, 6, 6, 7,
           0, 1, 2, 3, 4, 4, 5, 5, 6, 6, 7]

ops_vec = list(range(155))

vec_size = 155

avail_machs = [[6,7,8], [0,1], [6,7,8], [9,10], [0,1], [2,3], [4,5], [9,10],
               [6,7,8], [0,1], [6,7,8], [9,10], [0,1], [2,3], [4,5], [9,10],
               [6,7,8], [4,5], [6,7,8], [9,10], [0,1], [2,3], [4,5], [9,10],
               [6,7,8], [2,3], [6,7,8], [9,10], [0,1], [2,3], [4,5], [9,10],
               [6,7,8], [2,3], [6,7,8], [9,10], [0,1], [2,3], [4,5], [9,10],
               [6,7,8], [0,1], [9,10], [2,3], [6,7,8], [0,1], [2,3], [4,5], [9,10],
               [6,7,8], [0,1], [9,10], [2,3], [6,7,8], [0,1], [2,3], [4,5], [9,10],
               [6,7,8], [4,5], [9,10], [2,3], [6,7,8], [0,1], [2,3], [4,5], [9,10],
               [6,7,8], [2,3], [9,10], [0,1], [6,7,8], [0,1], [2,3], [4,5], [9,10],
               [6,7,8], [2,3], [9,10], [0,1], [6,7,8], [0,1], [2,3], [4,5], [9,10],
               [0,1], [2,3], [6,7,8], [9,10], [0,1], [4,5], [6,7,8], [2,3], [4,5], [6,7,8], [9,10], [9,10],
               [0,1], [2,3], [6,7,8], [9,10], [0,1], [4,5], [6,7,8], [2,3], [4,5], [6,7,8], [9,10], [9,10],
               [2,3], [2,3], [6,7,8], [9,10], [0,1], [4,5], [6,7,8], [0,1], [4,5], [6,7,8], [4,5], [9,10],
               [4,5], [2,3], [6,7,8], [9,10], [0,1], [4,5], [6,7,8], [2,3], [0,1], [6,7,8], [4,5], [9,10],
               [4, 5], [0, 1], [6, 7, 8], [9, 10], [0, 1], [4, 5], [2, 3], [6, 7, 8], [2,3], [6, 7, 8], [9, 10],
               [4, 5], [0, 1], [6, 7, 8], [9, 10], [0, 1], [4, 5], [2, 3], [6, 7, 8], [2,3], [6, 7, 8], [9, 10]]

proc_times = [[183, 189, 195], [283, 291], [242, 253, 264], [165, 177], [322, 344], [238, 256], [278, 295], [178, 195],
              [135, 147, 153], [172, 185],  [232, 243, 251], [283, 300], [279, 295],  [100,112], [108,116], [250,275],
              [125, 136, 140], [187, 199], [243, 257, 263], [186, 194], [272, 288], [211, 228], [119, 128], [138, 154],
              [119,126, 131], [168, 180], [230, 238, 250], [215,228], [208,220], [201,219], [204, 221], [168, 182],
              [190, 203, 210], [173, 187], [293, 309, 317], [385, 400], [165, 182], [165, 178], [193,212], [178,189],
              [162, 176, 183], [177, 191], [223, 238], [261, 278], [167, 179, 191], [129, 141], [178, 192], [178, 192], [185, 202],
              [225, 229, 242], [171, 187], [182,199], [122, 133], [225, 231, 239], [233,249], [199, 211], [314, 333], [267, 283],
              [178, 191, 195], [270,286], [185,202], [255,272], [105, 114, 123],  [300, 318], [241,253], [163,174], [210,222],
              [149,155, 161], [221,233], [166,181], [170,180], [193,200, 217], [255,270], [177, 191], [223, 238], [261, 278],
              [172, 179, 190], [194, 213], [189, 200], [135, 142], [144, 151, 158], [220, 228], [216, 230], [175, 195],  [248,265],
              [256, 278], [90, 96], [175, 188, 199], [240, 260], [309, 321], [275, 290], [366, 371,375], [89, 98], [170,183], [174, 181, 186], [280, 290], [133, 152],
              [120, 128], [125, 136], [205, 214, 222], [165, 178], [243, 260], [192, 203],[125,136, 142], [122,135], [138,151], [171, 179, 188],  [300,316], [240,252],
              [98, 109], [144, 160], [125, 129, 138], [250, 266],  [142, 156], [178, 185], [243, 260, 266], [193, 212], [172,180], [222, 229, 236], [175,191], [183,187],
              [119, 125], [140, 152], [135,144, 157], [80, 85], [108, 114], [118,130], [168,182, 189], [195,217], [238, 242], [94, 105, 108],  [185, 202], [136, 150],
              [182,196], [105,118], [207,220, 225], [282,300], [282,300], [385,405], [256,275], [303, 309, 322],  [135,145], [130,142, 149], [288, 301],
              [285,300], [72,81], [152,166, 174], [310,328], [172, 180], [182,196], [160, 165], [192, 205, 213], [98, 106], [116, 126, 132],[195, 217]]

jobs_prec = [[None, None, None, [0,1,2], None, [0,1,2,3,4]],
             [None, None, None, [0,1,2], None, [0,1,2,3,4]],
             [None, None, None, [0,1,2], None, [0,1,2,3,4]],
             [None, None, None, [0,1,2], None, [0,1,2,3,4]],
             [None, None, None, [0,1,2], None, [0,1,2,3,4]],
             [None, None, [0,1], None, None, [0,1,2,3,4]],
             [None, None, [0,1], None, None, [0,1,2,3,4]],
             [None, None, None, None, [1,2,3], [0,1,2,3,4]],
             [None, None, None, None, [1,2,3], [0,1,2,3,4]],
             [None, None, None, None, [1,2,3], [0,1,2,3,4]],
             [None, None, None, [0,1,2], None, None, [4,5], [0,1,2,3,4,5,6]],
             [None, None, None, [0,1,2], None, None, [4,5], [0,1,2,3,4,5,6]],
             [None, None, None, [0,1,2], None, None, [4,5], [0,1,2,3,4,5,6]],
             [None, None, [0,1], None, None, None, [3,4,5], [0,1,2,3,4,5,6]],
             [None, None, [0,1], None, None, None, [3,4,5], [0,1,2,3,4,5,6]],
             [None, None, [0,1], None, None, None, [3,4,5], [0,1,2,3,4,5,6]]]

jobshop = Jobshop(tag, n_orders, n_jobs, n_ops, n_machs, orders_vec, jobs_vec, ops_vec, vec_size, avail_machs, proc_times, jobs_prec)
