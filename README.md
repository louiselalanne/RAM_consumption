# RAM consumption 🖥️

Create an application which will graphically depict the RAM consumption using a bar graph as per the system 6 applications running in background.

- pyplot is a matplotlib module. The function of this pyplot is to make changes in figures. Like it creates a plotting area to create a figure, plot lines, images, histograms etc with labels. So I've imported the pyplot module to use the bar charts to represent the data.

- psutil library, the psutil (process and system utilities), is a cross-platform library for retrieving the information on running processes and system utilization(cpu,memory,disks,networks,sensors) in python.

- psutil.process_iter() is basically an iterator that provides various information about the background applications like process id, process name, cpu_usage, memory_usage etc.
