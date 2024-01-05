


use <myshapes.scad> 
 
 use<fdf.scad>
 
fn = 60;

// meter scale..

////bfr booster size
//bd = 12;
//h = 66;
cd = 3; //cone diameter
cdd = 7; 
bd = 15;
h = 54;
   d2 = bd+3;
   hh = 5;
   
    
fl = 3;
fh = h/2;
fhh = h/9;

td = 9;

//color("green")
//#c(100, 100, 1);

 translate([-bd/2-1-$t*11,  0, 4+$t*22])  
 scale([.26,.26, .25])  
ff();

 rotate([0,0, 30])  
 scale([.6,.6, .5])  
cc();
 
//       translate([20,0, 0])  
// scaleex();
 
 
module cc(){ 
    union(){
        difference(){
         %   shell(bd, 3); 
        }
        
         
        maintanks();
        subtanks();
       thrusters();
    }
}

module maintanks(){   
        translate([0,0,11 ])  tank(4,  8);
        translate([0,0,26 ])  tank(6,  15);
   }
   
   
module subtanks(){
         n = 8;
         a = 360/n;
           for(j=[0:1]) translate([0,0, 5-j*7]) 
       for(i=[0:n-1]) rotate([0,0, i*a]) translate([0,5, 0]) 
        translate([0,0,td ])  tank(5, 3);
   }
   
   
 
module tank( h, c){
     hull(){
//       translate([0,0,h-od ])  cy(od, c, fn);
//       translate([0,0,0 ])  rcy(od, c+1, c, fn);
       translate([0,0, h/2])  sp(c,   fn);
       translate([0,0, -h/2])  sp(c,   fn);
     }
     
 }
 
 module thrusters(){
     cone(1, 4, 2);
    n = 8;
    a = 360/n;
    for(i=[0:n-1]) rotate([0,0, i*a])
         translate([0,5, 0])    cone(1, 3, 2);
           
}
 
module cone(d, dd, h){
     hull(){
       translate([0,0, h+d])  sp(d,  fn); 
       translate([0,0, .1/2])  cy(dd, .1, fn);
         
     }
 }
 
 
module shell(d,c){
     hull(){
         //nose
       translate([0,0, h+d])  sp(cd,   fn);
       translate([0,0, h+d-2])  sp(cdd,   fn);
         
         //body
       translate([0,0, h/2])  cy(d, h, fn);
       translate([0,0, h/2])  cy(d2, hh, fn);
         
     }
    n = 3;
     a = 360/n;
     
       for(i=[0:n-1]) rotate([0,0, i*a]) translate([0,bd/2, 0])  fin();
}



module fin(){
        hull(){
            
            translate([0,0, fh/2])  cy(1, fh, fn);
            translate([0,fl, fhh/2])  cy(1, fhh, fn);
        }
}

 
module scaleex(d,c){
     
       translate([0,10, 66/2])  cy(12, 66, fn);
       translate([0,-10, 33/2])  cy(12, 33, fn);
}

