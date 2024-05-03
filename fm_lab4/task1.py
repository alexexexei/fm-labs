import numpy as np
import matplotlib.pyplot as plt


def build_f(xfunc, yfunc, fz1=16,
            fz2=5, clr=None, ttl=None,
            grid=True, xlab=None, ylab=None,
            xl1=None, xl2=None, yl1=None,
            yl2=None):
    plt.plot(xfunc, yfunc, color=clr)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.xlim(xl1, xl2)
    plt.ylim(yl1, yl2)
    plt.title(ttl)
    plt.gcf().set_size_inches(fz1, fz2)
    plt.grid(grid)
    plt.show()


def apply_noise(y, a, t):
    return y + a * (np.random.rand(len(t)) - 0.5)


def trapz(y, t, v):
    Y = []
    for k in v:
        Y_k = np.trapz(y * np.exp(-1j * 2 * np.pi * k * t), t)
        Y.append(Y_k)
    return Y


def undo_trapz(Y, t, v):
    y = []
    for k in t:
        y_k = np.trapz(Y * np.exp(1j * 2 * np.pi * k * v), v)
        y.append(y_k)
    return y


def numerical_diff(y, dt):
    ndiff = []
    for k in range(len(y) - 1):
        ndiff_k = (y[k + 1] - y[k]) / dt
        ndiff.append(ndiff_k)
    return ndiff


def spectral_diff(y, t, v):
    Y = trapz(y, t, v)
    dY = 2 * np.pi * 1j * v * Y
    spdiff = undo_trapz(dY, t, v)
    return spdiff, Y


T = 200
dt = 0.25
t = np.arange(-T / 2, T / 2 + dt, dt)
y = np.sin(t)

a = 0.2
y = apply_noise(y, a, t)

ndsin = numerical_diff(y, dt)

V = 1 / dt
dv = 1 / T
v = np.arange(-V / 2, V / 2 + dv, dv)
spdsin, Y = spectral_diff(y, t, v)

tdcos = -np.sin(t)

ndsin.append(y[-1] / 2)
spdsin = np.array(spdsin)
Y = np.array(Y)


build_f(t, y, ttl=f'Noisy sine, a={a}, dt={dt}', xlab='Time', ylab='Amplitude')
build_f(t, ndsin, ttl=f'Numerical derivative of sine, a={a}, dt={dt}',
        xlab='Time', ylab='Amplitude')

build_f(t, spdsin.real, ttl=f'Real part of spectral derivative of sine, a={a}, dt={dt}',
        xlab='Time', ylab='Amplitude')
build_f(t, spdsin.imag, ttl=f'Imaginary part of spectral derivative of sine, a={a}, dt={dt}',
        xlab='Time', ylab='Amplitude')
build_f(v, Y.real, ttl=f'Real part of Fourier image of sine, a={a}, dt={dt}',
        xlab='Frequency', ylab='Amplitude')
build_f(v, Y.imag, ttl=f'Imaginary part of Fourier image of sine, a={a}, dt={dt}',
        xlab='Frequency', ylab='Amplitude', xl1=-0.763, xl2=0.763)

plt.plot(t, ndsin, label='Num. der. of sine')
plt.plot(t, spdsin.real, label='Re. spec. der. of sine')
plt.plot(t, tdcos, color='r', label='True der. of cosine')
plt.title(f'True der. of cosine, num. der. of sine and spec. der. of sine comparison; a={a}, dt={dt}')
plt.gcf().set_size_inches(16, 5)
plt.grid(True)
plt.legend()
plt.show()