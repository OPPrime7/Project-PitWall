import pandas as pd
def get_heavy_braking():
    df = pd.read_csv("telemtry.csv")
    heavy_braking = df[df["Brake (%)"] >90]
    return heavy_braking 

def get_rapid_acceleration():
    df = pd.read_csv("telemtry.csv")
    rapid_acceleration = df[df["Throttle (%)"] >90]
    return rapid_acceleration

import matplotlib.pyplot as plt
plt.figure(figsize=(8,4))
heavy_braking = get_heavy_braking()
rapid_acceleration = get_rapid_acceleration()

df = pd.read_csv("telemtry.csv")
plt.subplot(2,1,1)
for i in range (len(df)-1):
    x = df["Turn Number"][i:i+2]
    y = df["Speed"][i:i+2]

    if df["Speed"][i+1]-df["Speed"][i]>= 150:
        plt.plot(x,y ,color = "blue")
    elif df["Speed"][i+1]-df["Speed"][i]>0:
        plt.plot(x,y, color = "green")
    else:
        plt.plot(x,y, color = "orange")
plt.title("Speed VS Turn Number")
plt.xlabel("Turn Number")
plt.ylabel("Speed (km/h)")
plt.grid(True)
plt.scatter(
    heavy_braking["Turn Number"],
    heavy_braking["Speed"],
    color = "red",
    label = "Heavy breaking"
)
plt.scatter(
    rapid_acceleration["Turn Number"],
    rapid_acceleration["Speed"],
    color = "blue",
    label = "Rapid Acceleration",
)

#lateralG_VS_Turn_Number
from telemtry_analysis import max_lateral_G
df = pd.read_csv("telemtry.csv")
plt.subplot(2,1,2)
plt.plot(df["Turn Number"], df["Lateral G"])
for i in range (len(df)-1):
    x = df["Turn Number"][i:i+2]
    y = df["Lateral G"][i:i+2]

    if df["Lateral G"][i+1] - df["Lateral G"][i]>1:
        plt.plot(x,y ,color = "orange")
    if df["Lateral G"][i+1] - df["Lateral G"][i]<-0.5:
        plt.plot(x,y ,color = "green")
plt.title("Lateral G VS Turn Number")
plt.xlabel("Turn Number")
plt.ylabel("Lateral G")
plt.grid(True)
plt.scatter(
    max_lateral_G["Turn Number"],
    max_lateral_G["Lateral G"],
    color = "red",
    label = "High Lateral G"
)
plt.tight_layout()
plt.show()