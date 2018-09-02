import os
import sys
import param_all
import plotting_tools as macro_plot
from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('index.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        material1 = request.form.get('material1')
        material2 = request.form.get('material2')
        material3 = request.form.get('material3')
        a = getattr(param_all, material1)
        b = getattr(param_all, material2)
        c = getattr(param_all, material3)
        x1 = request.form.get('x1')
        y1 = request.form.get('y1')
        x2 = request.form.get('x2')
        y2 = request.form.get('y2')
        x3 = request.form.get('x3')
        y3 = request.form.get('y3')
        material_1 = a(float(x1), float(y1))
        material_2 = b(float(x2), float(y2))
        material_3 = c(float(x3), float(y3))

        #### on channel
        a_1 = material_3.lattice_constant
        d = 2.0 * material_1.elastic_constant_12/material_1.elastic_constant_11
        a_2 = material_1.lattice_constant * (1.0-d*(a_1/material_1.lattice_constant-1.0))
        ips_1 = a_1/material_1.lattice_constant-1.0
        ips_2 = a_2/material_1.lattice_constant-1.0
        delta_valence = material_1.deformation_valence*(2*ips_1+ips_2)
        delta_conduction = material_1.deformation_conduction*(2*ips_1+ips_2)
        material_1.valence_band = material_1.valence_band_average + material_1.spin_orbit_splitting/3.0 + delta_valence
        material_1.valence_band = -1.0 * material_1.valence_band
        material_1.conduction_band = material_1.valence_band_average + material_1.spin_orbit_splitting/3.0 + material_1.band_gap + delta_conduction
        material_1.conduction_band = -1.0 * material_1.conduction_band

        #### on barrier
        a_1 = material_3.lattice_constant
        d = 2.0 * material_2.elastic_constant_12/material_2.elastic_constant_11
        a_2 = material_2.lattice_constant * (1.0-d*(a_1/material_2.lattice_constant-1.0))
        ips_1 = a_1/material_2.lattice_constant-1.0
        ips_2 = a_2/material_2.lattice_constant-1.0
        delta_valence = material_2.deformation_valence*(2*ips_1+ips_2)
        delta_conduction = material_2.deformation_conduction*(2*ips_1+ips_2)
        material_2.valence_band = material_2.valence_band_average + material_2.spin_orbit_splitting/3.0 + delta_valence
        material_2.valence_band = -1.0 * material_2.valence_band
        material_2.conduction_band = material_2.valence_band_average + material_2.spin_orbit_splitting/3.0 + material_2.band_gap + delta_conduction
        material_2.conduction_band = -1.0 * material_2.conduction_band

        #### on substrate
        material_3.valence_band = material_3.valence_band_average + material_3.spin_orbit_splitting/3.0
        material_3.valence_band = -1.0 * material_3.valence_band
        material_3.conduction_band = material_3.valence_band_average + material_3.spin_orbit_splitting/3.0 + material_3.band_gap
        material_3.conduction_band = -1.0 * material_3.conduction_band

        #### Plot Band Alignment
        energies = [(material_1.conduction_band,material_1.valence_band),(material_2.conduction_band,material_2.valence_band),(material_3.conduction_band,material_3.valence_band)]
        materials = [material1,material2,material3]
        macro_plot.energy_band_alignment_diagram(energies,materials,limit=10,arrowhead=0.1)
        return render_template('hello.html',name='Band Alignment', url='/static/images/BandAlignment.png')

if __name__ == '__main__':
    app.run(debug=True)