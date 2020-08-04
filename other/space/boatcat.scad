


use <myshapes.scad> 
 
 
 
fn = 60;

// meter scale..
 w = 5; //~9'
h = 7; // 2x'

    bd = 3; // standup in pontoons..
   d2 = bd+3;
   hh = 5;
    
fl = 3; //span fl + bd + winglets
fh = h/2;
fhh = h/9;

td = 9;

color("blue")
cy(15, 1, fn);



// rotate([0,0, $t *11])  
cc();
 
//       translate([20,0, 0])  
// scaleex();
 
 
module cc(){ 
    union(){
        difference(){
         %   shell(bd, 3); 
        }
        
         
//        maintanks();
//        subtanks();
//       thrusters(); //turbofan/edf/
//        tail();
        
    }
}
 
module shell(d,c){
     union(){
         //nose 
//       translate([0,0, h+d-2])  sp(cdd,   fn);
         
         //body
          translate([0,0, d])  rc(w, h, .01, 2);
    for(i=[-1,1])
       translate([w/2*i,0, d/2])  rotate([90,0, 0]) cy(d, h, fn); 
         
     }
        
}


module tail(){
    
    n = 3;
    a = 111; //360/n;
    for(i=[-1:1]) rotate([0,0, i*a]) tf();
            
    }
    
    
module tf(){   
    tl = 3;
    tll = 11;
    th = 11;
    
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
    
 
module cone(d, dd, h){
     hull(){
       translate([0,0, h+d])  sp(d,  fn); 
       translate([0,0, .1/2])  cy(dd, .1, fn);
         
     }
 }
 
   
 
 
module scaleex(d,c){
     
       translate([0,10, 66/2])  cy(12, 66, fn);
       translate([0,-10, 33/2])  cy(12, 33, fn);
}

