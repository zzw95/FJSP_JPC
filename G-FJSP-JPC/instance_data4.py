from collections import namedtuple
Jobshop = namedtuple('Jobshop', ['tag', 'n_orders', 'n_jobs', 'n_ops', 'n_machs', 'orders_vec', 'jobs_vec', 'ops_vec', 'vec_size', 'avail_machs', 'proc_times', 'jobs_prec'])
tag = 'inst4'
n_orders = 8
n_jobs = [6, 6, 6, 6, 6, 6, 6, 6]
n_ops = [[1,1,1,1,3,1], [1,1,1,1,3,1], [1,1,1,1,3,1], [1,1,1,1,3,1], [1,1,1,1,3,1], [1,1,1,1,3,1], [1,1,1,1,3,1], [1,1,1,1,3,1]]
n_machs = 6

orders_vec = [0,] *8 + [1, ]*8 + [2, ]*8 + [3, ]*8 + [4, ]*8 + [5, ]*8 + [6,]*8 + [7,] *8
jobs_vec= [0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,
           0, 1, 2, 3, 4, 4, 4, 5,]
ops_vec = list(range(64))

vec_size = 64

avail_machs = [[0,1], [0,1], [2,3], [4,5], [0,1], [2,3], [4,5], [4,5],
               [0,1], [0,1], [2,3], [4,5], [0,1], [2,3], [4,5], [4,5],
               [2,3], [2,3], [0,1], [4,5], [0,1], [2,3], [4,5], [4,5],
               [2,3], [2,3], [0,1], [4,5], [0,1], [2,3], [4,5], [4,5],
               [4,5], [0,1], [2,3], [4,5], [0,1], [2,3], [4,5], [4,5],
               [4,5], [0,1], [2,3], [4,5], [0,1], [2,3], [4,5], [4,5],
               [0,1], [0,1], [2,3], [2,3], [0,1], [2,3], [4,5], [4,5],
               [0,1], [0,1], [2,3], [2,3], [0,1], [2,3], [4,5], [4,5]]


proc_times = [[[60, 63], [65, 69]], [[302, 326], [322, 339]], [[122, 129], [135, 144]], [[210, 214], [224, 246]], [[174, 175], [188, 196]], [[208, 225], [224, 240]], [[180, 195], [198, 214]], [[400, 420], [425, 463]],
              [[90, 93], [100, 107]], [[220, 224], [232, 248]], [[144, 158], [152, 156]], [[308, 318], [318, 329]], [[244, 245], [258, 274]], [[302, 329], [318, 338]], [[260, 283], [276, 291]], [[304, 306], [322, 337]],
              [[70, 76], [75, 77]], [[306, 313], [322, 330]], [[110, 112], [126, 129]], [[280, 303], [296, 313]], [[180, 189], [198, 202]], [[312, 335], [328, 334]], [[300, 326], [320, 337]], [[208, 222], [218, 230]],
              [[102, 111], [110, 121]], [[208, 216], [222, 229]], [[130, 132], [148, 157]], [[240, 243], [262, 269]], [[190, 197], [202, 213]], [[310, 313], [326, 342]], [[300, 315], [318, 335]], [[205, 220], [215, 231]],
              [[108, 111], [116, 117]], [[206, 212], [224, 236]], [[150, 161], [172, 173]], [[320, 329], [345, 359]], [[452, 490], [472, 484]], [[258, 260], [274, 282]], [[150, 151], [175, 185]], [[280, 289], [298, 308]],
              [[82, 85], [90, 95]], [[250, 255], [276, 278]], [[125, 129], [125, 134]], [[250, 268], [250, 269]], [[125, 132], [135, 145]], [[120, 122], [136, 145]], [[124, 133], [138, 140]], [[375, 410], [400, 401]],
              [[60, 64], [66, 69]], [[300, 308], [315, 318]], [[206, 210], [222, 225]], [[178, 183], [190, 208]], [[290, 313], [310, 338]], [[208, 214], [222, 228]], [[180, 187], [194, 213]], [[300, 327], [320, 343]],
              [[80, 83], [90, 97]], [[100, 104], [105, 111]], [[123, 124], [136, 144]], [[210, 223], [226, 240]], [[278, 300], [293, 294]], [[370, 377], [390, 394]], [[200, 210], [218, 223]], [[300, 316], [310, 330]]]


jobs_prec = [[None, None, None, [0,1], None, [0,1,2,3,4]],
             [None, None, None, [0,1], None, [0,1,2,3,4]],
             [None, None, [0,1], None, None, [0,1,2,3,4]],
             [None, None, [0,1], None, None, [0,1,2,3,4]],
             [None, None, None, [0,1], None, [0,1,2,3,4]],
             [None, None, None, [0,1], None, [0,1,2,3,4]],
             [None, None, None, None, [0,1,2], [0,1,2,3,4]],
             [None, None, None, [0,1,2], None, [0,1,2,3,4]]]

jobshop = Jobshop(tag, n_orders, n_jobs, n_ops, n_machs, orders_vec, jobs_vec, ops_vec, vec_size, avail_machs, proc_times, jobs_prec)
