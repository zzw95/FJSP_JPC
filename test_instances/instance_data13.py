from collections import namedtuple
Jobshop = namedtuple('Jobshop', ['tag', 'n_orders', 'n_jobs', 'n_ops', 'n_machs', 'orders_vec', 'jobs_vec', 'ops_vec', 'vec_size', 'avail_machs', 'proc_times', 'jobs_prec'])
tag = 'inst13'
n_orders = 18
n_jobs = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 8, 8, 8, 8, 8, 8, 8, 9]
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
         [1,1,1,1,2,2,2,1],
         [1,1,1,1,1,1,1,1],
         [1,1,1,1,1,1,1,1,1],
         ]

n_machs = 12

orders_vec = [0,] *8 + [1, ]*8 + [2, ]*8 + [3, ]*8 + [4, ]*8 + [5, ]*9 + [6,]*9 + [7,] *9 + [8,]*9 + [9,]*9 \
             + [10,]*12 + [11,]*12 + [12,]*12 + [13,]*12 + [14,]*11 + [15,] *11 + [16,]*8 + [17,]*9

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
           0, 1, 2, 3, 4, 4, 5, 5, 6, 6, 7,
           0, 1, 2, 3, 4, 5, 6, 7,
           0, 1, 2, 3, 4, 5, 6, 7, 8]

ops_vec = list(range(172))

vec_size = 172

avail_machs = [[6,7,8], [0,1], [6,7,8], [9,10,11], [0,1], [2,3], [4,5], [9,10,11],
               [6,7,8], [0,1], [6,7,8], [9,10,11], [0,1], [2,3], [4,5], [9,10,11],
               [6,7,8], [2,3], [6,7,8], [9,10,11], [0,1], [2,3], [4,5], [9,10,11],
               [6,7,8], [2,3], [6,7,8], [9,10,11], [0,1], [2,3], [4,5], [9,10,11],
               [6,7,8], [4,5], [6,7,8], [9,10,11], [0,1], [2,3], [4,5], [9,10,11],
               [6,7,8], [0,1], [9,10,11], [2,3], [6,7,8], [2,3], [4,5], [9,10,11], [9,10,11],
               [6,7,8], [0,1], [9,10,11], [2,3], [6,7,8], [4,5], [2,3], [9,10,11], [9,10,11],
               [6,7,8], [0,1], [9,10,11], [2,3], [6,7,8], [0,1], [4,5], [9,10,11], [9,10,11],
               [6,7,8], [0,1], [9,10,11], [2,3], [6,7,8], [0,1], [4,5], [9,10,11], [9,10,11],
               [6,7,8], [0,1], [9,10,11], [2,3], [6,7,8], [4,5], [0,1], [9,10,11], [9,10,11],
               [0,1], [2,3], [6,7,8], [9,10,11], [0,1], [4,5], [6,7,8], [2,3], [4,5], [6,7,8], [9,10,11], [9,10,11],
               [0,1], [2,3], [6,7,8], [9,10,11], [0,1], [4,5], [6,7,8], [2,3], [4,5], [6,7,8], [9,10,11], [9,10,11],
               [0,1], [2,3], [6,7,8], [9,10,11], [0,1], [4,5], [6,7,8], [2,3], [4,5], [6,7,8], [9,10,11], [9,10,11],
               [0,1], [2,3], [6,7,8], [9,10,11], [0,1], [4,5], [6,7,8], [2,3], [4,5], [6,7,8], [9,10,11], [9,10,11],
               [4, 5], [0, 1], [6, 7, 8], [9, 10,11], [0, 1], [4, 5], [2, 3], [6, 7, 8], [2,3], [6, 7, 8], [9, 10,11],
               [4, 5], [0, 1], [6, 7, 8], [9, 10,11], [0, 1], [4, 5], [2, 3], [6, 7, 8], [2,3], [6, 7, 8], [9, 10,11],
               [6,7,8], [0,1], [6,7,8], [4,5], [9,10,11], [2,3], [6,7,8], [9,10,11],
               [6,7,8], [6,7,8], [9,10,11], [2,3], [6,7,8], [9,10,11], [4,5], [6,7,8], [9,10,11]]

proc_times = [[174, 186, 198], [235, 251],  [166,181,188], [173,187,191], [135,148], [165,174], [140,152], [185, 192, 208],
              [205, 214, 222], [165, 178], [243, 260, 263], [192, 203, 211], [136, 142], [122,135], [138,151], [171, 179, 183],
              [190, 198, 204], [171, 183], [210, 221, 232], [176, 191, 197], [238, 256], [172,185], [165,182], [217,228, 235],
              [118, 124, 131], [169, 181], [233, 238, 251], [217,229, 233], [228, 240], [207, 214], [209, 221], [168, 182, 188],
              [132, 146, 153], [169,177], [149, 161, 169], [211, 218, 221], [169,181], [204,217], [193,201], [255,270, 276],
              [122, 133, 144], [205,213], [222, 233, 244], [152, 161], [123, 134, 142], [303,311], [187,203], [159,166, 174], [242, 253, 264],
              [109, 117, 121], [211,226], [119,128, 132], [168, 174], [230, 242, 251], [215,229], [208,227], [201,212, 219],  [185, 193, 208],
              [182, 199, 204], [122, 133], [225, 231, 239], [233,249], [199, 211, 220], [314, 333], [267, 283], [165,179, 187], [135,148, 160],
              [244, 249, 262], [125,135], [105,114, 118], [185,203], [149,160, 166], [202, 218], [138, 148], [144,161, 165], [172, 179, 186],
              [89, 98, 105], [170, 183], [174, 186, 192], [203, 217], [218, 230, 235], [168, 182], [195, 217], [138,150, 156], [225, 238, 241],
              [263, 277], [167,179], [125, 129, 140], [212, 223, 231], [183, 200], [179, 195],  [205, 209, 212], [108,116], [250,275], [194, 213, 216], [175, 188, 199], [220, 229, 234],
              [142, 151], [194, 200], [162, 176, 184], [182,190, 199], [122,133], [265,281], [233, 249, 255], [121,131], [125,135], [205,214, 219], [165,178, 187], [243, 249, 260],
              [193,212], [178,189], [190, 199, 208], [241,253, 256], [163,174], [210,222], [175,190, 194], [114, 125], [171, 187], [233, 241, 248], [273, 286, 289], [177, 180, 191],
              [223, 238], [261, 278], [127, 138, 144], [178,192, 200], [270,286], [185,202], [250, 256, 262], [155,174],  [175,190], [144, 151, 158], [220, 228, 236], [216, 225, 230],
              [138, 151], [235,250], [187, 193, 199], [143, 146, 157], [186, 194], [76, 84], [129,140], [178, 188, 192], [160, 166], [182,195, 200], [186,194, 201],
              [66,72], [153, 162], [125,135, 140], [144, 152, 158], [121,128], [116,130], [178,195], [195, 200, 206], [212,225], [116,129, 133], [189, 194, 200],
              [191,200, 203], [142, 156], [178, 185, 190], [190, 203], [141, 153, 157], [166, 181], [173, 177, 187], [193, 200, 205],
              [98, 102, 107 ], [144, 152, 160], [162, 168, 176], [177, 191], [123, 125,134], [261, 267, 278], [167, 179], [155, 158, 161], [194, 205, 211]]

jobs_prec = [[None, None, None, [0,1], None, [0,1,2,3,4]],
             [None, None, None, [0,1], None, [0,1,2,3,4]],
             [None, None, None, None, [2,3], [0,1,2,3,4]],
             [None, None, None, None, [2,3], [0,1,2,3,4]],
             [None, None, None, None, [2,3], [0,1,2,3,4]],
             [None, None, [0,1], None, None, [0,1,2,3,4]],
             [None, None, [0,1], None, None, [0,1,2,3,4]],
             [None, None, [0,1], None, None, [0,1,2,3,4]],
             [None, None, None, [0,1], None, [0,1,2,3,4]],
             [None, None, None, [0,1], None, [0,1,2,3,4]],
             [None, None, None, [0,1,2], None, None, [4,5], [0,1,2,3,4,5,6]],
             [None, None, None, [0,1,2], None, None, [4,5], [0,1,2,3,4,5,6]],
             [None, None, None, [0,1,2], None, None, [4,5], [0,1,2,3,4,5,6]],
             [None, None, None, [0,1,2], None, None, [4,5], [0,1,2,3,4,5,6]],
             [None, None, None, [0,1,2], None, None, [4,5], [0,1,2,3,4,5,6]],
             [None, None, None, [0,1,2], None, None, [4,5], [0,1,2,3,4,5,6]],
             [None, None, [0,1], None, None, [3,4], None, [0,1,2,3,4,5,6]],
             [None, None, [0,1], None, None, [3,4], [0,1,2,3,4,5], None, [0,1,2,3,4,5,6,7]]]

jobshop = Jobshop(tag, n_orders, n_jobs, n_ops, n_machs, orders_vec, jobs_vec, ops_vec, vec_size, avail_machs, proc_times, jobs_prec)
