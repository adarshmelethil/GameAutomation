import sys
from time import sleep
from pymouse import PyMouse, PyMouseEvent

stop = False

class Mouse(PyMouseEvent):
  def __init__(self):
    PyMouseEvent.__init__(self)

  def move(self, x, y):
    global stop
    stop = True


if __name__ == "__main__":
  x, y, n, d = float(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4])

  m = PyMouse()
  mm = Mouse()
  mm.start()
  for _ in range(n):
    m.click(x, y)
    sleep(d)
    if stop:
      break
  