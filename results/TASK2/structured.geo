// Gmsh project created on Sat Mar 16 11:27:07 2024
//+
Point(1) = {0, 0, 0, 1.0};
//+
Point(2) = {0, 0.2, 0, 1.0};
//+
Point(3) = {0, 2, 0, 1.0};
//+
Point(4) = {4, 2, 0, 1.0};
//+
Point(5) = {4, 0, 0, 1.0};
//+
Line(1) = {3, 2};
//+
Line(2) = {2, 1};
//+
Line(3) = {5, 1};
//+
Line(4) = {4, 5};
//+
Line(5) = {3, 4};
//+
Curve Loop(1) = {5, 4, 3, -2, -1};
//+
Plane Surface(1) = {1};
//+
Physical Surface("walle", 6) = {1};
//+
//Physical Curve("walle", 6) += {2};
//+
Physical Curve("inlet", 7) = {2};
//+
Physical Curve("top_bottome", 8) = {5};
//+
Physical Curve("top_bottome", 8) += {3};
//+
Physical Curve("outlet", 9) = {4};
//+
Transfinite Surface {1};
//+
Transfinite Surface {1} = {3, 4, 5, 1};

//+
Transfinite Curve {1} = 15 Using Progression 1;
//+
Transfinite Curve {2} = 45 Using Progression 1;
//+
Transfinite Curve {4, 4} = 59 Using Progression 1;
//+
Transfinite Curve {5, 3} = 50 Using Progression 1;
//+
// Generate mesh
Mesh.ElementOrder = 1; // Quadratic elements
Mesh.ElementOrderBound = 1; // Linear elements on boundaries
Mesh.RecombineAll = 1; // Recombine elements
Mesh 2;

// Export mesh in SU2 format
//Mesh.MeshFormat = 2;
