"""生成销钉的 STL 模型（无需第三方库）。尺寸与 pin_114258.scad 一致，单位 mm。"""
import math
import struct

SEGMENTS = 96
TOTAL_H = 17.0
BOTTOM = (5.0, 7.5)   # (直径, 高度)
FLANGE = (6.0, 1.0)
TOP = (3.0, TOTAL_H - BOTTOM[1] - FLANGE[1])
BOTTOM_C = 0.5   # 下段底端倒角 C0.5
TOP_C = 0.3      # 上段顶端倒角 C0.3

# 轮廓：(半径, z) 从底面中心到顶面中心，绕 Z 轴旋转成实体
profile = [
    (0.0, 0.0),
    (BOTTOM[0] / 2 - BOTTOM_C, 0.0),
    (BOTTOM[0] / 2, BOTTOM_C),
    (BOTTOM[0] / 2, BOTTOM[1]),
    (FLANGE[0] / 2, BOTTOM[1]),
    (FLANGE[0] / 2, BOTTOM[1] + FLANGE[1]),
    (TOP[0] / 2, BOTTOM[1] + FLANGE[1]),
    (TOP[0] / 2, TOTAL_H - TOP_C),
    (TOP[0] / 2 - TOP_C, TOTAL_H),
    (0.0, TOTAL_H),
]


def point(r, z, i):
    a = 2 * math.pi * i / SEGMENTS
    return (r * math.cos(a), r * math.sin(a), z)


def triangles():
    for (r0, z0), (r1, z1) in zip(profile, profile[1:]):
        for i in range(SEGMENTS):
            a0, a1 = point(r0, z0, i), point(r0, z0, i + 1)
            b0, b1 = point(r1, z1, i), point(r1, z1, i + 1)
            if r0 > 0 and r1 > 0:
                yield a0, a1, b1
                yield a0, b1, b0
            elif r0 > 0:      # 收到轴心（顶面）
                yield a0, a1, b0
            else:             # 从轴心出发（底面）
                yield a0, b1, b0


def normal(p, q, s):
    u = [q[k] - p[k] for k in range(3)]
    v = [s[k] - p[k] for k in range(3)]
    n = (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])
    l = math.sqrt(sum(c * c for c in n)) or 1.0
    return tuple(c / l for c in n)


def main(path="pin_114258.stl"):
    tris = list(triangles())
    with open(path, "wb") as f:
        f.write(b"pin_114258".ljust(80, b" "))
        f.write(struct.pack("<I", len(tris)))
        for t in tris:
            f.write(struct.pack("<3f", *normal(*t)))
            for p in t:
                f.write(struct.pack("<3f", *p))
            f.write(b"\0\0")
    print(f"wrote {path}: {len(tris)} triangles")


if __name__ == "__main__":
    main()
