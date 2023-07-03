import subprocess
import sys


# Функция для отправки команды в cmd и вывод результата
def run(cmd: str) -> str:
    try:
        return subprocess.run(cmd, shell=True, capture_output=True, check=True, encoding="utf-8").stdout.strip()
    except:
        return None


# Возвращает уникальный id устройства
def device_id() -> str:
    # вызовы run для определенных ос; получение id
    if sys.platform == 'darwin':
        return run("ioreg -d2 -c IOPlatformExpertDevice | awk -F\\\" '/IOPlatformUUID/{print $(NF-1)}'",)

    elif sys.platform == 'win32' or sys.platform == 'cygwin' or sys.platform == 'msys':
        return run('wmic csproduct get uuid').split('\n')[2].strip()

    elif sys.platform.startswith('linux'):
        return run('cat /var/lib/dbus/machine-id') or run('cat /etc/machine-id')

    elif sys.platform.startswith('openbsd') or sys.platform.startswith('freebsd'):
        return run('cat /etc/hostid') or run('kenv -q smbios.system.uuid')
# <<wmic bios get serialnumber>>. Порядковый номер BIOS машины.
