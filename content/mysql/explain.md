###mysql explain
mysql explain 的输出结果, 类似于下面:

        +----+-------------+---------+-------+---------------+-----+---------+------+------+-------+
        | id | select_type | table   | type  | possible_keys | key | key_len | ref  | rows | Extra |
        +----+-------------+---------+-------+---------------+-----+---------+------+------+-------+
解释如下:
    ColumnMeaning
    idThe SELECT identifier
    select_typeThe SELECT type          
    tableThe table for the output row
    partitionsThe matching partitions
    typeThe join type
    possible_keysThe possible indexes to choose
    keyThe           index actually chosen
    key_lenThe length of the chosen key
    refThe col      umns compared to the index
    rowsEstimate of rows to be examined
    filtere datePercentage of rows filtered by table condition
    ExtraAdditional infor   mation

####refer:
- http://www.slideshare.net/ligaya/explain
- http://www.slideshare.net/ronaldbradford/10x-performance-improvements-a-case-study
- http://ustb80.blog.51cto.com/6139482/1064261
- http://hidba.org/?p=404
- http://www.cnblogs.com/iLoveMyD/archive/2012/06/12/2546679.html
- http://stackoverflow.com/questions/7643491/understanding-mysql-key-len-in-explain-statement
