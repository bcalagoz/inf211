import random

my_name = "Burak Can Alagoz"
my_id = "190102002006"
my_email = "b.alagoz2019@gtu.edu.tr"


class Transceiver:
    t_id = 0
    
    def __init__(self,x,y,tpower,rpower=0.001):
        self.x = x
        self.y = y
        self.tpower = tpower
        self.rpower = rpower
        self.id = Transceiver.t_id
        Transceiver.t_id += 1
        self.localtime = 0

    def get_coordinate_x(self):
        return self.x

    def get_coordinate_y(self):
        return self.y

    def get_coordinates(self):
        return (self.x,self.y)

    def get_tpower(self):
        return self.tpower

    def get_rpower(self):
        return self.rpower  

    def get_id(self):
        return self.id

    def get_localtime(self):
        return self.localtime

    def set_coordinates(self,x, y):
        self.x = x
        self.y = y

    def set_transmitting_power(self,tpower):
        self.tpower = tpower

    def set_receiving_power(self, rpower):
        self.rpower = rpower

    def update_local_time(self,new_time):
        self.localtime = new_time

    def distance(self,m):
        return (((self.x - m.x)**2)+((self.y - m.y)**2))**0.5

    def transmitted_power(self,*args): 
        try:
            return self.tpower/(((self.x - args[0][0])**2)+((self.y - args[0][1])**2))**0.5
        except:
            return self.tpower

    def __eq__(self,other):
        return self.transmitted_power(other.get_coordinates()) >= other.rpower and other.transmitted_power(self.get_coordinates()) >= self.rpower

    def __lt__(self,other):
        return self.transmitted_power(other.get_coordinates()) >= other.rpower

    def __gt__(self,other):
        return other.transmitted_power(self.get_coordinates()) >= self.rpower

    def __str__(self):
        string = "Class: Tower\n"
        string += "   Tower number: " + str(self.id)
        string += "\n   Coordinates: " + "<"+str(self.x)+","+str(self.y)+">"
        string += "\n   Transmitting Power: " + (str(float(self.tpower/1000))+"kW" if self.tpower >= 1000 else str(float(self.tpower*1000))+"mW" if self.tpower < 1 else str(self.tpower)+"W")
        string += "\n   Min. Receiving Power: "+ (str(float(self.rpower/1000))+"kW" if self.rpower >= 1000 else str(float(self.rpower*1000))+"mW" if self.rpower < 1 else str(self.rpower)+"W")
        return  string
        
class Robot(Transceiver):
    r_id = 0

    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.velocity = (vx,vy)
        self.tpower = 1 
        self.rpower = 0.01 
        self.id = Robot.r_id
        Robot.r_id += 1
        self.flag = True
        self.distime = 0
        self.localtime = 0
        
    def get_velocity(self):
        return self.velocity

    def get_status(self):
        return self.flag

    def get_disconnet_time(self):
        return self.distime

    def set_velocity(self,vx,vy):
        self.vx = vx
        self.vy = vy
        self.velocity = (vx,vy)

    def set_status(self,newstatus):
        self.flag = newstatus

    def update_disconnect(self):
        self.distime += 1
    
    def set_disconnet_time(self):
        self.distime = 0

    def update_location(self):
        self.localtime += 1
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        
    def __str__(self):
        return "Class: Robot\n"+"  Robot number: " + str(self.id) + "\n  Current Coordinates: " + "<"+str(self.x)+","+str(self.y)+">"+"\n  Current Velocity: " + "<"+str(self.vx)+","+str(self.vy)+">"+"\n  Transmitting Power: 1W"+"\n  Min. Receiving Power: 10.0mW"+"\n  Status: "+("Alive" if self.flag == True else "Dead")

class Guard(Robot):
    def __init__(self,x, y, vx,vy, period=60,localtime=0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.velocity = (vx,vy)
        self.period = period
        self.localtime = localtime
        self.distime = 0
        self.tpower = 1 
        self.rpower = 0.01 
        self.flag = True
        self.id = Robot.r_id
        Robot.r_id += 1

    def get_period(self):
        return self.period

    def set_period(self,period):
        self.period = period

    def update_location(self):
        self.localtime += 1
        if self.localtime % self.period == 0:
            temp = self.vx
            self.vx = self.vy
            self.vy = -temp
            self.x = self.x + self.vx
            self.y = self.y + self.vy
            self.velocity = (self.vx,self.vy)
        else:
            self.x = self.x + self.vx
            self.y = self.y + self.vy

    def __str__(self):
        return "Class: Guard\n"+"  Robot number: " + str(self.id) + "\n  Current Coordinates: " + "<"+str(self.x)+","+str(self.y)+">"+"\n  Current Velocity: " + "<"+str(self.vx)+","+str(self.vy)+">"+"\n  Transmitting Power: 1W"+"\n  Min. Receiving Power: 10.0mW"+"\n  Status: "+("Alive" if self.flag == True else "Dead")

class Psycho(Robot):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.randint(-10, 10)
        self.vy = random.randint(-10, 10)
        self.velocity = (self.vx,self.vy)
        self.tpower = 1 
        self.rpower = 0.01 
        self.id = Robot.r_id
        Robot.r_id += 1
        self.flag = True
        self.distime = 0
        self.localtime = 0
        self.period = random.randint(0, 100)

    def update_location(self):
        self.localtime += 1
        if self.localtime % self.period == 0:
            self.vx = random.randint(-10, 10)
            self.vy = random.randint(-10, 10)
            self.velocity = (self.vx,self.vy)
            self.period = random.randint(0, 100)
        else:
            self.x = self.x + self.vx
            self.y = self.y + self.vy

    def __str__(self):
        return "Class: Psycho\n"+"  Robot number: " + str(self.id) + "\n  Current Coordinates: " + "<"+str(self.x)+","+str(self.y)+">"+"\n  Current Velocity: " + "<"+str(self.vx)+","+str(self.vy)+">"+"\n  Transmitting Power: 1W"+"\n  Min. Receiving Power: 10.0mW"+"\n  Status: "+("Alive" if self.flag == True else "Dead")

class Battle_Field:
    def __init__(self):
        self.globalTime = 0
        self.transceiverList = []
        self.robotList = []
        self.deadList = []

    def add_transceiver(self,x,y,tpower,rpower = 0.001):
        t = Transceiver(x,y,tpower,rpower)
        self.transceiverList.append(t)

    def add_robot(self,x, y, vx,vy):
        r = Robot(x,y,vx,vy)
        self.robotList.append(r)
        
    def add_guard(self,x,y,vx,vy,timer=0,period=60):
        g = Guard(x,y,vx,vy,period,timer)
        self.robotList.append(g)

    def add_psycho(self,x, y):
        p =Psycho(x,y)
        self.robotList.append(p)

    def get_transceivers(self):
        for i in range(len(self.transceiverList)):
            yield self.transceiverList[i]
                   
    def get_robots(self):
        for i in range(len(self.robotList)):
            yield self.robotList[i]

    def kill_robot(self,robot):    
        robot.set_status(False)
        self.deadList.append(robot)
        a = robot.get_id()
        b=0
        for i in range(len(self.robotList)):
            if self.robotList[i].get_id()==a:
                 b = i
        del self.robotList[b]

    def get_deadrobots(self):
        for i in range(len(self.deadList)):
            yield self.deadList[i]

    def remove_robot(self,robotid):
        try:
            for r in range(len(self.robotList)):
                if self.robotList[r].get_id() == robotid:
                    del self.robotList[r]
        except:
            pass

    def remove_transceiver(self,trid):
        try:
            for t in range(len(self.transceiverList)):
                if self.transceiverList[t].get_id() == trid:
                    del self.transceiverList[t]
        except:
            pass

    def progress_time(self):
        self.globalTime += 1
        for t in self.transceiverList:
            t.update_local_time(t.localtime + 1)
        for r in self.robotList:
            r.update_location()
        for transceiver in self.transceiverList:
            for robot in self.robotList:
                if transceiver.__eq__(robot):
                    robot.update_disconnect()
                if robot.get_disconnet_time() > 60:
                    self.kill_robot(robot)

    def __str__(self):
        return ("Number of transceivers: " + str(len(self.transceiverList)) +
                "\nNumber of robots (alive): " + str(len(self.robotList)) +
                "\nNumber of dead robots: " + str(len(self.deadList)))

    def create_report(self):
        report_string = "Time: "+str(self.globalTime) + "s\n"  
        report_string +=  self.__str__()+"\n"
        for t in self.transceiverList:
            report_string += t.__str__() +"\n"
        for r in self.robotList:
            report_string += r.__str__() +"\n"
        for d in self.deadList:
            report_string += d.__str__() +"\n"
        return report_string.rstrip()





