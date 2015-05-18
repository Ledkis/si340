# TP 1 HMM

Modules:
- [tp_HMM.py](https://github.com/Ledkis/si340/blob/master/tp_1_hmm/tp_HMM.py)

Data folder:
- [dat](https://github.com/Ledkis/si340/tree/master/tp_1_hmm/dat)

Result folder:
- [res](https://github.com/Ledkis/si340/tree/master/tp_1_hmm/res)

## Travail � r�aliser

Cf module [tp_HMM.py](https://github.com/Ledkis/si340/blob/master/tp_1_hmm/tp_HMM.py)

Les r�sultats des mails segment� en en t�te et corps par l'algorithme de viterbi sont donn�s dans le dossier res


## Pour aller plus loin

### 1

Pour une mod�lisation des mails en plus de deux parties :  
en-t�te, corps, signature, il faudrait rajouter le nombre d'�tat correspondant 
(N en tout) � la mod�lisation du probl�me.

Il faudrait ainsi compl�ter la matrice A de transition entre ces diff�rents 
�tats, la matrice B de distribution de probabilit� d'observation des symboles 
selon l'�tat et le vecteur pi des probabilit� des �tats initiaux

Cela n�cessiterais une phase d'apprentissage pour �valuer A et B.

### 2

En sachant que les portions de mails d�butent toujours par le caract�re ">", 
on pourrait re-mod�liser en le probl�me en modifiant la matrice B et en rajoutant 
une pond�ration plus grande � ce caract�re pour l'�tat correspondant. 


### 3

Non trait�
