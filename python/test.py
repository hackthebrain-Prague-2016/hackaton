import numpy

class Tost(OVBox):
   def __init__(self):
      OVBox.__init__(self)
      self.signalHeader = None
      self.file = None

   def initialize(self):
      self.file = open("D:/Users/Stas/Documents/Projects/aeMindManipulus/BrainHack/gihub/data.log", "w")

   def uninitialize(self):
      self.file.close()

   def process(self):
      self.file.write("input: {}\n".format(len(self.input[0])))
      for chunkIndex in range( len(self.input[0]) ):
         # matrix
         if(type(self.input[0][chunkIndex]) == OVStreamedMatrixHeader):
            self.signalHeader = self.input[0].pop()
            self.file.write("matrix header: {}, {}, {}, {}\n".format(
               self.signalHeader.startTime,
               self.signalHeader.endTime,
               self.signalHeader.dimensionSizes,
               [lavel + "_norm" for label in self.signalHeader.dimensionLabels]))
         elif(type(self.input[0][chunkIndex]) == OVStreamedMatrixBuffer):
            chunk = self.input[0].pop()
            numpyBuffer = numpy.array(chunk).reshape(tuple(self.signalHeader.dimensionSizes))
            self.file.write("matrix buffer: {}\n".format(numpyBuffer))
         elif(type(self.input[0][chunkIndex]) == OVStreamedMatrixEnd):
            self.file.write("matrix end\n")
            self.input[0].pop()
         # signal
         elif(type(self.input[0][chunkIndex]) == OVSignalHeader):
            self.signalHeader = self.input[0].pop()
            self.file.write("signal header: {}, {}, {}, {}, {}\n".format(
               self.signalHeader.startTime,
               self.signalHeader.endTime,
               self.signalHeader.dimensionSizes,
               [lavel + "_norm" for label in self.signalHeader.dimensionLabels],
               self.signalHeader.samplingRate))
         elif(type(self.input[0][chunkIndex]) == OVSignalBuffer):
            chunk = self.input[0].pop()
            numpyBuffer = numpy.array(chunk).reshape(tuple(self.signalHeader.dimensionSizes))
            self.file.write("signal buffer: {}\n".format(numpyBuffer))
         elif(type(self.input[0][chunkIndex]) == OVSignalEnd):
            self.file.write("signal end\n")
            self.input[0].pop()
         # simulation   
         elif(type(self.input[0][chunkIndex]) == OVStimulationHeader):
            self.signalHeader = self.input[0].pop()
            self.file.write("simulation header\n")
         elif(type(self.input[0][chunkIndex]) == OVStimulationSet):
            chunk = self.input[0].pop()
            numpyBuffer = numpy.array(chunk).reshape(tuple(self.signalHeader.dimensionSizes))
            self.file.write("simulation set: {}\n".format(numpyBuffer))
         elif(type(self.input[0][chunkIndex]) == OVStimulationEnd):
            self.file.write("simulation end\n")
            self.input[0].pop()

box = Tost()
