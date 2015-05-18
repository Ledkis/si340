# -*- coding: utf-8 -*-

import numpy as np

def eucl_dist(x, y):
    """Compute the euclidian distance between vector x and y.
    """
    return np.sqrt(np.sum((x-y)**2))
    
def eval_distance_matrix(s1, s2,  d_eval = eucl_dist, debug = False):
    """Evaluate the distance matrix between the time series s1 and s2 using
    the distance d_eval.
    
    Parameter
    s1 -- time serie n°1    
    s2 -- time serie n°2
    d_val -- distance between s1(i) and s2(j)
            By default : d_val(i,j) = (s1(i)-s2(j))**2
    
    """
    
    nn = s1.shape[0]
    mm = s2.shape[0]
    
    if debug:
        print("s1=%s, s2=%s"%(s1.shape, s2.shape))
        
    
    #Initialisation of the distance matrix
    D = np.zeros((nn, mm));
    
    for i in range(nn):
        for j in range(mm):
            D[i, j] = d_eval(s1[i, :], s2[j, :])
            
    return D


def eval_cummuled_distance_matrix(D, gamma = 2, r = None, warping_window = lambda i,j,r : i-r<=j<=i+r):
    """Evaluate the cummuled distance matrix G from a distance matrix D
    
    Parameter
    r -- windows size for warping. If it is null we will not use the warping_window
    D -- distance matrix
    gamma -- diagonnal path ponderation
    r -- warping windows
    """
    
    #Use warping or not
    warp = False
    if r is not None:
        warp = True
    
    nn, mm = np.shape(D)
    G = np.zeros((nn, mm))
    
    for i in range(nn):
        for j in range(mm):
            #Initialisation
            if i == j == 0:
                G[i, j] = D[0, 0]
            else:
                if warp and warping_window(i, j, r):
                    continue;
                d = []
                if i > 0:
                    d.append(G[i-1, j] + D[i, j])
                if i > 0 and j > 0:
                    d.append(G[i-1, j-1] + gamma*D[i, j])
                if j > 0:
                    d.append(G[i, j-1] + D[i,j])
                G[i,j] = min(d)
    return G
    
def eval_time_normalized_dist(s1, s2, gamma, d_eval = eucl_dist, debug = False):
    """Compute the time normalized distance between two sequences s1 and s2
    
    Parameter
    d_eval -- mesure of distance used for evaluating the distance matrix
    """
    D = eval_distance_matrix(s1, s2, d_eval, debug=debug)
    G = eval_cummuled_distance_matrix(D, gamma)
    nn, mm = np.shape(G)
    time_normalized_dist = G[nn-1, mm-1] / (mm+nn)
    return time_normalized_dist
    
def dtw(A, s, debug = False):
    """Dtw algorithm to find from which sequence in the dict A the sequence s 
    is the closest.
    
    Parameter
    A -- Dictionnarie of sequences of the form : {'seq_name' : seq}
    """
    if debug:
        print("------------------------")
        print("----------DTW-----------")
    
    # List for all the dist associated to the seqs
    # d is of the form ("eq_name", dist)
    d = []
    for seq_name in A.keys():
        
        ref_seq = A[seq_name]

        dist = eval_time_normalized_dist(ref_seq, s, debug = False)
        
        d.append((seq_name, dist))
        
        if False and debug:        
            print("time_normalized_dist with %s = %s"%(seq_name, dist))
        
        
        
    closest_seq = min(d, key=lambda x: x[1])[0]
    
    if debug:
        print("The closest seq is : %s!"%closest_seq)
    
    return closest_seq
    
