import subprocess
import sys

p = subprocess.Popen(sys.argv[1:], shell=True, stdout = subprocess.PIPE)
stdout, stderr = p.communicate()

if p.returncode != 0: # 0 is success
    print("Execution failed: " + sys.argv[1:])
    print("Returned error code " + p.returncode)
    sys.exit(p.returncode)

sys.exit(0)
