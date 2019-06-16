import subprocess

p = subprocess.Popen(['netstat', '-tulnp', '|', 'grep', ':4200']);

for item in p.split('\n'):
    print(item)
print(p.split('\n'))