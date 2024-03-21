from static import double_attenuation, a_b_pars, intervals
from builder import build_f_t, build_fimg

f_t_1 = double_attenuation(a_b_pars[0][0], a_b_pars[0][1])
f_t_2 = double_attenuation(a_b_pars[1][0], a_b_pars[1][1])
f_t_3 = double_attenuation(a_b_pars[2][0], a_b_pars[2][1])

build_f_t(f_t_1, 'red', None)
build_f_t(f_t_2, 'red', None)
build_f_t(f_t_3, 'red', None)
build_fimg(f_t_1, intervals[1], 'purple', None)
build_fimg(f_t_2, intervals[1], 'purple', None)
build_fimg(f_t_3, intervals[1], 'purple', None)