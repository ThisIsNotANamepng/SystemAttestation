FROM fedora:latest

# Copy the bash script into the container
COPY entrypoint.sh /entrypoint.sh

# Make the script executable
RUN chmod +x /entrypoint.sh

# Install awk for scripting
RUN dnf install -y awk

# Set the script as the entry point
ENTRYPOINT ["/entrypoint.sh"]
