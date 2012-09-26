from joints import Joints
class FluentLegs():

    # init method
    def __init__(self, nao, feet):
        
        self.feet = feet

        # jobs for threading
        self.nao = nao
        self.joints = nao.joints
        self.chains = nao.chains
        self.log = nao.log

    def go(self):
        self.nao.go()
        
    ###################################
    # Balance
    ###################################
    def balanceOnLeft(self, duration=0):
        self.nao.balance(self.joints.SupportLeg.LLeg, duration)
        return self;

    def balanceOnRight(self, duration=0):
        self.nao.balance(self.joints.SupportLeg.RLeg, duration)
        return self;

    def balanceCenter(self, duration=0):
        self.nao.balance(self.joints.SupportLeg.Legs, duration)
        return self;


    ###################################
    # Out
    ###################################
    def lOut(self, duration=0, offset=0):

        # move leg out
        duration = self.nao.determineDuration(duration)       
        angle = 35 + offset
        self.nao.moveWithDegreesAndDuration(self.joints.LLeg.LHipRoll, angle, duration)

        # turn feet in
        self.feet.lTurnIn()
        self.feet.rTurnIn(0, -15)

        return self;

    def rOut(self, duration=0, offset=0):

        # move leg out
        duration = self.nao.determineDuration(duration)       
        angle = -35 - offset
        self.nao.moveWithDegreesAndDuration(self.joints.RLeg.RHipRoll, angle, duration)

        # turn feet in
        self.feet.rTurnIn()
        self.feet.lTurnIn(0, -15)

        return self;

    ###################################
    # Forward
    ###################################
    def lForward(self, duration=0, offset=0):

        # stiffen body & enable wb
        self.nao.stiff()
        self.nao.wbEndable()

        # constrain feet
        self.nao.footState(self.joints.SupportLeg.RLeg, self.joints.StateName.Fixed)
        self.nao.footState(self.joints.SupportLeg.LLeg, self.joints.StateName.Plane)

        # move leg forward
        duration = self.nao.determineDuration(duration)       
        angle = -90 - offset
        self.nao.moveWithDegreesAndDuration(self.joints.LLeg.LHipPitch, angle, duration)

        # block call
        self.go()

        # free feet & disable wb
        self.nao.footState(self.joints.SupportLeg.Legs, self.joints.StateName.Free)
        self.nao.wbDisable()

        return self;


    def rForward(self, duration=0, offset=0):

        # stiffen body & enable wb
        self.nao.stiff()
        self.nao.wbEndable()

        # constrain feet
        self.nao.footState(self.joints.SupportLeg.LLeg, self.joints.StateName.Fixed)
        self.nao.footState(self.joints.SupportLeg.RLeg, self.joints.StateName.Plane)

        # move leg forward
        duration = self.nao.determineDuration(duration)       
        angle = -90 - offset
        self.nao.moveWithDegreesAndDuration(self.joints.RLeg.RHipPitch, angle, duration)

        # block call
        self.go()

        # free feet & disable wb
        self.nao.footState(self.joints.SupportLeg.Legs, self.joints.StateName.Free)
        self.nao.wbDisable()
        
        return self;

    ###################################
    # Up
    ###################################
    def up(self, duration=0, offset=0):   
        self.rForward(duration, offset)
        self.lForward(duration, offset)
        return self;

    def lUp(self, duration=0, offset=0):
        self.balanceOnRight(duration)
        duration = self.nao.determineDuration(duration)       
        angle = -90 - offset
        self.nao.moveWithDegreesAndDuration(self.joints.LLeg.LHipPitch, angle, duration)
        return self;
        
    def rUp(self, duration=0, offset=0):
        self.balanceOnLeft(duration)
        duration = self.nao.determineDuration(duration)  
        angle = -90 - offset
        self.nao.moveWithDegreesAndDuration(self.joints.RLeg.RHipPitch, angle, duration)
        return self;


    ###################################
    # KneeUp
    ###################################
    def lKneeUp(self, duration=0, offset=0):
        self.balanceOnRight(duration)
        self.lUp(duration, offset)
        self.lKneeBent(duration, offset)
        return self;
        
    def rKneeUp(self, duration=0, offset=0):
        self.balanceOnLeft(duration)
        self.rUp(duration, offset)
        self.rKneeBent(duration, offset)
        return self;

    ###################################
    # Down
    ###################################
    def down(self, duration=0, offset=0):   
        self.rDown(duration, offset)
        self.lDown(duration, offset)
        return self;

    def lDown(self, duration=0, offset=0):
        self.balanceOnLeft(duration)
        duration = self.nao.determineDuration(duration)       
        angle = 0 + offset
        self.nao.moveWithDegreesAndDuration(self.joints.LLeg.LHipPitch, angle, duration)
        return self;
        
    def rDown(self, duration=0, offset=0):
        duration = self.nao.determineDuration(duration)  
        angle = 0 + offset
        self.nao.moveWithDegreesAndDuration(self.joints.RLeg.RHipPitch, angle, duration)
        return self;


    ###################################
    # Bent
    ###################################
    def kneesBent(self, duration=0, offset=0):   
        self.rKneeBent(duration, offset)
        self.lKneeBent(duration, offset)
        return self;

    def lKneeBent(self, duration=0, offset=0):
        duration = self.nao.determineDuration(duration)       
        angle = 90 + offset
        self.nao.moveWithDegreesAndDuration(self.joints.LLeg.LKneePitch, angle, duration)
        return self;
        
    def rKneeBent(self, duration=0, offset=0):
        duration = self.nao.determineDuration(duration)  
        angle = 90 + offset
        self.nao.moveWithDegreesAndDuration(self.joints.RLeg.RKneePitch, angle, duration)
        return self;


    ###################################
    # Straight
    ###################################
    def straight(self, duration=0, offset=0):   
        self.rStraight(duration, offset)
        self.lStraight(duration, offset)
        return self;

    def lStraight(self, duration=0, offset=0):
        duration = self.nao.determineDuration(duration) 
        angle = 0 - offset      
        self.nao.moveWithDegreesAndDuration(self.joints.LLeg.LKneePitch, angle, duration)
        return self;
        
    def rStraight(self, duration=0, offset=0):
        duration = self.nao.determineDuration(duration)  
        angle = 0 - offset
        self.nao.moveWithDegreesAndDuration(self.joints.RLeg.RKneePitch, angle, duration)
        return self;

