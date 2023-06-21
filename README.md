# NowCoder Practice Python  |  牛客网python练习 [牛客题霸部分](https://www.nowcoder.com/exam/oj?page=1&tab=Python篇&topicId=314)
夯实基础部分
## Key Points ✏️
* 巧用`type`判断类型
* 进制转换`int(i,16)`， `i`代表要被转换的数字 `16`代表转换成十六进制
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
  > num -- 分割次数。默认为`-1`, 即分隔所有。
  ```
  str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
  str.split( );       # 以空格为分隔符，包含 \n
  str.split(' ', 1); # 以空格为分隔符，分隔成两个
  ```
* 添加：
  * `append`在列表尾部添加，
  * `insert(index, obj)`可以指定添加顺序
* 删除：
  * `list.remove(obj)`移除列表中某个值的第一个匹配项
  * `list.pop([index=-1])`移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
  * 可以使用 del 语句来删除列表的的元素
* 排序：sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
  * `list.sort(key=None, reverse=False)` 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。
  * `sorted(iterable, cmp=None, key=None, reverse=False)`
* List列表：
   * 索引从0开始：Python中的列表索引是从0开始的，意味着列表的第一个元素的索引是0，第二个元素的索引是1，以此类推。因此，访问列表中的元素时，需要使用正确的索引值。
   * 负数索引：除了正数索引外，还可以使用负数索引来访问列表中的元素。负数索引从列表末尾开始计数，例如，-1表示最后一个元素，-2表示倒数第二个元素，以此类推。
   * 切片操作使用索引范围来指定子集的起始位置和结束位置，语法为 list[start:end]。切片操作将返回一个新的列表。此语法用于提取从索引start开始到索引end之前的元素，其中start是包含的，而end是不包含的
     ```
     my_list = [10, 20, 30, 40, 50]
     print(my_list[1:3])  # 输出: [20, 30]
     print(my_list[:3])   # 输出: [10, 20, 30]
     print(my_list[2:])   # 输出: [30, 40, 50]
     ```
* 指数相乘用2个乘号 **
* 在Python中，有多种方式可以格式化输出。以下是其中几种常用的方式：

   1. 通过占位符格式化输出：可以使用占位符（例如`%`）将要输出的值插入到字符串中的适当位置。常见的占位符有 `%s`（字符串）、`%d`（整数）、`%f`（浮点数）等。例如：
   
   ```python
   name = "Alice"
   age = 25
   print("My name is %s and I'm %d years old." % (name, age))
   ```
   
   2. 使用`str.format()`方法格式化输出：通过将要输出的值作为参数传递给`format()`方法，并使用大括号 `{}` 作为占位符，可以实现格式化输出。例如：
   
   ```python
   name = "Alice"
   age = 25
   print("My name is {} and I'm {} years old.".format(name, age))
   ```
   
   3. 使用f-strings（格式化字符串字面值）：在字符串前加上 `f` 前缀，可以直接在字符串中使用花括号 `{}` 插入变量或表达式。例如：
   
   ```python
   name = "Alice"
   age = 25
   print(f"My name is {name} and I'm {age} years old.")
   ```
* `x//y`用来得商（整除），`x%y`用来得余数，`{/y:.2f}`输出x除以y的非整除结果，保留两位小数
* x与y `x and y`，x或y `x or y`，非x `not int(x)`
* `x&y` 位与、`x|y` 位或，输出按照十进制的形式。
* `name in lst`检测name是否在lst中
* map 映射功能
* 判断一个列表是空
  ```
   if len(my_list) == 0
   if not my_list
   if my_list == []
  ```
* range(start, stop, step)
   * start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
   * stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
   * step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
