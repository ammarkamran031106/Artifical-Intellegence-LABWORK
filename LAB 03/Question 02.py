print("Smart Classroom Light Controller\n")

presence = ["No", "Yes", "Yes", "No", "No", "Yes", "Yes", "No"]
prevStud = "No"
prevLight = "OFF"
light = "OFF"

for s in range(8):
 stud = presence[s]
 if stud == "Yes" and light == "OFF": action = "Turning lights ON"; light = "ON"
 elif stud == "No" and light == "ON": action = "Turning lights OFF"; light = "OFF"
 else: action = "No action needed"
 print(f"Step {s+1}")
 print(f"Students Present: {stud}")
 print(f"Action Taken: {action}")
 print(f"Agent Memory → Previous Students: {prevStud}, Previous Light: {prevLight}")
 print("-"*45)
 prevStud = stud
 prevLight = light
