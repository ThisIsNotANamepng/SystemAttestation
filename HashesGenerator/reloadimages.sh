#cp entrypoint.sh Images/*/entrypoint.sh 

find Images -type d -exec cp entrypoint.sh {} \;
rm Images/entrypoint.sh

podman build --quiet -t attestation_alpine Images/Alpine/
podman build --quiet -t attestation_amazon Images/AmazonLinux/
podman build --quiet -t attestation_arch Images/Arch/
podman build --quiet -t attestation_debian Images/Debian/
podman build --quiet -t attestation_fedora Images/Fedora/
podman build --quiet -t attestation_oracle Images/OracleLinux/
podman build --quiet -t attestation_rocky Images/RockyLinux/
podman build --quiet -t attestation_ubuntu Images/Ubuntu/
