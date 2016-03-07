class Function(object):
    
    def transportation(self, var, dConst, constraint, continuity):
            if(var <= constraint):
                return dConst + var**2
            else:
                return -((var - constraint)**2) + continuity

    def savings(self, var, dConst):
        return dConst * var**(1/2)
