function [confusion, accuracy, D] = evaluation_recognition(x, DTW_cback, gamma, protocol, varargin);

% [confusion, accuracy, D] = evaluation_recognition(x, DTW_cback, gamma, protocol);
%
% Evaluation en reconnaissance par validation croisée
%
% -- Entrée ------------- 
%
% x: matrice de paramètres (PARAM)
% DTW_cback: handle de la fonction de DTW implémentée (@DTW par exemple)
% gamma: valeur du paramètre gamma passé à la fonction DTW_cback
% protocol:  1: 3 folds, 2N/3 apprentissage, N/3 test
%            2: N folds, 1 apprentissage, N-1 test
%            3: 2 folds, N/2 apprentissage (locuteur 1), N/2 test (locuteur 2)
%
% -- Sortie ------------- 
%
% confusion: matrice de confusion
% accuracy : taux de reconnaissance
% D        : matrice de distance sur l'ensemble de la base

if length(varargin)==0,
    D = evaluation_distance_matrix(x, DTW_cback, gamma);
else,
    D = varargin{1};
end;

Ndigit = size(x, 1);
Nutt = size(x, 2);

if protocol==1,
    randomize = 1;
    NFOLDS = 3;
    split = floor(Nutt / NFOLDS);
elseif protocol==2,
    randomize = 1;
    NFOLDS = Nutt;
    split = Nutt-1;
else,
    randomize = 0;
    NFOLDS = 2;
    split = Nutt / 2;
end;    

rand('state',0);
folds = zeros(Ndigit, Nutt);
for i = 1:Ndigit,
    if randomize == 1,
        folds(i,:) = randperm(Nutt);
    else,
        folds(i,:) = 1:Nutt;
    end;
end;
confusion = zeros(Ndigit, Ndigit);
for fold = 1:NFOLDS,
    % Construit les ensembles de test et d'apprentissage
    train_set = [];
    test_set  = [];
    for i=1:Ndigit,
        for j=folds(i,1:split),
            test_set = [test_set; ((j-1) + (i-1) * Nutt)+1 i];
        end;
        for j=folds(i,(split+1):end),
            train_set = [train_set; ((j-1) + (i-1) * Nutt)+1 i];
        end;
        % Rotate
        folds(i,:) = [folds(i,(split+1):end) folds(i,1:split)];
    end;
    % Reconnaissance proprement dite
    for i=1:size(test_set,1),
        [k, ndx] = min(D(test_set(i,1), train_set(:,1)));
        confusion(test_set(i,2), train_set(ndx, 2)) = confusion(test_set(i,2), train_set(ndx, 2))+1;
    end;
end;
accuracy = sum(diag(confusion)) / sum(sum(confusion));