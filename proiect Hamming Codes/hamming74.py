import numpy as np

class Hamming74:
    __G = np.array([[1,1,0,1],
                    [1,0,1,1],
                    [1,0,0,0],
                    [0,1,1,1],
                    [0,1,0,0],
                    [0,0,1,0],
                    [0,0,0,1]])
    __H = np.array([[1,0,1,0,1,0,1],
                    [0,1,1,0,0,1,1],
                    [0,0,0,1,1,1,1]])
    __D = np.array([[0,0,1,0,0,0,0],
                    [0,0,0,0,1,0,0],
                    [0,0,0,0,0,1,0],
                    [0,0,0,0,0,0,1]])                  
    @staticmethod
    def encode(data):
        encoded = np.dot(Hamming74.__G,data)%2
        return np.append(encoded,[encoded.sum()%2],axis=0)
    @staticmethod
    def decode(codeword):
        code,parity = codeword[:-1],codeword[-1]
        syndrome = np.dot(code,Hamming74.__H.T)%2
        if syndrome.sum() == 0:
            return np.dot(Hamming74.__D,code)%2,-1
        if code.sum()%2 == parity:
            return None,-2
        error_pos = syndrome[0] + syndrome[1]*2 + syndrome[2]*4 - 1
        new_code = code.copy()
        new_code[error_pos] = 1 - new_code[error_pos]
        return np.dot(Hamming74.__D,new_code)%2,error_pos


        
