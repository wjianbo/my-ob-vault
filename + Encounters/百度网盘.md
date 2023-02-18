# Install Baidu Net Disk on SteamDeck

## Enable AUR

Add to the following line to file `/etc/pacman.conf`
```
Server = http//repo.archlinux.fr/$arch
```

Excute: `sudo pacman -Sy`


## Install Baidu Net Disk

```
 git clone https://aur.archlinux.org/baidunetdisk-bin.git
 cd baidunetdisk-bin
 makepkg -si
```

- [AURとは何ですか？ArchLinuxおよびその派生物でAURを有効にする方法| Linuxから](https://blog.desdelinux.net/ja/que-es-aur-y-como-habilitarlo-en-arch-linux-y-derivados/#Habilitacion_de_AUR_en_Arch_Linux_y_derivados)
- [AUR (en) - baidunetdisk-bin](https://aur.archlinux.org/packages/baidunetdisk-bin)
- [Reddit - Dive into anything](https://www.reddit.com/r/SteamDeck/comments/ytmjpr/cannot_find_fake_root_binary_error/)
- [patch: command not found / Creating & Modifying Packages / Arch Linux Forums](https://bbs.archlinux.org/viewtopic.php?id=45933)


### Cannot find fake root binary error

```
sudo pacman -S fakeroot
```
