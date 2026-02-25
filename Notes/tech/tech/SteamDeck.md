系统更新后的问题：

- 通过 pacman 命令安装的软件会在系统更新后消失，但是通过 Discover 安装的软件不受影响，所以优先考虑通过 Discover 安装软件。

- 不出声音
解决办法：安装 pulseaudio

```shell
sudo pacman -S --noconfirm pulseaudio
```

- 浏览器无法播放视频
解决办法：安装 pipewire-media-session

```shell
sudo pacman -S --noconfirm pipewire-media-session
```