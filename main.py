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
                        dic[row[0]]['lat'] = row[4]
                        dic[row[0]]['lon'] = row[5]
        
    return dic

def get_name_description(clave, diccionario):

    for i in diccionario.keys():
        if(clave == i):
            print("ok")
        
        else:
            raise ValueError("Algo está sucediendo en el string del número de la clase Flight")


if __name__ == "__main__":

    diccionario_ej2=read_data("stops.csv", "stops_data.csv")
    
    name, description = get_name_description('1080', diccionario_ej2)



   # nombre,description = get_name_description('1080', diccionario_ej2)

   
    