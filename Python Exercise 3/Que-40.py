# 40. Consider a variable which has string value “Skyscend Business Solutions Pvt. Ltd.” print the following in one line.
# ◦ SKY
# ◦ SKYSCEND
# ◦ Bus
# ◦ solutions

x="Skyscend Business Solution Pvt.Ltd."

print(x.split()[0][0:3].upper() +"\n"+x.split()[0].upper()+"\n"+x.split()[1][0:3]+"\n"+x.split()[2].lower())
