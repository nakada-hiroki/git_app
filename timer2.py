class Stopwatch:
  def _init__(self):
    self.running = False
    self.time_start = 0
    self.time_elapsed = 0

  def start(self):
    if not self.running:
      self.running = True
      self.time_start = time.perf_counter() 
