# -*- coding: utf-8 -*-
"""
Created on Wed May 20 09:12:13 2015

@author: Utilisateur
"""

import numpy as np
import scipy.io

from period import period


def analysisPitchMarks(s,Fs):
    """
    Extrait les marques d’analyse.
    
    Parameters
    s -- signal à analyser
    Fs --  fréquence d’échantillonnage
    
    Return
    A  -- Matrice contenant les instants et les pitchs associés à chaque marque
    d’analyse.
    
    Plus précisément, A sera constituée de trois lignes, telles que 
    A(1,n) = t_a(n) est l’instant associé à la n eme marque d’analyse,
    A(2,n) = voise(n) est un booléen qui indique si le signal est voisé ou non
    au voisinage de cette marque, et
    A(3,n) = P_a(n) est le pitch associé à cette même marque
    (c’est à dire la période en nombre d’échantillons)
    dans le cas voisé, ou vaut 10ms dans le cas non voisé.
    
    Précisons maintenant comment déterminer les marques d’analyse.
    Par souci de simplicité, nous ne chercherons pas à aligner la marque
    t_a(n) sur le début d’une onde glottique.
    
    Pour calculer P_a(n) et t_a(n), on procédera par récurrence sur n ≥ 1 :
    – extraction d’une séquence x qui commence à l’instant t_a(n − 1),
    et dont la durée est égale à 2.5*P_a(n − 1) ;
    – calcul de P_a(n) et voise(n) à l’aide de la fonction periode ;
    – calcul de t_a(n) = t a (n − 1) + P a (n).
    L’algorithme sera initialisé en posant t_a(0) = 1 et P_a(0) = 10ms.
    """
    pass