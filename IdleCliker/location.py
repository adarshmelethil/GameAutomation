from time import time as now

from pymouse import PyMouseEvent

class Mouse(PyMouseEvent):
	def __init__(self):
		PyMouseEvent.__init__(self)

	def move(self, x, y):
		pass

	def click(self, x, y, button, pressed):
		print("Click:", x, y)


if __name__ == "__main__":
	m = Mouse()
	try:
		m.run()
	except KeyboardInterrupt:
		exit(0)
