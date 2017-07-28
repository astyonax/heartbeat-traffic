import numpy as np

def pma(data,axis=0):
    """
    principal modes analysis of 2D data - expects time on the axis=0 axis
    returns:
    sorted eigvals, and eigvects, correlation matrix
    """
    i=data[0]
    
    #MD=np.einsum('i,j->ij',i,i.T)
    MD=np.outer(i,i)
    #print "entering for loop"
    for i in data[1:]:
       #MD+=np.einsum('i,j->ij',i,i.T)
        MD+=np.outer(i,i)
    #print "exiting for loop"
    
    MD/=data.shape[0]
    #print "computing eigenvalues"
    l,e=np.linalg.eigh(MD)
    #print "done"

    idxx=np.argsort(l)[::-1]
    l=l[idxx]
    e=e[:,idxx]
    return l,e,MD
    
def get_XY(data,e):
    """
    Compute time evolution of the modes amplitude 
    as the scalar product btw the data and each mode 
    """
    return [(data*e[:,j]).sum(axis=1) for j in xrange(e.shape[1])]

def reconstruc_frommodes(e,ampl):
    ampl=np.array(ampl)
    e=np.array(e)
    
    rec=np.zeros((ampl.shape[1],e.shape[0]))*.1
   
    N=ampl.shape[1]
    e=e.T
    
    for eigvect,X in zip(e,ampl):
        
        rec0=np.tile(eigvect,(N,1))
        rec+=rec0*X[:,np.newaxis]
    return rec