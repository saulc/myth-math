


use <myshapes.scad> 
 use <cff.scad>
 
 
 
fn = 60;

// meter scale..

d = 12;
bl = 16;


wall = .1;
    
 
// ss();
 
s = 40;
 translate([-1800,0, 2000])  scale([s, s, s]) 
 cc();
 
 scale([100,100, 100]) layout1();
 scale([100,100, 100])  layout3();
 
 module layout3(){
     
 translate([0,0,0]) tripple();
     for(j=[1:3])
  for(i=[0:2])  rotate([ 0,0,i*120])  rotate([ 90,0, 0]) translate([0,0,bl*j]) mod(3);
      
 for(i=[0, 1])	  rotate([0,0,i*120-60])   translate([0,bl, -d/2+2])  pattern( 7, 40);
 }
     
     
 module layout1(){
     
 translate([0,0,bl*2+d/2]) mid();
     
  for(i=[0, 1,  3, 4]) translate([0,0,i*bl]) rotate([0,0, i*60]) mod();
  for(i=[1,2]) translate([i*bl , 0, bl*2.375]) rotate([0,90,0]) rotate([0,0,30])mod(6);
//  for(i=[-1,1]) translate([d/2, i*bl,  bl*2.5]) rotate([90,0,0]) mod(9);
      
//	translate([  d/4,  bl*1.6, 0])  rotate([90,0,90]) pattern(5, 60);  //more panels?
 for(i=[0, bl*6])	translate([ -d/2,  -25, i-bl/2]) rotate([0,90,0])  pattern( 7, 50);
 }
 
 
// scale([100,100, 100])
// tripple();
 
 module mid(){
      translate([0,0,-bl/2]) rotate([ 0,0,0])   mod(3);
  for(i=[0:3]) translate([0,0,0]) rotate([ 0,0,i*90])    rotate([ 90,0, 0])mod(3);
 }
 
 module tripple(){
     
  for(i=[0:2]) translate([0,0,0]) rotate([ 0,0,i*120])    rotate([ 90,0, 0])mod(3);
 }
 
module mod(r=3){ 
    union(){
      %  difference(){
            shell(d); 
        difference(){
            shell(d-wall, 1); 
        
        a = 360/r;
        for(i=[0:r-1]) rotate([0,0,i*a+30]) translate([ 0, d/2+d/6, bl/2]) c(wall, d, bl );
            shell(d/3,1) ;
        }
        }
          
        
    }
}
 
     
 

module pattern(x, l){
		
		qw = 1.2;
		ql = 1.2;
//		ww = x/qw-1; 
		k = l/ql -1;
		ww = 3;
		for(i=[0:k]) for(j=[-x:x])
	 translate([ 0+j*(qw+wall), (ql+wall)*i , 10]) 	cy(qw, wall, 6) ;
	
}

 
module shell(bd, z = 0){
     hull(){ 
         //body
       translate([0,0, bl/2])  cy(bd, bl*.8, 6);
       translate([0,0, bl/2])  cy(bd*.9-z, bl+z, 6);
     }
        
}

   
 