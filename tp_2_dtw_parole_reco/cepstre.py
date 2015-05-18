# -*- coding: utf-8 -*-
"""
Created on Mon May 18 10:09:47 2015

@author: Utilisateur
"""

import numpy as np

def cepstre(sig, fen, overlap, p):
    """Calcul le cepstre d'un signal sig
    
    Parameter
    sig -- Signal concidéré
    fen -- fenêtre appliqué au signal
    overlap -- Valeur de l'overlap
    p -- ordre des cepstres
    
    Return
    matrice (N,p) contenans en ligne les vecteurs cepstraux
    """

    N = len(sig)
    m = len(fen)
    
    #nombre de patchs
    npatch = int(np.floor((N-m)/overlap) + 1)
        
    sig_cepstre = np.zeros((npatch, p))
    
    for i in range(npatch):
        sig_fen = fen*sig[i*overlap : i*overlap + m]
        sig_f = np.fft.fft(sig_fen, p)
        sig_cepstre[i,:] = np.real(np.fft.ifft(np.log(np.abs(sig_f))))
        
    return sig_cepstre
        

if __name__  == "__main__":
    import scipy.io

    SIG = scipy.io.loadmat('sig.mat')['SIG']
    
    fen = np.hamming(256)
    sig = SIG[0,0][:, 0]
    p = 10
    overlap = 128
    
    sig_cep = cepstre(sig, fen, overlap, p)
    
    print(sig_cep.shape)