# -----------------------------------------------------------------------------
# Easy Port Scanner
# Copyright (C) 2024 Darko Milosevic <daremc86@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
# -----------------------------------------------------------------------------

import wx
import threading
import socket

class PortScannerApp(wx.Dialog):
    def __init__(self):
        super().__init__(None, title="Easy Port Scanner V1.0", size=(400, 300))
        self.panel = wx.Panel(self)

        # Controls
        wx.StaticText(self.panel, label="IP Address:", pos=(10, 10))
        self.ip_text = wx.TextCtrl(self.panel, pos=(100, 10), size=(200, -1))
        
        self.scan_button = wx.Button(self.panel, label="Scan", pos=(10, 50))
        self.stop_button = wx.Button(self.panel, label="Stop Scan", pos=(100, 50))
        self.stop_button.Disable()

        wx.StaticText(self.panel, label="Scan results:", pos=(10, 10))
        self.result_list = wx.ListBox(self.panel, pos=(100, 10), size=(360, 150))
        
        # Events
        self.scan_button.Bind(wx.EVT_BUTTON, self.start_scan)
        self.stop_button.Bind(wx.EVT_BUTTON, self.stop_scan)

        # Properties
        self.scanning = False
        self.thread = None

        self.Show()

    def start_scan(self, event):
        ip_address = self.ip_text.GetValue().strip()
        if not ip_address:
            wx.MessageBox("Please enter a valid IP address.", "Error", wx.OK | wx.ICON_ERROR)
            return

        self.result_list.Clear()
        self.scanning = True
        self.scan_button.Disable()
        self.ip_text.Disable()
        self.stop_button.Enable()

        # Startingg scan in another thread
        self.thread = threading.Thread(target=self.scan_ports, args=(ip_address,))
        self.thread.start()

    def stop_scan(self, event):
        self.scanning = False
        self.scan_button.Enable()
        self.stop_button.Disable()
        self.ip_text.Enable()
        if self.thread and self.thread.is_alive():
            self.thread.join()

    def scan_ports(self, ip):
        for port in range(1, 65536):  # Scannning all ports
            if not self.scanning:
                break

            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(0.5)
                    if s.connect_ex((ip, port)) == 0:
                        wx.CallAfter(self.result_list.Append, f"Port {port} is open")
            except Exception as e:
                pass

        wx.CallAfter(self.scan_complete)

    def scan_complete(self):
        self.scanning = False
        self.scan_button.Enable()
        self.stop_button.Disable()
        self.ip_text.Enable()

if __name__ == "__main__":
    app = wx.App()
    PortScannerApp()
    app.MainLoop()
