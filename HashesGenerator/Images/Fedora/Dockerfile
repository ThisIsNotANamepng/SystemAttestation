FROM fedora:latest

# Copy the bash script into the container
#COPY /home/jack/code/SystemAttestation/HashesGenerator/entrypoint.sh /entrypoint.sh
COPY entrypoint.sh /entrypoint.sh

# Make the script executable
RUN chmod +x /entrypoint.sh

# Set the script as the entry point
ENTRYPOINT ["/entrypoint.sh"]
