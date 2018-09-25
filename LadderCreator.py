import math
import calendar
import datetime
from dateutils import date
import subprocess
import io


date = datetime.date.today()
sn = (input("Substance/Medecine name:"))
snf = (f"{sn} Ladder.txt")
f = open((str(snf)), "w")

f.write(f"Substance/Medecine name: {sn}\n")
f.write("-" * 25)

f.write(f"\n\nLadder created: {date}")
cud = "Current Usage Dose (Daily): "  #Write the amount without weight units like mg or g
cudin = input(cud)
f.write(f"\n{cud}{cudin}")
dla = "Dosage Lowering Amount: "
dlain = input(dla)                    #Amount by which dose will be decreased each step
f.write(f"\n{dla}{dlain}")
dlp = "Dosage Lowering Period (Days): "
dlpin = input(dlp)                    #How much days between amount being decreased should pass
f.write(f"\n{dlp}{dlpin}\n\n")


print(f"Creating ladder for {sn}...")

while float(cudin) != 0:              #Until dosage = 0, keep incrementing data points
    cudin = float(cudin) - float(dlain)
    date = date + datetime.timedelta(days = int(dlpin))
    f.write("=" * 25)
    f.write(f"\nDate: {date}\n")
    f.write(f"Dosage: {cudin}\n")

f.close()
print(f"File \"{sn} Ladder\" created.")
