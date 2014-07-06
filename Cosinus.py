import math
print """
--------------------------------
       Cosinus v1.3
--------------------------------
ACHTUNG: Punkt als Dezimaltrennung verwenden!
Modus auswaehlen:
[1] 2 Seiten und eingeschlossener Winkel [2] 3 Seiten
"""
modus = int(raw_input(""))
if modus == 1:
	einheit = raw_input("In welcher Einheit sind die Angaben?")
	a = float(raw_input("Laenge einer Seite: "))
	b = float(raw_input("Laenge anliegender Seite: "))
	gamma = math.radians(float(raw_input("Groesse des eingeschlossenen Winkels: ")))
	cosgamma = math.cos(gamma)
	# seg1 = 2 * a * b * cos(gamma)
	seg1 = 2 * a * b * cosgamma
	# c^2 = a^2 + b^2 - seg1
	cqdr = math.pow(a, 2) + math.pow(b, 2) - seg1
	c = math.sqrt(cqdr)
	print "Die dritte Seite ist %f%s lang." % (c, einheit)
	#print "DEBUG: a = %r; b = %r, gamma = %r, cosgamma = %r, seg1 = %r, cqdr = %r, c = %r" % (a, b, gamma, cosgamma, seg1, cqdr, c)
else:
	einheit = raw_input("In welcher Einheit sind die Angaben?")
	a = float(raw_input("Laenge Seite 1 (Schenkel vom gesuchten Winkel): "))
	b = float(raw_input("Laenge Seite 2 (Zweiter Schenkel vom gesuchten Winkel): "))
	c = float(raw_input("Laenge Seite 3 (liegt Winkel gegenuber): "))
	seg1 = math.pow(a, 2) - math.pow(b, 2) - math.pow(c, 2)
	seg2 = 2 * b * c * -1
	seg3 = seg1 / seg2
	gamma = math.degrees(math.acos(seg3))
	print "Der Winkel ist %f gross." % gamma