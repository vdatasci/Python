#Source: http://pingfive.typepad.com/blog/2010/02/calculating-arc-length.html

import math, sys

class Arc(object):
    def __init__(self, chord, height):
        self.chord = float(chord)
        self.height = float(height)

    def _asin(self, leg, hypotenuse, degrees = True):
        radians = math.asin(leg/hypotenuse)
        if not degrees:
            return radians
        return math.degrees(radians)

    def _radius(self):
        return self.chord ** 2 / (8 * self.height) + self.height / 2

    def _circumference(self):
        return 2 * math.pi * self.radius

    def _angle(self):
        return 2 * self._asin(self.chord / 2, self.radius)

    def getLength(self):
        self.radius = self._radius()
        return self._angle() * self._circumference() / 360 

if __name__ == '__main__':
        arc = Arc(100, 10)
        print 'The arc length is %.1f' % arc.getLength()
