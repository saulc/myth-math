
use <myshapes.scad>


fn = 150;

id = 30;
w = 2;
 h = 60;
 vs = 18;
 
     v = 3;
     h3 = 188;
 ro = 90;
 rh = 11;
 
 
// v3();
// vv3();
 
// !dr();
// head();
 
// vl();
// #vv();
      rotate([0,0,$t*720]) 
wan();

 module wan(){
     union(){
         for(i=[0:2]) translate([0,0,i*(rh+3)]) rotate([0,0,i*40]) rtr();
     }
 }

 module rtr(){ 
     translate([4,0,0])
     difference(){
     intersection_for(i=[0:2]) rotate([0,0,i*120]) 
         translate([ro/3, 0, rh/2]) cy(ro, rh, fn);
     translate([0,0,4]) cy(rh*2, rh*2, 9); 
     }
         
 }
     
 
 
 module dr(){
     difference(){
     translate([0,0,4]) cy(9.4, 8, 6);
     translate([0,0,8]) cy(6.4, 8, 6);
         
     }
 }
 
 module head(){
 for(i=[-1,1]) translate([0, i*id, 0]) rotate([0,0,i* 45]) {
     rotate([0,0,i*$t* 540+(i>0?-90:0)])
 vl();
 vv();
 }
 }
 
 module vv(){
     difference(){
         union(){
     translate([0,0,h+4]) cy(15, 9, 6);
     translate([0,0,h/2]) cy(id+w+.8, h, fn);
         }
     translate([0,0,-1.2]) cn(id+.8, id-2, h, h-2, fn);
          for(i=[0:2]) rotate([0, 0, 0]) translate([0,0,i*vs+vs/2+1.5]) rotate([90, 0]) hull(){
              cy(14.5, id*2, fn);
             translate([0,0,-id]) rotate([0, 0, 90]) slot(9, id*2, 7);
          }
     }
 }
 
 
 module vl(){
     difference(){
         union(){
     translate([0,0,h/2-1.2]) cn(id, id-2, h/2, h/2-2, fn);
     translate([0,0,h-4])  mirror([0, 0, 1]) cn(id, id-2, h-4, h-4-2, fn);
//     translate([0,0,54/2]) cy(id, 54, fn);
     translate([0,0,h+3]) cy(15, 8, 6);
         }
         
          for(i=[0:2]) rotate([0, 0, i*120]) translate([0,id/2,i*vs+vs/2+1.5]) rotate([90, 0]) vcc();
     }
 }
 
 
 module vcc(){
     difference(){
  #   translate([0,0,id/2]) cy(10, id+11, fn);
//         vc();
     }
 }
 module vc(){
     rotate_extrude(angle=360, convexity = 2)
     projection()
     translate([5, 0,0]) 
     hull(){
     translate([5,5,0]) cy(10, 1, fn);
     translate([5,id-5,0]) cy(10, 1, fn);
//     translate([5,40,0]) c(10, 1, 1);
     }
     
 }
 
 
 
 
 module vv3(){
     difference(){
     translate([0,0,h3/2]) cy(id+w+.8, h3, fn);
     translate([0,0,55/2+1.2]) cy(id+.8, 55, fn);
          for(j=[0:2])  for(i=[0:v-1]) rotate([0, 0, 0]) translate([0,0,i*17+9+j*21*v]) rotate([90, 0]) cy(14.5, id*2, fn);
     }
 }
 module v3(){
     difference(){
     translate([0,0,h3/2]) cy(id, h3, fn);
     translate([0,0,54-2]) cy(9.4, 4.2, 6);
         
        for(j=[0:2])  for(i=[0:v-1]) rotate([0, 0, j*120]) translate([0,id/2,i*17+9+j*21*v]) rotate([90, 0]) vcc();
     }
 }
 
 
 