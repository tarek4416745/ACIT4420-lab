import wmi
from reportlab.pdfgen import canvas
f = wmi.WMI()
c = canvas.Canvas("process.pdf")
height = 350
for process in f.Win32_Process():
    print(f"{process.ProcessId:<10} {process.Name}")
    c.drawString(100, height, f"{process.ProcessId:<10} {process.Name}")
    height = height + 20
c.save()


