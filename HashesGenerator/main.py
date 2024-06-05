import subprocess

systems = ["alpine", "amazon", "arch", "debian", "fedora", "oracle", "rocky", "ubuntu"]
package="grep"

for system in systems:
    command = "podman run attestation_"+system+":latest signature "+package
    subprocess.run((command).split()) 
