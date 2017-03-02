$fn = 100;
tack_d = 1.5;

difference(){
cube([25,50,5 ],true);
translate([0,0,-20])   
cylinder(d=tack_d,h=40);    
translate([0,8,-20])   
cylinder(d=tack_d,h=40);    
translate([5,0,-20])   
cylinder(d=tack_d,h=40);    
}