


use <myshapes.scad> 
 
 
 
fn = 60;

// meter scale..

////bfr booster size
//bd = 12;
//h = 66;
cd = 3; //cone diameter
cdd = 7; 

sc = 11;

bd = 15 *sc;
h = 66 *sc;
   d2 = bd+3;
   hh = 5;
   
    wingOffset = -22;
    wingOffsetz = 2;
fl = 33*sc; //span fl + bd + winglets
fh = h/2;
fhh = h/9;

td = 9;

//color("green")
//#c(100, 100, 1);



// rotate([0,0, $t *11])  
ff();
 
//       translate([20,0, 0])  
// scaleex();
 
 
module ff(){ 
    union(){
        difference(){
         %   shell(bd, 3); 
        }
        
         
//        maintanks();
        subtanks();
       thrusters(); //turbofan/edf/
        tail();
        
    }
}

module tail(){
    
    n = 3;
    a = 111; //360/n;
    for(i=[-1:1]) rotate([0,0, i*a]) tf();
            
    }
    
    
module tf(){   
    tl = 3 *sc;
    tll = 11 *sc;
    th = 11 *sc;
    
        translate([-bd/2,0, tl+5 ]) 
    hull(){
        translate([-th,0, 0 ])  cy(1, tl, fn);  
        translate([0,0,0 ])  cy(1, tll, fn);  
   }
   
   }
   
module maintanks(){   
        translate([0,0,11 ])  tank(4,  8);
        translate([0,0,24 ])  tank(6,  13);
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
     cone(11*sc, 4*sc, 2);
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
       translate([10,0, h+d*2])  sp(cd,   fn);
       translate([0,0, h+d-2])  sp(cdd,   fn);
         
         //body
       translate([0,0, h/2])  cy(d, h, fn);
       translate([0,0, h/2])  cy(d2, hh, fn);
         
     }
       
//       for(i=[0:n-1]) rotate([0,0, i*a])  
//     translate([wingOffset, 0, wingOffsetz])
       translate([wingOffset,0, h/2+wingOffsetz])  wings();
}

   

module wings(){
    
       translate([0,0, 0])  wg();
      mirror([0,1,0]) translate([0,0, 0])  wg();
}

module wg(){
    zz = 7; //sweep back.
    
       translate([0,bd/2-2, 0])  
    union(){
        //turbofans
        # translate([-5,fl/3,0])  cy(7, 7, fn);
//        # translate([-3,fl/2,0])  cy(3, 7, fn);
        hull(){
            
            translate([0,0, fh/2])  cy(1, fh, fn);
            #translate([0,fl, fhh/2-zz])  cy(1, fhh, fn);
        }
        hull(){
            
            translate([0,fl, fhh/2-zz])  cy(1, fhh, fn);
            translate([-7,fl+3, fhh/2-zz*2.3])  cy(1, 1, fn);
        }
    }
}

 
module scaleex(d,c){
     
       translate([0,10, 66/2])  cy(12, 66, fn);
       translate([0,-10, 33/2])  cy(12, 33, fn);
}

