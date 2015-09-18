Title: 标准文件头
Date: 2014-09-02

### stddef.h

NULL
offsetof
size_t

### ctype.h

Defines set of functions used to classify characters by their types or to convert between upper and lower case in a way that is independent of the used character set 


isdigit
islower
isalpha

### stdint.h(c99)

int8_t/uint8_t
int16_t/uint16_t
int32_t/uint32_t
int64_t/uint64_t

这个头文件是c99定义的, 使用的时候可以用`ifdef __STDC_VERSION__` 检查版本.

### limits.h

Defines macro constants specifying the implementation-specific properties of the integer types.

INT_MAX
INT_MIN

### stdio.h

stdin
stdout
stderr

### unistd.h

STDIN_FILENO
STDOUT_FILENO
STDERR_FILENO
