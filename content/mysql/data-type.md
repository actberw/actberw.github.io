Title: mysql 数据类型
Tags: mysql
Date: 2014-07-10 20:44:00

## String Types

mysql字符串指用单引号(‘'’)或双引号(‘"’)引起来的字符序列。例如：

'a string'

"another string"

如果 [sql_mode](/posts/mysql/sql-mode.html) 启用了ANSI_QUOTES，则只能用单引号引用字符串, 用双引号引用的字符串被解释为一个识别符。

The string types are CHAR, VARCHAR, BINARY, VARBINARY, BLOB, TEXT, ENUM, and SET. Variable-length string types are stored using a length prefix plus data. 

## 数字类型

- Integer Types (Exact Value) - INTEGER, INT, SMALLINT, TINYINT, MEDIUMINT, BIGINT
- Fixed-Point Types (Exact Value) - DECIMAL, NUMERIC
- Floating-Point Types (Approximate Value) - FLOAT, DOUBLE
- Bit-Value Type - BIT

The DECIMAL and NUMERIC types store exact numeric data values, Storage for the integer and fractional parts of each value are determined separately.. These types are used when it is important to preserve exact precision, for example with monetary data

The declaration syntax for a DECIMAL column is DECIMAL(M,D). The ranges of values for the arguments in MySQL 5.6 are as follows:

- M is the maximum number of digits (the precision). It has a range of 1 to 65.
- D is the number of digits to the right of the decimal point (the scale). It has a range of 0 to 30 and must be no larger than M.

Values for DECIMAL columns in MySQL 5.6 are stored using a binary format that packs nine decimal digits into 4 bytes. The storage requirements for the integer and fractional parts of each value are determined separately. 

MySQL supports an extension for optionally specifying the display width of integer data types in parentheses following the base keyword for the type.
The display width does not constrain the range of values that can be stored in the column. Nor does it prevent values wider than the column display width from being displayed correctly. All integer types can have an optional (nonstandard) attribute UNSIGNED. Unsigned type can be used to permit only nonnegative numbers in a column or when you need a larger upper numeric range for the column. Data type descriptions use these conventions:

- M indicates the maximum display width for integer types. For floating-point and fixed-point types, M is the total number of digits that can be stored (the precision). For string types, M is the maximum length. The maximum permissible value of M depends on the data type.
- D applies to floating-point and fixed-point types and indicates the number of digits following the decimal point (the scale). The maximum possible value is 30, but should be no greater than M−2.

## 时间类型

DATE, DATETIME, TIMESTAMP

refer:

- [http://dev.mysql.com/doc/refman/5.6/en/string-literals.html](http://dev.mysql.com/doc/refman/5.6/en/string-literals.html)
- [https://dev.mysql.com/doc/refman/5.6/en/storage-requirements.html](https://dev.mysql.com/doc/refman/5.6/en/storage-requirements.html)
- [https://dev.mysql.com/doc/refman/5.6/en/precision-math-decimal-characteristics.html](https://dev.mysql.com/doc/refman/5.6/en/precision-math-decimal-characteristics.html)
