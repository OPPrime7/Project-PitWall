import pandas as pd
D_A = pd.read_csv("driver_A.csv")
D_B = pd.read_csv("driver_B.csv")

print(f"""==============================================PROJECT PitWall v1.1=============================================
=================================================DRIVERS COMPARISION===============================================""")
for i in range (1,D_A["Turn Number"].max()+1):
    Driver_A = D_A.loc[D_A["Turn Number"]== i, "Minimum_Speed (km/h)"].iloc[0]
    Driver_B = D_B.loc[D_B["Turn Number"]== i, "Minimum_Speed (km/h)"].iloc[0]
    Gap = D_A.loc[D_A["Turn Number"]==i,"Turn_Time"].iloc[0] - D_B.loc[D_B["Turn Number"]==i,"Turn_Time"].iloc[0]
    print(f"""At Turn {i}
Driver A : {Driver_A}km/h
Driver B : {Driver_B}km/h
Gap : {Gap:+.2f}s""")
    if Gap > 0:
        print(f"Driver B has gained {abs(Gap):.2f} seconds\n")
    if Gap < 0:
        print(f"Driver A has gained {abs(Gap):.2f} seconds\n")