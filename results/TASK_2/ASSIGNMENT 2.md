<a name="_bum1s8drs34"></a>ASSIGNMENT 2 
## <a name="_swu0kba818le"></a>Mesh File
- The Mesh file is in its native format .su2.
- I have used the gmsh software to generate my mesh file.
- The geometry has the following Boundary conditions: 
  - Velocity inlet
  - Zero pressure outlet
  - Adiabatic walls on the left and top 
  - Axisymmetric on the bottom.
- The following snippet shows the details of the Geometry.

  ![](Aspose.Words.04ddf8b4-4b16-447b-a2df-a351ae641344.001.png)  

- The output mesh file looks like this : 

  ![](Aspose.Words.04ddf8b4-4b16-447b-a2df-a351ae641344.002.png)


## <a name="_enuov1hng7c5"></a>Configuration File
- In the configuration file, I learned about the MATH\_PROBLEM  option and how it can be adjusted to get a DIRECT or ADJOINT solution.
- We used the FLUID\_MODEL as INC\_RANS and MATH\_PROBLEM as DIRECT because of turbulent nature of the flow. Turbulence model being SA(Spalart Allmaras).
- I have taken inlet velocity as 15 m/s with outlet pressure as 1E5.
- For the time being, other conditions are as per standard rules.
- To run the simulation, we must give the command SU2\_CFD config.cfg from our terminal window.
## <a name="_wqgxooo58ne2"></a>My Output
- After running the command I got the three files as output: history, flow.vtu and surface.vtu .
- I visualized the solution on Paraview, which can be seen in the screenshot below.

  ![](Aspose.Words.04ddf8b4-4b16-447b-a2df-a351ae641344.003.png)

- To validate my results I have compared the results with data taken from a research paper.
- Here I’ll be plotting the mean centerline velocity as a function of the distance from the ![](Aspose.Words.04ddf8b4-4b16-447b-a2df-a351ae641344.004.png)nozzle.

![](Aspose.Words.04ddf8b4-4b16-447b-a2df-a351ae641344.005.png)

