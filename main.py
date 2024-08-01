import gen
import sys

dates = []
times = []
seats = [chr(ord('A') + i) for i in range(6 if len(sys.argv) < 3 else int(sys.argv[2]))]
if len(sys.argv) < 2:
    secret = ""
    print("Empty Secrets")
else:
    secret = sys.argv[1]
    print(f"Secret: {secret}")

# Read dates and times
with open("dates.txt", "r") as f:
    for line in f.readlines():
        dates.append(line.replace("\n", ""))
with open("times.txt", "r") as f:
    for line in f.readlines():
        times.append(line.replace("\n", ""))

# Generate and Save
history = {}
with open("result.csv", "w") as f:
    f.write(f"date,time,seat,code\n")
    for date in dates:
        for time in times:
            for s in seats:
                code = gen.generate_serial_code(date, time, s, secret)
                if code in history.keys():
                    print(f"Duplicate code: {code}")
                history[code] = True
                f.write(f"{date},{time},{s},{code}\n")
