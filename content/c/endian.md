Title: 大端和小端
Tags: endian
Date: 2014-09-27

字节序就是跨越多字节的程序对象的存储规则, 有两种字节序: Big-endian, Little-endian. 

Big-endian systems store the most significant byte in the smallest address and the least significant byte is stored in the largest address. 最高有效字节存储在低地址.

Little-endian systems, in contrast, store the least significant byte in the smallest address. 最低有效字节存储在低地址.

大端和小端就是表示多字节的哪一端存储在该值的起始位置. 例如c中整数占四字节 `int x = 0x01234567`, 大端的在内存的存储是`01 23 45 67`, 小端 `67 45 23 01`.

Standard byte order for networks is big endian, also known as network byte order.

    #define BIG_ENDIAN      0
    #define LITTLE_ENDIAN   1

    int TestByteOrder() {
       short int word = 0x0001;
       char *byte = (char *) &word;
       return(byte[0] ? LITTLE_ENDIAN : BIG_ENDIAN);
    }

refer:

- [http://www.codeproject.com/Articles/4804/Basic-concepts-on-Endianness](http://www.codeproject.com/Articles/4804/Basic-concepts-on-Endianness)
- [http://stackoverflow.com/questions/12791864/c-program-to-check-little-vs-big-endian/12792301#12792301](http://stackoverflow.com/questions/12791864/c-program-to-check-little-vs-big-endian/12792301#12792301)
