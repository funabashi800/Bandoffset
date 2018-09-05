class AlP(object):
    def __init__(self,x,y):
        self.lattice_constant = 5.451
        self.elastic_constant_11 = 1.32
        self.elastic_constant_12 = 0.63
        self.elastic_constant_44 = 0.62
        self.valence_band_average = -8.09
        self.spin_orbit_splitting = 0.07
        self.band_gap = 3.58 #Ganma
        self.deformation_valence = 3.15
        self.deformation_conduction = -5.54 #Ganma
        self.conduction_band = 0.0
        self.valence_band = 0.0

    def info(self):
        print("Lattice constant : {}".format(self.lattice_constant))
        print("Valence band average : {}".format(self.valence_band_average))
        print("Spin orbit : {}".format(self.spin_orbit))
        print("Band gap : {}".format(self.band_gap))

class AlAs(object):
    def __init__(self,x,y):
        self.lattice_constant = 5.660
        self.elastic_constant_11 = 1.25
        self.elastic_constant_12 = 0.53
        self.elastic_constant_44 = 0.54
        self.valence_band_average = -7.49
        self.spin_orbit_splitting = 0.28
        self.band_gap = 2.95 #Ganma
        self.deformation_valence = 2.47
        self.deformation_conduction = -5.64 #Ganma
        self.conduction_band = 0.0
        self.valence_band = 0.0

    def info(self):
        print("Lattice constant : {}".format(self.lattice_constant))
        print("Valence band average : {}".format(self.valence_band_average))
        print("Spin orbit : {}".format(self.spin_orbit))
        print("Band gap : {}".format(self.band_gap))

class GaP(object):
    def __init__(self,x,y):
        self.lattice_constant = 5.451
        self.elastic_constant_11 = 1.41
        self.elastic_constant_12 = 0.62
        self.elastic_constant_44 = 0.70
        self.valence_band_average = -7.40
        self.spin_orbit_splitting = 0.08
        self.band_gap = 2.74 #Ganma
        self.deformation_valence = 1.70
        self.deformation_conduction = -7.14 #Ganma
        self.conduction_band = 0.0
        self.valence_band = 0.0

    def info(self):
        print("Lattice constant : {}".format(self.lattice_constant))
        print("Valence band average : {}".format(self.valence_band_average))
        print("Spin orbit : {}".format(self.spin_orbit))
        print("Band gap : {}".format(self.band_gap))

class InSb(object):
    def __init__(self,x,y):
        self.lattice_constant = 6.479
        self.elastic_constant_11 = 0.66
        self.elastic_constant_12 = 0.36
        self.elastic_constant_44 = 0.30
        self.valence_band_average = -6.09
        self.spin_orbit_splitting = 0.81
        self.band_gap = 0.17 #Ganma
        self.deformation_valence = -0.36
        self.deformation_conduction = -6.17 #Ganma
        self.conduction_band = 0.0
        self.valence_band = 0.0

    def info(self):
        print("Lattice constant : {}".format(self.lattice_constant))
        print("Valence band average : {}".format(self.valence_band_average))
        print("Spin orbit : {}".format(self.spin_orbit))
        print("Band gap : {}".format(self.band_gap))

class InAs(object):
    def __init__(self,x,y):
        self.lattice_constant = 6.058
        self.elastic_constant_11 = 0.83
        self.elastic_constant_12 = 0.45
        self.elastic_constant_44 = 0.40
        self.valence_band_average = -6.67
        self.spin_orbit_splitting = 0.38
        self.band_gap = 0.36 #Ganma
        self.deformation_valence = -1.00
        self.deformation_conduction = -5.08 #Ganma
        self.conduction_band = 0.0
        self.valence_band = 0.0

    def info(self):
        print("Lattice constant : {}".format(self.lattice_constant))
        print("Valence band average : {}".format(self.valence_band_average))
        print("Spin orbit : {}".format(self.spin_orbit))
        print("Band gap : {}".format(self.band_gap))

class InP(object):
    def __init__(self,x,y):
        self.lattice_constant = 5.869
        self.elastic_constant_11 = 1.02
        self.elastic_constant_12 = 0.58
        self.elastic_constant_44 = 0.46
        self.valence_band_average = -7.04
        self.spin_orbit_splitting = 0.11
        self.band_gap = 1.35 #Ganma
        self.deformation_valence = -1.27
        self.deformation_conduction = -5.04 #Ganma
        self.conduction_band = 0.0
        self.valence_band = 0.0

    def info(self):
        print("Lattice constant : {}".format(self.lattice_constant))
        print("Valence band average : {}".format(self.valence_band_average))
        print("Spin orbit : {}".format(self.spin_orbit))
        print("Band gap : {}".format(self.band_gap))

class GaSb(object):
    def __init__(self,x,y):
        self.lattice_constant = 6.096
        self.elastic_constant_11 = 0.88
        self.elastic_constant_12 = 0.40
        self.elastic_constant_44 = 0.43
        self.valence_band_average = -6.25
        self.spin_orbit_splitting = 0.82
        self.band_gap = 0.72 #Ganma
        self.deformation_valence = -0.79
        self.deformation_conduction = -6.85 #Ganma
        self.conduction_band = 0.0
        self.valence_band = 0.0

    def info(self):
        print("Lattice constant : {}".format(self.lattice_constant))
        print("Valence band average : {}".format(self.valence_band_average))
        print("Spin orbit : {}".format(self.spin_orbit))
        print("Band gap : {}".format(self.band_gap))

class GaAs(object):
    def __init__(self,x,y):
        self.lattice_constant = 5.653
        self.elastic_constant_11 = 1.18
        self.elastic_constant_12 = 0.54
        self.elastic_constant_44 = 0.59
        self.valence_band_average = -6.92
        self.spin_orbit_splitting = 0.34
        self.band_gap = 1.42 #Ganma
        self.deformation_valence = -1.16
        self.deformation_conduction = -7.17 #Ganma
        self.conduction_band = 0.0
        self.valence_band = 0.0

    def info(self):
        print("Lattice constant : {}".format(self.lattice_constant))
        print("Valence band average : {}".format(self.valence_band_average))
        print("Spin orbit : {}".format(self.spin_orbit))
        print("Band gap : {}".format(self.band_gap))

class AlSb(object):
    def __init__(self,x,y):
        self.lattice_constant = 6.136
        self.elastic_constant_11 = 0.88
        self.elastic_constant_12 = 0.43
        self.elastic_constant_44 = 0.41
        self.valence_band_average = -6.66
        self.spin_orbit_splitting = 0.65
        self.band_gap = 2.22 #Ganma
        self.deformation_valence = -1.38
        self.deformation_conduction = -6.97 #Ganma
        self.conduction_band = 0.0
        self.valence_band = 0.0

    def info(self):
        print("Lattice constant : {}".format(self.lattice_constant))
        print("Valence band average : {}".format(self.valence_band_average))
        print("Spin orbit : {}".format(self.spin_orbit))
        print("Band gap : {}".format(self.band_gap))

##### Ternary ######

class AlAsSb(object):
    def __init__(self, x, y):
        a = AlAs(x,y)
        b = AlSb(x,y)
        self.lattice_constant = x*a.lattice_constant+(1.0-x)*b.lattice_constant
        self.elastic_constant_11 = x*a.elastic_constant_11+(1.0-x)*b.elastic_constant_11
        self.elastic_constant_12 = x*a.elastic_constant_12+(1.0-x)*b.elastic_constant_12
        self.elastic_constant_44 = x*a.elastic_constant_44+(1.0-x)*b.elastic_constant_44
        self.valence_band_average = x*a.valence_band_average+(1.0-x)*b.valence_band_average
        self.spin_orbit_splitting = x*a.spin_orbit_splitting+(1.0-x)*b.spin_orbit_splitting+x*(1.0-x)*0.15
        self.band_gap = x*a.band_gap+(1.0-x)*b.band_gap+x*(1.0-x)*0.84
        self.deformation_valence = x*a.deformation_valence+(1.0-x)*b.deformation_valence
        self.deformation_conduction = x*a.deformation_conduction+(1.0-x)*b.deformation_conduction
        self.conduction_band = 0.0
        self.valence_band = 0.0

    def info(self):
        print("Lattice constant : {}".format(self.lattice_constant))
        print("Valence band average : {}".format(self.valence_band_average))
        print("Spin orbit : {}".format(self.spin_orbit))
        print("Band gap : {}".format(self.band_gap))

class AlGaP(object):
    def __init__(self,x,y):
        a = AlP(x,y)
        b = GaP(x,y)
        self.lattice_constant = x*a.lattice_constant+(1.0-x)*b.lattice_constant
        self.elastic_constant_11 = x*a.elastic_constant_11+(1.0-x)*b.elastic_constant_11
        self.elastic_constant_12 = x*a.elastic_constant_12+(1.0-x)*b.elastic_constant_12
        self.elastic_constant_44 = x*a.elastic_constant_44+(1.0-x)*b.elastic_constant_44
        self.valence_band_average = x*a.valence_band_average+(1.0-x)*b.valence_band_average
        self.spin_orbit_splitting = x*a.spin_orbit_splitting+(1.0-x)*b.spin_orbit_splitting
        self.band_gap = x*a.band_gap+(1.0-x)*b.band_gap+x*(1.0-x)
        self.deformation_valence = x*a.deformation_valence+(1.0-x)*b.deformation_valence
        self.deformation_conduction = x*a.deformation_conduction+(1.0-x)*b.deformation_conduction
        self.conduction_band = 0.0
        self.valence_band = 0.0

    def info(self):
        print("Lattice constant : {}".format(self.lattice_constant))
        print("Valence band average : {}".format(self.valence_band_average))
        print("Spin orbit : {}".format(self.spin_orbit))
        print("Band gap : {}".format(self.band_gap))

class AlGaAs(object):
    def __init__(self,x,y):
        a = AlAs(x,y)
        b = GaAs(x,y)
        self.lattice_constant = x*a.lattice_constant+(1.0-x)*b.lattice_constant
        self.elastic_constant_11 = x*a.elastic_constant_11+(1.0-x)*b.elastic_constant_11
        self.elastic_constant_12 = x*a.elastic_constant_12+(1.0-x)*b.elastic_constant_12
        self.elastic_constant_44 = x*a.elastic_constant_44+(1.0-x)*b.elastic_constant_44
        self.valence_band_average = x*a.valence_band_average+(1.0-x)*b.valence_band_average
        self.spin_orbit_splitting = x*a.spin_orbit_splitting+(1.0-x)*b.spin_orbit_splitting
        self.band_gap = x*a.band_gap+(1.0-x)*b.band_gap+x*(1.0-x)*0.37
        self.deformation_valence = x*a.deformation_valence+(1.0-x)*b.deformation_valence
        self.deformation_conduction = x*a.deformation_conduction+(1.0-x)*b.deformation_conduction
        self.conduction_band = 0.0
        self.valence_band = 0.0

    def info(self):
        print("Lattice constant : {}".format(self.lattice_constant))
        print("Valence band average : {}".format(self.valence_band_average))
        print("Spin orbit : {}".format(self.spin_orbit))
        print("Band gap : {}".format(self.band_gap))

class AlGaSb(object):
    def __init__(self,x,y):
        a = AlSb(x,y)
        b = GaSb(x,y)
        self.lattice_constant = x*a.lattice_constant+(1.0-x)*b.lattice_constant
        self.elastic_constant_11 = x*a.elastic_constant_11+(1.0-x)*b.elastic_constant_11
        self.elastic_constant_12 = x*a.elastic_constant_12+(1.0-x)*b.elastic_constant_12
        self.elastic_constant_44 = x*a.elastic_constant_44+(1.0-x)*b.elastic_constant_44
        self.valence_band_average = x*a.valence_band_average+(1.0-x)*b.valence_band_average
        self.spin_orbit_splitting = x*a.spin_orbit_splitting+(1.0-x)*b.spin_orbit_splitting+x*(1.0-x)*0.30
        self.band_gap = x*a.band_gap+(1.0-x)*b.band_gap+x*(1.0-x)*0.47
        self.deformation_valence = x*a.deformation_valence+(1.0-x)*b.deformation_valence
        self.deformation_conduction = x*a.deformation_conduction+(1.0-x)*b.deformation_conduction
        self.conduction_band = 0.0
        self.valence_band = 0.0

    def info(self):
        print("Lattice constant : {}".format(self.lattice_constant))
        print("Valence band average : {}".format(self.valence_band_average))
        print("Spin orbit : {}".format(self.spin_orbit))
        print("Band gap : {}".format(self.band_gap))

class AlInP(object):
    def __init__(self,x,y):
        a = AlP(x,y)
        b = InP(x,y)
        self.lattice_constant = x*a.lattice_constant+(1.0-x)*b.lattice_constant
        self.elastic_constant_11 = x*a.elastic_constant_11+(1.0-x)*b.elastic_constant_11
        self.elastic_constant_12 = x*a.elastic_constant_12+(1.0-x)*b.elastic_constant_12
        self.elastic_constant_44 = x*a.elastic_constant_44+(1.0-x)*b.elastic_constant_44
        self.valence_band_average = x*a.valence_band_average+(1.0-x)*b.valence_band_average
        self.spin_orbit_splitting = x*a.spin_orbit_splitting+(1.0-x)*b.spin_orbit_splitting
        self.band_gap = x*a.band_gap+(1.0-x)*b.band_gap
        self.deformation_valence = x*a.deformation_valence+(1.0-x)*b.deformation_valence
        self.deformation_conduction = x*a.deformation_conduction+(1.0-x)*b.deformation_conduction
        self.conduction_band = 0.0
        self.valence_band = 0.0

    def info(self):
        print("Lattice constant : {}".format(self.lattice_constant))
        print("Valence band average : {}".format(self.valence_band_average))
        print("Spin orbit : {}".format(self.spin_orbit))
        print("Band gap : {}".format(self.band_gap))

class AlInAs(object):
    def __init__(self,x,y):
        a = AlAs(x,y)
        b = InAs(x,y)
        self.lattice_constant = x*a.lattice_constant+(1.0-x)*b.lattice_constant
        self.elastic_constant_11 = x*a.elastic_constant_11+(1.0-x)*b.elastic_constant_11
        self.elastic_constant_12 = x*a.elastic_constant_12+(1.0-x)*b.elastic_constant_12
        self.elastic_constant_44 = x*a.elastic_constant_44+(1.0-x)*b.elastic_constant_44
        self.valence_band_average = x*a.valence_band_average+(1.0-x)*b.valence_band_average
        self.spin_orbit_splitting = x*a.spin_orbit_splitting+(1.0-x)*b.spin_orbit_splitting+x*(1.0-x)*0.15
        self.band_gap = x*a.band_gap+(1.0-x)*b.band_gap+x*(1.0-x)*0.70
        self.deformation_valence = x*a.deformation_valence+(1.0-x)*b.deformation_valence
        self.deformation_conduction = x*a.deformation_conduction+(1.0-x)*b.deformation_conduction
        self.conduction_band = 0.0
        self.valence_band = 0.0

    def info(self):
        print("Lattice constant : {}".format(self.lattice_constant))
        print("Valence band average : {}".format(self.valence_band_average))
        print("Spin orbit : {}".format(self.spin_orbit))
        print("Band gap : {}".format(self.band_gap))

class GaPAs(object):
    def __init__(self,x,y):
        a = GaP(x,y)
        b = GaAs(x,y)
        self.lattice_constant = x*a.lattice_constant+(1.0-x)*b.lattice_constant
        self.elastic_constant_11 = x*a.elastic_constant_11+(1.0-x)*b.elastic_constant_11
        self.elastic_constant_12 = x*a.elastic_constant_12+(1.0-x)*b.elastic_constant_12
        self.elastic_constant_44 = x*a.elastic_constant_44+(1.0-x)*b.elastic_constant_44
        self.valence_band_average = x*a.valence_band_average+(1.0-x)*b.valence_band_average
        self.spin_orbit_splitting = x*a.spin_orbit_splitting+(1.0-x)*b.spin_orbit_splitting
        self.band_gap = x*a.band_gap+(1.0-x)*b.band_gap+x*(1.0-x)*0.21
        self.deformation_valence = x*a.deformation_valence+(1.0-x)*b.deformation_valence
        self.deformation_conduction = x*a.deformation_conduction+(1.0-x)*b.deformation_conduction
        self.conduction_band = 0.0
        self.valence_band = 0.0

    def info(self):
        print("Lattice constant : {}".format(self.lattice_constant))
        print("Valence band average : {}".format(self.valence_band_average))
        print("Spin orbit : {}".format(self.spin_orbit))
        print("Band gap : {}".format(self.band_gap))

class GaAsSb(object):
    def __init__(self,x,y):
        a = GaAs(x,y)
        b = GaSb(x,y)
        self.lattice_constant = x*a.lattice_constant+(1.0-x)*b.lattice_constant
        self.elastic_constant_11 = x*a.elastic_constant_11+(1.0-x)*b.elastic_constant_11
        self.elastic_constant_12 = x*a.elastic_constant_12+(1.0-x)*b.elastic_constant_12
        self.elastic_constant_44 = x*a.elastic_constant_44+(1.0-x)*b.elastic_constant_44
        self.valence_band_average = x*a.valence_band_average+(1.0-x)*b.valence_band_average
        self.spin_orbit_splitting = x*a.spin_orbit_splitting+(1.0-x)*b.spin_orbit_splitting+x*(1-x)*0.60
        self.band_gap = x*a.band_gap+(1.0-x)*b.band_gap+x*(1.0-x)*1.2
        self.deformation_valence = x*a.deformation_valence+(1.0-x)*b.deformation_valence
        self.deformation_conduction = x*a.deformation_conduction+(1.0-x)*b.deformation_conduction
        self.conduction_band = 0.0
        self.valence_band = 0.0

    def info(self):
        print("Lattice constant : {}".format(self.lattice_constant))
        print("Valence band average : {}".format(self.valence_band_average))
        print("Spin orbit : {}".format(self.spin_orbit))
        print("Band gap : {}".format(self.band_gap))

class GaInP(object):
    def __init__(self,x,y):
        a = GaP(x,y)
        b = InP(x,y)
        self.lattice_constant = x*a.lattice_constant+(1.0-x)*b.lattice_constant
        self.elastic_constant_11 = x*a.elastic_constant_11+(1.0-x)*b.elastic_constant_11
        self.elastic_constant_12 = x*a.elastic_constant_12+(1.0-x)*b.elastic_constant_12
        self.elastic_constant_44 = x*a.elastic_constant_44+(1.0-x)*b.elastic_constant_44
        self.valence_band_average = x*a.valence_band_average+(1.0-x)*b.valence_band_average
        self.spin_orbit_splitting = x*a.spin_orbit_splitting+(1.0-x)*b.spin_orbit_splitting
        self.band_gap = x*a.band_gap+(1.0-x)*b.band_gap+x*(1.0-x)*0.79
        self.deformation_valence = x*a.deformation_valence+(1.0-x)*b.deformation_valence
        self.deformation_conduction = x*a.deformation_conduction+(1.0-x)*b.deformation_conduction
        self.conduction_band = 0.0
        self.valence_band = 0.0

    def info(self):
        print("Lattice constant : {}".format(self.lattice_constant))
        print("Valence band average : {}".format(self.valence_band_average))
        print("Spin orbit : {}".format(self.spin_orbit))
        print("Band gap : {}".format(self.band_gap))

class GaInAs(object):
    def __init__(self,x,y):
        a = GaAs(x,y)
        b = InAs(x,y)
        self.lattice_constant = x*a.lattice_constant+(1.0-x)*b.lattice_constant
        self.elastic_constant_11 = x*a.elastic_constant_11+(1.0-x)*b.elastic_constant_11
        self.elastic_constant_12 = x*a.elastic_constant_12+(1.0-x)*b.elastic_constant_12
        self.elastic_constant_44 = x*a.elastic_constant_44+(1.0-x)*b.elastic_constant_44
        self.valence_band_average = x*a.valence_band_average+(1.0-x)*b.valence_band_average
        self.spin_orbit_splitting = x*a.spin_orbit_splitting+(1.0-x)*b.spin_orbit_splitting+x*(1.0-x)*0.15
        self.band_gap = x*a.band_gap+(1.0-x)*b.band_gap+x*(1.0-x)*0.38
        self.deformation_valence = x*a.deformation_valence+(1.0-x)*b.deformation_valence
        self.deformation_conduction = x*a.deformation_conduction+(1.0-x)*b.deformation_conduction
        self.conduction_band = 0.0
        self.valence_band = 0.0

class GaInSb(object):
    def __init__(self,x,y):
        a = GaSb(x,y)
        b = InSb(x,y)
        self.lattice_constant = x*a.lattice_constant+(1.0-x)*b.lattice_constant
        self.elastic_constant_11 = x*a.elastic_constant_11+(1.0-x)*b.elastic_constant_11
        self.elastic_constant_12 = x*a.elastic_constant_12+(1.0-x)*b.elastic_constant_12
        self.elastic_constant_44 = x*a.elastic_constant_44+(1.0-x)*b.elastic_constant_44
        self.valence_band_average = x*a.valence_band_average+(1.0-x)*b.valence_band_average
        self.spin_orbit_splitting = x*a.spin_orbit_splitting+(1.0-x)*b.spin_orbit_splitting
        self.band_gap = x*a.band_gap+(1.0-x)*b.band_gap+x*(1.0-x)*0.42
        self.deformation_valence = x*a.deformation_valence+(1.0-x)*b.deformation_valence
        self.deformation_conduction = x*a.deformation_conduction+(1.0-x)*b.deformation_conduction
        self.conduction_band = 0.0
        self.valence_band = 0.0

    def info(self):
        print("Lattice constant : {}".format(self.lattice_constant))
        print("Valence band average : {}".format(self.valence_band_average))
        print("Spin orbit : {}".format(self.spin_orbit))
        print("Band gap : {}".format(self.band_gap))

class InPAs(object):
    def __init__(self,x,y):
        a = InP(x,y)
        b = InAs(x,y)
        self.lattice_constant = x*a.lattice_constant+(1.0-x)*b.lattice_constant
        self.elastic_constant_11 = x*a.elastic_constant_11+(1.0-x)*b.elastic_constant_11
        self.elastic_constant_12 = x*a.elastic_constant_12+(1.0-x)*b.elastic_constant_12
        self.elastic_constant_44 = x*a.elastic_constant_44+(1.0-x)*b.elastic_constant_44
        self.valence_band_average = x*a.valence_band_average+(1.0-x)*b.valence_band_average
        self.spin_orbit_splitting = x*a.spin_orbit_splitting+(1.0-x)*b.spin_orbit_splitting+x*(1.0-x)*0.10
        self.band_gap = x*a.band_gap+(1.0-x)*b.band_gap+x*(1.0-x)*0.28
        self.deformation_valence = x*a.deformation_valence+(1.0-x)*b.deformation_valence
        self.deformation_conduction = x*a.deformation_conduction+(1.0-x)*b.deformation_conduction
        self.conduction_band = 0.0
        self.valence_band = 0.0

    def info(self):
        print("Lattice constant : {}".format(self.lattice_constant))
        print("Valence band average : {}".format(self.valence_band_average))
        print("Spin orbit : {}".format(self.spin_orbit))
        print("Band gap : {}".format(self.band_gap))

class InPSb(object):
    def __init__(self,x,y):
        a = InP(x,y)
        b = InSb(x,y)
        self.lattice_constant = x*a.lattice_constant+(1.0-x)*b.lattice_constant
        self.elastic_constant_11 = x*a.elastic_constant_11+(1.0-x)*b.elastic_constant_11
        self.elastic_constant_12 = x*a.elastic_constant_12+(1.0-x)*b.elastic_constant_12
        self.elastic_constant_44 = x*a.elastic_constant_44+(1.0-x)*b.elastic_constant_44
        self.valence_band_average = x*a.valence_band_average+(1.0-x)*b.valence_band_average
        self.spin_orbit_splitting = x*a.spin_orbit_splitting+(1.0-x)*b.spin_orbit_splitting+x*(1.0-x)*0.75
        self.band_gap = x*a.band_gap+(1.0-x)*b.band_gap+x*(1.0-x)*1.30
        self.deformation_valence = x*a.deformation_valence+(1.0-x)*b.deformation_valence
        self.deformation_conduction = x*a.deformation_conduction+(1.0-x)*b.deformation_conduction
        self.conduction_band = 0.0
        self.valence_band = 0.0

    def info(self):
        print("Lattice constant : {}".format(self.lattice_constant))
        print("Valence band average : {}".format(self.valence_band_average))
        print("Spin orbit : {}".format(self.spin_orbit))
        print("Band gap : {}".format(self.band_gap))

class InAsSb(object):
    def __init__(self,x,y): 
        a = InAs(x,y)
        b = InSb(x,y)
        self.lattice_constant = x*a.lattice_constant+(1.0-x)*b.lattice_constant
        self.elastic_constant_11 = x*a.elastic_constant_11+(1.0-x)*b.elastic_constant_11
        self.elastic_constant_12 = x*a.elastic_constant_12+(1.0-x)*b.elastic_constant_12
        self.elastic_constant_44 = x*a.elastic_constant_44+(1.0-x)*b.elastic_constant_44
        self.valence_band_average = x*a.valence_band_average+(1.0-x)*b.valence_band_average
        self.spin_orbit_splitting = x*a.spin_orbit_splitting+(1.0-x)*b.spin_orbit_splitting+x*(1.0-x)*1.20
        self.band_gap = x*a.band_gap+(1.0-x)*b.band_gap+x*(1.0-x)*0.58
        self.deformation_valence = x*a.deformation_valence+(1.0-x)*b.deformation_valence
        self.deformation_conduction = x*a.deformation_conduction+(1.0-x)*b.deformation_conduction
        self.conduction_band = 0.0
        self.valence_band = 0.0

    def info(self):
        print("Lattice constant : {}".format(self.lattice_constant))
        print("Valence band average : {}".format(self.valence_band_average))
        print("Spin orbit : {}".format(self.spin_orbit))
        print("Band gap : {}".format(self.band_gap))

###### Quaternary ######

class AlGaInP(object):
    def __init__(self, x, y): 
        a = AlP(x,y)
        b = GaP(x,y)
        c = InP(x,y)

        self.lattice_constant = x*a.lattice_constant+y*b.lattice_constant+(1-x-y)*c.lattice_constant
        self.elastic_constant_11 = x*a.elastic_constant_11+y*b.elastic_constant_11+(1-x-y)*c.elastic_constant_11
        self.elastic_constant_12 = x*a.elastic_constant_12+y*b.elastic_constant_12+(1-x-y)*c.elastic_constant_12
        self.elastic_constant_44 = x*a.elastic_constant_44+y*b.elastic_constant_44+(1-x-y)*c.elastic_constant_44
        self.valence_band_average = x*a.valence_band_average+y*b.valence_band_average+(1-x-y)*c.valence_band_average
        self.spin_orbit_splitting = x*a.spin_orbit_splitting+y*b.spin_orbit_splitting+(1-x-y)*c.spin_orbit_splitting \
                -x*y*0.0 -x*(1-x-y)*0.0 -y*(1-x-y)*0.0
        self.band_gap = x*a.band_gap+(1-x)*b.band_gap \
                -x*y*0.0 -x*(1-x-y)*0.0 -y*(1-x-y)*0.79
        self.deformation_valence = x*a.deformation_valence+y*b.deformation_valence+(1-x-y)*c.deformation_valence
        self.deformation_conduction = x*a.deformation_conduction+y*b.deformation_conduction+(1-x-y)*c.deformation_conduction
        self.conduction_band = 0.0
        self.valence_band = 0.0

    def info(self):
        print("Lattice constant : {}".format(self.lattice_constant))
        print("Valence band average : {}".format(self.valence_band_average))
        print("Spin orbit : {}".format(self.spin_orbit))
        print("Band gap : {}".format(self.band_gap))

class AlGaInAs(object):
    def __init__(self,x,y): 
        a = AlAs(x,y)
        b = GaAs(x,y)
        c = InAs(x,y)

        self.lattice_constant = x*a.lattice_constant+y*b.lattice_constant+(1-x-y)*c.lattice_constant
        self.elastic_constant_11 = x*a.elastic_constant_11+y*b.elastic_constant_11+(1-x-y)*c.elastic_constant_11
        self.elastic_constant_12 = x*a.elastic_constant_12+y*b.elastic_constant_12+(1-x-y)*c.elastic_constant_12
        self.elastic_constant_44 = x*a.elastic_constant_44+y*b.elastic_constant_44+(1-x-y)*c.elastic_constant_44
        self.valence_band_average = x*a.valence_band_average+y*b.valence_band_average+(1-x-y)*c.valence_band_average
        self.spin_orbit_splitting = x*a.spin_orbit_splitting+y*b.spin_orbit_splitting+(1-x-y)*c.spin_orbit_splitting \
                -x*y*0.0 -x*(1-x-y)*0.15 -y*(1-x-y)*0.15
        self.band_gap = x*a.band_gap+(1-x)*b.band_gap \
                -x*y*0.37 -x*(1-x-y)*0.70 -y*(1-x-y)*0.38
        self.deformation_valence = x*a.deformation_valence+y*b.deformation_valence+(1-x-y)*c.deformation_valence
        self.deformation_conduction = x*a.deformation_conduction+y*b.deformation_conduction+(1-x-y)*c.deformation_conduction
        self.conduction_band = 0.0
        self.valence_band = 0.0

    def info(self):
        print("Lattice constant : {}".format(self.lattice_constant))
        print("Valence band average : {}".format(self.valence_band_average))
        print("Spin orbit : {}".format(self.spin_orbit))
        print("Band gap : {}".format(self.band_gap))

class AlGaAsSb(object):
    def __init__(self,x,y): 
        a = AlGaAs(x,y)
        b = AlGaSb(x,y)
        c = AlAsSb(y,x)
        d = GaAsSb(y,x)

        self.lattice_constant = (x*(1-x)*(y*a.lattice_constant+(1-y)*b.lattice_constant))/(x*(1-x)+y*(1-y)) \
            + (y*(1-y)*(x*c.lattice_constant+(1-x)*d.lattice_constant))/(x*(1-x)+y*(1-y))
        self.elastic_constant_11 = (x*(1-x)*(y*a.elastic_constant_11+(1-y)*b.elastic_constant_11))/(x*(1-x)+y*(1-y)) \
            + (y*(1-y)*(x*c.elastic_constant_11+(1-x)*d.elastic_constant_11))/(x*(1-x)+y*(1-y))
        self.elastic_constant_12 = (x*(1-x)*(y*a.elastic_constant_12+(1-y)*b.elastic_constant_12))/(x*(1-x)+y*(1-y)) \
            + (y*(1-y)*(x*c.elastic_constant_12+(1-x)*d.elastic_constant_12))/(x*(1-x)+y*(1-y))
        self.elastic_constant_44 = (x*(1-x)*(y*a.elastic_constant_44+(1-y)*b.elastic_constant_44))/(x*(1-x)+y*(1-y)) \
            + (y*(1-y)*(x*c.elastic_constant_44+(1-x)*d.elastic_constant_44))/(x*(1-x)+y*(1-y))
        self.valence_band_average = (x*(1-x)*(y*a.valence_band_average+(1-y)*b.valence_band_average))/(x*(1-x)+y*(1-y)) \
            + (y*(1-y)*(x*c.valence_band_average+(1-x)*d.valence_band_average))/(x*(1-x)+y*(1-y))
        self.spin_orbit_splitting = (x*(1-x)*(y*a.spin_orbit_splitting+(1-y)*b.spin_orbit_splitting))/(x*(1-x)+y*(1-y)) \
            + (y*(1-y)*(x*c.spin_orbit_splitting+(1-x)*d.spin_orbit_splitting))/(x*(1-x)+y*(1-y))
        self.band_gap = (x*(1-x)*(y*a.band_gap+(1-y)*b.band_gap))/(x*(1-x)+y*(1-y)) \
            + (y*(1-y)*(x*c.band_gap+(1-x)*d.band_gap))/(x*(1-x)+y*(1-y))
        self.deformation_valence = (x*(1-x)*(y*a.deformation_valence+(1-y)*b.deformation_valence))/(x*(1-x)+y*(1-y)) \
            + (y*(1-y)*(x*c.deformation_valence+(1-x)*d.deformation_valence))/(x*(1-x)+y*(1-y))
        self.deformation_conduction = (x*(1-x)*(y*a.deformation_conduction+(1-y)*b.deformation_conduction))/(x*(1-x)+y*(1-y)) \
            + (y*(1-y)*(x*c.deformation_conduction+(1-x)*d.deformation_conduction))/(x*(1-x)+y*(1-y))
        self.conduction_band = 0.0
        self.valence_band = 0.0

    def info(self):
        print("Lattice constant : {}".format(self.lattice_constant))
        print("Valence band average : {}".format(self.valence_band_average))
        print("Spin orbit : {}".format(self.spin_orbit))
        print("Band gap : {}".format(self.band_gap))

class GaInPAs(object):
    def __init__(self,x,y): 
        a = GaInP(x,y)
        b = GaInAs(x,y)
        c = GaPAs(y,x)
        d = InPAs(y,x)

        self.lattice_constant = (x*(1-x)*(y*a.lattice_constant+(1-y)*b.lattice_constant))/(x*(1-x)+y*(1-y)) \
            + (y*(1-y)*(x*c.lattice_constant+(1-x)*d.lattice_constant))/(x*(1-x)+y*(1-y))
        self.elastic_constant_11 = (x*(1-x)*(y*a.elastic_constant_11+(1-y)*b.elastic_constant_11))/(x*(1-x)+y*(1-y)) \
            + (y*(1-y)*(x*c.elastic_constant_11+(1-x)*d.elastic_constant_11))/(x*(1-x)+y*(1-y))
        self.elastic_constant_12 = (x*(1-x)*(y*a.elastic_constant_12+(1-y)*b.elastic_constant_12))/(x*(1-x)+y*(1-y)) \
            + (y*(1-y)*(x*c.elastic_constant_12+(1-x)*d.elastic_constant_12))/(x*(1-x)+y*(1-y))
        self.elastic_constant_44 = (x*(1-x)*(y*a.elastic_constant_44+(1-y)*b.elastic_constant_44))/(x*(1-x)+y*(1-y)) \
            + (y*(1-y)*(x*c.elastic_constant_44+(1-x)*d.elastic_constant_44))/(x*(1-x)+y*(1-y))
        self.valence_band_average = (x*(1-x)*(y*a.valence_band_average+(1-y)*b.valence_band_average))/(x*(1-x)+y*(1-y)) \
            + (y*(1-y)*(x*c.valence_band_average+(1-x)*d.valence_band_average))/(x*(1-x)+y*(1-y))
        self.spin_orbit_splitting = (x*(1-x)*(y*a.spin_orbit_splitting+(1-y)*b.spin_orbit_splitting))/(x*(1-x)+y*(1-y)) \
            + (y*(1-y)*(x*c.spin_orbit_splitting+(1-x)*d.spin_orbit_splitting))/(x*(1-x)+y*(1-y))
        self.band_gap = (x*(1-x)*(y*a.band_gap+(1-y)*b.band_gap))/(x*(1-x)+y*(1-y)) \
            + (y*(1-y)*(x*c.band_gap+(1-x)*d.band_gap))/(x*(1-x)+y*(1-y))
        self.deformation_valence = (x*(1-x)*(y*a.deformation_valence+(1-y)*b.deformation_valence))/(x*(1-x)+y*(1-y)) \
            + (y*(1-y)*(x*c.deformation_valence+(1-x)*d.deformation_valence))/(x*(1-x)+y*(1-y))
        self.deformation_conduction = (x*(1-x)*(y*a.deformation_conduction+(1-y)*b.deformation_conduction))/(x*(1-x)+y*(1-y)) \
            + (y*(1-y)*(x*c.deformation_conduction+(1-x)*d.deformation_conduction))/(x*(1-x)+y*(1-y))
        self.conduction_band = 0.0
        self.valence_band = 0.0

    def info(self):
        print("Lattice constant : {}".format(self.lattice_constant))
        print("Valence band average : {}".format(self.valence_band_average))
        print("Spin orbit : {}".format(self.spin_orbit))
        print("Band gap : {}".format(self.band_gap))

class GaInAsSb(object):
    def __init__(self,x,y): 
        a = GaInAs(x,y)
        b = GaInSb(x,y)
        c = GaAsSb(y,x)
        d = InAsSb(y,x)

        self.lattice_constant = (x*(1-x)*(y*a.lattice_constant+(1-y)*b.lattice_constant))/(x*(1-x)+y*(1-y)) \
            + (y*(1-y)*(x*c.lattice_constant+(1-x)*d.lattice_constant))/(x*(1-x)+y*(1-y))
        self.elastic_constant_11 = (x*(1-x)*(y*a.elastic_constant_11+(1-y)*b.elastic_constant_11))/(x*(1-x)+y*(1-y)) \
            + (y*(1-y)*(x*c.elastic_constant_11+(1-x)*d.elastic_constant_11))/(x*(1-x)+y*(1-y))
        self.elastic_constant_12 = (x*(1-x)*(y*a.elastic_constant_12+(1-y)*b.elastic_constant_12))/(x*(1-x)+y*(1-y)) \
            + (y*(1-y)*(x*c.elastic_constant_12+(1-x)*d.elastic_constant_12))/(x*(1-x)+y*(1-y))
        self.elastic_constant_44 = (x*(1-x)*(y*a.elastic_constant_44+(1-y)*b.elastic_constant_44))/(x*(1-x)+y*(1-y)) \
            + (y*(1-y)*(x*c.elastic_constant_44+(1-x)*d.elastic_constant_44))/(x*(1-x)+y*(1-y))
        self.valence_band_average = (x*(1-x)*(y*a.valence_band_average+(1-y)*b.valence_band_average))/(x*(1-x)+y*(1-y)) \
            + (y*(1-y)*(x*c.valence_band_average+(1-x)*d.valence_band_average))/(x*(1-x)+y*(1-y))
        self.spin_orbit_splitting = (x*(1-x)*(y*a.spin_orbit_splitting+(1-y)*b.spin_orbit_splitting))/(x*(1-x)+y*(1-y)) \
            + (y*(1-y)*(x*c.spin_orbit_splitting+(1-x)*d.spin_orbit_splitting))/(x*(1-x)+y*(1-y))
        self.band_gap = (x*(1-x)*(y*a.band_gap+(1-y)*b.band_gap))/(x*(1-x)+y*(1-y)) \
            + (y*(1-y)*(x*c.band_gap+(1-x)*d.band_gap))/(x*(1-x)+y*(1-y))
        self.deformation_valence = (x*(1-x)*(y*a.deformation_valence+(1-y)*b.deformation_valence))/(x*(1-x)+y*(1-y)) \
            + (y*(1-y)*(x*c.deformation_valence+(1-x)*d.deformation_valence))/(x*(1-x)+y*(1-y))
        self.deformation_conduction = (x*(1-x)*(y*a.deformation_conduction+(1-y)*b.deformation_conduction))/(x*(1-x)+y*(1-y)) \
            + (y*(1-y)*(x*c.deformation_conduction+(1-x)*d.deformation_conduction))/(x*(1-x)+y*(1-y))
        self.conduction_band = 0.0
        self.valence_band = 0.0

    def info(self):
        print("Lattice constant : {}".format(self.lattice_constant))
        print("Valence band average : {}".format(self.valence_band_average))
        print("Spin orbit : {}".format(self.spin_orbit))
        print("Band gap : {}".format(self.band_gap))

class InPAsSb(object):
    def __init__(self,x,y): 
        a = InP(x,y)
        b = InAs(x,y)
        c = InSb(x,y)

        self.lattice_constant = x*a.lattice_constant+y*b.lattice_constant+(1-x-y)*c.lattice_constant
        self.elastic_constant_11 = x*a.elastic_constant_11+y*b.elastic_constant_11+(1-x-y)*c.elastic_constant_11
        self.elastic_constant_12 = x*a.elastic_constant_12+y*b.elastic_constant_12+(1-x-y)*c.elastic_constant_12
        self.elastic_constant_44 = x*a.elastic_constant_44+y*b.elastic_constant_44+(1-x-y)*c.elastic_constant_44
        self.valence_band_average = x*a.valence_band_average+y*b.valence_band_average+(1-x-y)*c.valence_band_average
        self.spin_orbit_splitting = x*a.spin_orbit_splitting+y*b.spin_orbit_splitting+(1-x-y)*c.spin_orbit_splitting \
                -x*y*0.10 -x*(1-x-y)*0.75 -y*(1-x-y)*1.2
        self.band_gap = x*a.band_gap+(1-x)*b.band_gap \
                -x*y*0.28 -x*(1-x-y)*1.3 -y*(1-x-y)*0.58
        self.deformation_valence = x*a.deformation_valence+y*b.deformation_valence+(1-x-y)*c.deformation_valence
        self.deformation_conduction = x*a.deformation_conduction+y*b.deformation_conduction+(1-x-y)*c.deformation_conduction
        self.conduction_band = 0.0
        self.valence_band = 0.0

    def info(self):
        print("Lattice constant : {}".format(self.lattice_constant))
        print("Valence band average : {}".format(self.valence_band_average))
        print("Spin orbit : {}".format(self.spin_orbit))
        print("Band gap : {}".format(self.band_gap))