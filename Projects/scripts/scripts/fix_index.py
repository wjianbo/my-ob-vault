import os
import re
import yaml

# 指定根文件夹路径
root_folder = "blog-content"

# 遍历根文件夹及其子文件夹
for folder_path, _, filenames in os.walk(root_folder):
    for filename in filenames:
        if filename == "_index.md":
            file_path = os.path.join(folder_path, filename)
            
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            
            # 提取 YAML 信息
            match = re.match(r"(?s)^---\n(.*?)\n---", content)
            if not match:
                print(f"文件 {file_path} 缺少 YAML 信息，跳过处理")
                continue
            
            yaml_content = match.group(1)
            yaml_data = yaml.safe_load(yaml_content)
            
            # 检查是否存在 sort_by: date
            if "sort_by" in yaml_data and yaml_data["sort_by"] == "date":
                print(f"文件 {file_path} 已包含 sort_by: date，跳过处理")
                continue
            
            # 添加 sort_by: date
            yaml_data["sort_by"] = "date"
            new_yaml_content = yaml.dump(yaml_data, allow_unicode=True, sort_keys=False).strip()
            
            # 生成新的文件内容
            new_content = f"---\n{new_yaml_content}\n---\n{content[match.end():]}"
            
            # 写回文件
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(new_content)
            
            print(f"已更新文件 {file_path}，添加 sort_by: date")