# System Attestation 

__This project is nowhere near finished, it is not production ready, check back later__

This tool is created to check the integrity of system files on Linux systems. It works by getting the sha256 hash of an installed binary on a fresh, safe podman container, and then serving the verified hash of the built binary to the client, which compares it to the hash of installed binary on the client system. It consists of three components. 

### Hashes Generator

The main part of the system. It manages the containers. It should only have to be run sporadically, only when a package is updated or a new package is requested

### Hashes Server

This example has an arbitrary implementation, its just a basic way to retrieve the signatures from the generator.

Should probably handle some of the security stuff. Maybe it could have a database with all of the avalable programs, and if the submitted program isn't in the database then it stops.

Determining the newest version of the package is the server's responsibility

### Client

Retrieves the signatures for all binaries on the client system


## Other

We have to keep in mind that different OSs/Architectures and different versions of the binary generate different hashes. Also, the DNF package manager doesn't keep old versions of packages. This means that we have to create images for every kind of operating system and architecture we want. Also, we'll have to keep a record of old versions of packages, when a new version of the package is released it has to create a new entry for the new version (if you use dnf, you can specify relsease-version=29 to get old versions of packages). Since these hashes will be used in the future, they should probably be signed with a system pgp key. 

## TODO

    - Alpine doesn't include bash by default, entrypoint won't work
    - I also want a dashboard for seeing where the package versions for the fleet of images are at, and to manage how the server is doing, the amount of packages upgraded recently, etc.