# GUI 图形用户界面
# 输入框 列表框 按钮 复选框 等窗口组件

def foo():
    listA = []
    print('input the number:')
    while True:
        num = input()
        if num == '.':
            break
        listA.append(eval(num))
    sumList = sum(listA)
    return sumList

if __name__ == '__main__':
    print(foo())


# 面向对象
# 抽象 & 继承
class Dog(object):
    counter = 0
    def __init__(self,name):
        self.name = name
        Dog.counter += 1
    def greet(self):
        print('Hi! I am %s, my number is %d' % self.name, Dog.counter)
    # def setName(self,name):
    #     self.name = name
dog = Dog('Ming')
# dog.setName('Ming')
dog.greet()
# 1定义类 2创建实例 3通过实例使用属性或方法

# 继承：单继承、多继承
class BarkingDog(Dog):
    def greet(self):
        print('Woof! I am %s, my number is %d' % self.name,Dog.counter)

# 重载

# 默认情况下，Python类的成员属性与方法都是public
# 访问控制符：双下划线（__）在类内部可见   单下划线（_）在模块内部可见