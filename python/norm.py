import numpy

class Normalization(OVBox):
   def __init__(self):
      OVBox.__init__(self)
      self.signalHeader = None
      self.min = None
      self.max = None

   def initialize(self):
      pass

   def uninitialize(self):
      pass

   def process(self):
      for chunkIndex in range( len(self.input[0]) ):
         if(type(self.input[0][chunkIndex]) == OVSignalHeader):
            self.signalHeader = self.input[0].pop()
            outputHeader = OVSignalHeader(
               self.signalHeader.startTime,
               self.signalHeader.endTime,
               self.signalHeader.dimensionSizes,
               [lavel + "_norm" for label in self.signalHeader.dimensionLabels],
               self.signalHeader.samplingRate)
            self.output[0].append(outputHeader)
         
         elif(type(self.input[0][chunkIndex]) == OVSignalBuffer):
            chunk = self.input[0].pop()
            numpyBuffer = numpy.array(chunk).reshape(tuple(self.signalHeader.dimensionSizes))
            chunkMax = numpyBuffer.max(axis=0)
            chunkMin = numpyBuffer.max(axis=0)

            if self.min is None or self.min > chunkMin:
               self.min = chunkMin

            if self.max is None or self.max < chunkMax:
               self.max = chunkMax

            minmax_range = (self.max - self.min) / 2
            numpyBuffer = (numpyBuffer - self.min) / minmax_range - 1
            chunk = OVSignalBuffer(chunk.startTime, chunk.endTime, numpyBuffer.tolist())
            self.output[0].append(chunk)
         elif(type(self.input[0][chunkIndex]) == OVSignalEnd):             
            self.output[0].append(self.input[0].pop())

box = Normalization()
