Title:  三角形的面积
Date: 2014-08-10 20:00:00
Tags: algorithm, triangle

1. 已知三边(a, b, c)求三角形面积.  
海伦公式:
假设三角形三边分别为(a, b, c), 则三角形的面积  
$S = \sqrt{p(p-a)(p-b)(p-c)}$, 其中$p=\frac{a + b+ c}{2}$

        float space(float a, float b, float c) {
            int p;
            p = (a + b + c) / 2;
            return sqrt(p * (p - a) * (p - b) * (p - c));
        }

2. 已知平面三点的坐标求三角形的面积  
利用向量叉乘
$S = \frac{1}{2}|\overrightarrow{AB}||\overrightarrow{AC}| * sign\angle{A} = \frac{1}{2}|\overrightarrow{AB} * \overrightarrow{AC}|$

        typedef struct point {
            float x;
            float y;
        } point_t;

        float space(point_t A, point_t B, point_t C) {
            point_t AB = {B.x - A.x, B.y - A.y}, AC = {C.x - A.x, C.y - A.y};
            return fabs(AB.x * AC.y - AB.y * AC.x) / 2;
        }

refer

- [http://sxyd.sdut.edu.cn/gaoshu1/lesson/7.4%20%20shuliangji.htm](http://sxyd.sdut.edu.cn/gaoshu1/lesson/7.4%20%20shuliangji.htm)
- [http://blog.csdn.net/fox64194167/article/details/8147460](http://blog.csdn.net/fox64194167/article/details/8147460)
