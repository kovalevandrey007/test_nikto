import subprocess

def check_command(cmd, text):
    result = subprocess.run ( cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    if text in out and result.returncode == 0:
        return True
    else:
        return False
