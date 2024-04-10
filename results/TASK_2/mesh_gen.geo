// Gmsh project created on Tue Apr  9 15:13:09 2024
SetFactory("OpenCASCADE");
// Define the geometry 
Point(1) = {0, 0, 0, 1.0};
//+
Point(2) = {0.1, 0, 0, 1.0};
//+
Point(3) = {0.1, 0.01, 0, 1.0};
//+
Point(4) = {0.1, 0.1, 0, 1.0};
//+
Point(5) = {0., 0.1, 0, 1.0};
//+
Point(6) = {0., 0.005, 0, 1.0};
//+
Line(1) = {1, 2};
//+
Line(2) = {6, 3};
//+
Line(3) = {1, 6};
//+
Line(4) = {2, 3};
//+
Line(5) = {6, 5};
//+
Line(6) = {3, 4};
//+
Line(7) = {5, 4};
//+
Curve Loop(1) = {5, 7, -6, -2};
//+
Plane Surface(1) = {1};
//+
Curve Loop(2) = {3, 2, -4, -1};
//+
Plane Surface(2) = {2};
// Define boundary conditions
Physical Curve("inlet", 8) = {3};
//+
Physical Curve("outlet", 9) = {4};
//+
Physical Curve("wall", 10) = {1,6};
//+
Physical Curve("symmetry", 11) = {5,7};
// This one is important!
Physical Surface("fluid", 12) = {1,2};
// Define mesh 
Transfinite Curve {3, 4} = 20 Using Progression 1;
//+
Transfinite Curve {5, 6} = 50 Using Progression 1.05;
//+
Transfinite Curve {1, 2, 7} = 200 Using Progression 1.0;
//+
Transfinite Surface {2} = {1, 2, 3, 6};
//+
Transfinite Surface {1} = {6, 3, 4, 5};
//+
Recombine Surface {1, 2};
