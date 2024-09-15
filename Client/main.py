"""
System attestation client
"""

import subprocess
import os

def get_sha256_hash(input_string):
    # Define the file path
    file_path = f"/bin/{input_string}"

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return None

    # Compute the SHA-256 hash using sha256sum
    try:
        result = subprocess.run(['sha256sum', file_path], capture_output=True, text=True, check=True)
        hash_value = result.stdout.split()[0]  # The hash is the first part of the output
        return hash_value
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running sha256sum: {e}")
        return None

def get_server_hash(name, version, architecture):
    print("Retrieves the server's hash of the given binary and version")

files = os.listdir("/bin")
for file_name in files:
    file_path = os.path.join("/bin", file_name)
    if os.path.isfile(file_path):  # Ensure it's a file, not a directory
        hash_value = get_sha256_hash(file_name)
        if hash_value:
            print(f"{file_path}: {hash_value}")
        else:
            print(f"Failed to compute hash for {file_path}")

