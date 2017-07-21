#task_worker
#执行任务的进程
import time,sys,queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager): #创建类似的QueueManager
	pass  

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr) #连接到服务器

m = QueueManager(address=(server_addr,5000),authkey=b'abc') 
#端口和验证码要和服务器的一致
m.connect() #从网络连接

task = m.get_task_queue() 
result = m.get_result_queue()

for i in range(10):  #从task队列取任务 并把结果写入result队列
	try:
		n = task.get(timeout=1)
		print('run task %d * %d' % (n,n))
		r = '%d * %d = %d' % (n,n,n*n)
		time.sleep(1)
		result.put(r)
	except Queue.Empty:
		print('task queue is empty.')

print('worker exit.')