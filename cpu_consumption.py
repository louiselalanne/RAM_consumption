import matplotlib .pyplot as plt
import psutil as p

app_list = []
app_percentage = []
count = 0

for process in p.process_iter():
    count = count +1
    if count <= 6:
        name = process.name()
        cpu_usage = p.cpu_percent()
        print("name: ", name, ' - cpu usage: ', cpu_usage)
        app_list.append(name)
        app_percentage.append(cpu_usage)

plt.figure(figsize=(15,7))
plt.xlabel("Application")
plt.ylabel("Usage")
plt.bar(app_list, app_percentage, width=0.6, color=("pink", "purple", "blue", "red", "green", "orange"))
plt.show()