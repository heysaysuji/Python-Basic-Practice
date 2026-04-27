# ---- A simple game that tests your ability to estimate 20 seconds accurately


import time

input("Press Enter and count 20 seconds")
start = time.time()


input("Press Enter after you finish counting 20 seconds")
end = time.time()



et = end - start  #By subtracting the start time from the end, you can calculate the time actualy taken
print("Actual time required :", et, "seconds")
print("Time Difference :", abs(et = 20), "seconds")
