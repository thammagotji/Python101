import math

class Buffer:
    # attribute
    detail = 'Class Buffer can be utilized to calculate the concentration of acid and its conjugate base by following this form: Buffer(name,pKa,pH,concentration).'

    # constructor
    def __init__(self,name='Phosphate Buffer',pKa=6.86,pH=7,conc=0.5):
        self.buffername = name      # buffer name
        self.pKa = pKa              # acid dissociation constant (pKa)
        self.pH = pH                # pH
        self.conc = conc            # concentration of buffer

    # method
    def help(self):
        print(self.detail)

    def name(self):
        print(f'Buffer name: {self.buffername}')

    def prep(self):
        temp = pow(10, self.pH-self.pKa)    # temp = [A-]/[HA]
        A = (temp*self.conc)/(temp+1)       # A = concentration of conjugate base
        HA = self.conc-A                    # HA = concentration of acid
        print('Concentration of conjugate base: '+ str(A) +' Molar')
        print('Concentration of acid: '+ str(HA) +' Molar')

class Dilute(Buffer):
    # attribute
    detail = 'Class Dilute can be used to determine the volume of a diluted solution by following this form: Dilute(concentration1,concentration2,volume1)'

    # constructor
    def __init__(self,conc,conc2,vol1):
        super().__init__(conc)
        self.conc1 = conc
        self.conc2 = conc2
        self.vol = vol1
    
    # method
    def help(self):
        print(self.detail)

    def dilutionFactor(self):
        dfactor = self.conc2/self.conc1
        print('Dilution Factor: ' + str(dfactor))

    def volume(self):
        vol1 = (self.conc2*self.vol)/self.conc1
        print('Volume of sample: '+ str(vol1) +' mL')
        print('Volume of water required: '+ str(self.vol-vol1) +' mL')
        

# instance
print('============================================================================================================================================')
buffer1 = Buffer()
buffer1.help()
buffer1.name()
buffer1.prep()
print('============================================================================================================================================')
buffer1 = Buffer('Acetic Buffer',4.8,4,0.5)
buffer1.name()
buffer1.prep()
print('============================================================================================================================================')
diluted = Dilute(0.5,0.05,100)
diluted.help()
diluted.dilutionFactor()
diluted.volume()