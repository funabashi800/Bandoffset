class AlP(object):
    def __init__(self):
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
    def __init__(self):
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
    def __init__(self):
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
    def __init__(self):
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
    def __init__(self):
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
    def __init__(self):
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
    def __init__(self):
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
    def __init__(self):
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
    def __init__(self):
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

class AlAsSb(object):
    def __init__(self, x):
        a = AlAs()
        b = AlSb()
        self.lattice_constant = x*a.lattice_constant+(1-x)*b.lattice_constant
        self.elastic_constant_11 = 0.88
        self.elastic_constant_12 = 0.43
        self.elastic_constant_44 = 0.41
        self.valence_band_average = -6.66
        self.spin_orbit_splitting = 0.65
        self.band_gap = 0.0
        self.deformation_valence = -1.38
        self.deformation_conduction = -6.97 #Ganma
        self.conduction_band = 0.0
        self.valence_band = 0.0

    def info(self):
        print("Lattice constant : {}".format(self.lattice_constant))
        print("Valence band average : {}".format(self.valence_band_average))
        print("Spin orbit : {}".format(self.spin_orbit))
        print("Band gap : {}".format(self.band_gap))

class AlGaP(object):
    def __init__(self):
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

class AlGaAs(object):
    def __init__(self):
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

class AlGaSb(object):
    def __init__(self):
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

class AlInP(object):
    def __init__(self):
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

class AlInAs(object):
    def __init__(self,x):
        self.lattice_constant = x*AlAs.lattice_constant+(1-x)*InAs.lattice_constant
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

class AlPAs(object):
    def __init__(self):
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

class GaAsSb(object):
    def __init__(self):
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

class GaInP(object):
    def __init__(self):
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

class GaInSb(object):
    def __init__(self):
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

class InPAs(object):
    def __init__(self):
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

class InPSb(object):
    def __init__(self):
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

class InAsSb(object):
    def __init__(self):
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