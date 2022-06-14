import csv

def read_data(filename1, filename2):

    dic = {}

    with open(filename1, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            #rellenamos el diccionario con las claves de stop
            #print(row)
           #dic[row[0]] = None #primer campo stops
           dic2 = {
                'description':None,
                'id':None,
                'lat':None,
                'lon':None,
                'name':None
            }
           id = row[0]
           
           with open(filename2, 'r') as file2:
                reader2 = csv.reader(file2)
                for row2 in reader2:
                    #print(row2)
                    if id == row2[0]:
                        dic[row[0]] = dic2
                        dic[row[0]]['name'] = row[2]
                        dic[row[0]]['description'] = row[3]
                        dic[row[0]]['lat'] = row2[4]
                        dic[row[0]]['lon'] = row2[5]
        
    return dic


def get_name_description(clave,diccionario):
    registro = diccionario.get(clave)
    if registro == None:
        raise ValueError("No existe esa clave")
    else:
        return registro['name'],registro['description']


def search_by_lon(lon,diccionario):
    try:
        num = float(lon)%2
    except ValueError:
        raise ValueError("La lon no es un float")
        
    claves = diccionario.keys()
    encontrado = False
    clave_encontrada = ""
    for clave in claves:
        lon_clave = diccionario.get(clave)
        if lon_clave['lon'] == lon:
            encontrado = True
            clave_encontrada = clave
    if encontrado:
        return clave_encontrada
    else:
        raise ValueError("El valor de lon no existe")
    


if __name__ == "__main__":

    diccionario_ej2=read_data("stops.csv", "stops_data.csv")
    
    name,descri = get_name_description('1080',diccionario_ej2)
    #print(name)
    #print(descri)

    res = search_by_lon('728257.03',diccionario_ej2)

    print(res)
   # nombre,description = get_name_description('1080', diccionario_ej2)

   
    