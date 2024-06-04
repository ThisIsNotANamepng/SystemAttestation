import os
import subprocess

def start_container(image_name, container_name, mounted_volume):
    # Command to start the Podman container
    command = ['podman', 'run', '--name', container_name, '-v', mounted_volume, '-d', image_name]
    subprocess.run(command, check=True)

def extract_information(container_name, command_to_extract_info, output_file):
    # Command to execute inside the container to extract information
    command = ['podman', 'exec', container_name, 'bash', '-c', command_to_extract_info]
    # Run the command and capture output to a file
    with open(output_file, 'w') as f:
        subprocess.run(command, stdout=f, check=True)

def stop_and_remove_container(container_name):
    # Command to stop and remove the Podman container
    subprocess.run(['podman', 'stop', container_name], check=True)
    subprocess.run(['podman', 'rm', container_name], check=True)

if __name__ == "__main__":
    # Define variables
    IMAGE_NAME = "your_podman_image"
    CONTAINER_NAME = "your_container_name"
    MOUNTED_VOLUME = "/path/to/host/directory:/path/to/container/directory"
    OUTPUT_FILE = "/path/to/output/file.txt"
    COMMAND_TO_EXTRACT_INFO = "your_command_to_extract_info"

    # Start the Podman container
    start_container(IMAGE_NAME, CONTAINER_NAME, MOUNTED_VOLUME)

    # Extract information from inside the container
    extract_information(CONTAINER_NAME, COMMAND_TO_EXTRACT_INFO, OUTPUT_FILE)

    # Stop and remove the container
    stop_and_remove_container(CONTAINER_NAME)
