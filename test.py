from warnings import catch_warnings
import sys
import img
import math
__author__ = 'Valera'

f = open("2.csv", 'r')
i = 0
s = []
for line in f:
    s.append(line.replace(' ', '').replace('\0', '').split(','))
    i += 1
    print(s[i-1])
print(i)
f.close()
max = 0
min = 0
first = True
start = ''
end = s[len(s) - 1]
x = 0
y = 0
img.set_gradient(400)
del s[len(s) - 1]
for t in s:
    x = 0
    del t[len(t) - 1]
    print(len(t))
    del t[len(t) - 1]
    for rep in t:
        if first:
            print(type(rep))
            start = rep[0]
            del t[0]
            print(t[0])
            first = False
        rep.replace(' ', '')
        rep.strip('')

        try:
            # rep = float(rep)
            if rep != 'o':
                if max < float(rep):
                    max = float(rep)
                elif min > float(rep):
                    min = float(rep)
            else:
                print('>>> o = ' + rep)
            if float(rep) > 0:
                print('>>> \%s' % (rep))
                gp =  255 - img.get_gradient(float(rep))
                # img.set_pix(y, x, (gp, gp, gp)) # 255 white , polojitel
                img.set_pix_trouble(y,x, (gp, gp, gp))
                print(gp)
            else:
                # gp = 255 - img.get_gradient(math.fabs(float(rep)))
                # img.set_pix(y, x, (gp, gp, gp))
                img.set_pix_trouble(y,x, (0,0,0))
                # img.set_pix(y, x, (0, 0, 0)) # 0 - black , otricat
            x += 1
        except Exception:
            print(sys.exc_info())
            x += 1

    y += 1

img.show()
print('max =\%d min=\%d' % (max, min))
