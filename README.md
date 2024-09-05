NowCoder Practice Python  |  牛客网python练习: [牛客题霸部分](https://www.nowcoder.com/exam/oj?page=1&tab=Python篇&topicId=314)
夯实基础部分
===========
## Key Points ✏️
* int 类型的整数具有任意精度。这意味着整数的取值范围仅受限于可用内存，而不像某些编程语言中整数的大小受限于固定的字节数;
* 在 Python 中，float 类型的浮点数通常是基于 IEEE 754 双精度浮点数标准存储的，这意味着它在内存中占用 64 位（8 字节）。其取值范围和精度如下：

  范围：约为 1.8 × 10^−308 到 1.8×10^308 精度：有效数字约为 15-17 位十进制数

* Binary: 加号 + 作为二元运算符时用于将两个操作数相加 uniary作为一元运算符时用于表示数值的正号
* 牢记运算优先顺序
  ```
      3------9 输出 *12*
      3+-+-+-2 输出 *1*
      3*4**5 输出 48
  ```
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

## String 字符串格式化
python最先的格式化字符串方法是%，但他的致命缺点是支持的类型有限，只支持int,str,double,其他所有类型只能转换为这几个类型，还有如果传递的是元组，那么必须还要传入一个单值元组，为此，添加了str.format（）以解决％-formatting中的一些问题，

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
  
## 迭代器和生成器
* 将列表生成式中[]改成() 之后数据结构是否改变？ 答案：会发生改变，从列表变为生成器:
  ```shell
  >>> L = [x*x for x in range(10)]
  >>> L
  [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
  >>> g = (x*x for x in range(10))
  >>> g
  <generator object <genexpr> at 0x0000028F8B774200>
  >>>
  ```
  通过列表生成式，可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含百万元素的列表，不仅是占用很大的内存空间，如：我们只需要访问前面的几个元素，后面大部分元素所占的空间都是浪费的。因此，没有必要创建完整的列表（节省大量内存空间）。在Python中，我们可以采用生成器：边循环，边计算的机制—>generator
  
* 666 and True => 666  
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

  
## OOP
### *args and **kwargs
* 当你不确定你的函数里将要传递多少参数时你可以用*args.例如,它可以传递任意数量的参数
  ```
  >>> def print_everything(*args):
        for count, thing in enumerate(args):
  ...         print '{0}. {1}'.format(count, thing)
  ...
  >>> print_everything('apple', 'banana', 'cabbage')
  0. apple
  1. banana
  2. cabbage
  ```
* 而**kwargs则是将一个 **可变的关键字参数的字典** 传给函数实参，同样参数列表长度可以为0或为其他值。相似的,**kwargs允许你使用没有事先定义的参数名:
  ```
  >>> def table_things(**kwargs):
  ...     for name, value in kwargs.items():
  ...         print '{0} = {1}'.format(name, value)
  ...
  >>> table_things(apple = 'fruit', cabbage = 'vegetable')
  cabbage = vegetable
  apple = fruit
  ```
  正如前面所说的，args类型是一个tuple，而kwargs则是一个字典dict，并且args只能位于kwargs的前面。

  
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
* 未完待续……在 Python 中，参数通常是通过**对象引用**传递的。但理解参数传递时，需要区分**可变类型**和**不可变类型**。

## 基本数据类型（不可变类型）
- **例子:** `int`（整数）, `float`（浮点数）, `bool`（布尔值）, `str`（字符串）, `tuple`（元组）
- **行为:** 当你将不可变的数据类型（如整数、浮点数或布尔值）作为参数传递给函数时，实际上传递的是该对象引用的**副本**。这意味着函数不能直接修改原始对象。在函数内部对参数进行的修改，只会影响局部变量的副本，**不会改变函数外部的原始对象**。

**例子：**
```python
def modify_value(x):
    x = 10
    print("函数内部:", x)

a = 5
modify_value(a)
print("函数外部:", a)
```

**输出：**
```
函数内部: 10
函数外部: 5
```

在这个例子中，`a` 在函数外部的值依然是 `5`，因为在函数内部修改的只是局部变量 `x` 的副本。

### 可变数据类型
- **例子:** `list`（列表）, `dict`（字典）, `set`（集合）
- **行为:** 当你将可变数据类型（如列表或字典）作为参数传递时，传递的是对原始对象的引用。**因此，在函数内部修改对象时，外部的原始对象也会被修改**。

**例子：**
```python
def modify_list(lst):
    lst.append(4)
    print("函数内部:", lst)

my_list = [1, 2, 3]
modify_list(my_list)
print("函数外部:", my_list)
```

**输出：**
```
函数内部: [1, 2, 3, 4]
函数外部: [1, 2, 3, 4]
```

在这个例子中，`my_list` 在函数外部也发生了变化，因为函数内部的 `lst` 和外部的 `my_list` 指向同一个对象。

### 总结
- **不可变类型:** 传递的是值（引用的副本），在函数内部的修改**不会**影响外部的原始对象。
- **可变类型:** 传递的是引用，函数内部对对象的修改**会**影响外部的原始对象。
