#------------------------------------------#
# Title: CDInventory.py
# Desc:  CDINventory to store CD Inventory data
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# MKot, 2022-Nov-11, Modified Code, replace the inner data structure by dictionaries; 
#                    add the functionality of loading existing data;
#                    add functionality of deleting an entry.
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of dict to hold data
dicRow = {}  # dict of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('\nl, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 2. Exit the program if the user chooses so
        print('You have exited the program.')
        break
    
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 4. Add data to the table (2d-list) each time the user wants to add data
        intID = int(input('Enter an ID: '))
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        dicRow = {'ID' : intID, 'Title' : strTitle, 'Artist' : strArtist}
        lstTbl.append(dicRow)
       
    elif strChoice == 'i':
        # 5. Display the current data from the memory to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ',')
    
    elif strChoice == 'd':
        # 6. Delete the entry from the memory
        delRow = int(input('Enter the ID number of the entry you want to delete: '))
        for i in range(len(lstTbl)):
            if lstTbl[i]['ID'] == delRow:
                del lstTbl[i]
                print('Your entry has been deleted.')
    
    elif strChoice == 's':
        # 7. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')
        strRow = ''
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
        print('\nYour entry was saved.')
   
    elif strChoice == 'l':
        # 3. Loading existing data from the file
       print('Existing data in the file.\nID, Title, Artist')
       objFile = open(strFileName, 'r')
       for row in objFile:
          lstRow = row.strip().split(',')
          dicRow = {'ID' : int(lstRow[0]), 'Title' : lstRow[1], 'Artist' : lstRow[2]}
          print(*dicRow.values(), sep = ',')
       objFile.close()
       pass       
        
    else:
        print('Invalid Entry! Please choose either l, a, i, d, s or x!')

