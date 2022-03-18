import pickle

with open('model_pickle', 'rb') as file:  
    arbre = pickle.load(file)
    print(arbre.predict([[1995, 10000, 5]]))

