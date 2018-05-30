
class call(object):
	def __init__(self,ids,caller_name,call_num,time,reason):
		print "adding caller"
		self.id= ids
		self.caller_name=caller_name
		self.call_num= call_num
		self.time= time
		self.reason=reason
	def display(self):
		print "ID:", self.id, "Name:", self.caller_name, "Number:", self.call_num, "Time:",self.time, "Reason for Call:", self.reason
		return self

class call_center(object):
	def __init__(self):
		self.calls_list=[]
		self.callqueue=0
	def add_call(self,x):
		# print x
		self.calls_list.append(x)
		self.callqueue+=1
		# print self.calls_list
		# print self.callqueue
		return self
	def remove_call(self):
		print "Removing caller"
		self.calls_list.pop()
		self.callqueue-=1
		print self.calls_list
		print self.callqueue
	def info(self):
		print "Number of Calls:" ,self.callqueue
		for i in range(0,len(self.calls_list)):
			print self.calls_list[i].caller_name, self.calls_list[i].call_num
		return self



call1= call("0", "Andy", "4087729399", "4:30", "I've fallen and I cant get up")
call2= call("1", "John", "4087729399", "4:30", "I've fallen and I cant get up")
call3= call("3", "Nate", "4087729399", "4:30", "I've fallen and I cant get up")
call4= call("4", "Andie", "4087729399", "4:30", "I've fallen and I cant get up")

testcallcenter=call_center()
# 
testcallcenter.add_call(call1).add_call(call2).add_call(call3).add_call(call4).info()


