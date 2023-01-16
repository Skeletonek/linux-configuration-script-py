debian_configuration = {}
ubuntu_configuration = {}

fedora_configuration = {
    1: "dnf install -y https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm "
       "https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm",
    2: "flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo",
    3: "printf \"# Custom config beneath\n\" >> /etc/dnf/dnf.conf;"
       "printf \"max_parallel_download=10\n\" >> /etc/dnf/dnf.conf;"
       "printf \"fastestmirror=True\n\" >> /etc/dnf/dnf.conf;"
       "printf \"keepcache=True\n\" >> /etc/dnf/dnf.conf",
    4: "dnf swap -y mesa-va-drivers mesa-va-drivers-freeworld;"
       "dnf swap -y mesa-vdpau-drivers mesa-vdpau-drivers-freeworld",
    5: "dnf remove PackageKit -y"
}

arch_configuration = {}