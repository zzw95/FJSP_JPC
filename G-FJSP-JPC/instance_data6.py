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


proc_times = [[[120, 121], [132, 140]], [[125, 130], [136, 139]], [[205, 211], [214, 228]],
                  [[132, 140], [146, 153]], [[178, 180], [185, 191]], [[150, 164], [163, 177]], [[221, 238], [233, 234]], [[166, 176], [181, 194]], [[170, 179], [180, 194]], [[293, 303], [300, 328]], [[385, 409], [400, 406]],
                  [[78, 84], [88, 90]], [[244, 246], [260, 267]], [[172, 187], [186, 192]], [[178, 186], [190, 191]], [[325, 336], [338, 368]], [[360, 382], [378, 406]], [[267, 291], [279, 284]], [[325, 347], [342, 368]],
                  [[94, 100], [102, 108]], [[175, 178], [184, 185]], [[230, 231], [244, 256]], [[270, 292], [288, 306]], [[182, 199], [195, 206]], [[242, 249], [258, 265]], [[186, 204], [194, 200]], [[272, 274], [288, 305]],
                  [[66, 69], [75, 78]], [[250, 275], [262, 283]], [[125, 128], [135, 141]], [[244, 250], [258, 264]], [[120, 129], [128, 131]], [[116, 123], [130, 143]], [[175, 183], [195, 203]], [[295, 299], [318, 326]],
                  [[108, 115], [116, 121]], [[211, 228], [228, 244]], [[119, 123], [128, 133]], [[138, 143], [154, 163]], [[350, 379], [372, 407]], [[205, 216], [218, 222]], [[308, 323], [320, 327]], [[300, 319], [319, 328]],
                  [[125, 137], [138, 151]], [[235, 238], [250, 262]], [[75, 81], [88, 90]], [[228, 239], [240, 254]], [[178, 182], [192, 193]], [[270, 283], [286, 300]], [[185, 196], [202, 214]], [[255, 269], [272, 299]],
                  [[116, 126], [129, 134]], [[189, 203], [200, 213]], [[190, 197], [205, 224]], [[282, 307], [290, 319]], [[322, 323], [333, 345]], [[265, 287], [277, 278]], [[322, 330], [344, 359]], [[238, 255], [256, 275]], [[278, 303], [295, 306]], [[279, 306], [294, 307]],
                  [[155, 157], [174, 188]], [[212, 226], [225, 234]], [[175, 181], [190, 194]], [[285, 293], [298, 326]], [[320, 340], [340, 348]], [[333, 336], [352, 380]], [[290, 308], [310, 314]], [[314, 336], [333, 334]], [[267, 273], [283, 289]], [[300, 311], [322, 327]],
                  [[135, 140], [147, 151]], [[172, 188], [185, 196]], [[165, 173], [182, 193]], [[165, 179], [178, 180]], [[243, 244], [260, 268]], [[193, 210], [212, 220]], [[172, 189], [190, 196]], [[194, 205], [213, 217]], [[232, 245], [250, 274]], [[283, 285], [302, 328]]]

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


