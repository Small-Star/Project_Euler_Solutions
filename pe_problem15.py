#Project Euler - Problem 15 Solution
#04/13/2016

#Problem: Lattice paths: Find all the routes in a 20x20 grid
#Solution Strategy: nxn case is solved by (n-1xn-1 + n-2xn)x2. Solve with recursion.

#Store calculated paths. Note: for efficiency, paths are stored with the greater dimension first (e.g. 3x4 path and 4x3 path both resolve to the 4x3 path)
path_costs = {(1,1):2}

def lattice_paths(w,h):
    #Return number of lattice paths for a lattice of wxh squares

    val = path_costs.get((max(w,h),min(w,h)),0)
    new_val = 0

    #Check to see if path has already been calculated
    if not val == 0:
        return val
    
    #Edge case: 1x1
    elif (w == 1) and (h == 1):
        return 2
    
    #Edge case: (w or h) == 1
    elif ((w == 1) or (h == 1)):
        new_val = 1 + lattice_paths(max(w,h) - 1,(min(w,h)))
        path_costs[(max(w,h),1)] = new_val
        return new_val

    #Anything else can be reduced to (n-1xn) + (nxn-1)
    else:
        new_val = lattice_paths(w,h - 1) + lattice_paths(w - 1,h)
        path_costs[(max(w,h),min(w,h))] = new_val
        return new_val
