---
title: Steam Deck 桌面模式安装中日文输入法 
date: 2023-08-17
taxonomies:
  tags: ["Linux", "Steam Deck"]
---

安装中日文输入法（Steam Deck 桌面模式）

1. 通过 Discover - Software Center 安装 ：

  - Fcitx 5
  - Mozc for Fcitx 5
  - Rime for Fcitx 5

2. 通过 Fcitx Configuration 添加 Rime 和 Mozc。

3. 安装配置管理工具[東風破](https://github.com/rime/plum) /plum/ 

```
curl -fsSL https://raw.githubusercontent.com/rime/plum/master/rime-install | bash
```

4. 用東風破安裝口令安装所需的输入方案（需要在 plum 目录下执行）

```
bash rime-install wubi
```

5. 修改配置文件`~/.local/share/fcitx5/rime/build/default.yaml`

```yaml
schema_list:
  - schema: wubi86
  - schema: luna_pinyin_simp
```

配置文件的位置可能不同，参考[这里](https://github.com/rime/home/wiki/UserData)。

6. 右键点击输入法图标，选择 Deploy 使配置生效。

中间遇到的问题: 刚安装完成时 Rime 的图标没有显示，重启后可以显示。