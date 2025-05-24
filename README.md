# System Attestation

__This project is nowhere near finished, it is not production ready,__

This is a research project which aims to showcase a supply chain security technique. It's targeted for Linux machines, from HPC supercomputers to embedded devices.

This tool is designed to verify the integrity of system files on Linux systems. It operates by first calculating the SHA-256 hash of an installed binary within a clean, secure Podman container. It then provides the verified hash of this binary to the client. The client compares this hash to the hash of the installed binary on their own system. The tool comprises three main components.

## Components

### Generator

The fleet of containers from which good hashes are recorded and stored. When a hash is missing (either a apckage or a package version), a container is spun up and recorded, then deleted

Every xx minutes should update all packages and get the newest hashes

#### Containers

At first run, the generator should list all packages in the repo, install all packages possible without breakages ("`dnf install "*" --skip-broken`), and then install the ones which can't be installed in bulk on fresh images and add them to the database

From then on in production, every xx minutes it should check the current version of every package, test the most recent version for every package in the database, then install the poackages which have been updated in a fresh image 

### Server

Takes api requests, returns a hash if in the database, and gets the hash from the generator if a hash is missing

For security, it only passes packages for install to the generator which are in a database of good packages or somehow else sanitized

Determining the newest version of the package is the server's responsibility

#### Database



## Other

We have to keep in mind that different OSs/Architectures and different versions of the binary generate different hashes. Also, the DNF package manager doesn't keep old versions of packages. This means that we have to create images for every kind of operating system and architecture we want. Also, we'll have to keep a record of old versions of packages, when a new version of the package is released it has to create a new entry for the new version (if you use dnf, you can specify release-version=29 to get old versions of packages). Since these hashes will be used in the future, they should probably be signed with a system pgp key.

## Production Considerations

When running `dnf install "*"` it says the installed disk space used will be 292 GB, so I need an actual server. Of course, we don't need to do a bulk download but it would be cool. It would also need to spin up containers pretty fast

## TODO

    - Alpine doesn't include bash by default, entrypoint won't work
    - I also want a dashboard for seeing where the package versions for the fleet of images are at, and to manage how the server is doing, the amount of packages upgraded recently, etc.
    - coreutils are weird, you can't get the version of 'ls' with pacman -Qi because it's installed as coreutils with other things, so you'd either have to add exceptions for coreutils packages or omit them
