import argparse

parser = argparse.ArgumentParser(description='请在命令行中传入一个数字')

# 传入一个参数
# type是要传入的参数的数据类型  help是该参数的提示信息
# parser.add_argument('integers', type=str, help='传入的数字')

# 传入多个参数
# nargs是用来说明传入的参数个数，'+' 表示传入至少一个参数。
# parser.add_argument('integers', type=str, nargs='+',help='传入的数字')

# 改变数据类型
# 我们看到代码中有type这个关键词，该关键词可以传入list, str, tuple, set, dict等。
# parser.add_argument('integers', type=int, nargs='+',help='传入的数字')

# 位置参数
parser.add_argument('param1', type=str,help='姓')
parser.add_argument('param2', type=str,help='名')

# 可选参数 + 默认值  
parser.add_argument('--family', type=str, default='张',help='姓')
parser.add_argument('--name', type=str, required=True, default='三', help='名')

# 必需参数
parser.add_argument('--family', type=str, help='姓')
parser.add_argument('--name', type=str, required=True, default='', help='名')

args = parser.parse_args()

#获得传入的参数
# print(args)

#获得integers参数
# print(args.integers)

# 打印姓名
# print(args.param1+args.param2)

# 打印姓名with可选参数 
print(args.family+args.name)