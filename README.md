# System Attestation

__This project is nowhere near finished, it is not production ready,__

This is a research project which aims to showcase a supply chain security technique. It's targeted for Linux machines, from HPC supercomputers to embedded devices.

This tool is designed to verify the integrity of system files on Linux systems. It operates by first calculating the SHA-256 hash of an installed binary within a clean, secure Podman container. It then provides the verified hash of this binary to the client. The client compares this hash to the hash of the installed binary on their own system. The tool comprises three main components.

## Components

### Generator

The main part of the system. It manages the containers on the server. It should only have to be run sporadically, only when a package is updated or a new package is requested

### Server

This example has an arbitrary implementation, its just a basic way to retrieve the signatures from the generator.

Should probably handle some of the security stuff. Maybe it could have a database with all of the available programs, and if the submitted program isn't in the database then it stops.

Determining the newest version of the package is the server's responsibility.

### Client

Retrieves the signatures for the binaries on a client system and compares them to the ones on the server.

## Other

We have to keep in mind that different OSs/Architectures and different versions of the binary generate different hashes. Also, the DNF package manager doesn't keep old versions of packages. This means that we have to create images for every kind of operating system and architecture we want. Also, we'll have to keep a record of old versions of packages, when a new version of the package is released it has to create a new entry for the new version (if you use dnf, you can specify release-version=29 to get old versions of packages). Since these hashes will be used in the future, they should probably be signed with a system pgp key.

## TODO

    - Alpine doesn't include bash by default, entrypoint won't work
    - I also want a dashboard for seeing where the package versions for the fleet of images are at, and to manage how the server is doing, the amount of packages upgraded recently, etc.
    - Add a cron job for the images to upgrade packages every 15 minutes or something
