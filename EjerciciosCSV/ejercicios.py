#http://datos.neuquen.gob.ar/it/dataset/datos-ficticios-extraidos-del-sistema-siuned/resource/d2565c27-159e-42d6-b3a7-aa952a258c1a
import csv

    
def contasexos(): 
    with open("persona.csv", newline="") as File:  
        reader = csv.DictReader(File)
        contador_F = 0
        contador_M = 0
        for column in reader:
            if (column["PERSEXO"]) == "F":
                contador_F += 1
            else   :
                contador_M += 1
    print(f"Hay {contador_F} mujeres y {contador_M} hombres" )

def est_civil():
    with open("persona.csv", newline="") as File:
        reader = csv.DictReader(File)
        casados = 0
        for row in reader:
            if (row["ESTADOCIVILCOD"]) == "2":
                casados +=1
            else:
                pass
        if casados == 329:
            print("TODOS ESTAN CASADOS")
        else:
            print("NO TODOS ESTAN CASADOS")

def cont_apellido():
    with open("persona.csv", newline="") as File:
        reader = csv.DictReader(File)
        lista = []
        for row in reader:
            lista.append(row["PERAPELLIDO"])
        if len(lista) == len(set(lista)):
            print("HAY APELLIDOS REPETIDOS")
        else:
            print("NO HAY APELLIDOS REPETIDOS")

def nacidos_capital():
    with open("persona.csv", newline="") as File:
        reader = csv.DictReader(File)
        localidades = []
        for row in reader:
            localidades.append(row["PERLOCALIDADNAC"])
        cont1 = localidades.count("NEUQUEN CAPITAL                                             ")       
        cont2 = localidades.count("NQN. CAPITAL                                                ")
        total = cont1 + cont2
        porcentaje = round(total / len(localidades) * 100, 2)
        print(f"Hay {total} personas nacidas en Neuquen Capital\nRepresentan un {porcentaje}% del total de la lista")

def discapacitados():
    with open("persona.csv", newline="") as File:
        reader = csv.DictReader(File)
        count = 0
        for row in reader:
            if row["DISCAPACIDADCOD"] == "0":
                count +=1
            else:
                pass
        print(f"{count} personas presentan una discapacidad")   

contasexos()
est_civil()
cont_apellido()
nacidos_capital()
discapacitados()