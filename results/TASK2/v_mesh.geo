// Gmsh project created on Wed Mar 13 00:45:34 2024
//+
Point(1) = {0, -0.125, 0, 1.0};
Point(2) = {1, -0.125, 0, 1.0};
Point(3) = {1, 0.125, 0, 1.0};
Point(4) = {0, 0.125, 0, 1.0};
//+
Line(1) = {1, 2}; Transfinite Curve {1} = 40 Using Progression 1;
Line(2) = {2, 3}; Transfinite Curve {2} = 20 Using Progression 1;
Line(3) = {3, 4}; Transfinite Curve {3} = 40 Using Progression 1;
Line(4) = {4, 1}; Transfinite Curve {4} = 20 Using Progression 1;

Physical Curve("inlet", 5) = {4};
Physical Curve("outlet", 6) = {2};
Physical Curve("wall", 7) = {3,1};

Curve Loop(1) = {4, 1, 2, 3};
Plane Surface(1) = {1};
Physical Surface("fluid", 1) = {1};

Compound Curve {2,4};
Compound Curve {1,3};

Transfinite Surface {1};

// Generate mesh
Mesh.ElementOrder = 1; // Quadratic elements
Mesh.ElementOrderBound = 1; // Linear elements on boundaries
Mesh.RecombineAll = 1; // Recombine elements
Mesh 2;

// Export mesh in SU2 format
//Mesh.MeshFormat = 2;
