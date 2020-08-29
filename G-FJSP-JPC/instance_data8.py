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


proc_times = [[[218, 238], [230, 237]], [[175, 188], [195, 210]], [[195, 202], [217, 227]], [[208, 212], [210, 221]], [[282, 306], [290, 303]], [[222, 237], [233, 253]], [[265, 290], [281, 302]], [[333, 345]],
              [[165, 172], [179, 191]], [[135, 137], [148, 158]], [[244, 254], [262, 270]], [[125, 132], [135, 143]], [[105, 112], [114, 118]], [[285, 303], [303, 326]], [[136, 149], [150, 157]], [[218, 234]],
              [[108, 109], [116, 123]], [[250, 252], [272, 276]], [[125, 133], [138, 144]], [[250, 265], [266, 282]], [[211, 222], [228, 249]], [[119, 130], [128, 138]], [[138, 145], [154, 167]], [[250, 261]],
              [[204, 209], [213, 218]], [[108, 114], [113, 121]], [[212, 213], [229, 235]], [[189, 203], [200, 211]], [[125, 130], [135, 148]], [[144, 150], [158, 173]], [[220, 236], [228, 230]], [[272, 285]],
              [[141, 145], [152, 159]], [[178, 195], [185, 190]], [[190, 209], [203, 204]], [[241, 251], [253, 269]], [[166, 181], [181, 195]], [[173, 177], [187, 192]], [[195, 211], [203, 208]], [[285, 293]],
              [[114, 118], [125, 128]], [[171, 181], [187, 192]], [[233, 242], [244, 258]], [[272, 279], [286, 310]], [[187, 205], [199, 207]], [[143, 149], [157, 168]], [[186, 194], [194, 205]], [[256, 265]],
              [[98, 105], [109, 118]], [[144, 155], [160, 162]], [[162, 170], [176, 181]], [[177, 189], [191, 195]], [[223, 233], [238, 244]], [[162, 176], [178, 192]], [[207, 214], [209, 217]], [[338, 361]],
              [[138, 143], [151, 166]], [[235, 248], [250, 264]], [[175, 186], [188, 201]], [[228, 237], [240, 255]], [[178, 194], [192, 208]], [[270, 291], [286, 310]], [[178, 183], [192, 201]], [[185, 199]],
              [[99, 105], [108, 116]], [[170, 174], [183, 194]], [[174, 175], [186, 200]], [[201, 214], [212, 225]], [[161, 165], [165, 166]], [[190, 208], [198, 207]], [[230, 237], [244, 265]], [[163, 173], [174, 183]], [[210, 217], [222, 238]], [[190, 196]],
              [[255, 262], [272, 292]], [[153, 166], [167, 179]], [[197, 211], [213, 223]], [[178, 187], [183, 194]], [[279, 281], [294, 317]], [[300, 314], [319, 343]], [[138, 146], [154, 162]], [[350, 365], [372, 403]], [[205, 212], [218, 221]], [[308, 326]],
              [[155, 167], [174, 189]], [[216, 218], [232, 239]], [[266, 272], [282, 289]], [[147, 150], [151, 164]], [[172, 176], [185, 192]], [[208, 216], [222, 229]], [[165, 178], [178, 193]], [[243, 256], [260, 270]], [[193, 212], [212, 218]], [[322, 323]],
              [[177, 178], [189, 199]], [[112, 120], [125, 137]], [[175, 187], [190, 208]], [[198, 205], [207, 220]], [[320, 346], [340, 347]], [[233, 253], [242, 254]], [[314, 323], [333, 338]], [[172, 186], [190, 200]], [[194, 196], [213, 233]], [[250, 264]]]

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
