# TP 2 Reconnaissance de Parole

Modules: 
- [tp_2.py](https://github.com/Ledkis/si340/blob/master/tp_2_dtw_parole_reco/tp_2_DTW_parole_reco.py)
- [cepstre.py](https://github.com/Ledkis/si340/blob/master/tp_2_dtw_parole_reco/cepstre.py)
- [dtw.py](https://github.com/Ledkis/si340/blob/master/tp_2_dtw_parole_reco/dtw.py)

Data:
- sig.mat

Result folders:
- [changement de la fonction de calcul de distance](https://github.com/Ledkis/si340/tree/master/tp_2_dtw_parole_reco/res_d_eval)
- [changement de la fonction de la valeur de gamma](https://github.com/Ledkis/si340/tree/master/tp_2_dtw_parole_reco/res_p)
- [changement de la fonction de la valeur de l'ordre du cepstre](https://github.com/Ledkis/si340/tree/master/tp_2_dtw_parole_reco/res_gamma)

## 2 Paramétrisation 

Cf module [cepstre.py](https://github.com/Ledkis/si340/blob/master/tp_2_dtw_parole_reco/cepstre.py)

## 3 - Alignement temporel par programmation dynamique

Cf module [dtw.py](https://github.com/Ledkis/si340/blob/master/tp_2_dtw_parole_reco/dtw.py)

## 4 - Application aux données de parole

### 1

Grace à la fonction eval_err_mat() du module  [tp_2.py](https://github.com/Ledkis/si340/blob/master/tp_2_dtw_parole_reco/tp_2_DTW_parole_reco.py)
on obtient les matrices err_MAT suivante :

Pour rappel de eval_err_mat():

```python
def eval_err_mat():
    """ calcule la matrice d'erreur err_MAT où le coefficient i,j donne le nombre
    d'erreur lorsque l'on a cherche pour un signal à le comparer à l'ensemble
    des autres signaux. 
    
    Une erreur correspond au moment ou on se trompe de catégorie pour un signal 
    donné, c'est à dire pour un signal d'une ligne i, dire que sur une même colonne
    il se rapproche plus d'un signal d'une autre ligne.
    
    Concrêtement que pour une prononciation de test "0", il a trouver par exemple
    sur une colonne un "6" plus proche que la prononciation "0" de 
    cette même colonne (dont la prononciation est évidement différente 
    de celle de la prononciation de test, mais normalement plus proche que
    celle du "6").
    
    """
```

pour Gamma = 1, p = 10 sur les signaux SIGs : 

```python
np.array([[ 0,  2,  1,  1,  3,  6,  2,  2,  3,  3,  3,  9],
       [ 4,  4,  8,  8,  9,  6, 10, 10,  9,  7, 10, 10],
       [ 6,  7,  5,  9, 10, 10,  8,  7, 10, 11, 10, 10],
       [10,  8,  7, 10,  8,  7, 10, 11,  8, 11, 10, 10],
       [ 8,  8,  8,  9,  7, 11, 10, 10,  8,  7,  9, 10],
       [ 7,  9,  7,  5,  5,  8,  8,  8,  5,  9,  8,  9],
       [ 4,  5,  8,  5,  5,  4,  5, 10,  8,  7, 10,  5],
       [11, 10,  8,  7,  4,  5,  5,  6,  5,  7,  7,  7],
       [11,  7,  8,  3,  2,  8,  3,  2,  5,  5,  4,  3],
       [10,  8,  9,  9,  7,  8,  7,  7,  9,  5, 10,  7]])
```
	   
Pour le signal SIG{0, 0} le résultat est très satisfaisant car l'on ne s'est pas
trompé une fois, ce qui n'est pas le cas pour l'ensemble des autres signaux, 
où finalement l'erreur total est très élevé : **59%**.

On pourra noter au passage que l'utilisation des cepstres accélère grandement le 
calcul des distance

### 2 - Influence de gamma : 

Pour Gamma = 2, p = 10 on obtient la matrice err_MAT suivante 

```python	   
np.array([[ 3,  5,  3,  8,  6,  8,  5,  7,  8,  8,  6, 10],
       [ 8,  8, 11,  7,  9, 11, 11, 10, 10, 10, 10, 10],
       [ 8,  9,  9,  9, 10, 11, 10,  9, 10, 10, 10, 10],
       [11, 11, 11, 11, 10, 10, 11, 11, 11, 11, 11, 10],
       [10, 10, 10, 10,  8, 10, 10, 11, 10,  8,  9, 10],
       [ 9,  9,  9, 10,  9, 10, 10,  9, 10, 10,  9, 10],
       [ 6,  8, 10,  9,  9,  8,  7,  9,  8,  7,  9, 10],
       [11,  8,  9,  7,  4,  5,  5,  7,  6,  6,  7,  7],
       [ 4,  9,  6,  4,  3,  6,  4,  2,  6,  4,  4,  4],
       [ 9,  9, 10, 10,  7, 11,  8,  9, 10,  8,  9, 10]])
```   
Dont le pourcentage d'erreur total est 70%. Pour gamma = 3 l'erreur monte à **75.9%**.

Aussi uniquement pour le SIG{0, 0}, on obtient avec gamma entre 1 et 5 la suite
d'erreur suivante : 0, 3, 7, 9, 10.

Enfin quelques images des matrices res et res_abs sont disponibles dans le dossier
res_gamma.

Tout cela nous permet de dire que gamma à une grande influence sur sur les scores
de similarité, en augmentant leur taux d'erreur lorsque sa valeur augmente.

Les meilleurs résultats sont obtenus pour gamma = 1.


### 3 - L'utilisation de la distance euclidienne implicite le fait que l'on soit dans
un espace euclidien.

(Reste non compris )

## 5 - Evaluation de la reconnaissance - Non traité