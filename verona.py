import sys
import win32ui
from win32com.client import Dispatch

v = (sys.getwindowsversion())

if v[3] == 0:
    win32ui.MessageBox('Attention, you are running Microsoft Windows 3.1. Please call CenturyABS at (512) 467-7188 for support or installation issues.', 'OS Version', 0),
elif v[3] == 1:
    win32ui.MessageBox('Attention, you are running Microsoft Windows 95/98 or Millenium Edition. Please call CenturyABS at (512) 467-7188 for support or installation issues.', 'OS Version', 0)
elif v[3] == 2:
    win32ui.MessageBox('Congratulations, you are running Microsoft Windows 2000 or XP', 'OS Version', 0)
else:
    win32ui.MessageBox('Attention, you are running Microsoft Windows Vista or some other unrecognized Operating System. Please call CenturyABS at (512) 467-7188 for support or installation issues.', 'OS Version', 0)


ie = Dispatch("InternetExplorer.Application")
ie.Visible = 1
ie.Navigate('https://vision21.txdot.gov/Login/Login.aspx')

abs = Dispatch("CenturyABS.Application")
abs.Visible = 1
