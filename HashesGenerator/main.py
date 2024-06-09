import subprocess

"""
systems = ["alpine", "amazon", "arch", "debian", "fedora", "oracle", "rocky", "ubuntu"]
package="grep"

for system in systems:
    command = "podman run attestation_"+system+":latest signature "+package
    subprocess.run((command).split()) 


I'm going to deprecate the install function because I don't think allowing users to arbritrarily install a package, even from the repo is a good idea. There will be a form or something to request new packages

def install(package, system):
    command = "podman run attestation_"+system+":latest install "+package
    result = subprocess.run((command).split(), capture_output=True, text=True) 
    print("Result from bash script:", result.stdout)    

    
I'm going to deprecate the uphrade function in favor of a cron job or something which upgrades the whole system every 15 minutes or something. Few users would be more up to date than that.

def upgrade(package, system):
    command = "podman run attestation_"+system+":latest upgrade "+package
    result = subprocess.run((command).split(), capture_output=True, text=True) 
    print("Result from bash script:", result.stdout)    

"""

def signature(package, system):
    command = "podman run attestation_"+system+":latest signature "+package
    result = subprocess.run((command).split(), capture_output=True, text=True) 
    return (result.stdout).split()[0]

def version(package, system):
    command = "podman run attestation_"+system+":latest version "+package
    result = subprocess.run((command).split(), capture_output=True, text=True) 
    return (result.stdout).split()[0]


systems = ["amazon", "arch", "debian", "fedora", "oracle", "rocky", "ubuntu"]
package="grep"

for system in systems:
    print(system, ":", signature("grep", system), version("grep", system))
