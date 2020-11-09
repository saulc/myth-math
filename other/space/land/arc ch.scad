
use <myshapes.scad>


fn = 55;



 wall = 11;
 dd = 100;
 c = 55;
 cc = 3;
 
 width = 3333;
 height = 222;
 dis = 3111;
 
// single();
 
 //posts//pillion
//for(i=[-1,1]) translate([i*dis/2, 0, -width]) cy(width, width*3, fn);


//    for(i=[0:2]) translate([ 0, i*width*1.1 , 0])
  %  trip();


module trip(){  
    double();
    
    //main rails
    for(i=[-1,1]) translate([0, i*width/4 , 0]) 
      rotate([0, 90, 0]) cy(dd, dis*3, fn);
    
    
    //cross supports
    cs = 1;
    for(i=[-cs:cs]) translate([  i*width*.55 , 0]) {
      rotate([0, 90, 60]) cy(dd/2, width, fn);
        
     translate([0, 0, 0])  rotate([0, 90, -60]) cy(dd/2, width, fn);
    }
    
}

module double(){
        n = dis / height;
        k= n*1.2;
        echo(k);
        for(i=[-k: k]) 
        translate([i*(height+11), 0,  133-.314159*(i*i) ])    block(width, height); 
	 
    
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





