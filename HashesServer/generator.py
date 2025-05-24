import subprocess
import sqlite3
import os

"""
systems = ["alpine", "amazon", "arch", "debian", "fedora", "oracle", "rocky", "ubuntu"]
package="grep"

for system in systems:
    command = "podman run attestation_"+system+":latest signature "+package
    subprocess.run((command).split()) 

"""

def new_package(system, package):
    # Makes new container and installs a package
    ## Change to podman exec

    ##Need to edit to make a new container for package

    print("Installing", package)
    if system == "amazon":
        command = ["podman", "exec", "-i", "attestation_amazon", "sh", "-c", f"dnf install -y {package}"]

    elif system == "arch":
        command = ["podman", "exec", "-i", "attestation_arch", "sh", "-c", f"pacman -Sy --noconfirm {package}"]
    
    elif system == "debian":
        command = ["podman", "exec", "-i", "attestation_debian", "sh", "-c", f"apt install -y {package}"]

    elif system == "fedora":
        command = ["podman", "exec", "-i", "attestation_fedora", "sh", "-c", f"dnf install -y {package}"]

    elif system == "oracle":
        command = ["podman", "exec", "-i", "attestation_oracle", "sh", "-c", f"yum install -y {package}"]

    elif system == "rocky":
        command = ["podman", "exec", "-i", "attestation_rocky", "sh", "-c", f"dnf install -y {package}"]

    elif system == "ubuntu":
        command = ["podman", "exec", "-i", "attestation_ubuntu", "sh", "-c", f"apt install -y {package}"]


    store_package(system, package, get_container_version(package, system), signature(system, package))

    result = subprocess.run((command), capture_output=True, text=True) 
    print(result)    

def signature(system, package):
    # Takes (package, os), and returns the hash and version

    command = "podman exec attestation_"+system+f" sha256sum /bin/{package}"

    result = subprocess.run((command).split(), capture_output=True, text=True) 
    print(result)

    return (result.stdout).split()[0]

def get_database_version(system, package):
    # Get the version of a package in the database
    command = "podman run attestation_"+system+":latest version "+package
    result = subprocess.run((command).split(), capture_output=True, text=True) 

    return (result.stdout).split()[0]

def get_latest_version(system, package):
    # Get the most updated version of a package
    print()

def store_package(system, package, version, hash):
    # Takes (package, system, version, hash) and stores it in the database

    conn = sqlite3.connect('../database.db')
    cursor = conn.cursor()

    data = (package, version, hash)
    cursor.execute('INSERT INTO '+system+' (package, version, hash) VALUES (?, ?, ?)', data)

    conn.commit()
    conn.close()

def get_container_version(package, system):
    # Gets the version of a $package from the container fleet

    if system == "amazon":
        command = ["podman", "exec", "-i", "attestation_amazon", "sh", "-c", f"dnf list installed {package} | awk 'NR==2 {{print $2}}'"]

    elif system == "arch":
        command = ["podman", "exec", "-i", "attestation_arch", "sh", "-c", f"pacman -Qi {package} | awk '/^Version/ {{print $3}}'"]
    
    elif system == "debian":
        command = ["podman", "exec", "-i", "attestation_debian", "sh", "-c", f"apt show {package} | grep -i '^Version:' | awk '{{print $2}}'"]

    elif system == "fedora":
        command = ["podman", "exec", "-i", "attestation_fedora", "sh", "-c", f"dnf list installed {package} | awk 'NR==2 {{print $2}}'"]

    elif system == "oracle":
        command = ["podman", "exec", "-i", "attestation_oracle", "sh", "-c", f"yum list installed {package} | awk 'NR==3 {{print $2}}'"]

    elif system == "rocky":
        command = ["podman", "exec", "-i", "attestation_rocky", "sh", "-c", f"dnf list installed {package} | awk 'NR==2 {{print $2}}'"]

    elif system == "ubuntu":
        command = ["podman", "exec", "-i", "attestation_ubuntu", "sh", "-c", f"apt show {package} | grep -i '^Version:' | awk '{{print $2}}'"]


    result = subprocess.run((command), capture_output=True, text=True)
    print(result)    

    return (result.stdout).split()[0]

def start_containers(systems):
    # We make containers with the ntrypoint for package stuff, they don't stsy running which makes us have to resart it eerytime we need to use it, this keeps them running
    # We also want to create new containers every time we want to scan a new package, so this will likely get deprecated later

    for system in systems:
        os.system("docker run -d --name attestation_"+system+" --entrypoint tail attestation_"+system+" -f /dev/null")

def package_safety(system, package):
    # Determines whether a user input string is a safe package to install

    return True

"""
systems = ["arch", "debian", "fedora", "oracle", "rocky", "ubuntu"]
package="sl"

for system in systems:
    hash = signature(package, system)
    version = get_container_version(package, system)

    print(system, ":", hash, version)

    store_package(package, system, version, hash)
"""