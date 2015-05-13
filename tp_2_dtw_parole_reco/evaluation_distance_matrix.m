function dista = evaluation_distance_matrix(x, DTW_cback, gamma);

% D = evaluation_distance_matrix(x, DTW_cback, gamma);
%
% Calcule la matrice de distance globale D
%
% x: vecteur de paramètres (PARAM)
% DTW_cback: handle de la fonction de DTW implémentée (@DTW par exemple)
% gamma: valeur du paramètre gamma passé à la fonction DTW_cback
%

Ndigit = size(x, 1);
Nutt = size(x, 2);

N = Ndigit*Nutt;

dista = zeros(N,N);

for i=1:N,
    for j=i:N,
        figure_i = floor((i-1) / Nutt)+1;
        utterance_i = mod ((i-1) ,Nutt)+1;
        figure_j = floor((j-1) / Nutt)+1;
        utterance_j = mod ((j-1) ,Nutt)+1;
        dista(i,j) = feval(DTW_cback, x{figure_i, utterance_i}, x{figure_j, utterance_j}, gamma);
        dista(j,i) = dista(i,j);
    end;
end;