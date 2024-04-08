# <a name="_bum1s8drs34"></a>Quick Start 
## <a name="_swu0kba818le"></a>Mesh File
- The Mesh file is in its native format .su2 .
- It has triangular meshing with 10216 triangular cells, 5233 points, and two boundaries (or “markers”) named *airfoil* and *farfield*. 

  

  ![](Aspose.Words.2ce079df-077d-425b-926c-ec925e630d0c.001.png)

## <a name="_enuov1hng7c5"></a>Configuration File
- In the configuration file, I learned about the MATH\_PROBLEM  option and how it can be adjusted to get a DIRECT or ADJOINT solution.
- We used the EULER SOLVER with tangency conditions for the airfoil and characteristic boundary flow conditions for the Farfield.
- The output files are Paraview, Restart and a flow.csv file which contains data of all the properties related to flow. 
- To run the simulation, we have to give the command SU2\_CFD config.cfg from our terminal window.
## <a name="_wqgxooo58ne2"></a>My Output
- After running the command I got the three files as output.
- I visualized the solution on Paraview, which can be seen in the below screenshot.

  ![](Aspose.Words.2ce079df-077d-425b-926c-ec925e630d0c.002.png)

- I plotted the pressure coefficient variable against the position of points on the airfoil, and it looked like:

  ![](Aspose.Words.2ce079df-077d-425b-926c-ec925e630d0c.003.png)

