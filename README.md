# NowCoder Practice Python  |  牛客网python练习 [牛客题霸部分](https://www.nowcoder.com/exam/oj?page=1&tab=Python篇&topicId=314)
夯实基础部分
## Key Points ✏️
* 巧用`type`判断类型
* 进制转换`int(i,16)`， `i`代表要被转换的数字 `16`代表转换成十六进制
* 大小写转换
  ```
  str1 = "www.mAnhuAn.net is learNing pyThon's weBsiTe"
  str1.lower() # 全小写
  str1.upper() # 全大写
  str1.capitalize()  # 全字符串中首字母大写
  str_val = str.title() # 字符串中每个单词的首字母大写

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
  * `append()`在列表尾部添加，
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
* 指数相乘用2个乘号 `**`
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
* map(function, iterable,) 函数会根据提供的函数对指定序列做映射。第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
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
* 元组
  * `tuple()`创建tuple或者转化成元组
  * 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
  * 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
* 字典
  * dictionary中items以列表返回可遍历的（键值）元组数组
  * .keys
  * 字典获取元素的方法i['key值']，或者i.get('key值')
  * zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
  ```
      >>> a = [1,2,3]
      >>> b = [4,5,6]
      >>> c = [4,5,6,7,8]
      >>> zipped = zip(a,b)     # 打包为元组的列表
      [(1, 4), (2, 5), (3, 6)]
      >>> zip(a,c)              # 元素个数与最短的列表一致
      [(1, 4), (2, 5), (3, 6)]
      >>> zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
      [(1, 2, 3), (4, 5, 6)
  ```
* ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值
* 进制转换
  > hex  16进制
  > int  10进制
  >  oct  8进制
  >  bin  2进制
* count() 方法用于统计字符串里某个字符或子字符串出现的次数。可选参数为在字符串搜索的开始与结束位置。
* str.index(substring, beg=0, end=len(string))，
  > substring -- 指定检索的字符串。 beg -- 开始索引，默认为 0。 end -- 结束索引，默认为字符串的长度。
* [字符串处理支持多种操作](https://www.runoob.com/python3/python3-string.html)
* round()保留几位小数 返回浮点数x的四舍五入值。
* eval()神奇公式： 用来执行一个字符串表达式，并返回表达式的值。
* OOP
* 正则表达式
    * `re.match(pattern, string, flags=0)` 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回None
       * pattern：匹配的正则表达式
       * string：要匹配的字符串。
       * fl：标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。参见：正则表达式修饰符 - 可选标志
    * `re.sub(pattern, repl, string, count=0, flags=0)` re模块提供了re.sub用于替换字符串中的匹配项。
      * pattern : 正则中的模式字符串。
      * repl : 替换的字符串，也可为一个函数。
      * string : 要被查找替换的原始字符串。
      * count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
      * flags : 编译时用的匹配模式，数字形式。
    * `re.search(pattern, string, flags=0)` 扫描整个字符串并返回第一个成功的匹配
      ```
      import re
 
      print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
      print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配
      ```
* 未完待续……
