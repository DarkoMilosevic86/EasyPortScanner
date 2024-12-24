import os

script = "EasyPortScanner.pyw"
icon = "port_scanner_icon.ico"
version_file = "version.txt"
output_dir = "dist"

pyinstaller_command = (
    f"pyinstaller --noconsole --icon={icon} --version-file={version_file} {script}"
)

def build_scanner(target, source, env):
    print("Building scanner with PyInstaller...")
    if os.system(pyinstaller_command) != 0:
        raise RuntimeError("PyInstaller build failed.")

Command(output_dir, script, build_scanner)
