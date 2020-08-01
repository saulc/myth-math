


use <myshapes.scad> 
 
 
 
fn = 60;

// meter scale..
 
sun = 865*1000;
mer = 3031.9;
venus = 7521;


moon = 2159;
dmoon = 238900;

earth = 7900;
mars = 4200;
//jupiter = 86881;

dme = 29.367*1000000;
dv = 67.615*1000000;
de = 94.348*1000000;
dm = 129*1000000;
dj = 478.97*1000*1000;
    
    
    
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

function angularV(d, t) = 2*d*pi / t;

ave = angularV(de, 365);    

avmars = angularV(dm, 687); 
avmer = angularV(dme, 88);  
avv = angularV(dv, 225);  
avj = angularV(dj, 4300);  

avmoon = angularV(dmoon, 27.3);  



see = 1111;

 rotate([0,0, $t *11]) color("white") 
planet(sun*11, 0, 0);
  
//color("green")
//planet(earth*see, de, 365);

color("red")
planet(mars*see, dm, avmars);
color("red")
planet(mer*see, dme, avmer);
color("red")
planet(venus*see, dv, avv);

////color("yellow")
////planet(jupiter*see/10, dj, 43);



er();

module er( ){
    a = ave*1;
       rotate([0,0, $t*a]) translate([0, de, 0])  
        color("green") sp(earth*see, fn);
    
    
        rotate([0,0, $t*a]) translate([0, de+dmoon, 0])  
        color("yellow") sp(moon*11, fn);
    
}
 //655.2 hours 27.3 days moon orbit

 

module planet(s, dis, av){
    a = av*1;
       rotate([0,0, $t*a]) translate([0, dis, 0])  sp(s, fn);
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

 
