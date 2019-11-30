from collections import namedtuple
Jobshop = namedtuple('Jobshop', ['tag', 'n_orders', 'n_jobs', 'n_ops', 'n_machs', 'orders_vec', 'jobs_vec', 'ops_vec', 'vec_size', 'avail_machs', 'proc_times', 'jobs_prec'])
tag = 'inst14'
n_orders = 20
n_jobs = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8, 8, 8, 8, 8, 8, 8, 8]

n_ops = [[1,1,1,1,3,1],
         [1,1,1,1,3,1],
         [1,1,1,1,3,1],
         [1,1,1,1,3,1],
         [1,1,1,1,3,1],
         [1,1,1,1,3,1],
         [1,1,1,1,3,1],
         [1,1,1,2,3,1],
         [1,1,1,2,3,1],
         [1,1,1,2,3,1],
         [1,1,1,2,3,1],
         [1,1,1,2,3,1],
         [1,1,1,1,3,1,1,1],
         [1,1,1,1,3,1,1,1],
         [1,1,1,1,3,1,1,1],
         [1,1,1,1,3,1,1,1],
         [1,1,1,1,2,2,2,1],
         [1,1,1,1,2,2,2,1],
         [1,1,1,1,2,2,2,1],
         [1,1,1,1,2,2,2,1]]

n_machs = 12

orders_vec = [0,] *8 + [1, ]*8 + [2, ]*8 + [3, ]*8 + [4, ]*8+[5, ]*8 + [6,]*8 + [7,] *9 + [8,]*9 + [9,]*9\
             + [10,]*9 + [11,]*9 + [12,]*10 + [13,]*10 + [14,]*10 + [15,]*10 + [16,]*11 + [17,]*11 + [18,]*11 + [19,]*11

jobs_vec= [0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5, 6, 7,
           0, 1, 2, 3, 4, 4, 4, 5, 6, 7,
           0, 1, 2, 3, 4, 4, 4, 5, 6, 7,
           0, 1, 2, 3, 4, 4, 4, 5, 6, 7,
           0, 1, 2, 3, 4, 4, 5, 5, 6, 6, 7,
           0, 1, 2, 3, 4, 4, 5, 5, 6, 6, 7,
           0, 1, 2, 3, 4, 4, 5, 5, 6, 6, 7,
           0, 1, 2, 3, 4, 4, 5, 5, 6, 6, 7,]

ops_vec = list(range(185))

vec_size = 185

avail_machs = [[6,7,8], [0,1], [6,7,8], [9,10,11], [0,1], [2,3], [4,5], [9,10,11],
               [6,7,8], [0,1], [6,7,8], [9,10,11], [0,1], [2,3], [4,5], [9,10,11],
               [6,7,8], [0,1], [6,7,8], [9,10,11], [0,1], [2,3], [4,5], [9,10,11],
               [6,7,8], [0,1], [6,7,8], [9,10,11], [0,1], [2,3], [4,5], [9,10,11],
               [6,7,8], [0,1], [6,7,8], [9,10,11], [0,1], [2,3], [4,5], [9,10,11],
               [0,1], [2,3], [6,7,8], [6,7,8], [4,5], [6,7,8], [9,10,11], [9,10,11],
               [0,1], [2,3], [6,7,8], [6,7,8], [4,5], [6,7,8], [9,10,11], [9,10,11],
               [6,7,8], [0,1], [9,10,11], [2,3], [6,7,8], [2,3], [4,5], [9,10,11], [9,10,11],
               [6,7,8], [0,1], [9,10,11], [2,3], [6,7,8], [2,3], [4,5], [9,10,11], [9,10,11],
               [6,7,8], [0,1], [9,10,11], [2,3], [6,7,8], [0,1], [4,5], [9,10,11], [9,10,11],
               [6,7,8], [0,1], [9,10,11], [2,3], [6,7,8], [0,1], [4,5], [9,10,11], [9,10,11],
               [6,7,8], [0,1], [9,10,11], [2,3], [6,7,8], [0,1], [4,5], [9,10,11], [9,10,11],
               [6,7,8], [0,1], [2,3], [9,10,11], [6,7,8], [4,5], [9,10,11], [0,1], [2,3], [9,10,11],
               [6,7,8], [0,1], [2,3], [9,10,11], [6,7,8], [4,5], [9,10,11], [0,1], [2,3], [9,10,11],
               [6,7,8], [0,1], [2,3], [9,10,11], [6,7,8], [4,5], [9,10,11], [0,1], [2,3], [9,10,11],
               [6,7,8], [0,1], [2,3], [9,10,11], [6,7,8], [4,5], [9,10,11], [0,1], [2,3], [9,10,11],
               [0,1], [2,3], [6,7,8], [9,10,11], [4,5], [6,7,8], [4,5], [6,7,8], [6,7,8], [9,10,11], [9,10,11],
               [0,1], [2,3], [6,7,8], [9,10,11], [4,5], [6,7,8], [4,5], [6,7,8], [6,7,8], [9,10,11], [9,10,11],
               [0,1], [2,3], [6,7,8], [9,10,11], [0,1], [4,5], [2,3], [4,5], [2,3], [4,5], [9,10,11],
               [0,1], [2,3], [6,7,8], [9,10,11], [0,1], [4,5], [2,3], [4,5], [2,3], [4,5], [9,10,11]]


proc_times = [[89, 98, 104], [160,163], [174, 181, 186], [101,108, 114], [118,130], [168,182], [195, 217], [218, 222, 228],
              [119, 125, 138], [140, 152], [135,144, 150], [75, 80, 85], [129, 141], [156, 163], [178, 192], [185, 189, 202],
              [90, 97, 102], [177, 184], [204, 211, 221], [176, 191, 197], [238, 256], [172, 185], [165, 182], [160,165, 178],
              [125, 129, 138],[151, 162], [217, 228, 235], [166,181,188], [223, 238], [261, 278], [167, 178], [233, 238, 251],
              [94, 105, 108], [171, 187], [182,190, 199], [122, 133, 140], [265,281], [233,249], [185, 202], [136, 150, 153],
              [193,212], [178,189], [190, 199, 208], [241,253, 256], [163,174], [109,114, 120], [211, 218, 227], [119,126, 131],
              [177, 191], [207, 214], [168,174,180], [190, 198, 205], [282, 290], [222, 233, 244], [165, 177, 183], [172, 179, 190],
              [149, 161, 169], [238, 256], [211, 218, 221], [169,181],  [255,270, 276], [204,217], [193,201], [125, 135, 142], [144, 151, 158],
              [116, 126, 132],  [278, 295], [178, 184, 195], [189, 200], [220, 228, 234], [216, 230], [175, 195], [195, 211, 217], [225, 229, 242],
              [119,128, 132], [168, 174], [230, 242, 251], [215,229], [201,212, 219],  [166,181], [193,212], [185, 193, 208], [171, 179, 183],
              [243, 260, 263], [221,233], [192, 203, 211], [136, 142], [185, 192, 208], [122,135], [138,151], [159,166, 174], [242, 253, 264],
              [168, 182, 188], [235, 251], [173,187,191], [135,148], [123, 134, 142], [165,174], [140,152], [187, 193, 199], [143, 146, 157],
              [149,155, 161], [170,180], [212, 225], [175, 184,190], [200, 210, 220], [132, 136], [168,175, 181],  [193,200], [255,270], [218, 230, 235],
              [232, 240, 251], [283, 300], [279, 295], [199, 211, 220], [149,160, 166], [267, 283], [165,179, 187], [203, 217], [168, 182], [135,148, 160],
              [225, 231, 239], [233,249], [314, 333], [222, 233, 244], [174, 186, 192], [303,311],  [144,161, 165], [187,203],  [179, 195],  [205, 209, 212],
              [178,192, 200], [270,286], [185,202], [250, 256, 262], [233, 249, 255], [155,174],  [182,190, 199], [175,190], [129,140], [178, 188, 192],
              [155, 160],  [233, 252], [162, 176, 184], [173, 177, 187],[199, 211], [172, 179, 186], [267, 283], [195, 200, 206], [223, 225, 238], [261, 267, 278], [220, 228, 236],
              [241, 253], [166, 181], [178, 191, 195], [125,136, 140], [270,286], [162, 176, 183], [177, 191],  [105,114, 118], [205,214, 219], [165,178, 187], [243, 249, 260],
              [233, 239], [210,222], [175,190, 194], [217,229, 233], [114, 125], [171, 187],  [273,291], [185,202], [255,272], [105, 114], [194, 213, 216],
              [300, 318], [241,253], [163,174, 178], [210, 218, 222], [175,190], [202, 218], [138, 148], [108,116], [250,275], [235,250],  [220, 229, 234]]


jobs_prec = [[None, None, None, [0,1,2], None, [0,1,2,3,4]],
             [None, None, None, [0,1,2], None, [0,1,2,3,4]],
             [None, None, None, [0,1,2], None, [0,1,2,3,4]],
             [None, None, None, [0,1,2], None, [0,1,2,3,4]],
             [None, None, None, [0,1,2], None, [0,1,2,3,4]],
             [None, None, None, None, None, [0,1,2,3,4]],
             [None, None, None, None, None, [0,1,2,3,4]],
             [None, None, [0,1], None, None, [0,1,2,3,4]],
             [None, None, [0,1], None, None, [0,1,2,3,4]],
             [None, None, [0,1], None, None, [0,1,2,3,4]],
             [None, None, [0,1], None, None, [0,1,2,3,4]],
             [None, None, [0,1], None, None, [0,1,2,3,4]],
             [None, None, None, [0,1,2], None, None, [4,5], [0,1,2,3,4,5,6]],
             [None, None, None, [0,1,2], None, None, [4,5], [0,1,2,3,4,5,6]],
             [None, None, None, [0,1,2], None, None, [4,5], [0,1,2,3,4,5,6]],
             [None, None, None, [0,1,2], None, None, [4,5], [0,1,2,3,4,5,6]],
             [None, None, None, [0,1,2], None, None, None, [0,1,2,3,4,5,6]],
             [None, None, None, [0,1,2], None, None, None, [0,1,2,3,4,5,6]],
             [None, None, None, [0,1,2], None, None, None, [0,1,2,3,4,5,6]],
             [None, None, None, [0,1,2], None, None, None, [0,1,2,3,4,5,6]]]

jobshop = Jobshop(tag, n_orders, n_jobs, n_ops, n_machs, orders_vec, jobs_vec, ops_vec, vec_size, avail_machs, proc_times, jobs_prec)
