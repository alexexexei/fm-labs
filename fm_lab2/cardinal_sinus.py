from static import cardinal_sinus, a_b_pars, intervals, colors_strs
from builder import build_f_t, build_fimg

f_t_1 = cardinal_sinus(a_b_pars[0][0], a_b_pars[0][1])
f_t_2 = cardinal_sinus(a_b_pars[1][0], a_b_pars[1][1])
f_t_3 = cardinal_sinus(a_b_pars[2][0], a_b_pars[2][1])

build_f_t(f_t_1, colors_strs[0], None)
build_f_t(f_t_2, colors_strs[0], None)
build_f_t(f_t_3, colors_strs[0], None)
build_fimg(f_t_1, intervals[0], colors_strs[1], None)
build_fimg(f_t_2, intervals[0], colors_strs[1], None)
build_fimg(f_t_3, intervals[0], colors_strs[1], None)