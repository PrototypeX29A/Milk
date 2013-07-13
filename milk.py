import pprint
import os
import hashlib

def sha256(s):
  h = hashlib.sha256((s)).digest()[0:8]
  return  h.encode("hex")
  

class MilkDrop:

  def play(self):
    self.spill()
    os.system('play %s' % self.filename())


class SoxDrop(MilkDrop):

  def __init__(self, indrops, effect):
    self.indrops = indrops
    self.effect = effect 
    self._filename = None

  def filename(self):
    if self._filename == None: 
      pprint.pprint(self.indrops)
      self._filename =  sha256("soxdrop%s%s" % (self.effect, "".join(map(lambda x: x.filename(), self.indrops))))
    return self._filename+'.wav'
    
  def spill(self, filename = None):
    if filename == None:
      filename = self.filename()
    if os.path.exists(filename):
      return
    for drop in self.indrops:
      drop.spill()
    infiles =  " ".join(map(lambda x: x.filename(), self.indrops))
    os.system('sox %s %s %s' % (infiles, filename, self.effect)) 
    print('sox %s %s %s\n' % (infiles, filename, self.effect)) 
    
class FileDrop(MilkDrop):
  
  def __init__(self, filename):
    self._filename = filename

  def filename(self):
    return self._filename

  def spill(self):
    pass
