#!/bin/bash

: '
Takes three commands. 
    - install - install the specified package
    - signature - gets the sha256 signature for the specified package. Different distros keep them in different spots, so the script will have to change depending 
    - upgrade - upgrade the specified package
    - version

'

# Default command if no arguments are provided
action=""

# Check if arguments are provided
if [ "$#" -gt 0 ]; then
    cmd="$@"
fi


if [ "$1" == "install" ]; then
    install_command="$2"
    #echo "Install command: $install_command"
    action="install"
    # Add code to execute for 'install' command
elif [ "$1" == "upgrade" ]; then
    upgrade_option="$2"
    #echo "Upgrade option: $upgrade_option"
    action="upgrade"
    # Add code to execute for 'upgrade' command
elif [ "$1" == "signature" ]; then
    package="$2"
    #echo "Package: $package"
    action="retrieve"
    # Add code to execute for 'signature' command
else
    echo "Unknown command: $1"
    exit 1
fi


# Check if /etc/os-release exists
if [ ! -f /etc/os-release ]; then
    echo "Error: /etc/os-release not found"
    exit 1
fi

# Read the first line of /etc/os-release
first_line=$(head -n 1 /etc/os-release)

# Determine the OS
if grep -q "Alpine" <<< "$first_line"; then
    #echo "System: Ubuntu"
    distro="Alpine"

elif grep -q "Amazon" <<< "$first_line"; then
    #echo "System: Ubuntu"
    distro="Amazon"

elif grep -q "Arch" <<< "$first_line"; then
    #echo "System: Ubuntu"
    distro="Arch"

elif grep -q "Debian" <<< "$first_line"; then
    #echo "System: Ubuntu"
    distro="Debian"

elif grep -q "Fedora" <<< "$first_line"; then
    #echo "System: Fedora"
    distro="Fedora"

elif grep -q "Oracle" <<< "$first_line"; then
    #echo "System: Ubuntu"
    distro="Oracle"

elif grep -q "Rocky" <<< "$first_line"; then
    #echo "System: Ubuntu"
    distro="Rocky"

elif grep -q "Ubuntu" <<< "$first_line"; then
    #echo "System: Ubuntu"
    distro="Ubuntu"

else
    echo "Unknown distribution"
    exit 1
fi


# Check the architecture. This can come later because we might not even be able to support different architectures (we'd likely have to emulate stuff)
#arch=$(uname -m)
#echo "Architecture: $arch"

# Add further logic based on the detected distribution and architecture
if [ "$distro" == "Alpine" ]; then
    # Fedora specific logic

    if [ "$action" == "retrieve" ]; then

        output=$(sha256sum /bin/${package})
        echo $output

    fi

elif [ "$distro" == "Amazon" ]; then
    # Ubuntu specific logic
    #echo "Performing Ubuntu specific tasks..."

    if [ "$action" == "retrieve" ]; then

        output=$(sha256sum /bin/${package})
        echo $output

    fi

elif [ "$distro" == "Arch" ]; then
    # Ubuntu specific logic
    #echo "Performing Ubuntu specific tasks..."

    if [ "$action" == "retrieve" ]; then

        output=$(sha256sum /bin/${package})
        echo $output

    fi

elif [ "$distro" == "Debian" ]; then
    # Ubuntu specific logic
    #echo "Performing Ubuntu specific tasks..."

    if [ "$action" == "retrieve" ]; then

        output=$(sha256sum /bin/${package})
        echo $output

    fi

elif [ "$distro" == "Fedora" ]; then
    # Ubuntu specific logic
    #echo "Performing Ubuntu specific tasks..."

    if [ "$action" == "retrieve" ]; then

        output=$(sha256sum /bin/${package})
        echo $output

    fi

elif [ "$distro" == "Oracle" ]; then
    # Ubuntu specific logic
    #echo "Performing Ubuntu specific tasks..."

    if [ "$action" == "retrieve" ]; then

        output=$(sha256sum /bin/${package})
        echo $output

    fi

elif [ "$distro" == "Rocky" ]; then
    # Ubuntu specific logic
    #echo "Performing Ubuntu specific tasks..."

    if [ "$action" == "retrieve" ]; then

        output=$(sha256sum /bin/${package})
        echo $output

    fi

elif [ "$distro" == "Ubuntu" ]; then
    # Ubuntu specific logic
    #echo "Performing Ubuntu specific tasks..."

    if [ "$action" == "retrieve" ]; then

        output=$(sha256sum /bin/${package})
        echo $output

    fi

fi

