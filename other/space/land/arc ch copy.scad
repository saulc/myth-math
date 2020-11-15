
use <myshapes.scad>


fn = 55;



 wall = 11;
 dd = 100;
 c = 22;
 cc = 3;
 
 width = 555;
 height = 88;
 dis = 1111;
 
 single();
 
 //posts//pillion
for(i=[-1,1]) translate([i*dis, 0, -220]) cy(111, 444, fn);
    

module single(){
        k = dis / height;
        for(i=[-k: k]) 
        translate([i*(height+11), 0,  111-.3*(i*i) ])    block(width, height); 
	 
    
}

module block(a, b){
    difference(){
    hull(){
	translate([0, 0, dd/2-cc/2])  rotate([0, 0, ]) rc(b+cc, a, cc, c);
	translate([0, 0, 0])  rotate([0, 0, 0]) rc(b, a, dd, c);
    }
    
	translate([0, 0, -11])  rotate([0, 0, 0]) rc(b*.55, a*.88, dd, c);
}
//	translate([0, 0, 0])  rotate([0, 0, 0]) 
}





