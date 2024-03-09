import numpy as np

def tri3_elem_arrays(nen, xe, ye, k, Q):
    
    return #ke, fe

def tri3_assemble_global_arrays(numnp, numel, nen, p, LM, k, Q):

    #Initialize K and F using np.zeros of appropriate sizes.

    #Loop over elements
    #for i_elem in range(numel):

        #Get the coordinates of this element.
        #xe = ...
        #ye = ...

        #Compute the element arrays.
        #ke, fe = tri3_elem_arrays(nen, xe, ye, k, Q)

        #Add the contribution of this element to the global arrays.
        #K = ...
        #F = ...
        
    return #K,F

def tri3_apply_BCs(nodeFlag, To, Ti, K, F):
    
    return #K,F


def solve_fea_heat2d(p, LM, nodeFlag, k, Q, To, Ti):

    #Using p, LM arrays, compute numnp, numel and nen below.
    #numnp = ...
    #numel = ...
    #nen = ...

    #Get the assembled K and F. Uncomment this after you complete the function.
    #K, F = tri3_assemble_global_arrays(numnp, numel, nen, p, LM, k, Q):

    #Apply BCs to modify the global arrays.
    #K, F = tri3_apply_BCs(nodeFlag, To, Ti, K, F)

    #Solve for T using the assembled and BC applied K and F.
    #T = ...

    return #T