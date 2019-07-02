# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#importare librarii necesare
import pandas as pd


#PASUL 1: citire data cu panda 
dataset=pd.read_csv("/Users/horatiusicoie/Downloads/bonuri.csv")
dataset.describe()

#PASUL 2: Determinarea numarului de bonuri unice si produse unice din magazin
#Functia describe pentru a afla numarul de bonuri unice si produse unice din magazin
dataset.describe()

#PASUL 3:
#Distribuirea numerului de produse (min, max, std, quartile)
#Folosim functia count pentru a observa numarul de ocurente al produselor pe bonuri
#De asemenea, introducem un nou data frame care sa contina produsele sub forma de integers pentru a calcula min, max, std si quartile
count_dataset=pd.DataFrame(dataset.groupby("BID").count())
#df=dataset.pivot_table(index=["BID"], aggfunc="size")   
#ambele variante pot fi folosite pentru a vizualiza graficul .
#print(count_dataset)
count_dataset["NumeProdus"].min()
count_dataset["NumeProdus"].max()
count_dataset["NumeProdus"].std()
count_dataset["NumeProdus"].quantile()
count_dataset["NumeProdus"].mean()
#Distributia numarului de produse pe bonuri este una normala.

#4:
new_dataset=dataset.iloc[:, 0:2]
#remove index, transformare dataset in dictionar pentru a putea rezolva

dictionar_bonuri=new_dataset.groupby("BID")["NumeProdus"].apply(list).to_dict()
#nested_list=[{k: v} for k, v in new_dataset_1.items()]

#Creeare o functie cu parametrii stabiliti drept cele doua produse pe care le vom cauta .
def coaparitii_produse():
    for k,v in dictionar_bonuri:
#Am incercat sa fac un for loop pentru a itera prin toate bonurile, sa creez o variabila numita counter 
#ca atunci cand exista o coaparitie pe doua bonuri diferite dintre doua produse valoarea sa creasca  cu 1,
#iar daca nu, valoarea sa ramana neschimbata, functia va avea return counter. Acesta este rationamentul
#insa primesc Value Error. Am pus un comment mai sus am incercat sa fac cu un "nested list", nu am reusit nici asa

        
    
    
    
    
    
    








