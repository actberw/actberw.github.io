inline 

GNU89:
"inline": the function may be inlined (it's just a hint though). An out-of-line version is always emitted and externally visible. Hence you can only have such an inline defined in one compilation unit, and every other one needs to see it as an out-of-line function (or you'll get duplicate symbols at link time).
"static inline" will not generate a externally visible out-of-line version, though it might generate a file static one. The one-definition rule does not apply, since there is never an emitted external symbol nor a call to one.
"extern inline" will not generate an out-of-line version, but might call one (which you therefore must define in some other compilation unit. The one-definition rule applies, though; the out-of-line version must have the same code as the inline offered here, in case the compiler calls that instead.
C99 (or GNU99):
"inline": like GNU "extern inline"; no externally visible function is emitted, but one might be called and so must exist
"extern inline": like GNU "inline": externally visible code is emitted, so at most one translation unit can use this.
"static inline": like GNU "static inline". This is the only portable one between gnu89 and c99

extern inline 会生成一个extern 函数
static inline 会生成一个static 函数
inline 不会生成函数, 代码直接内嵌(declaration 用 inline, defination时不用定义inline).

gcc 默认-O0 优化级别不会进行 inline 的, 所以直接定义一个inline函数然后进行调用会报错.


- "static inline" means "we have to have this function, if you use it
   but don't inline it, then make a static version of it in this
   compilation unit"

 - "extern inline" means "I actually _have_ an extern for this function,
   but if you want to inline it, here's the inline-version"

refer:

- [http://stackoverflow.com/questions/216510/extern-inline](http://stackoverflow.com/questions/216510/extern-inline)
- [http://wangcong.org/blog/archives/2021](http://wangcong.org/blog/archives/2021)
