import matplotlib.pyplot as plt
from drivers_comparision import D_A
from drivers_comparision import D_B

Gaps = []
Turns = []
Times_A = []
Times_B = []
for i in range (1,D_A["Turn Number"].max()+1):
    Gap = D_A.loc[D_A["Turn Number"]==i, "Turn_Time"].iloc[0] - D_B.loc[D_B["Turn Number"]==i, "Turn_Time"].iloc[0]
    times_a = D_A.loc[D_A["Turn Number"]==i, "Turn_Time"].iloc[0]
    times_b = D_B.loc[D_B["Turn Number"]==i, "Turn_Time"].iloc[0]
    Gaps.append(Gap)
    Turns.append(i)
    Times_A.append(times_a)
    Times_B.append(times_b)

plt.bar(Turns, Gaps, color=["red" if Gap > 0 else "blue" for Gap in Gaps])
plt.axhline(0, linestyle="--")
plt.xlabel("Turn Number")
plt.ylabel("Time Loss (s)")
plt.title("Time Loss by Turn")
plt.xticks(Turns)
plt.grid(True)
plt.show()

turns = D_A["Turn Number"]
driver_A_time = D_A["Turn_Time"]
driver_B_time = D_B["Turn_Time"]
x = np.arange (len(turns))
width = 0.35
plt.figure(figsize=(10,5))
plt.bar(
    x - width / 2,
    driver_A_time,
    width,
    label = "Driver A",
    color = "Red"
)
plt.bar(
    x + width / 2,
    driver_B_time,
    width,
    label = "Driver B",
    color = "Blue"
)
plt.xticks(x, turns)
plt.xlabel("Turn Number")
plt.ylabel("Turn Time (In Seconds)")
plt.title("Indivisual Turn VS Time")
plt.legend()
plt.grid(axis="y", alpha = 0.3)
plt.tight_layout()
plt.show()
