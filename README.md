# NowCoder Practice Python  |  牛客网python练习 [牛客题霸部分](https://www.nowcoder.com/exam/oj?page=1&tab=Python篇&topicId=314)
夯实基础部分
## Key Points ✏️
* 巧用`type`判断类型
* `.format` 括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换。
   ```
   "{:.2f}".format(float1)
   ```
* 进制转换`int(i,16)`， `i`代表要被转换的数字 `16`代表转换成16进制
* 大小写转换
  ```
  str1.lower() # 全小写
  str1.upper() # 全大写
  str1.capitalize()  # 首字母大写
  ```
* `strip([chars])` 方法用于移除字符串头尾指定的字符（默认为空格）或字符序列。
  > chars -- 移除字符串头尾指定的字符序列。
  > 注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
* `str.split(str="", num=string.count(str)).`
  > str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
  > num -- 分割次数。默认为 -1, 即分隔所有。
  ```
  str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
  str.split( );       # 以空格为分隔符，包含 \n
  str.split(' ', 1 ); # 以空格为分隔符，分隔成两个
  ```
* 添加：
  * `append`在列表尾部添加，
  * `insert(index, obj)`可以指定添加顺序
* 删除：
  * `list.remove(obj)`移除列表中某个值的第一个匹配项
  * `list.pop([index=-1])`移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
  * 可以使用 del 语句来删除列表的的元素
* 排序：sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
  * `list.sort( key=None, reverse=False)` 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。
  * `sorted(iterable, cmp=None, key=None, reverse=False)`
