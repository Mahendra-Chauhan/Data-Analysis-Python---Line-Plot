### LINE PLOT ##
import matplotlib.pyplot as plt
from matplotlib import style

days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
ahmedabad_temperature = [30,30.5,40,40.7,41,42,48,49.5,38,24,23,47,48,98,54]
style.use("ggplot")
plt.plot(days,ahmedabad_temperature, color="g", marker="o", markersize="10", linestyle="--", linewidth=2, label="Templine" )
plt.axis([0,16,10,100])
plt.title("Ahmedabad_Random Temperature",fontsize=16)
plt.xlabel("days", fontsize=13)
plt.ylabel("temperature",fontsize=13)
plt.legend(loc=2)
plt.grid(color="r", linestyle="-", linewidth="2")
plt.show()

## Now adding 2 mumbai temperature and add 2 graphs together.

days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
ahmedabad_temperature = [30,30.5,40,40.7,41,42,48,49.5,38,24,23,47,48,50,54]
mumbai_temperature = [25,40,30,45,43,41,38,35,37,42,25,20,28,33,37]
style.use("ggplot")
plt.plot(days,ahmedabad_temperature, color="g", marker="o", markersize="10", linestyle="--", linewidth=2, label="Ahmedabadtempline" )
plt.plot(days,mumbai_temperature, color="b", marker="o", markersize="10", linewidth=2, label="Mumabitempline" )
plt.axis([0,16,10,60])
plt.title("Ahmedabad_Mumabi - Temperature",fontsize=16)
plt.xlabel("days", fontsize=13)
plt.ylabel("temperature",fontsize=13)
plt.legend(loc=2)
plt.grid(color="r", linestyle="-", linewidth="2")
plt.show()



