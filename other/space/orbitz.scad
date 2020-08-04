


use <myshapes.scad> 
 
use <fff.scad> 
 
 
 
 
fn = 60;

// m miles scale..

//diameter in miles
sun = 865*1000;
mer = 3031.9;
venus = 7521;

moon = 2159;
dmoon = 238900;

earth = 7900;
mars = 4200;
jupiter = 86881;

// miles from sun
dme = 29.367*1000000; 
dv = 67.615*1000000;
de = 94.348*1000000;
dm = 129*1000000;
dj = 478.97*1000*1000;
    
    ds = 111*1000000;
    
pi = 3.14159265;

//orbit speed to angular velocity
//me 88 days
//venus 225 days
//mars 687 earth days? per revolution around the sun duh...
//jupiter 4300 days== 12 years == 99k hours
// v = d/t
// d = vt
// t = d/v
// c = 2r pi
// av = c / t
// av = 2*r*pi / t (in days?)

//funciton dis(a, b) = sqrt( (a*a -

function angularV(d, t) = 2*d*pi / (t*24*360);

ave = angularV(de, 365 );    

//solar satelite, plutoes
avs = angularV(ds, 888 );   
echo(avs);
avmars = angularV(dm, 687 ); 
avmer = angularV(dme, 88);  
avv = angularV(dv, 225);  
avj = angularV(dj, 4300);  

//avmoon = angularV(dmoon, 27.3);  

// ------------------------------------ //
// ------------------------------------ //
// ------------------------------------ //



see = 1111; //scale planets/stars to see them...

color("grey")
planet(earth*see/2, ds, avs, 11);

color("grey")
planet(earth*see/2, ds, avs, 22);


 rotate([0,0, $t *11]) color("white") 
planet(sun*11, 0, 11, 0);
  
color("green")
planet(earth*see, de, ave, 0);

color("red")
planet(mars*see, dm, avmars, -5);
color("orange")
planet(mer*see, dme, avmer, 0);
color("orange")
planet(venus*see, dv, avv, 0);

color("yellow")
planet(jupiter*see/10, dj, avj, 0);


color("blue") cy(see*111111, 1, fn);


// ------------------------------------ //
//
//for(i=[-3:5])
//color("yellow")
//planet(mars*see, dm*1.2+i*2, avmars, 1);
// ------------------------------------ //
// ------------------------------------ //



//scale the ship more, its tiny...but huge?
ee = 111111;
vv = 111;

//function getPos( ) =  [vv*de*cos($t/pi), vv*de*sin($t/pi), 0];
// function getPos( ) = [de, 0,0]; 
// function getRos( ) = [de, 0,$t*vv]; 
// 
//rotate(getPos()) 
//translate(getPos())   
//scale([ee, ee, ee])
//cc();

ship(vv, 0);
trip = dm - de;

module ship(  av, off){
    a = av*1;
       rotate([0,0, $t*a + off*11]) translate([0, ds + $t*trip, 0]) 
   rotate([0,-90, 0])  scale([ee, ee, ee])     cc();
    
}
 

// ------------------------------------ //
// ------------------------------------ //
// ------------------------------------ //


// ------------------------------------ //
// ------------------------------------ //
// ------------------------------------ //



//er();

module er( ){
    a = ave*1;
       rotate([0,0, $t*a]) translate([0, de, 0])  
        color("green") sp(earth*111, fn);
    
    
        rotate([0,0, $t*a]) translate([0, de+dmoon, 0])  
        color("yellow") sp(moon*11, fn);
    
}
 //655.2 hours 27.3 days moon orbit

 

module planet(s, dis, av, off){
    a = av*1;
       rotate([0,0, $t*a + off*11]) translate([0, dis, 0])  sp(s, fn);
}
 
// 
module shell(d,c){
     hull(){
       translate([0,0, h+d])  sp(cd, h, fn);
       translate([0,0, h+d-2])  sp(cdd, h, fn);
       translate([0,0, h/2])  cy(d, h, fn);
       translate([0,0, h/2])  cy(d+2, 3, fn);
     }
    n = 2;
     a = 360/n;
     
       for(i=[0:n-1]) rotate([0,0, i*a]) translate([0,bd/2, 0])  fin();
}

 
