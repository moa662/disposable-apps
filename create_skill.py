#!/usr/bin/env python3
"""
智能体技能创建工具
自动创建WorkBuddy技能的基本结构
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime

def create_skill(skill_name, description, author=None, version="1.0.0"):
    """创建新的智能体技能"""
    
    # 确定安装目录
    workbuddy_dir = Path.home() / ".workbuddy" / "skills"
    skill_dir = workbuddy_dir / skill_name
    
    # 如果目录已存在，询问是否覆盖
    if skill_dir.exists():
        print(f"⚠️  技能目录 '{skill_name}' 已存在！")
        response = input("是否覆盖？(y/N): ").lower()
        if response != 'y':
            print("❌ 操作取消")
            return False
    
    # 创建目录结构
    skill_dir.mkdir(parents=True, exist_ok=True)
    (skill_dir / "scripts").mkdir(exist_ok=True)
    (skill_dir / "references").mkdir(exist_ok=True)
    (skill_dir / "assets").mkdir(exist_ok=True)
    
    # 创建SKILL.md文件
    skill_md_content = f"""---
name: {skill_name}
description: "{description}"
---

# {skill_name.replace('-', ' ').title()} Skill

## 使用场景
当用户需要...时使用本技能。

## 核心功能
1. 功能一：...
2. 功能二：...
3. 功能三：...

## 使用方法
```bash
# 基本使用示例
python scripts/main.py --input data.txt

# 高级选项
python scripts/main.py --help
```

## 配置选项
- `--input`: 输入文件路径
- `--output`: 输出文件路径
- `--format`: 输出格式（json/csv/html）

## 示例代码
```python
# 在Python中使用
from scripts.processor import SkillProcessor

processor = SkillProcessor()
result = processor.process("input.txt")
print(result)
```

## 注意事项
1. 确保输入文件格式正确
2. 操作前会自动创建备份
3. 支持撤销操作

## 更新日志
### v{version} ({datetime.now().strftime('%Y-%m-%d')})
- 初始版本创建
"""

    with open(skill_dir / "SKILL.md", "w", encoding="utf-8") as f:
        f.write(skill_md_content)
    
    # 创建示例脚本
    main_script = """#!/usr/bin/env python3
\"\"\"
主处理脚本 - {skill_name}
\"\"\"

import argparse
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description='{skill_name} - {description}')
    parser.add_argument('--input', '-i', required=True, help='输入文件路径')
    parser.add_argument('--output', '-o', default='output.txt', help='输出文件路径')
    parser.add_argument('--verbose', '-v', action='store_true', help='详细输出模式')
    
    args = parser.parse_args()
    
    # 检查输入文件是否存在
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"❌ 错误：输入文件不存在 - {args.input}")
        sys.exit(1)
    
    # 读取输入文件
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ 读取文件失败: {e}")
        sys.exit(1)
    
    # 处理逻辑（示例）
    processed_content = f"处理结果: {len(content)} 字符"
    
    # 输出结果
    output_path = Path(args.output)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(processed_content)
    
    if args.verbose:
        print(f"✅ 处理完成！")
        print(f"📥 输入文件: {args.input}")
        print(f"📤 输出文件: {args.output}")
        print(f"📊 处理结果: {processed_content}")
    else:
        print(f"✅ 处理完成！结果保存到: {args.output}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
""".format(skill_name=skill_name, description=description)

    with open(skill_dir / "scripts" / "main.py", "w", encoding="utf-8") as f:
        f.write(main_script)
    
    # 创建工具脚本
    utils_script = """#!/usr/bin/env python3
\"\"\"
工具函数 - {skill_name}
\"\"\"

import json
import yaml
from typing import Dict, Any, List
from pathlib import Path

def read_config(config_path: str) -> Dict[str, Any]:
    \"\"\"读取配置文件\"\"\"
    config_file = Path(config_path)
    
    if not config_file.exists():
        return {{}}
    
    if config_file.suffix in ['.yaml', '.yml']:
        with open(config_file, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    elif config_file.suffix == '.json':
        with open(config_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        raise ValueError(f"不支持的配置文件格式: {{config_file.suffix}}")

def save_results(results: Any, output_path: str, format: str = 'json'):
    \"\"\"保存处理结果\"\"\"
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    if format == 'json':
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
    elif format == 'txt':
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(str(results))
    else:
        raise ValueError(f"不支持的输出格式: {{format}}")
    
    return output_file

def log_message(message: str, level: str = "INFO"):
    \"\"\"日志记录\"\"\"
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{{timestamp}}] [{{level}}] {{message}}")

def validate_input(input_data: Any, schema: Dict[str, Any]) -> bool:
    \"\"\"验证输入数据\"\"\"
    # 简单的验证逻辑示例
    if not input_data:
        return False
    
    # 根据schema验证
    for key, value_type in schema.items():
        if key not in input_data:
            return False
        
        if not isinstance(input_data[key], value_type):
            return False
    
    return True
""".format(skill_name=skill_name)

    with open(skill_dir / "scripts" / "utils.py", "w", encoding="utf-8") as f:
        f.write(utils_script)
    
    # 创建工作流程文档
    workflow_doc = f"""# {skill_name.replace('-', ' ').title()} 工作流程

## 流程图
```
用户请求 → 参数解析 → 数据读取 → 处理逻辑 → 结果输出 → 报告生成
```

## 详细步骤

### 1. 参数解析
- 解析命令行参数
- 验证参数有效性
- 加载配置文件

### 2. 数据读取
- 检查输入文件存在性
- 根据文件类型选择读取方法
- 数据格式验证

### 3. 处理逻辑
- 应用业务规则
- 数据转换和计算
- 错误处理和恢复

### 4. 结果输出
- 格式化输出数据
- 生成报告文件
- 保存处理日志

### 5. 清理工作
- 临时文件清理
- 资源释放
- 状态保存

## 错误处理
- 输入文件不存在 → 提示用户并提供解决方案
- 数据格式错误 → 尝试修复或提供格式说明
- 处理失败 → 保存中间状态以便恢复
- 权限问题 → 提示用户检查权限

## 性能优化
- 大文件分块处理
- 内存使用监控
- 缓存中间结果
- 并行处理支持
"""

    with open(skill_dir / "references" / "workflow.md", "w", encoding="utf-8") as f:
        f.write(workflow_doc)
    
    # 创建示例配置文件
    config_example = {
        "skill_name": skill_name,
        "version": version,
        "created_at": datetime.now().isoformat(),
        "author": author or os.getenv("USERNAME", "Unknown"),
        "settings": {
            "input_format": "auto",
            "output_format": "json",
            "log_level": "INFO",
            "backup_enabled": True,
            "max_file_size": 104857600  # 100MB
        },
        "features": [
            "data_processing",
            "report_generation",
            "error_recovery"
        ]
    }
    
    with open(skill_dir / "assets" / "config.example.json", "w", encoding="utf-8") as f:
        json.dump(config_example, f, ensure_ascii=False, indent=2)
    
    # 创建README文件
    readme_content = f"""# {skill_name.replace('-', ' ').title()}

{description}

## 快速开始

### 安装
1. 复制本技能到WorkBuddy技能目录：
   ```bash
   cp -r {skill_name} ~/.workbuddy/skills/
   ```

2. 确保脚本可执行：
   ```bash
   chmod +x scripts/*.py
   ```

### 使用
在WorkBuddy中提及相关功能时，本技能会自动加载。

### 命令行使用
```bash
# 基本用法
python scripts/main.py --input data.txt --output result.json

# 查看帮助
python scripts/main.py --help
```

## 文件结构
```
{skill_name}/
├── SKILL.md                    # 技能定义
├── scripts/                    # 执行脚本
│   ├── main.py                # 主处理脚本
│   └── utils.py               # 工具函数
├── references/                 # 参考资料
│   └── workflow.md            # 工作流程
├── assets/                     # 资源文件
│   └── config.example.json    # 配置示例
└── README.md                   # 本文件
```

## 配置说明
复制 `assets/config.example.json` 为 `config.json` 并根据需要修改。

## 开发指南
1. 在 `scripts/` 目录中添加新的处理模块
2. 在 `SKILL.md` 中更新功能说明
3. 在 `references/` 中添加相关文档
4. 测试确保功能正常

## 许可证
MIT License

## 作者
{author or os.getenv("USERNAME", "Unknown")} ({datetime.now().strftime('%Y-%m-%d')})
"""

    with open(skill_dir / "README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    # 创建安装脚本
    install_script = """#!/bin/bash
# 安装脚本 - {skill_name}

set -e

echo "🔧 安装 {skill_name} 技能..."

# 检查WorkBuddy技能目录
WORKBUDDY_SKILLS_DIR="$HOME/.workbuddy/skills"
if [ ! -d "$WORKBUDDY_SKILLS_DIR" ]; then
    echo "📁 创建WorkBuddy技能目录..."
    mkdir -p "$WORKBUDDY_SKILLS_DIR"
fi

# 复制技能文件
SKILL_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SKILL_NAME="{skill_name}"

echo "📂 复制技能文件到: $WORKBUDDY_SKILLS_DIR/$SKILL_NAME"
cp -r "$SKILL_DIR" "$WORKBUDDY_SKILLS_DIR/"

# 设置脚本权限
echo "🔐 设置脚本权限..."
chmod +x "$WORKBUDDY_SKILLS_DIR/$SKILL_NAME/scripts/"*.py 2>/dev/null || true

echo "✅ 安装完成！"
echo ""
echo "🎯 使用方法："
echo "1. 在WorkBuddy中提及相关功能"
echo "2. 或使用命令行: python scripts/main.py --help"
echo ""
echo "📁 安装位置: $WORKBUDDY_SKILLS_DIR/$SKILL_NAME"
""".format(skill_name=skill_name)

    with open(skill_dir / "install.sh", "w", encoding="utf-8") as f:
        f.write(install_script)
    
    # 设置文件权限
    os.chmod(skill_dir / "scripts" / "main.py", 0o755)
    os.chmod(skill_dir / "install.sh", 0o755)
    
    print(f"✅ 技能 '{skill_name}' 创建成功！")
    print(f"📁 技能目录: {skill_dir}")
    print(f"📝 主要文件:")
    print(f"   - SKILL.md: 技能定义文档")
    print(f"   - scripts/main.py: 主处理脚本")
    print(f"   - scripts/utils.py: 工具函数")
    print(f"   - references/workflow.md: 工作流程文档")
    print(f"   - assets/config.example.json: 配置示例")
    print(f"   - README.md: 详细说明")
    print(f"   - install.sh: 安装脚本")
    print()
    print("🚀 下一步:")
    print(f"1. 编辑 SKILL.md 文件完善技能说明")
    print(f"2. 修改 scripts/main.py 实现具体功能")
    print(f"3. 运行安装脚本: bash install.sh")
    print(f"4. 在WorkBuddy中测试技能")
    
    return True

def main():
    """命令行入口"""
    if len(sys.argv) < 2:
        print("用法: python create_skill.py <技能名称> [描述]")
        print("示例: python create_skill.py data-processor \"数据处理和分析工具\"")
        sys.exit(1)
    
    skill_name = sys.argv[1]
    description = sys.argv[2] if len(sys.argv) > 2 else f"{skill_name.replace('-', ' ')} 工具"
    
    # 获取作者信息
    author = os.getenv("USERNAME", "Unknown")
    
    try:
        success = create_skill(skill_name, description, author)
        if success:
            sys.exit(0)
        else:
            sys.exit(1)
    except Exception as e:
        print(f"❌ 创建技能失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()