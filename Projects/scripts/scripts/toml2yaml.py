import os
import re
import yaml
import toml

# 指定根文件夹路径
root_folder = "blog-content"

# 遍历根文件夹及其子文件夹中的所有 Markdown 文件
for folder_path, _, filenames in os.walk(root_folder):
    for filename in filenames:
        if filename.endswith(".md"):
            file_path = os.path.join(folder_path, filename)
            
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            
            # 检查是否为 TOML 格式
            toml_match = re.match(r"(?s)^\+\+\+\n(.*?)\n\+\+\+\n(.*)", content)
            yaml_match = re.match(r"(?s)^---\n(.*?)\n---\n(.*)", content)
            
            if toml_match:
                # 提取 TOML 和正文
                toml_content = toml_match.group(1)
                body_content = toml_match.group(2)
                
                # 解析 TOML 为字典
                toml_data = toml.loads(toml_content)
                
                # 转换为 YAML 格式
                yaml_content = yaml.dump(toml_data, allow_unicode=True, sort_keys=False).strip()
                
                # 生成新的文件内容
                new_content = f"---\n{yaml_content}\n---\n{body_content}"
                
                # 写回文件
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(new_content)
            
            elif yaml_match:
                # 如果已经是 YAML 格式，跳过
                continue