# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import dtw
import cepstre as cp

import numpy as np
import matplotlib.pylab as plt
import scipy.io

#Data Init

SIG = scipy.io.loadmat('sig.mat')['SIG']

fen = np.hamming(256)
p = 10
overlap = 128

gamma = 2

def eval_dist_on_sigs(SIG, index_ref, p, gamma, d_eval= dtw.eucl_dist):
    """
    
    Parameter
    SIG - La matrics contenant l'ensemble des signaux rangés dans chacunes de ses
            cases
    index_ref -- index dans la matrics SIG du signal de test, que l'on va venir
            comparer à tous les autres
    d_eval -- Distance utilisé pour calculer la matrice des distances
    
    Return
    res -- matrics des distance du signal de test à l'ensemble des autres
            singaux
    res_abs -- matrice ou pour chaque colonne donne un 1 pour le signal ayant
            une distance minimal avec le signal de test, 0 pour les autres
    err -- Nombre d'erreur, c'est à dire le nombre de fois où la plus petite
            distance entre le signal de test est autre signal pour une colonne ne se
            trouvais pas dans le ligne du signal de test
            
    err_p -- Pourcentage d'erreur
    """
    
    lign_ref, col_ref = index_ref
    
    # On récupère le signal de référence
    ref_sig = SIG[index_ref][:,0]
    
    # On calcul son cepstre
    ref_sig_cep = cp.cepstre(ref_sig, fen, overlap, p)
    
    res = np.zeros((SIG.shape))
    res_abs = np.zeros((SIG.shape))
    
    for col in range(SIG.shape[1]):
        
        # Evaluate res
        for ligne in range(SIG.shape[0]):
            sig_cep = cp.cepstre(SIG[ligne,col][:, 0], fen, overlap, p)
            dist = dtw.eval_time_normalized_dist(sig_cep, ref_sig_cep, gamma, d_eval)
            res[ligne, col] = dist
        
        # Evaluate res_abs
        argmin = np.argmin(res[:, col])    
        err = 0
        for ligne in range(SIG.shape[0]):
            if ligne == argmin:
                res_abs[ligne, col] = 1
            else:
                res_abs[ligne, col] = 0
     
     # Evaluate err           
    err = res_abs[lign_ref, :].size - np.sum(res_abs[lign_ref, :])
    
    # Evaluate err_p
    err_p = err*100/SIG.shape[1]
                
    return res, res_abs, err, err_p
    

def test_gamma():
    """ Test pour différentes valeur de gamma
    """
    plt.figure()
    for gamma in range(1, 20):
        res, res_abs, err, err_p = eval_dist_on_sigs(SIG, (0, 0), p, gamma)
        print(err)
#        plt.matshow(res)
#        plt.title("gamma = %s"%gamma)
#        plt.savefig("resGamma/gamma_%s.png"%gamma)
#        plt.matshow(res_abs)
#        plt.title("gamma = %s"%gamma)
#        plt.savefig("resGamma/gamma_%s_abs.png"%gamma)
        
def test_p():
    """ Test pour différentes valeur de p
    """
    plt.figure()
    gamma = 1
    for p in range(1, 20):
        res, res_abs, err, err_p = eval_dist_on_sigs(SIG, (0, 0), p, gamma)
        print(err_p)
#        plt.matshow(res)
#        plt.title("p = %s (gamma=%s)"%(p, gamma))
#        plt.savefig("res_p/p_%s.png"%(p))
#        plt.matshow(res_abs)
#        plt.title("p = %s (gamma=%s)"%(p, gamma))
#        plt.savefig("res_p/p_%s_abs.png"%(p))
        
def test_d_eval():
    """ Test pour différentes fonctions d_eval
    """
    gamma = 1
    p = 10
    for expo in range(1, 20):
        d_eval = lambda x,y : np.sqrt(np.sum((x-y)**expo))
        res, res_abs, err, err_p = eval_dist_on_sigs(SIG, (0, 0), p, gamma, d_eval)
        print(err_p)
#        plt.matshow(res)
#        plt.title("expo = %s (p=%s,gamma=%s)"%(expo, p, gamma))
#        plt.savefig("res_d_eval/expo_%s.png"%(expo))
#        plt.matshow(res_abs)
#        plt.title("expo = %s (p=%s,gamma=%s)"%(expo, p, gamma))
#        plt.savefig("res_d_eval/expo_%s_abs.png"%(expo))

def eval_err_mat():
    """ calcule la matrice d'erreur err_MAT où le coefficient i,j donne le nombre
    d'errreur lorsque l'on a cherche pour un signal à le comparer à l'ensemble
    des autres signaux. 
    
    Une erreur correspond au moment ou on se trompe de catégorie pour un signal 
    donné, c'est à dire pour un signal d'une ligne i, dire que sur une même colonne
    il se rapproche plus d'un signal d'une autre ligne.
    
    Concrêtement que pour une prononciation de test "a", il a trouver par exemple
    sur une colonne un "b" plus proche que la prononciation "a" de 
    cette même colonne (dont la prononciation est évidement différente 
    de celle de la prononcation de test, mais normalement plus proche que
    celle du "b").
    
    Le paramètre err_p_total correspond au pourcentage d'erreur total
    
    """
    
    
    err_MAT = np.zeros(SIG.shape)
    for i in range(SIG.shape[0]):
        for j in range (SIG.shape[1]):
            res, res_abs, err, err_p = eval_dist_on_sigs(SIG, (i, j), p, gamma)
            err_MAT[i, j] = err
            print("%s  (err for i=%s, j=%s)"%(err, i,j))
    err_p_total = (np.sum(err_MAT)/err_MAT.size)*100/SIG.shape[1]
    return err_MAT, err_p_total
    
# err_MAT, err_p = eval_err_mat()