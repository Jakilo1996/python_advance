## argparse
argparse模块是标准库中最大的模块之一，拥有大量的配置选项，这里只说明最常用、最基本的用法。

argparse自带说明文档，用python filename.py -h或者python filename.py --help就可以查看使用说明，非常方便，

```python
# metavar
import argparse
parser = argparse.ArgumentParser(description='Simple argparse test')
parser.add_argument('-t', dest='test', metavar='test', action='store', help='test option')
args = parser.parse_args()
print(args.test)
```
--- 
### 运行步骤
##### argparse模块的使用只需要四步就行，

1. 创建一个 ArgumentParser 实例

2. 使用 add_argument() 方法声明想要支持的选项

3. 使用parse_args()方法解析命令行参数

4. 获取参数值
---
### 参数介绍
- ArgumentParser实例的description参数是一个描述文字
#### add_argument()的参数说明

- name or flags	一个命名或者一个选项字符串的列表，例如 foo 或 -f, --foo。
- dest	解析结果被指派给属性的名字，即调用时候的名字。如果不指定，则会用第一个参数name or flags的名称。
- metavar	生成帮助信息，比如以上的[-t test]和-t test中的test。如果没有metavar，会使用大写的dest参数。
- action	指定跟属性对应的处理逻辑， 通常的值为 store，存储参数的值，这个是默认的动作。
- nargs	nargs 命名参数关联不同数目的命令行参数到单一动作。
- default	默认值，如果一个选项需要默认值，可以用default设置
- type	默认情况下，解析器会将命令行参数当作简单字符串读入。type默认是str，也可以指定为int、float等
- choices	表示受限制的参数值。可以是一个list对象、set对象等。
- required	默认required=False，可以用required=True表示必选参数
- help	参数简短描述的字符串

---
### add_argument()的参数说明参数及实例

#### name or flags   dest
add_argument()方法必须知道它是否是一个选项，例如 -f 或 --foo，或是一个位置参数，例如一组文件名。 -f认为是选项参数  位置参数也可以直接接收
第一个传递给 add_argument() 的参数必须是一系列 flags 或者是一个简单的参数名。如果是位置参数，指定的属性就是它本身，不能再用dest指定。

```python
import argparse

parser = argparse.ArgumentParser(description='Name or flags test')
# 加-的认为是 一个选项  调用时 -f f_arg 认为是f的参数 并复制给--foo
parser.add_argument('-f', '--foo')
# 不能这样写 parser.add_argument('bar', dest='bar_arg')
parser.add_argument('bar')
args = parser.parse_args()
print(dir(args))
print(args.foo)
print(args.bar)
# 其中的bar是位置参数，是必须要传入的参数。

# cmd line
#  python 01_arg_name.py -f f_arg bar_arg

# out_put
# ['__class__', '__contains__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_get_args', '_get_kwargs', 'bar', 'foo']
# f_arg
# bar_arg
```
---
#### action
ArgumentParser对象将命令行参数与动作相关联。这些动作可以做与它们相关联的命令行参数的任何事，
尽管大多数动作只是简单的向parse_args()返回的对象上添加属性。action命名参数指定了这个命令行参数应当如何处理。相应的动作有：

##### 'store'
 存储参数的值，这个是默认动作。

##### 'store_const'
- 存储被const命名参数指定的值。选项的值会变成一个固定值。   
- 传入store_const时 需要传入参数 const 用来指定选项的默认值 是否可以是一个列表
- 如果指定了默认值，在使用选项进行传参，就会报错

##### 'store_true' and 'store_false'
- 这些是'store_const'分别用作存储True和False值的特殊用例。它们的默认值对应的是Flase和True。比如一个选项--foo，action是'store_true'，
- 如果运行时命令行没有指定--foo，则存储的值是False；
- 如果运行时指定了--foo，则存储的值是True。


##### 'append'
-存储一个列表，并且将每个参数值追加到列表中。在允许多次使用选项时很有用。

```python
import argparse
parser = argparse.ArgumentParser(description='store const args')
# action default_value store
parser.add_argument('--foo_1',action='store')
# action set_default_value store_const
parser.add_argument('--foo_2',action='store_const',const=42)
# action store_ture
parser.add_argument('--foo_3',action='store_true')
# action store_false
parser.add_argument('--foo_4',action='store_false')
# action append
parser.add_argument('--foo_5',action='append')

# 获得命令行输入的参数
args= parser.parse_args()
print(f'store --foo_1:{args.foo_1}')
print(f'store_const --foo_2:{args.foo_2}')
print(f'store_true --foo_3:{args.foo_3}')
print(f'store_false --foo_4:{args.foo_4}')
print(f'store_false --foo_5:{args.foo_5}')

# cmd line    python 02_arg_action.py --foo_1 2 --foo_2 --foo_3 --foo_4 --foo_5 5 --foo_5 4
# output
# store --foo_1:2
# store_const --foo_2:42
# store_true --foo_3:True
# store_false --foo_4:False
# store_false --foo_5:['5', '4']

# cmd_line   p
# python 02_arg_action.py --foo_2 3
# output
# 02_arg_action.py: error: unrecognized arguments: 3


# cmd_line
# python 02_arg_action.py
# output   未传入参数时， 存储的值 与false true 默认值刚好相反 没有这个选项时存储的是False；有这个选项时存储的是True。
# store --foo_1:None
# store_const --foo_2:None
# store_true --foo_3:False
# store_false --foo_4:True
```
---

#### nargs
ArgumentParser对象通常关联一个单独的命令行参数到一个单独的被执行的动作。

##### nargs 命名参数关联不同数目的命令行参数到单一动作。可以思考一下和action中append的区别。支持的值有：

- N 一个整数  根据整数的数量来设定命令行参数
- '?' 表示有或者没有选项的值。
- '*' 表示0个或者大于0个。
- '+' 表示大于等于一个。其实'?'、'*'、'+'和正则表达式意义差不多
```python
import  argparse
parser = argparse.ArgumentParser(description='nargs test')
# 一个
parser.add_argument('--foo_1',nargs=1)
parser.add_argument('--foo_2',nargs=2)

# 有或没有  没有None  有 技能接收一个
parser.add_argument('--foo_3',nargs='?')
# '*' 表示0个或者大于0个。不管传入几个都用列表来接收
parser.add_argument('--foo_4',nargs='*')
# '+' 表示大于等于一个  不管传入几个，都用列表来接收   不足一个  # 报错 expected at least one argument
parser.add_argument('--foo_5',nargs="+")

args = parser.parse_args()
print(f'"N"--foo_1:{args.foo_1}')
print(f'"N"--foo_2:{args.foo_2}')

print(f'"?"--foo_3:{args.foo_3}')
print(f'"*"--foo_4:{args.foo_4}')

print(f'"+"--foo_3:{args.foo_5}')

# cmd_line
# python 03_arg_nargs.py --foo_1 2 --foo_2 a b --foo_3 a --foo_4  --foo_5 s

# ouput
# "N"--foo_1:['2']
# "N"--foo_2:['a', 'b']
# "?"--foo_3:a
# "*"--foo_4:[]
# "+"--foo_3:['s']

# cmd_line
#  python 03_arg_nargs.py

# output   都没有值时  都为空
# "N"--foo_1:None
# "N"--foo_2:None
# "?"--foo_3:None
# "*"--foo_4:None
# "+"--foo_3:None
# "*"--foo_4:None
# "+"--foo_3:None

# cmd_line
# python 03_arg_nargs.py --foo_3  --foo_4

# output
# "N"--foo_1:None
# "N"--foo_2:None
# "?"--foo_3:None
# "*"--foo_4:[]
# "+"--foo_3:None

```
---
#### choices
- 从choices选项中指定参数的值。指定当前选项的取值范围 未传入 取值为None
- 传入超过一个值 报错 unrecognized arguments
- 传入非取值范围  报错  invalid choice 
- 结合default 使用默认值，未传入 取默认值

```python
import argparse


parser = argparse.ArgumentParser(description='choices test')
parser.add_argument('--foo',choices=['arg1','arg2','arg3'],default='arg1')
args = parser.parse_args()
print(f'current foo arg: {args.foo}')

# command line
#  python 04_arg_choices.py

# output
# current foo arg: arg1

# command line    python 04_arg_choices.py --foo arg2
# output
# current foo arg: arg2
```
---
#### required
默认required=False， 表示非必选参数

可以用required=True   表示必选参数  不能和default 否则不会报错
```python
import argparse

parser = argparse.ArgumentParser(description='choices test')
parser.add_argument('--foo',choices=['arg1','arg2','arg3'],required=True)
args = parser.parse_args()
print(f'current foo arg: {args.foo}')


# command_line
# python 05_arg_required.py

# output
# error: the following arguments are required: --foo
```
---
#### type

##### 默认情况下，解析器会将命令行参数当作简单字符串读入。
- type默认是str，也可以指定为int、float等
- 传入错误的type 报错invalid int value: 'b'
- 如果指定格式为list  会将字符串参数的每个元素拆分列表的每一个元素存储
- 如果指定格式为tuple  会将字符串参数的每个元素拆分元祖的每一个元素存储
- 如果指定格式为set  会将字符串参数的每个元素拆分集合的每一个元素存储
- 注意 # 尝试后认为不支持字典
```python
import argparse

parser = argparse.ArgumentParser(description='type test')

parser.add_argument('--foo_1', type=int)
parser.add_argument('--foo_2', type=float)
parser.add_argument('--foo_3', type=list)
parser.add_argument('--foo_4', type=tuple)
parser.add_argument('--foo_5', type=set)
# parser.add_argument('--foo_6', type=dict)
args = parser.parse_args()
print(f"int foo_1:{args.foo_1}")
print(f"float foo_2:{args.foo_2}")
print(f"list foo_3:{args.foo_3}")
print(f"tuple foo_4:{args.foo_4}")
print(f"set foo_5:{args.foo_5}")
# 不支持字典
# print(f"dict foo_6:{args.foo_6}")
# int foo_1:2
# float foo_2:3.0
# list foo_3:['1', 'a', 'b']
# tuple foo_4:('b', '2', '3', '4', 's')
# set foo_5:{'a', 'b', 's', 'd'}


# command_line  python 06_arg_type.py --foo_1 2 --foo_2 3 --foo_3 1ab --foo_4 b234s --foo_5 bsadad
# output
```