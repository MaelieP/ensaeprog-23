##Première idée
#ici on voit les camions comme les objets. On définit alors camions comme étant l'équivalent des objets du problème du sac à dos.
#  On définit alors une utilité qui est la somme des utilités des trajets que le camion peut faire
#il faut trier les camions par prix 
#il semblerait que cette façon de faire ne donne pas du tout les bons résultats puisqu'en fait c toujours le premier camion qui prend qui 
#a une utilité beaucoup plus grande et donc qu'on prend beaucoup
def prog_dyn(graphe, routes, camions) :
    """Renvoie une collection de camions, où chaque camion a une puissance p et un coùt c.
    """
  
    #commencer par calculer les utilités
    route=convert_to_list(routes, True)
       
    cam=convert_to_list(camions, False)
    
    W=25*10**9 #contrainte budegétaire    
    nb_c=len(cam)
    nb_r=len(route)
    trajet=[0 for i in range (nb_r)] #on enregistre si le trajet est fait ou non (on doit le parcourir au plus une fois)
    x=[0 for i in range(nb_c)] #indique le nb de fois qu'on prend un camion
    power=[0 for i in range(nb_c)] #puissance associée au camion
    #on lit les fichiers
    cam.sort(key=lambda x: x[1], reverse=True) #on trie les camions par prix décroissants
    w=[0 for i in range(nb_c)]#cout 
    utilite=[0 for i in range(nb_c)]#utilite  
    
    # on calcule l'utilité du camion i
    #pour ça, on parcourt les camions, on note les trajets que peut faire chaque camion et on somme les utilite
    for i in range(nb_c) :                
        u=0.0
        w[i]=int(cam[i][1])
        power[i]=int(cam[i][0])
         #indique le trajet
        cpt=0 #compte le nb de trajet d'un camion       
        for j in range(nb_r) :          
            
            if trajet[j]!=1 and  int(route[j][0])<=power[i] :
                u+=float(route[j][1])
                trajet[j]=1
                cpt+=1
                
        utilite[i]=(u,i, cpt)
    print(utilite)
        
   
    utilite.sort(key = lambda x :x[0], reverse=True) #on trie le tableau selon l'utilite
    w_conso=0 #inférieur a la CB?
    
    #print(utilite)
    for element in utilite :
        (u,k, cpt)=element
        while cpt*w[k]+w_conso >W :
            cpt-=1
        if cpt*w[k]+w_conso <=W :
            x[k]=cpt
            w_conso+=w[k]*cpt
        else :
            x[k]=0
    
   
    return x
    




def enleve_camion_inutile(liste_camion ) :
    """un camion est inutile si il coûte plus cher et a une puissance inférieur à celle d'un autre
    Résultat : On renvoie une liste dans laquelle les camions qui ne servent à rien ont été retirés
    """
    camion=convert_to_list(liste_camion, True)
    camion_utile=[]
    fichier=open("input/trucks.22.out","x")
    fichier.write('185') #on a lance le programme une première fois pour avoir que pour le fichier trucks 2 il y avait 185 camions
    #on se servira uniquement de cette fonction pour trucks.2
    for element in camion :
        bool=False
        (p, c)= element
        for element2 in camion :
            (p2,c2)=element2
            if (p<p2 and c>c2 ):
                bool=True
        if not bool :
            camion_utile.append(element)
            fichier.write("\n"+ str(p)+" "+str(c))
            
    fichier.close()
    
    #Complexité : O(nb_c**2) avec nb_c le nombre de camions




def convert_to_list(fichier, bool) :
    """transforme un fichier en liste de liste 
    bool=False : on rajoute dans chaque sous list i qui indique la position de l'élément, on numérote
    c'est utile de rajouter i si on trie par exemple"""
    f=open(fichier)
    l1=f.readline().split()
    cpt=0
    liste=f.readlines()
    tab=[]
    for line in liste :
        l=[]
        line=line.split()
        
        for j in line :
            
            l.append(float(j))
        if not bool :
            l.append(cpt)
            cpt+=1
        tab.append(l)
    f.close()
    return tab
    #la complexité de la fonction est O(len(liste))



#deuxième idée,        
def glouton( trajet, camion):
    """
    Idée : on trie les trajets en fonction de leur utilité. On trie les camions en fonction de leur poids. 
    Tant que la contrainte budgétaire n'est pas dépassée, on continue de rajouter 
    camions. Ainsi, on n'a pas la solution optimale mais on a une solution qui donne d'assez bons ordres de grandeur

    Complexité : C(convert_to_list(trajet))+ C(convert_to_list(camion)) + C(camion.sort())+C(trajet.sort())+O(len(trajet)*len(camion)+
  O(len(camion)*len(camion)) car on suppose que la fonction count est implementée de telle sorte à ce que la complexité soit linéaire en la taille de la liste
  donc en supposant que C(l.sort())=len(l)*ln(len(l))  et avec nb_t=nombre de trajet et nb_c nombre de camion
  complexité = O(nb_t + nb_c**2)+ O(nb_t*log(nb_t)+nb_r*log(nb_r)+O(nb_t*nb_c))
  soit O(nb_c**2+nb_t*log(nb_t)+nb_t*nb_c)
  La complexité d'un algorithme glouton du sac à dos classique est O(nlog(n)) si la liste n'est pas triée

    Paramètres :
    camion est fichier qu'on transforme en une liste de tuples de la forme (a,b,i) avec a puissance, b prix, i le numero du camion
    trajet idem avec a puissance min et b utilite

    """
    camion=convert_to_list(camion, False)
    trajet=convert_to_list(trajet,  True)
    W=25*10**9
    camion.sort(key=lambda x: x[1])
    camions=[-1 for i in range(len(trajet))]#indique quel camion on prend pour le trajet i
    j=0
    prix_total=0
    trajet.sort(key=lambda x : x[1], reverse=True)
    
    for element in trajet : #on parcourt tous les trajets
        (power, cout)=element
        #on cherche le camion dont le prix est le moins cher et qui peut parcourir le trajet element, on l'affecte alors à ce trajet
        l=0
        bool=False
        while l<len(camion) and not bool: #on parcourt tous les camions, on s'arrete des qu'on trouve un camion qui convient
            (a,b,num)=camion[l]
            if prix_total +b>W : #on regarde si le prix total + le nv prix depasse la cb
                break
            if  a > power : 
                camions[j]= l #pour le trajet j on prend le camion i
                prix_total+=b#on augement le prix paye
                bool=True
            l+=1
             
        j+=1 #on change de trajet
    
    counts=[]
    for elmt in camion :
        (a,b,k)=elmt
        c=camions.count(k)
        if c!=0 :
            counts.append((k,c))
    return counts,  W-prix_total #on renvoie la collection , les affectations et l'argent qu'il reste


import itertools



def algo_naif(trajet, camions1) :
    """on teste toutes les possibilités, on est sur d'avoir la possibilité optimale
    mais le complexité va être très grande (on teste 2**n possibilités avec n=len(trajet))
     Paramètres :
    camion est fichier qu'on transforme en une liste de tuples de la forme (a,b,i) avec a puissance, b prix, i le numero du camion
    trajet idem : on le transforme en liste de [a,b] avec a puissance min et b utilite
    """
    #en gros, on teste toutes les possibilités
    camion=convert_to_list(camions1, False)
    trajet=convert_to_list(trajet,  False)
    n = len(trajet)
    camion.sort(key=lambda x: x[1])
    W=25*10**9    
    best_utilite = 0
    best_att = []
    for j in range(0, len(trajet)+1) :
        for i in itertools.combinations(trajet , j ):
         #en gros on a 2**n choix car pour chaque trajet, on peut choisir de le prendre ou pas 
    #du coup, on regarde le camion le plus intéressant à prendre pour chaque trajet comme on a fait avant
    #on va donc chercher la meilleure utilité dans les 2**n cas
            camions=[]
            prix_total=0
            utilite=0
            for element in i :
                bool=False
                for cam in camion : #on parcourt tous les camions
                    (a,b,j)=cam
                    if bool or prix_total +b>W : #on regarde si le prix total + le nv prix depasse la cb
                        break
                
                    if  a > element[0] : 
                        camions.append((j,element[2])) #pour le trajet element[2] on prend le camion j
                        prix_total+=b
                        bool=True
                utilite+=element[1]     
            if utilite > best_utilite :
                best_utilite=utilite  
                best_att=camions
    return best_att, best_utilite , W-prix_total               

   #on ne peut pas tester sur les plus gros graphes car la complexité en 2**n est beaucoup trop grande! Mais étant donné qu'on a testé toutes
   # les possibilités, on a forcément la bonne.     
        
#avec efficacité





        
        
        
      






    
   
    
    
  



    









    
   
    
    
  



    



