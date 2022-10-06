# Poissons-equation
I used Hooke's law at a time of infinity to represent the laplacian operator. Just give it initial contitions, boundary conditions, and you can put any conservative field inside it as well.
<br />
Solves Laplace equation, Poissons equation, wave equation, heat equation, field equations, and customize the boundaries/initial conditions to be whatever functions you want. <br />
You could vibrate a point in the middle if you want, pulse points along the boundary, throw electrons around. The limits are your imagination.<br />
Use arrows, "W" and "S" to fly around. It uses my 3d conversion file to plot the 3d points on a 2d 1920x1080 plane
<br />
My secret is that the laplace and poisson equation is just basically taking the time limit as it approaches infinity of the 3d function which is also kind of the wave equation. By taking the limit at time of infinity, that's basically how I get rid of the time dependence (as long as it is at a steady state at t=inf). And this is the reason the divergence of the gradient of the potential function can satisfy the equation. A 2d version of Hooke's law is the governing equation which can discretely be substituted in for the Laplacian of the potential. 

<br /><br />
2 free ends wave equation
<br />
![wave equation](https://github.com/BryceP-44/Poissons-equation/blob/main/wave3d3gif.gif)
<br />
black hole
<br />
![black hole](https://github.com/BryceP-44/Poissons-equation/blob/main/black%20hole.PNG)
<br />
2 free ends 2 sine ends (wave3d2)
<br />
![free ends](https://github.com/BryceP-44/Poissons-equation/blob/main/2%20free%202%20sine%20boundaries.PNG)
<br />
first test run (wave3d1)
<br />
![first test run](https://github.com/BryceP-44/Poissons-equation/blob/main/first%20test.PNG)
<br />
4 corners at 0 and the middle point at -200
<br />
![saddle](https://github.com/BryceP-44/Poissons-equation/blob/main/3d5.PNG)





