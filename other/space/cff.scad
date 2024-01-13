


use <myshapes.scad> 
 use <fdf.scad>
 
 
fn = 60;

// meter scale..

////bfr booster size
//bd = 12;
//h = 66;

    n = 6;
cd = 3; //cone diameter
cdd = 7; 
    ww  = 9; //dual hull spacing
h = 66;

bd = 15;
d2 = bd+3;
hh = 5;
   //------------------
   //------ wings -----
    zz = 11; //sweep back.
    wingAngle = 13;
   
    wingOffset = -4; //bd/4;
    wingOffsetz = -21;
fl = 44;
fh = 36;
fhh = h/9;

td = 9;

//color("green")
//#c(100, 100, 1);



// rotate([0,0, $t *11])  
 //rotate([0,80, 0])  
//cc();
s = 10;
 translate([-70,0, -300])  scale([s, s, s]) 
 cc();
 
 
// translate([-20,0, 00]) cy(1, 2, fn);
// ff(); //mostly for scale
//       translate([20,0, 0])  
// scaleex();
 
 
module cc(){ 
    union(){
        #
        difference(){
            union(){
                    shell(bd, 3); 
                intake();
            }
            incut();
        }
        
//          translate([-12,  0,0 ])     thrusters();
//        maintanks();
        for(i=[-1,1]) translate([0,  i*ww, ])  
                 rotate([0,0,  0])   thrusters(); //turbofan/edf/
        tail();
        jets(); 
    }
}

module jets(){
     for(i=[-1,,1]) translate([bd-2,  i*bd/2, 10]) {
        //turbofans
//         translate([0,0,0])  cy(5, 7, fn);
//         translate([0,5.5*i,0])  cy(5, 7, fn);
//        # translate([-3,fl/2,0])  cy(3, 7, fn);
     }
}


    
module tail(){
    
        translate([0,0, 0 ]) mirror([1,0,0]) tf();
    n = 3;
    a = 120; //360/n;
    for(i=[-1,1]) rotate([0,0, i*a])
 rotate([0,0, i*a + $t*$t *11*-i])  
        translate([-4,0, 0 ]) tf();
            
    }
    
    tl = 3;
    tll = 14;
    th = 6;
module incut(){
    
     translate([-7,0, 0 ]) 
    for(i=[-1,1]) rotate([0,0, i*88])   translate([-6,0, h-tll+4 ]) 
    hull(){
        translate([-th-1,0, tll ])  rotate([0,0, 90])   cy(11-3, tl, 6);  
        translate([-th,0, tll/2 ])  rotate([0,0, 90])   cy(11-3, tll, 6);  
        translate([-th/2,-2*i, -tll/2]) rotate([0,0, 90])   cy(7-3, tll, 6);   
   }
   
   }
   
module intake(){
     
     translate([-7,0, 0 ]) 
    for(i=[-1,1]) rotate([0,0, i*88])   translate([-6,0, h-tll ]) 
    hull(){
        translate([-th,0, tll/2 ])  rotate([0,0, 90])   cy(11, tl, 6);  
        translate([-th/2,-2*i, -tll/2]) rotate([0,0, 90])   cy(7, tll, 6);   
   }
   
   }
   
module tf(){   
    tl = 3;
    tll = 11;
    th = 21;
    
        translate([0,0,  tll ]) 
    hull(){
        translate([-th,0, -tll ])  cy(1, tl, fn);  
        translate([0,0,0 ])  cy(1, tll, fn);  
   }
   
   }
   
    
module maintanks(){   
        translate([0,0,11 ])  tank(4,  8);
        translate([0,0,24 ])  tank(6,  13);
   }
   
   
module subtanks(){ 
         a = 360/n;
           for(j=[0:1]) translate([0,0, 5-j*7]) 
       for(i=[0:n-1]) rotate([0,0, i*a]) translate([0,5, 0]) 
        translate([0,0,td ])  tank(5, 6);
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
        translate([0,0, -4]) cone(1, 4, 7);
        subtanks();
     
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
       translate([-10,0, h+d*2])  sp(cd,   fn);
       translate([0,0, h+d-2])  sp(cdd,   fn);
         
         //body
       for(i=[-1,1]) translate([0,i*ww, h/2]) { 
           cy(d, h, fn);
            cy(d2, hh, fn);
       }
         
//       translate([0,0-ww, h/2])  cy(d, h, fn);
//       translate([0,0-ww, h/2])  cy(d2, hh, fn);
     }
       
//       for(i=[0:n-1]) rotate([0,0, i*a])  
//     translate([wingOffset, 0, wingOffsetz])
       translate([wingOffset,0, h/2+wingOffsetz])  wings();
}

   

module wings(){
    
       translate([0,ww, 0])  wg();
      mirror([0,1,0]) translate([0,ww, 0])  wg();
}

module wg(){
    
 rotate([0,0, wingAngle + $t *11])  
    
    union(){
        hull(){
         translate([1,bd/2-5,fh/2])  cy(9, fh, fn);
         translate([0,bd/2+14,fh/2-2.5])  cy(3, fh/2, fn);
        }
        hull(){
            
            translate([0,0, fh/2])  cy(3, fh, fn);
            translate([0,fl, fhh/2+zz])  cy(1, fhh, fn);
        }
        hull(){
            //            winglets
            translate([0,fl, fhh/2+zz])  cy(1, fhh, fn);
            translate([7*$t,fl+3, fhh/2])  cy(1, 1, fn);
        }
    }
}

 
module scaleex(d,c){
     
       translate([0,10, 66/2])  cy(12, 66, fn);
       translate([0,-10, 33/2])  cy(12, 33, fn);
}

