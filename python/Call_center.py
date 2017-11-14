class Call(object):
    def __init__(self,unique_id,name,phone,time,reason):
        self.unique_id=unique_id
        self.name=name
        self.phone=phone
        self.time=time
        self.reason=reason

   def callAttributes(self):
        print self.unique_id
        print self.name
        print self.phone
        print self.time
        print self.reason
        print ""
    
class Callcenter(object):
    queue_size: 0
    call_queue: []
    def __init__(self)
    