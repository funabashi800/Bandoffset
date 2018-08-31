import param
import sys
from param import InSb, GaSb, InP, GaAs, AlSb, Ternary
import plotting_tools as macro_plot

print("Please input the buffer or substrate material")
sub = globals()[input("material : ")]
if len(str(sub)) > 20:
    print("Please input one of the materials and composition")
    material = globals()[input("material : ")]
    material_1 = material()
    comp_1 = int(input("composition : "))
    print("Please input the other material and composition")
    material = globals()[input("material : ")]
    material_2 = material()
    comp_2 = int(input("composition : "))
    if comp_1 + comp_2 != 1.0:
        print("Oops! Value error: there is wrong composition value in your input")
        sys.exit()
    else:
        buffer = Ternary()
        buffer.lattice_constant = material_1.lattice_constant * comp_1 + material_2.lattice_constant * comp_2
else:
    buffer = sub()

print("Please input the back barrier or barrier on the buffer layer\n")
ba = globals()[input("material : ")]
if len(str(ba)) > 20:
    print("Please input one of the materials and composition")
    ba_1 = globals()[input("material : ")]
    material_1 = ba_1()
    comp_1 = int(input("composition : "))
    print("Please input the other material and composition")
    ba_2 = globals()[input("material : ")]
    material_2 = ba_2()
    comp_2 = int(input("composition : "))
    if comp_1 + comp_2 != 1.0:
        print("Oops! Value error: there is wrong composition value in your input")
        sys.exit()
    else:
        barrier = Ternary()
        barrier.lattice_constant = material_1.lattice_constant * comp_1 + material_2.lattice_constant * comp_2
        barrier.elastic_constant_11 = material_1.elstic_constant_11 * comp_1 + material_2.elstic_constant_11 * comp_2
        barrier.elastic_constant_12 = material_1.elastic_constant_12 * comp_1 + material_2.elastic_constant_12 * comp_2
        barrier.elastic_constant_44 = material_1.elastic_constant_44 * comp_1 + material_2.elastic_constant_44 * comp_2
        barrier.valence_band_average = material_1.valence_band_average * comp_1 + material_2.valence_band_average * comp_2
        barrier.spin_orbit_splitting = material_1.spin_orbit_splitting * comp_1 + material_2.spin_orbit_splitting * comp_2
        barrier.band_gap = material_1.band_gap * comp_1 + material_2.band_gap * comp_2
        barrier.deformation_valence = material_1.deformation_valence * comp_1 + material_2.deformation_valence * comp_2
        barrier.deformation_conduction = material_1.deformation_conduction * comp_1 + material_2.deformation_conduction * comp_2
else:
    barrier = ba()

print("Please input the channel material\n")
ch = globals()[input("material : ")]
if len(str(ch)) > 20:
    print("Please input one of the materials and composition")
    ch_1 = globals()[input("material : ")]
    material_1 = ch_1()
    comp_1 = int(input("composition : "))
    print("Please input the other material and composition")
    ch_2 = globals()[input("material : ")]
    material_2 = ch_2()
    comp_2 = int(input("composition : "))
    if comp_1 + comp_2 != 1.0:
        print("Oops! Value error: there is wrong composition value in your input")
        
    else:
        channel = Ternary()
        channel.lattice_constant = material_1.lattice_constant * comp_1 + material_2.lattice_constant * comp_2
        channel.elastic_constant_11 = material_1.elstic_constant_11 * comp_1 + material_2.elstic_constant_11 * comp_2
        channel.elastic_constant_12 = material_1.elastic_constant_12 * comp_1 + material_2.elastic_constant_12 * comp_2
        channel.elastic_constant_44 = material_1.elastic_constant_44 * comp_1 + material_2.elastic_constant_44 * comp_2
        channel.valence_band_average = material_1.valence_band_average * comp_1 + material_2.valence_band_average * comp_2
        channel.spin_orbit_splitting = material_1.spin_orbit_splitting * comp_1 + material_2.spin_orbit_splitting * comp_2
        channel.band_gap = material_1.band_gap * comp_1 + material_2.band_gap * comp_2
        channel.deformation_valence = material_1.deformation_valence * comp_1 + material_2.deformation_valence * comp_2
        channel.deformation_conduction = material_1.deformation_conduction * comp_1 + material_2.deformation_conduction * comp_2
else:
    channel = ch()

# buffer band energy

buffer_valence = buffer.valence_band_average + (buffer.spin_orbit_splitting / 3)
buffer_valence = buffer_valence * -1
buffer_conduction = buffer.valence_band_average + (buffer.spin_orbit_splitting / 3) + buffer.band_gap
buffer_conduction = buffer_conduction * -1

# barrier band energy

a = buffer.lattice_constant
d = 2 * barrier.elastic_constant_12 / barrier.elastic_constant_11
a_ = barrier.lattice_constant * (1 - d * (a / barrier.lattice_constant - 1))
ips = a / barrier.lattice_constant - 1
ips_ = a_ /barrier.lattice_constant - 1

delta_valence = barrier.deformation_valence * (2 * ips + ips_)
delta_conduction = barrier.deformation_conduction * (2 * ips + ips_)

barrier_valence = barrier.valence_band_average + (barrier.spin_orbit_splitting / 3) + delta_valence
barrier_valence = barrier_valence * -1
barrier_conduction = barrier.valence_band_average + (barrier.spin_orbit_splitting / 3) + barrier.band_gap + delta_conduction
barrier_conduction = barrier_conduction * -1

# channel band energy

a = buffer.lattice_constant
d = 2 * channel.elastic_constant_12 / channel.elastic_constant_11
a_ = channel.lattice_constant * (1 - d * (a / channel.lattice_constant - 1))
ips = a / channel.lattice_constant - 1
ips_ = a_ /channel.lattice_constant - 1

delta_valence = channel.deformation_valence * (2 * ips + ips_)
delta_conduction = channel.deformation_conduction * (2 * ips + ips_)

channel_valence = channel.valence_band_average + (channel.spin_orbit_splitting / 3) + delta_valence
channel_valence = channel_valence * -1
channel_conduction = channel.valence_band_average + (channel.spin_orbit_splitting / 3) + channel.band_gap + delta_conduction
channel_conduction = channel_conduction * -1

# plot band alignment


energies = [[channel_conduction,channel_valence],[barrier_conduction,barrier_valence],[buffer_conduction,buffer_valence]]
materials = [ch,ba,sub]
macro_plot.energy_band_alignment_diagram(energies,materials,limit=10,arrowhead=0.1)
