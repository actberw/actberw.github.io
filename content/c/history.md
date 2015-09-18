Title: C语言历史
Date: 2014--09-01
Tags: c89, ansi c

C语言在1972年诞生与bell实验室, 作者Dennis Ritchie。 早期一些想法跟规则源自于B语言，所以叫做C。
![history](/img/01.0-history.jpg)

### C语言早期发展

1969-1973年在美国电话电报公司（AT&T）贝尔实验室开始了C语言的最初研发。根据C语言的发明者丹尼斯·里奇 (Dennis Ritchie) 说，C 语言最重要的研发时期是在1972年(PDP-11 Unix system)。

说明：丹尼斯·里奇(Dennis Ritchie)，C语言之父，UNIX之父。1978年与布莱恩·科尔尼干(Brian Kernighan)一起出版了名著《C程序设计语言(The C Programming Language)》，现在此书已翻译成多种语言，成为C语言方面最权威的教材之一。2011年10月12日（北京时间为10月13日），丹尼斯·里奇去世，享年70岁。

C语言之所以命名为C，是因为C语言源自Ken Thompson发明的 B语言，而B语言则源自BCPL语言。

C语言的诞生是和UNIX操作系统的开发密不可分的，原先的UNIX操作系统都是用汇编语言写的，1973年UNIX操作系统的核心用C语言改写，从此以后，C语言成为编写操作系统的主要语言。

### K&R C

1978年，丹尼斯·里奇(Dennis Ritchie)和布莱恩·科尔尼干(Brian Kernighan)出版了一本书，名叫《The C Programming Language》（中文译名为《C程序设计语言》）。这本书被C语言开发者们称为“K&R”，很多年来被当作C语言的非正式的标准说明。人们称这个版本的C语言为“K&R C”。

1988年丹尼斯·里奇(Dennis Ritchie)和布莱恩·科尔尼干(Brian Kernighan)修改此书，出版了《The C Programming Language》第二版，第二版涵盖了ANSI C语言标准。

### ANSI C (C89, C90)

1970到80年代，C语言被广泛应用，从大型主机到小型微机，也衍生了C语言的很多不同版本。

为统一C语言版本，1983年美国国家标准局（American National Standards Institute，简称ANSI）成立了一个委员会，来制定C语言标准。1989年C语言标准被批准，被称为ANSI X3.159-1989 "Programming Language C"。这个版本的C语言标准通常被称为ANSI C。又由于这个版本是 89 年完成制定的，因此也被称为 C89。

1990年ANSI C标准被 ISO 采纳为国际标准 ISO/IEC 9899:1990, 因为这个版本是1990年发布的，因此也被称为C90。

Therefore, the terms "C89" and "C90" refer to the same programming language, `__STDC__` 宏可以用来检查是否支持 ANSI C. 

gcc参数: `-ansi`, `i-std=c90`

### C99
The C standard was further revised in the late 1990s, leading to the publication of ISO/IEC 9899:1999 in 1999, which is commonly referred to as "C99". It has since been amended three times by Technical Corrigenda.`__STDC_VERSION__` 宏用来坚持是否支持C99.


引入的新特性:  `inline functions`, 变长数组, 两个头文件: <stdbool.h>, <stdint.h>

gcc参数: `-std=c99`

### C11

In 2007, work began on another revision of the C standard, informally called "C1X" until its official publication on 2011-12-08. The C standards committee adopted guidelines to limit the adoption of new features that had not been tested by existing implementations.
引入的新特性: type generic macros, anonymous structures, improved Unicode support, atomic operations, multi-threading, and bounds-checked functions. 两个头文件: <stdalign.h>, <stdnoreturn.h>

refer:

- http://www.soimort.org/posts/160/
- https://en.wikipedia.org/wiki/C_(programming_language)
- http://www.crifan.com/summary_c_language_version_c89_amd1_c99_c11/
