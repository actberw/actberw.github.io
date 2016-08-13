Title: 位图(bitmap)
Tag:bitmap
Date: 2016-03-10

## 相关计算

1. 位图数组大小: (max - 1)/ 32 + 1 (32为每个元素位数) (max 不是需要的位数，而是要表示的数字的最大值. (max + 0x1f) >> 5)
2. 数组索引计算: num / 32 (or num >> 5)
3. 位索引计算: num % 32 (or num & 0x1f)

##c++ 实现

    #include <iostream>
    #include <cstddef>
    #include <cstdint>

    class Bitmap {
    private:
            size_t size_;
            uint32_t *data_;
            static const int SHIFT = 5;
            static const int MASK = 0x1f;
            ~Bitmap() { delete [] data_;}
    public:
            Bitmap(size_t size) {
            ¦   size_ = size;
            ¦   data_ = new uint32_t[(size - 1) >> SHIFT + 1];
            }

            ~Bitmap() { delete [] data_; }
            size_t size() {return size_;}

            void set(size_t pos) {
            ¦       data_[pos >> SHIFT] |= 1 << (pos & MASK);
            }

            void clear(size_t pos) {
            ¦       data_[pos >> SHIFT] &= ~(1 << (pos & MASK));
            }
            bool test(size_t pos) {
            ¦       return data_[pos >> SHIFT] & 1 << (pos & MASK);
            }

    };

## 应用

- 在2.5亿个整数中找出不重复的整数，注，内存不足以容纳这2.5亿个整数(采用2-Bitmap)
- 腾讯面试题：给40亿个不重复的unsigned int的整数，没排过序的，然后再给一个数，如何快速判断这个数是否在那40亿个数当中？

####refer:
- http://dongxicheng.org/structure/bitmap/
