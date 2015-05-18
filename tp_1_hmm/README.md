## Travail à réaliser

Cf module tp_HMM.py

Les résultats des mails segmenté en en tête et corps par l'algorithme de viterbi sont donnés dans le dossier res


## Pour aller plus loin

1 -

Pour une modélisation des mails en plus de deux parties :  
en-tête, corps, signature, il faudrait rajouter le nombre d'état correspondant 
(N en tout) à la modélisation du problème.

Il faudrait ainsi compléter la matrice A de transition entre ces différents 
états, la matrice B de distribution de probabilité d'observation des symboles 
selon l'état et le vecteur pi des probabilité des états initiaux

Cela nécessiterais une phase d'apprentissage pour évaluer A et B.

2  -

En sachant que les portions de mails débutent toujours par le caractère ">", 
on pourrait re-modéliser en le problème en modifiant la matrice B et en rajoutant 
une pondération plus grande à ce caractère pour l'état correspondant. 


3 -

