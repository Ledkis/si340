# -*- coding: utf-8 -*-

import numpy as np

FOLDER_PATH = "dat/"

RESULT_FOLDER_PATH = "res/"

def getMailsData():
    mails = open(FOLDER_PATH + "mail.lst", "r").read().split("\n")[:-1] # On prend pas la dernière ligne
    
    data = []
    for datPath in mails:
        vect = [int(val) for val in open(FOLDER_PATH + datPath, "r").read().split("\n")[:-1]]
        data.append(np.array(vect))
    
    return data
    

def codeur(mailFile):
    data = []
    
    for line in mailFile.read().split("\n")[:-1]:
        for char in line:
            ascii = ord(char)
            if ascii < 256:
                data.append(ord(char))
    
    return np.array(data)
    
    
    
def datFileToNpArray(datFile):
    data = []
    
    for line in datFile.read().split("\n")[:-1]:
        data.append([float(val) for val in  line.split("\t")])
        
    return np.array(data)
    

def segment(mailFile, mailName, index):
    newMail = []
    mailData = mailFile.read().split("\n")
    
    charCount = 0
    for line in mailData:
        newCharCount = charCount + len(line)
        if index > charCount and index < newCharCount:
            lineIndex = newCharCount - index
            newMail.append(line[:lineIndex])
            newMail.append("\n****************************************** HERE *****************************************\n")
            newMail.append(line[lineIndex:])
        else:
            newMail.append(line)
        charCount = newCharCount
            
    
    resFile = open(RESULT_FOLDER_PATH + mailName, "w")
    
    for line in newMail:
        resFile.write(line +"\n")
            
            
    resFile.close()
    

        
    
    
def verterbi(O, A, B, pi, N, T):
    """
    O: Vecteur d'observation
    A: Matrice de transition
    B: Matrice de distribution de probabilité d'observation des symboles selon l'état
    pi: Probabilité des états à l'état initial
    N: Nombre d'état
    T: Nombre d'observation
    """
    
    # On passe tout en log
    
    A = np.log(A)
    B = np.log(B)
    pi = np.log(pi)
    
    
    # Preparation
    
    delta = np.zeros((T, N))
    phi = np.zeros((T, N))
    
    q_ideal = np.zeros(T)
    
    
    # Initialisation
    
    o_0 = O[0] # 1er observation
    
    for i in range(N):
        delta[0, i] = pi[i] + B[i, o_0]
        
    phi[0, :] = np.zeros((1, N))
    
    
    # Récursion
    
    for t in range(1, T-1):
        for j in range(N):
            o_t = O[t]
            bo_t = B[j, o_t]
            v = delta[t-1, :] + A[:, j]
            delta[t, j] = np.max(v) + bo_t
            phi[t, j] = np.argmax(v)
            
    # arrêt
            
    q_ideal[T-1] = np.argmax(phi[T - 2, :])
            
    
    # retropopagation
    
    for t in reversed(range(T-1)):
        q_ideal[t] = phi[t, q_ideal[t+1]]
        
    
    return q_ideal
    


## Application


A = np.array([[0.999218078035812,  0.000781921964187974],
             [0, 1]])
        
B = np.transpose(datFileToNpArray(open(FOLDER_PATH + "P.dat", "r")))

pi = np.array([1, 0])

N = 2

    
def vertabiOnMail(mailName, A, B, pi, N):
    
    
    mailData = codeur(open(FOLDER_PATH + mailName, "r"))
    T = len(mailData)
    print("mail: %s, size=%s, data=%s"%(mailName, T, mailData))
    path = verterbi(mailData, A, B, pi, N, T)
    index = np.where(path==1)[0][0]
    print("index=%s"%index)
    segment(open(FOLDER_PATH + mailName, "r"), mailName, index)
    
# ouput in res/ folder
    
for i in range(1, 31):
    vertabiOnMail("mail%s.txt"%i, A, B, pi, N)