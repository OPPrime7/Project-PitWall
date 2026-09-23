import pandas as pd
df = pd.read_csv("telemtry.csv")

#defining_function
heavy_braking =  df[df["Brake (%)"]>90]
rapid_acceleration = df[df["Throttle (%)"]>=100]
max_lateral_G = df[df["Lateral G"]>1.1]
max_speed_row = df.loc[df["Speed"].idxmax()]
min_speed_row = df.loc[df["Speed"].idxmin()]
max_LateralG_row = df.loc[df["Lateral G"].idxmax()]
max_steering_angle = df.loc[df["Steering Angle"].idxmax()]

#printing
print(f"""==============================================PROJECT PitWall v1.0=============================================
=================================================SESSION SUMMARY===============================================
      \n
      Maximum Speed in this lap {int(max_speed_row["Speed"])} km/h at ending of turn {int(max_speed_row["Turn Number"])}
      Minimum Speed in this lap {int(min_speed_row["Speed"])} km/h at starting of turn {int(min_speed_row["Turn Number"])}
      Max Lateral G reading {(max_LateralG_row["Lateral G"])} G at turn {int(max_LateralG_row["Turn Number"])} 
      Average Speed this lap : {int(df["Speed"].mean())} km/h
      Maximun Steering Angle {df["Steering Angle"].max()}° at Lap {int(max_steering_angle["Turn Number"])}""")
print("\n")
#HEAVY_BRAKING_DETECTION
print("===========================Heavy Braking at==============================")
for i in heavy_braking["Turn Number"]:
      print(f"""Turn""",i)

#RAPID_ACCELERATION_DETECTION
print("===========================Rapid Acceleration at===============================")
for i in rapid_acceleration["Turn Number"]:
      print(f"""Turn""",i)

#HIGHEST_LATERAL_G_DETECTION
print("===========================High Lateral G observed at==========================")
for i in max_lateral_G["Turn Number"]:
      print(f"""Turn""",i)
