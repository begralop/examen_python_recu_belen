import csv

def read_data(filename1, filename2):

    with open(filename1, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
           

    with open(filename2, 'r') as file2:
        reader2 = csv.reader(file2)
        for row2 in reader2:
            print(row2)
            

    dicc_res = {}
    
    for i in reader:





if __name__ == "__main__":

    fichero=read_data("stops.csv", "stops_data.csv")
   
    