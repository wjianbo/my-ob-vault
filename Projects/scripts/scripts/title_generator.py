import os
import re
import yaml

# 指定文件夹路径
folder_path = "blog-content/journal"

# 遍历文件夹中的所有 Markdown 文件
for filename in os.listdir(folder_path):
    print(filename)
    if filename.endswith(".md"):
        file_path = os.path.join(folder_path, filename)
        
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        
        # 分离 YAML 和正文
        match = re.match(r"(?s)^---\n(.*?)\n---\n(.*)", content)
        if not match:
            continue  # 如果没有 YAML Front Matter，跳过该文件
        
        yaml_content = match.group(1)
        body_content = match.group(2)
        
        # 解析 YAML
        yaml_data = yaml.safe_load(yaml_content)
        if "title" in yaml_data:
            continue  # 如果已经有 title 字段，跳过该文件
        
        # 从正文生成标题
        lines = body_content.strip().split("\n")
        first_line = lines[0] if lines else "无内容"
        title = first_line[:15]  # 截取前 15 个字符作为标题
        
        # 更新 YAML 数据
        yaml_data["title"] = title
        
        # 重新生成文件内容
        new_yaml_content = yaml.dump(yaml_data, allow_unicode=True, sort_keys=False).strip()
        new_content = f"---\n{new_yaml_content}\n---\n{body_content}"
        
        # 写回文件
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(new_content)