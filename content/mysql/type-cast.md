Title: 类型转换
Tags: mysql

##  Expression Evaluation, cast and convert

When an operator is used with operands of different types, type conversion occurs to make the operands compatible. Some conversions occur implicitly

    mysql> SELECT 1+'1';
            -> 2
    mysql> SELECT CONCAT(2,' test');
            -> '2 test'

The `CAST(expr AS type)` function takes an expression of any type and produces a result value of a specified type, similar to CONVERT(). See the description of CONVERT() for more information.
`CONVERT(expr USING transcoding_name)` converts data between different character sets.

The type for the result can be one of the following values:

- BINARY[(N)]
- CHAR[(N)]
- DATE
- DATETIME
- DECIMAL[(M[,D])]
- JSON (added in MySQL 5.7.8)
- SIGNED [INTEGER]
- TIME
- UNSIGNED [INTEGER]

## conversion rule

The following rules describe how conversion occurs for comparison operations:

- If one or both arguments are NULL, the result of the comparison is NULL, except for the NULL-safe <=> equality comparison operator. For NULL <=> NULL, the result is true. No conversion is needed.
- If both arguments in a comparison operation are strings, they are compared as strings.
- If both arguments are integers, they are compared as integers.
- Hexadecimal values are treated as binary strings if not compared to a number.
- If one of the arguments is a TIMESTAMP or DATETIME column and the other argument is a constant, the constant is converted to a timestamp before the comparison is performed. This is done to be more ODBC-friendly. Note that this is not done for the arguments to IN()! To be safe, always use complete datetime, date, or time strings when doing comparisons. For example, to achieve best results when using BETWEEN with date or time values, use CAST() to explicitly convert the values to the desired data type.
- If one of the arguments is a decimal value, comparison depends on the other argument. The arguments are compared as decimal values if the other argument is a decimal or integer value, or as floating-point values if the other argument is a floating-point value.
- In all other cases, the arguments are compared as floating-point (real) numbers.

For comparisons of a string column with a number, MySQL cannot use an index on the column to look up the value quickly. If str_col is an indexed string column, the index cannot be used when performing the lookup in the following statement:

    SELECT * FROM tbl_name WHERE str_col=1;

The reason for this is that there are many different strings that may convert to the value 1, such as '1', ' 1', or '1a'.

反过来，如果使用一个字符串作为查询参数，对一个数字字段做比较查询，MySQL 则是可以有效利用索引的, 原因则是，MySQL 可以将查询参数 '30' 转换为确定的数值 30，之后可以快速地在索引中找到与之相等的数值。

隐式类型转换有无法命中索引的风险, 注意一个安全问题：假如 password 类型为字符串，查询条件为 int 0 则会匹配上,  会对表字段做类型转换。 如果隐式转换发生在传入的值上面，就并不会影响到优化器对执行计划的选择。 相反，如果隐式转换发生在数据表字段（也就是数据库中的数据）上，则必定会影响到优化器对执行计划的选择


refer:

- [https://dev.mysql.com/doc/refman/5.5/en/type-conversion.html](https://dev.mysql.com/doc/refman/5.5/en/type-conversion.html)
- [http://dev.mysql.com/doc/refman/5.7/en/cast-functions.html](http://dev.mysql.com/doc/refman/5.7/en/cast-functions.html)
- [http://blog.xupeng.me/2012/02/08/type-conversion-and-index-selection-of-mysql/](http://blog.xupeng.me/2012/02/08/type-conversion-and-index-selection-of-mysql/)
- [https://vagosec.org/2013/04/mysql-implicit-type-conversion/](https://vagosec.org/2013/04/mysql-implicit-type-conversion/)
