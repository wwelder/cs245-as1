// 销钉 3D 模型（按零件 #114258 图纸），单位 mm
// 由三段同轴圆柱组成，总高 17 mm

$fn = 96;

total_h   = 17.0;   // 总高
top_d     = 3.0;    // 上段直径
flange_d  = 6.0;    // 中间法兰直径
flange_h  = 4.0;    // 中间法兰厚度
bottom_d  = 5.0;    // 下段直径
bottom_h  = 6.0;    // 下段高度
top_h     = total_h - flange_h - bottom_h;  // 上段高度 = 7.0

union() {
    cylinder(d = bottom_d, h = bottom_h);                       // 下段 Ø5
    translate([0, 0, bottom_h]) cylinder(d = flange_d, h = flange_h);   // 中段 Ø6 × 4
    translate([0, 0, bottom_h + flange_h]) cylinder(d = top_d, h = top_h); // 上段 Ø3
}
