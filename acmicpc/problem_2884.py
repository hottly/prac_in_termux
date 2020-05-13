#enter a time HH:MM
#print time before 45minutes


class clock:
   
    def __init__(self, t_time="NONE"):
        if t_time == "NONE":
            self.HH = 0
            self.MM = 0
        else:
            self.HH = int(t_time.split(":")[0])
            self.MM = int(t_time.split(":")[1])

    def tick_minute_forward(self):
        if self.MM+1 == 60:
            self.MM = 0
            self.tick_hour_forward()
        else:
            self.MM = self.MM+1

    def tick_hour_forward(self):
        if self.HH+1 == 24:
            self.HH = 0
        else:
            self.HH = self.HH+1

    def tick_hour_backward(self):
        if self.HH-1<0:
            self.HH = 23
        else:
            self.HH = self.HH-1

    def tick_minute_backward(self):
        if self.MM-1<0:
            self.MM = 59
            self.tick_hour_backward()
        else:
            self.MM = self.MM-1
        
    def tick_times(self, times, ward):
        for i in range(0, times): 
            if ward == "-":
                self.tick_minute_backward()
            else:
                self.tick_minute_forward()
  
    def set_time(self, t_time):
        self.HH = int(t_time.split(":")[0])
        self.MM = int(t_time.split(":")[1])


t = input()
c = clock(t)

c.tick_times(45,"-")
print("%d:%d"%(c.HH,c.MM))
