
import simple_draw as sd



shift = 50

for x in range(6):
        lb = sd.get_point(0+x, 0)
        rb = sd.get_point(100+x, 50)
        sd.rectangle(lb, rb, color=sd.COLOR_YELLOW, width=2)

sd.pause()