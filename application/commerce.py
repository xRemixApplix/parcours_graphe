import math
import random
import matplotlib

class Ville:
    # Constructeur d'une nouvelle ville
    def __init__(self, lon, lat, nom):
        self.lon = lon
        self.lat = lat
        self.nom = nom
    
    # Calcul de la distance avec une autre ville
    def distance(self, ville):
        distance_x = (ville.lon-self.lon)*40000*math.cos((self.lat+ville.lat)*math.pi/360)/360
        distance_y = (self.lat-ville.lat)*40000/360

        return math.sqrt(distance_x**2 + distance_y**2)


class GestionnaireCircuit:
    villes_destinations = []

    def ajouter_ville(self, ville):
        self.villes_destinations.append(ville)

    def getVille(self, index):
        return self.villes_destinations[index]

    def nombres_villes(self):
        return len(self.villes_destinations)


class Circuit:
    def __init__(self, gestionnaire_circuit, circuit = None):
        self.gestionnaire_circuit = gestionnaire_circuit
        self.circuit = []
        self.fitness = 0.0
        self.distance = 0
        if circuit is not None:
            self.circuit = circuit
        else:
            for _ in range(0, self.gestionnaire_circuit.nombres_villes()):
                self.circuit.append(None)

    def __len__(self):
        return len(self.circuit)

    def __getitem__(self, index):
        return self.circuit[index]

    def __setitem__(self, key, value):
        self.circuit[key] = value

    def genere_individu(self):
        for indice_ville in range(0, self.gestionnaire_circuit.nombres_villes()):
            self.setVille(indice_ville, self.gestionnaire_circuit.getVille(indice_ville))
        random.shuffle(self.circuit)

    def getVille(self, circuit_position):
        return self.circuit[circuit_position]

    def setVille(self, circuit_position, ville):
        self.circuit[circuit_position] = ville
        self.fitness = 0.0
        self.distance = 0

    def getFitness(self):
        if self.fitness == 0:
            self.fitness = 1/float(self.getDistance())

        return self.fitness

    def getDistance(self):
        if self.distance == 0:
            circuit_distance = 0
            for indice_ville in range(0, self.taille_circuit()):
                ville_origine = self.getVille(indice_ville)
                ville_arrivee = None
                if indice_ville+1 < self.taille_circuit():
                    ville_arrivee = self.getVille(indice_ville+1)
                else:
                    ville_arrivee = self.getVille(0)
                circuit_distance += ville_origine.distance(ville_arrivee)
            self.distance = circuit_distance
        
        return self.distance

    def taille_circuit(self):
        return len(self.circuit)

    def contient_ville(self, ville):
        return ville in self.circuit


class Population:
    def __init__(self, gestionnaire_circuit, taille_population, init):
        self.circuits = []
        for i in range(0, taille_population):
            self.circuits.append(None)

        if init:
            for i in range(0, taille_population):
                nouveau_circuit = Circuit(gestionnaire_circuit)
                nouveau_circuit.genere_individu()
                self.sauvegarder_circuit(i, nouveau_circuit)

    def __setitem__(self, key, value):
        self.circuits[key] = value

    def __getitem__(self, index):
        return self.circuits[index]

    def sauvegarder_circuit(self, index, circuit):
        self.circuits[index] = circuit

    def getCircuit(self, index):
        return self.circuits[index]

    def getFittest(self):
        fittest = self.circuits[0]
        for i in range(0, self.taille_population()):
            if fittest.getFitness() <= self.getCircuit(i).getFitness():
                fittest = self.getCircuit(i)

        return fittest

    def taille_population(self):
        return len(self.circuits)


class GA:
    def __init__(self, gestionnaire_circuit):
        self.gestionnaire_circuit = gestionnaire_circuit
        self.taux_mutation = 0.015
        self.taille_tournoi = 5
        self.elitisme = True

    def evoluer_population(self, pop):
        nouvelle_population = Population(self.gestionnaire_circuit, pop.taille_population(), False)
        elitisme_offset = 0
        if self.elitisme:
            nouvelle_population.sauvegarder_circuit(0, pop.getFittest())
            elitisme_offset = 1
        
        for i in range(elitisme_offset, nouvelle_population.taille_population()):
            parent1 = self.selection_tournoi(pop)
            parent2 = self.selection_tournoi(pop)
            enfant = self.crossover(parent1, parent2)
            nouvelle_population.sauvegarder_circuit(i, enfant)

        for i in range(elitisme_offset, nouvelle_population.taille_population()):
            self.muter(nouvelle_population.getCircuit(i))

        return nouvelle_population

    def crossover(self, parent1, parent2):
        enfant = Circuit(self.gestionnaire_circuit)

        start_pos = int(random.random()*parent1.taille_circuit())
        end_pos = int(random.random()*parent1.taille_circuit())

        for i in range(0, enfant.taille_circuit()):
            if start_pos < end_pos and i > start_pos and i < end_pos:
                enfant.setVille(i, parent1.getVille(i))
            elif start_pos > end_pos:
                if not (i<start_pos and i> end_pos):
                    enfant.setVille(i, parent1.getVille(i))

        for  i in range(0, parent2.taille_circuit()):
            if not enfant.contient_ville(parent2.getVille(i)):
                for ii in range (0, enfant.taille_circuit()):
                    if enfant.getVille(ii) == None:
                        enfant.setVille(ii, parent2.getVille(i))
                        break

        return enfant

    def muter(self, circuit):
        for circuit_pos1 in range(0, circuit.taille_circuit()):
            if random.random() < self.taux_mutation:
                circuit_pos2 = int(circuit.taille_circuit()*random.random())

                ville1 = circuit.getVille(circuit_pos1)
                ville2 = circuit.getVille(circuit_pos2)

                circuit.setVille(circuit_pos2, ville1)
                circuit.SetVille(circuit_pos1, ville2)

    def selection_tournoi(self, pop):
        tournoi = Population(self.gestionnaire_circuit, self.taille_tournoi, False)
        for i in range(0, self.taille_tournoi):
            random_id = int(random.random()*pop.taille_population())
            tournoi.sauvegarder_circuit(i, pop.getCircuit(random_id))
        fittest = tournoi.getFittest()
        
        return fittest


###############################################################################################
###############################################################################################

if __name__ == '__main__':
   
   gc = GestionnaireCircuit()   

   #on cree nos villes
   ville1 = Ville(3.002556, 45.846117, 'Clermont-Ferrand')
   gc.ajouter_ville(ville1)
   ville2 = Ville(-0.644905, 44.896839, 'Bordeaux')
   gc.ajouter_ville(ville2)
   ville3 = Ville(-1.380989, 43.470961, 'Bayonne')
   gc.ajouter_ville(ville3)
   ville4 = Ville(1.376579, 43.662010, 'Toulouse')
   gc.ajouter_ville(ville4)
   ville5 = Ville(5.337151, 43.327276, 'Marseille')
   gc.ajouter_ville(ville5)
   ville6 = Ville(7.265252, 43.745404, 'Nice')
   gc.ajouter_ville(ville6)
   ville7 = Ville(-1.650154, 47.385427, 'Nantes')
   gc.ajouter_ville(ville7)
   ville8 = Ville(-1.430427, 48.197310, 'Rennes')
   gc.ajouter_ville(ville8)
   ville9 = Ville(2.414787, 48.953260, 'Paris')
   gc.ajouter_ville(ville9)
   ville10 = Ville(3.090447, 50.612962, 'Lille')
   gc.ajouter_ville(ville10)
   ville11 = Ville(5.013054, 47.370547, 'Dijon')
   gc.ajouter_ville(ville11)
   ville12 = Ville(4.793327, 44.990153, 'Valence')
   gc.ajouter_ville(ville12)
   ville13 = Ville(2.447746, 44.966838, 'Aurillac')
   gc.ajouter_ville(ville13)
   ville14 = Ville(1.750115, 47.980822, 'Orleans')
   gc.ajouter_ville(ville14)
   ville15 = Ville(4.134148, 49.323421, 'Reims')
   gc.ajouter_ville(ville15)
   ville16 = Ville(7.506950, 48.580332, 'Strasbourg')
   gc.ajouter_ville(ville16)
   ville17 = Ville(1.233757, 45.865246, 'Limoges')
   gc.ajouter_ville(ville17)
   ville18 = Ville(4.047255,48.370925, 'Troyes')
   gc.ajouter_ville(ville18)
   ville19 = Ville(0.103163,49.532415, 'Le Havre')
   gc.ajouter_ville(ville19)
   ville20 = Ville(-1.495348, 49.667704, 'Cherbourg')
   gc.ajouter_ville(ville20)
   ville21 = Ville(-4.494615, 48.447500, 'Brest')
   gc.ajouter_ville(ville21)
   ville22 = Ville(-0.457140, 46.373545, 'Niort')
   gc.ajouter_ville(ville22)


# On initialise la population avec 50 circuits
pop = Population(gc, 50, True)
print("Distance initiale : " + str(pop.getFittest().getDistance()))
meilleure_population = pop.getFittest()

# On genere une carte representant notre solution
lons = []
lats = []
noms = []
for ville in meilleure_population.circuit:
    lons.append(ville.lon)
    lats.append(ville.lat)
    noms.append(ville.nom)

lons.append(lons[0])
lats.append(lats[0])
noms.append(noms[0])
