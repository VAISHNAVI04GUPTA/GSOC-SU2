# SU2 Project
## Installation
- Downlaod and Install SU2 from [SU2 Website](https://su2code.github.io/download.html)
- Run some basic test cases from tutorial section
- I have included my results from tutorials in test_cases Folder.
## Starting with the Case Study
### Mesh Generation
- Setup a mesh using mesh generator softwares like gmsh.
- We can also use a Python file to generate a mesh for our case.
- I have used both the options : rectangle.py file and structured.geo file.
### Understanding the Case.
- Here, I have worked with an axisymmetric turbulent jet.
- Studied about Different flow conditions like Reynolds Number, Mach number, Viscosity etc.
### Writing a Configuration file.
- To solve our case we write a configuration file which has all the details about solver type, specifications, boundary conditions and inlet/outlet data.
- I have used the file named RANS_jet.cfg
### Post-Processing
- After running the config file from command line we get output files.
- In this case, I got history.csv, restart.dat, surface.vtu and vol_solution.vtu.
- For visualizing the results I have used ParaView software.
- The images in TASK2 folder shows the results.
