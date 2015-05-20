# -*- coding: utf-8 -*-
"""
Created on Wed May 20 10:24:30 2015

@author: Utilisateur
"""

import numpy as np

def nextpow2(x):
    m_f = np.log2(np.abs(x))
    m_i = np.ceil(m_f)
    return m_i.astype(int)

def period(x, Fs, Pmin = 1/300, Pmax = 1/80, seuil = 0.7):
    """
    function [P,voise] = periode(x,Fs,Pmin,Pmax,seuil);
    [P,voise] = periode(x,Fs,Pmin,Pmax);
    Si voise = 1, P est la période du signal x en nombre d'échantillons 
    Si voise = 0, P est égal à 10ms.Fs
    
    Renvoie un couple [P, voise] ou voise est un booléen qui indique si x est 
    voisé ou non, et P est la période en nombre d’échantillons dans le cas 
    voisé, ou vaut 10ms dans le cas non voisé.
    """
    
    nn, mm = x.shape
    
    x = x.reshape(nn*mm, order='F')
    x = x - np.mean(x)
    N = x.shape[0]
    
    Nmin = np.ceil(Pmin*Fs)
    Nmax = np.floor(Pmax*Fs)
    Nmax = np.min((Nmax,N))
    
    Nfft = 2** nextpow2(2*N-1)
    X = np.fft.fft(x, Nfft)
    S = (X * np.conj(X)) / N
    r = np.real(np.fft.ifft(S))
    
    rmax,I = np.max(r[Nmin-1:Nmax-1]), np.argmax(r[Nmin-1:Nmax-1])
    P = I + Nmin - 2
    corr = (rmax/r[0]) * (N/(N-P))
    voise = corr > seuil
    
    if not voise:
        P = np.round(10e-3*Fs)
    
    return voise, P
    
if __name__ == "__main__":
    import scipy.io
    
    x = scipy.io.loadmat('aeiou.mat')['s']
    Fs = 22050
    
    Pmin = 1/300
    Pmax = 1/80
    seuil = 0.7
    
    voise, P = period(x, Fs)