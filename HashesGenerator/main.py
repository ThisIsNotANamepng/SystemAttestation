import subprocess

system="ubuntu"
package="grep"

command = "podman run attestation_"+system+":latest signature "+package

print((command).split())

subprocess.run((command).split()) 
