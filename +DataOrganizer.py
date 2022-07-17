print('----------------------------------------------- DataOrganizer')
print('----------------------------------------------- Discord: Ozym1ndias#3112\n')

_Data = []
__Data = []
fileName = ''


def fileName():
    dataFile = input('What is the name of the file you want to organize?\n>> ')
    if(f'{dataFile[-3:-1]}{dataFile[-1]}' != 'txt'):
        print('The file extension must be .txt')
        return fileName()
    return dataFile

def txt2list(fileName):
    with open(fileName, 'r') as Data:
        for line in Data.readlines():
            _Data.append(line.replace('\n', ''))
        #print(_Data)
        print(f'The length of the data is: {len(_Data)}') # Check for the length of the list

def cleaner(_Data):
    #__Data = list(set(_Data))
    #print(__Data)
    for dataPoint in _Data:
        if(dataPoint == _Data[-1]):
            if dataPoint[0] != '+':
                dataPoint = f'+{dataPoint}'
            __Data.append(dataPoint)
            break
        if dataPoint[0] != '+':
            dataPoint = f'+{dataPoint}'
        if(dataPoint[-1] != ','):
            dataPoint = f'{dataPoint},'
        __Data.append(dataPoint)
    #print(f'The length of the unique data is: {len(__Data)}') # Check for the length of the unique list
    return __Data

def write2txtfile(__Data):
    #print(len(__Data))
    #print('This works!')
    with open('oDataTelstra@AUS.txt', 'w') as uData:
        for number in __Data:
            uData.write(str(number))
            uData.write('\n')

def main():
    fN = fileName()
    txt2list(fN)
    __Data = cleaner(_Data)
    write2txtfile(__Data)



if(__name__ == '__main__'):
    main()