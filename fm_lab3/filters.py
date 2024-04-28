import numpy as np

from help import get_U


def filter_U(u: list, freqs: list, v_0, filter):
    flt_U = get_U(u)
    for i in range(len(freqs)):
        freq = freqs[i]
        if filter(freq, v_0):
            flt_U[i] = 0

    return flt_U


def high_filter(freq, v_0):
    if -v_0 <= freq <= v_0:
        return False
    return True


def low_filter(freq, v_0):
    if -v_0 <= freq <= v_0:
        return True
    return False


def special_filter(freq, v_0: list):
    for i in range(len(v_0)):
        if v_0[i][0] <= freq <= v_0[i][1]:
            return True
    return False


def special_filter2(freq, v_0: list):
    return not special_filter(freq, v_0)


def filter_high(freqs: list, u: list, v_0):
    if isinstance(v_0, list) or \
            len(freqs) <= 0 or \
            len(u) <= 0:
        return None

    flt_U = filter_U(u, freqs, v_0, high_filter)
    flt_u = np.fft.ifft(np.fft.ifftshift(flt_U))
    return flt_u, flt_U


def filter_low(freqs: list, u: list, v_0):
    if isinstance(v_0, list) or \
            len(freqs) <= 0 or \
            len(u) <= 0:
        return None

    flt_U = filter_U(u, freqs, v_0, low_filter)
    flt_u = np.fft.ifft(np.fft.ifftshift(flt_U))
    return flt_u, flt_U


def filter_special(freqs: list, u: list, v_0: list):
    if not isinstance(v_0, list) or \
            len(v_0) <= 0 or \
            len(freqs) <= 0 or \
            len(u) <= 0:
        return None

    flt_U = filter_U(u, freqs, v_0, special_filter)
    flt_u = np.fft.ifft(np.fft.ifftshift(flt_U))
    return flt_u, flt_U


def filter_special2(freqs: list, u: list, v_0: list):
    if not isinstance(v_0, list) or \
            len(v_0) <= 0 or \
            len(freqs) <= 0 or \
            len(u) <= 0:
        return None

    flt_U = filter_U(u, freqs, v_0, special_filter2)
    flt_u = np.fft.ifft(np.fft.ifftshift(flt_U))
    return flt_u, flt_U