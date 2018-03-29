from numpy import mean

def calculateMeanAndAplly(b,g,r):
    '''
    Calcula a media de tres pixels e retorna um pixel com essa media
    '''
    
    average = mean([b,g,r])

    return [average,average,average]

def toGreen(b,g,r):
    '''
    converte todo o pixel para a banda verde
    '''
    return [0,g,0]

def toRed (b,g,r):
    '''
    converte todo o pixel para a banda vermelha
    '''
    return [0,0,r]

def toBlue (b,g,r):
    '''
    converte todo o pixel para a banda azul
    '''
    return [b,0,0]
    


