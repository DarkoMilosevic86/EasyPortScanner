# EasyPortScanner
Easy Port Scanner is a simple, open source tool for scanning ports on a network using an IP address, and shows the open ports in the list.
# Features
* Scans all ports in range,
* Including Stop scan,
* Shows scan results in the list
# Installing EasyPortScanner
To install Easy Port Scanner, you can download .zip archive from the [https://github.com/DarkoMilosevic86/EasyPortScanner/releases](https://github.com/DarkoMilosevic86/EasyPortScanner/releases) page.
# Building EasyPortScanner from source
To build Easy Port Scanner, you need the following:
* Python3 32 or 64,
* PIP3,
* wxPython,
* pyinstaller,
* scons
Please clone Easy Port Scanner repository using the following command:
```cmd
git clone https://github.com/DarkoMilosevic86/EasyPortScanner.git
```
Go to the EasyPortScanner folder and then install necessary packages from the requirements.txt
```cmd
pip install -r requirements.txt
```
Then run scons to build Easy Port Scanner:
```cmd
scons
```
The Easy Port Scanner build will be placed in dist folder
