# SpiderWebConfiguration
Repository for the calculation  of a spiderweb configurarion based on "Spiderweb Central Configurations" by Hénot and Rousseau.(https://link.springer.com/article/10.1007/s12346-019-00330-y).



*In progress* <br>
**Files**: <br>
basic_functions.py - Necessary Functions to write the main system.<br>
Diff_potential.py - Decision about the linear stability of a central configuration <br>
fsolve_method.py  - Methods to solve the non-linear systems associated (fsolve function from numpy)<br>
main_plot.py - Plot all specified central configurations <br>
main.py - function to generate the points of central configurations <br>
main_instability.py - generate data about the linear stability for all central configurations <br>
mass_dist_generator.py - Generator of a mass distribution. At this moment this is not random.<br>
parameters.py  - Parameters to be used in the program. <br>
points_configuration.py - Generates the points of a specific central configuration <br>
plot_data.py  - Plot a specific central configuration<br>
read_data.py  - read the data files <br>
writing_file.py - Generated the data files <br>


**Folders** <br>
data - Folder with data files with point for central configurations and information about linear stability <br>
figs - Folder with the figs <br>
N_body_simulation - Folder with code files for the N-body simulation <br>


**Issues** <br>

fsolve does not provide a solution in some cases (It seems fixed) <br>
N_body_simulation nedded to be addapted 



             



