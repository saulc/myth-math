


use <myshapes.scad>  
 
 
 x = 234;
 y = 458;
 z = 188;
 ry = 222;
 
 bd = 46;
 d2 = 33;
  
 ww = 77;
 wb = 266;
 
fn = 60;
  

//color("green")  
 
 cc();
 
 
module cc(){  
        difference(){
            union(){
                    shell(d2, 0); 
                 
        } 
                  translate([ 0, 0, -3])   shell(d2+5, 4);  
        
    }
}
   
     
 
module shell(d,c){
    difference(){
    union(){
     hull(){
         //nose 
         
         //body
       for(i=[-1,1]) translate([ i*(x/2-d),0, d2/2]) rotate([90,0,0]) cy(d2, y-c, 6); 
       for(i=[-1,1]) translate([ i*(x/2 + 5-d),0, z/2+d2/2-c]) rotate([90,0,0]) cy(d2, y-c, 6); 
       }
     hull(){
       for(i=[-1,1]) translate([ i*(x/2-d),-bd/3, z]) rotate([90,0,0]) cy(d2, ry-bd-c, 6); 
       for(i=[-1,1]) translate([ i*(x/2-d),0, z/2]) rotate([90,0,0]) cy(d2, ry-c, 6); 
       }
           
//       for(i=[-1,1]) translate([ i*x/2,-y, z/2]) cy(d2, z, 6); 
          if(c==0) 
           for(j=[-1,1])  for(i=[-1,1]) translate([ j*(x/2-22),i*wb/2, d2/2+d/2])
           rotate([90,0,90]) cy(ww*1.9, 33, 6); 
     }
     
                  translate([ 0, y/2-c, 64])   rotate([90,0,0]) rc(x-44-c, 111-c, 5, 11);
       for(j=[-1,1])  for(i=[-1,1]) translate([ j*(x/2-22),i*wb/2, d2/2+d/2])
           rotate([90,0,90]) cy(ww+d, 35, fn); 
    }
        
}

    
