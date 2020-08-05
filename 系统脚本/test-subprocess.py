import subprocess

popen = subprocess.Popen("ls /root;ls /",shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

out = popen.stdout.read()
err = popen.stderr.read()
print("out:",out.decode("utf-8"))
print("err:",err.decode("utf-8"))
