# -*- coding: utf-8 -*-
"""
SY32 : Vision et apprentissage
Printemps 2020

TD01 : Apprentissage automatique
"""

import numpy as np

class CatClassifier():
    """ Classifieur de chats 
    
    On distingue deux types de chat : type A (-1) et type B (+1).
    On classifie les chats en fonction de leur poids x à l'aide du classifier
    f_h défini telle que : f_h(x) = -1 si x <= h et +1 sinon.
    
    Parameters
    ----------
    
    Attributes
    ----------
    h_hat : float
            Valeur optimale de h.
    
    """
    
    h_hat = -np.Inf
    
    def __init__(self):
        pass
    
    def predict(self, X, h=None):
        """
        Prédit le type de chat pour les poids X et le paramètre h
        
        Parameters
        ----------
        X : array-like of shape (n_sample, n_features)
            Poids des chats
        
        h : float (default=h_hat)
            Paramètre de décision 
        
        Returns
        -------
        y : array-like of shape (n_samples,)
            Type des chats
        """
        if h is None:
            h = self.h_hat
        
        y = []

        for item in X:
            if item <= h :
                y.append(-1)
            else:
                y.append(1)

        print(y)

        return np.array(y)
    
    def err_emp(self, X, y, h=None):
        """
        Calcule l'erreur empirique de f_h sur l'ensemble (X,y).

        Parameters
        ----------
        X : array-like of shape (n_sample, n_features)
            Poids des chats
            
        y : array-like of shape (n_samples,)
            Type des chats
            
        h : float (default=h_hat)
            Paramètre de décision 

        Returns
        -------
        erreur : float
                 Erreur empirique

        """
        if h is None:
            h = self.h_hat
        
        # TODO
        
        pass
    
    def fit(self, X, y):
        """
        Calcule la valeur optimale de h sur l'ensemble (X,y).
        L'attribut h_hat est mis à jour.'
        
        Parameters
        ----------
        X : array-like of shape (n_sample, n_features)
            Poids des chats
        
        y : array-like of shape (n_samples,)
            Type des chats
        
        Returns
        -------
        self : object
        """
        
        # TODO
        
        return self
        pass