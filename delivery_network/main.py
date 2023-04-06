
from graph import UnionFind
from graph import Graph, graph_from_file,temps_calcul_naif, temps_calcul_kruskal, power_min_kruskal, represente, dfs_initial, calcul_trajets_total, calcul_trajets_total2
from test import test_q4, test_kruskal
from camion import convert_to_list, glouton, enleve_camion_inutile, algo_naif, prog_dyn
"""## test q4
print(test_q4())

##test de la question 7##
G="input/network.00.in"
represente(G, 1, 2)
represente(G, 8, 6)

G1="input/network.01.in"
represente(G1, 1, 3) 
#represente(G1, 7, 3) #pas de chemin car 7 et 3 ne sont pas des composantes connectées 



##Question 10 du tp2##
print(temps_calcul_naif("input/network.1.in", "input/routes.1.in"))
#print("Avec le tp1, il faudrait " + str(temps_calcul_naif("input/network.2.in", "input/routes.2.in"))+" min pour le graphe 2")

#en faisant le test plusieurs fois, sur route.1.in et le graphe 1, on observe que le temps est très court (0.02 secondes)
#Si on prend la route 2 et le graphe 2, on voit que le temps nécessaire est entre 30h et 50h. C'est beaucoup trop long!!
#au-delà du graphe 2, c'est beaucoup trop long


## Question 14 ##
# On teste la fonction kruskal qu'on vient de créer
g1 = graph_from_file("input/network.00.in")
g2 = graph_from_file("input/network.01.in")
g3 = graph_from_file("input/network.02.in")
g4 = graph_from_file("input/network.03.in")

#On applique kruskal à nos graphes pour les transformer en arbre couvrant de poids minimal
print("Voici le graphe de kruskal issu du graphe 00", g1.kruskal())
# Pour ce g1, on obtient comme résultat : 
#The graph has 10 nodes and 9 edges.
#1-->[(8, 0, 1), (2, 11, 1), (6, 12, 1)]
#2-->[(5, 4, 1), (3, 10, 1), (1, 11, 1)]
#3-->[(4, 4, 1), (2, 10, 1)]
#4-->[(3, 4, 1), (10, 4, 1)]
#5-->[(2, 4, 1), (7, 14, 1)]
#6-->[(1, 12, 1)]
#7-->[(5, 14, 1)]
#8-->[(1, 0, 1), (9, 14, 1)]
#9-->[(8, 14, 1)]
#10-->[(4, 4, 1)]

#Ce graphe contient les 9 arrêtes qui demandent la puissance de camion 
# la plus faible et il connecte tous les nœuds sans faire de cycle 

print("Voici g2.kruskal()", g2.kruskal())
print("Voici g3.kruskal()", g3.kruskal())
print("Voici g4.kruskal()", g4.kruskal())

# On la test grâce à une fonction test test_kruskal()#
print(test_kruskal())


#g=(graph_from_file("input/network.1.in").kruskal())
#print(dfs_initial(g))

##test power_min_kruskal

g=(graph_from_file("input/network.1.in").kruskal())
print(power_min_kruskal(g, 11, 6, dfs_initial(g))==([11, 8, 20, 17, 6], 15))


##question 5 du tp2##
print("Le temps mis pour parcourir tous les trajets du graph 1 est ", temps_calcul_kruskal("input/network.1.in", "input/routes.1.in"), " secondes")
print("Le temps mis pour parcourir tous les trajets du graph 2 est ", temps_calcul_kruskal("input/network.2.in", "input/routes.2.in"), " secondes")
print("Le temps mis pour parcourir tous les trajets du graph 3 est ", temps_calcul_kruskal("input/network.3.in", "input/routes.3.in"), " secondes")
print("Le temps mis pour parcourir tous les trajets du graph 4 est ", temps_calcul_kruskal("input/network.4.in", "input/routes.4.in"), " secondes")
print("Le temps mis pour parcourir tous les trajets du graph 5 est ", temps_calcul_kruskal("input/network.5.in", "input/routes.5.in"), " secondes")
print("Le temps mis pour parcourir tous les trajets du graph 6 est ", temps_calcul_kruskal("input/network.6.in", "input/routes.6.in"), " secondes")
print("Le temps mis pour parcourir tous les trajets du graph 7 est ", temps_calcul_kruskal("input/network.7.in", "input/routes.7.in"), " secondes")
print("Le temps mis pour parcourir tous les trajets du graph 8 est ", temps_calcul_kruskal("input/network.8.in", "input/routes.8.in"), " secondes")
print("Le temps mis pour parcourir tous les trajets du graph 9 est ", temps_calcul_kruskal("input/network.9.in", "input/routes.9.in"), " secondes")
print("Le temps mis pour parcourir tous les trajets du graph 10 est ", temps_calcul_kruskal("input/network.10.in", "input/routes.10.in"), " secondes")
#on trouve des temps beaucoup plus courts. Par exemple pour le premier, on trouve 0.0020 sec
#pour le second, on trouve environ 10 secondes
#pour le troisième, on trouve environ 1min10
#pour le 5eme, 22 secondes ..
#Les 10 trajets mettent moins de 2 min chacun!
#on trouve donc des temps bien plus courts!!

# On trouve des temps bcp plus courts dans la question 15 que dans la question 10 car on utilise l'algorithem de Kruskal
#on passe de 30h pour le graphe 2 à seulement quelques secondes





##Question 16
#on crée les fichiers
#for i in range (1,11) :
    #print(calcul_trajets_total(i))"""

##question 18
"""for i in range (1,11) :
    print(calcul_trajets_total2(i))"""
#print(glouton("input/network.5.in", "input/routes.5.2.out", "input/trucks.1.in"))
#print(prog_dyn("input/network.2.in", "input/routes.2.2.out", "input/trucks.1.in"))
#pas optimal
#print(enleve_camion_inutile("input/trucks.2.in"))

"""ici on teste l'algorithme naif sur un petit graphe qu'on a cree, on voit que c'est beaucoup trop long"""

#print(algo_naif("input/network.00.in", "input/routes.00.2.out", "input/trucks.0.in"))
#print(convert_to_list("input/routes.5.2.out", False))



#enleve_camion_inutile("input/trucks.2.in")


##resultat pour l'algorithme glouton
for i in range(1,11) :
    for j in [0,1] :
                print(glouton("input/routes."+str(i)+".2.out", "input/trucks."+str(j)+".in"))    
    print(glouton("input/routes."+str(i)+".2.out", "input/trucks.22.out"))