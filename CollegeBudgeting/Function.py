class Function(object):
    def __init__(self, const):
        self.constraint = const
    
    def savings(self, var, switch, dConst, continuity):
        return {
            '1' : dConst + var**2,
            '2' : -((var - self.constraint)**2) + continuity,
        }[switch]


