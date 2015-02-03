Title: a20gate
Tags: a20, real mode
Date: 2014-09-21

### real mode 模式寻址  
8086/8088 的地址线有 20 条: A0 ~ A19, 最大可以访问1M内存. 它的寻址方法是：segment:offset，这是一种被称为 logic address（逻辑地址）表示法. 物理地址 = 段地址 * 0x10 + 偏移地址。F000:FFFF = F0000 + FFFF = FFFFF，这是 8086/8088 所能访问的最高地址。8086/8088 的寻址范围是可以表示为：从 0000:0000 - 0000:FFFF,1000:0000 - 1000:FFFF, ... ,F000:0000 - F000:FFFF 段

### 访问 extended memory  
80286 intel实现了24 位的Address bus，那么在real mode下80286能够访问到的最高地址: FFFF:FFFF = FFFF0 + FFFF = 10FFEFh(h表示16进制). 这已经是logic address所能表达的极限范围了，100000h 以上的内存被称为extend memory，从100000h ~ 10FFEFh这片内存区域在 DOS 下被称为 High Memory（高端内存）。高端内存是 80286 在 real mode 所能访问到的区域，而 8086/8088 所不能访问到的。

### wraparound 现象  
当在 8086/8088 下执行 FFFF:FFFF 这个内存寻址时，会产生什么结果呢? 结果很明显: 由于 8086/8088 只有 20 条 address bus，从A0 ~ A19，地址10FFEF的高4位会被抛弃，实际上送上 address bus 的只有0FFEF, 所以 8086/8088 下访问 FFFF:FFFF 地址结果只能访问到 1M 以内的地址。这就是 wraparound 现象：访问 1M 以上地址都会回绕到 1M 内的模值。

由于80286具有24条address bus，对于FFFF:FFFF地址的访问，会正确得到访问, 不存在 wraparound 现象。所以访问高端内存时，在real mode下80286 和 8086/8088 的行为不一致！

### 引入 A20 Gate  
为了使用 80286 和 8086/8088 在 real mode 下的行为一致，即在80286下也产生wraparound现象。IBM 想出了古怪方法：当 80286 运行在 real mode 时，将 A20 地址线（第 21 条 address bus）置为 0，这样使得 80286 在 real mode 下第 21 条 address line 无效，从而人为造成了 wraparound 现象。

refer: 

- [0][http://www.mouseos.com/arch/a20gate.html](http://www.mouseos.com/arch/a20gate.html)
- [1][http://docs.huihoo.com/gnu_linux/own_os/booting-a20_4.htm](http://docs.huihoo.com/gnu_linux/own_os/booting-a20_4.htm)
