#task_master
#服务进程负责启动Queue 把Queue注册到网络上 然后往Queue里面写入任务
import random,time,queue
from multiprocessing.managers import BaseManager

task_queue = queue.Queue() #发送任务队列
result_queue = queue.Queue() #接收结果队列

class QueueManager(BaseManager):
	pass

QueueManager.register('get_task_queue',callable=lambda:task_queue)
QueueManager.register('get_result_queue',callable=lambda:result_queue)
#把Queue注册到网络上 get_xx_queue是两个接口

manager = QueueManager(address=('',5000),authkey=b'abc') #绑定端口5000 验证码abc

manager.start() #启动Queue

task = manager.get_task_queue()
result = manager.get_result_queue() #获得通过网络访问的Queue对象
#通过接口去访问

for i in range(10):
	n = random.randint(0,10000)
	print('Put task %d...' % n)
	task.put(n) #放任务

print('Try get result...')
for i in range(10):
	r = result.get(timeout=10)
	print('Result: %s' % r) #读取结果

manager.shutdown() #关闭 
print('master exit.s')

#在服务器进程端控制manager的启动和关闭即可 manager封装了Queue的接口
#读写Queue的内容必须通过该接口 而不能直接操作task_queue或result_queue

