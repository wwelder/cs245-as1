// 销钉 3D 模型（按零件 #114258 图纸），单位 mm
// 由三段同轴圆柱组成，总高 17 mm；两端各有 45° 倒角

$fn = 96;

total_h   = 17.0;   // 总高
top_d     = 3.0;    // 上段直径
flange_d  = 6.0;    // 中间法兰直径
flange_h  = 1.0;    // 中间法兰厚度
bottom_d  = 5.0;    // 下段直径
bottom_h  = 7.5;    // 下段高度
top_h     = total_h - flange_h - bottom_h;  // 上段高度 = 8.5
bottom_c  = 0.5;    // 下段底端倒角 C0.5
top_c     = 0.3;    // 上段顶端倒角 C0.3

// 半剖轮廓绕 Z 轴旋转成实体
rotate_extrude()
    polygon([
        [0, 0],
        [bottom_d / 2 - bottom_c, 0],
        [bottom_d / 2, bottom_c],
        [bottom_d / 2, bottom_h],                       // 下段 Ø5
        [flange_d / 2, bottom_h],
        [flange_d / 2, bottom_h + flange_h],            // 中段 Ø6 × 1
        [top_d / 2, bottom_h + flange_h],
        [top_d / 2, total_h - top_c],                   // 上段 Ø3
        [top_d / 2 - top_c, total_h],
        [0, total_h],
    ]);
