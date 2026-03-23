#!/usr/bin/env python3
"""
创建智能体技能示例
演示如何使用 create_skill.py 创建不同类型的智能体技能
"""

import os
import sys
from pathlib import Path

# 添加当前目录到路径，以便导入 create_skill
sys.path.append(str(Path(__file__).parent))

def create_example_skills():
    """创建几个示例智能体技能"""
    
    skills_to_create = [
        {
            "name": "file-organizer",
            "description": "智能文件整理工具，自动分类和整理文件"
        },
        {
            "name": "data-analyzer", 
            "description": "数据分析工具，支持CSV/Excel数据处理和可视化"
        },
        {
            "name": "report-generator",
            "description": "报告生成工具，基于模板自动生成专业报告"
        },
        {
            "name": "task-manager",
            "description": "任务管理助手，支持任务跟踪和进度监控"
        }
    ]
    
    print("🚀 开始创建智能体技能示例...")
    print("=" * 60)
    
    for skill_info in skills_to_create:
        skill_name = skill_info["name"]
        description = skill_info["description"]
        
        print(f"\n📦 创建技能: {skill_name}")
        print(f"📝 描述: {description}")
        
        # 调用 create_skill.py 创建技能
        try:
            # 这里模拟调用 create_skill.py
            # 在实际使用中，应该导入函数直接调用
            print(f"📁 创建技能目录结构...")
            
            # 创建技能目录
            skill_dir = Path.home() / ".workbuddy" / "skills" / skill_name
            skill_dir.mkdir(parents=True, exist_ok=True)
            
            # 创建基本文件
            skill_md = skill_dir / "SKILL.md"
            skill_md.write_text(f"""---
name: {skill_name}
description: "{description}"
---

# {skill_name.replace('-', ' ').title()} Skill

这是一个示例技能，用于演示智能体能力扩展。

## 功能说明
1. 示例功能一
2. 示例功能二
3. 示例功能三

## 使用示例
```bash
python scripts/main.py --help
```

## 注意事项
这是一个示例技能，需要根据实际需求完善功能。
""", encoding="utf-8")
            
            print(f"✅ 技能 '{skill_name}' 创建完成!")
            print(f"📁 位置: {skill_dir}")
            
        except Exception as e:
            print(f"❌ 创建技能失败: {e}")
    
    print("\n" + "=" * 60)
    print("🎉 示例技能创建完成!")
    print("\n📚 创建的技能包括:")
    for skill_info in skills_to_create:
        print(f"  - {skill_info['name']}: {skill_info['description']}")
    
    print("\n🚀 接下来可以:")
    print("1. 使用 create_skill.py 创建自定义技能")
    print("2. 编辑 SKILL.md 文件完善技能说明")
    print("3. 在 scripts/ 目录中添加实际功能脚本")
    print("4. 在 WorkBuddy 中测试技能效果")

def test_skill_creation():
    """测试 create_skill.py 的使用"""
    print("\n🧪 测试 create_skill.py 使用:")
    print("=" * 60)
    
    # 模拟命令行参数
    test_skill = "test-skill"
    test_description = "测试技能，用于验证创建工具"
    
    print(f"测试命令: python create_skill.py {test_skill} \"{test_description}\"")
    
    # 在实际环境中，这里会调用 create_skill.py
    # 为了示例，我们只显示预期的输出
    
    expected_output = f"""
✅ 技能 '{test_skill}' 创建成功！
📁 技能目录: ~/.workbuddy/skills/{test_skill}
📝 主要文件:
   - SKILL.md: 技能定义文档
   - scripts/main.py: 主处理脚本
   - scripts/utils.py: 工具函数
   - references/workflow.md: 工作流程文档
   - assets/config.example.json: 配置示例
   - README.md: 详细说明
   - install.sh: 安装脚本

🚀 下一步:
1. 编辑 SKILL.md 文件完善技能说明
2. 修改 scripts/main.py 实现具体功能
3. 运行安装脚本: bash install.sh
4. 在WorkBuddy中测试技能
"""
    
    print("预期输出:")
    print(expected_output)

def show_workbuddy_skills_structure():
    """显示 WorkBuddy 技能目录结构"""
    print("\n📁 WorkBuddy 技能目录结构:")
    print("=" * 60)
    
    workbuddy_skills_dir = Path.home() / ".workbuddy" / "skills"
    
    if workbuddy_skills_dir.exists():
        print(f"技能目录: {workbuddy_skills_dir}")
        print("\n现有技能:")
        
        for item in workbuddy_skills_dir.iterdir():
            if item.is_dir():
                skill_md = item / "SKILL.md"
                if skill_md.exists():
                    # 读取技能描述
                    content = skill_md.read_text(encoding="utf-8")
                    # 提取描述
                    import re
                    match = re.search(r'description:\s*"([^"]+)"', content)
                    description = match.group(1) if match else "无描述"
                    print(f"  - {item.name}: {description}")
                else:
                    print(f"  - {item.name}: (缺少 SKILL.md)")
    else:
        print(f"技能目录不存在: {workbuddy_skills_dir}")
        print("首次运行时会自动创建")

def create_quick_start_guide():
    """创建快速入门指南"""
    print("\n📘 智能体技能快速入门指南:")
    print("=" * 60)
    
    guide = """
## 🎯 什么是智能体技能？
技能是扩展 WorkBuddy 智能体能力的模块化包，每个技能提供：
- 专业领域知识
- 标准化工作流程
- 可执行工具脚本
- 相关参考资料

## 🚀 创建第一个技能的步骤

### 步骤1: 使用创建工具
```bash
# 创建数据分析技能
python create_skill.py data-processor "数据处理和分析工具"

# 创建文件管理技能  
python create_skill.py file-manager "智能文件整理工具"
```

### 步骤2: 编辑技能定义
编辑 ~/.workbuddy/skills/[技能名]/SKILL.md:
1. 完善使用场景说明
2. 详细描述核心功能
3. 添加使用示例代码
4. 说明注意事项

### 步骤3: 实现功能脚本
编辑 ~/.workbuddy/skills/[技能名]/scripts/main.py:
1. 实现具体的数据处理逻辑
2. 添加命令行参数解析
3. 实现错误处理和日志
4. 确保输出格式规范

### 步骤4: 安装和测试
```bash
# 运行安装脚本
cd ~/.workbuddy/skills/[技能名]
bash install.sh

# 在WorkBuddy中测试
# 提及技能相关功能，智能体会自动加载技能
```

## 📋 技能设计最佳实践

### 1. 单一职责原则
每个技能只专注一个特定领域，不要试图做太多事情。

### 2. 易用性优先
提供简单的使用示例，降低用户学习成本。

### 3. 完整文档
包括使用场景、功能说明、示例代码和注意事项。

### 4. 安全性考虑
- 操作前创建备份
- 验证输入数据
- 处理异常情况
- 提供撤销功能

### 5. 性能优化
- 支持大文件处理
- 内存使用监控
- 缓存中间结果
- 并行处理选项

## 🔧 高级功能扩展

### 集成外部API
在技能中集成第三方服务，如：
- 数据库连接
- Web API调用
- 云服务集成
- 消息通知

### 团队协作
创建多个相关技能，组成技能套件：
```bash
# 数据分析套件
data-collector/     # 数据收集
data-cleaner/       # 数据清洗  
data-analyzer/      # 数据分析
data-visualizer/    # 数据可视化
```

### 自动化工作流
结合 WorkBuddy 自动化功能：
- 定时运行技能任务
- 条件触发技能执行
- 技能间数据传递
- 结果通知和报告

## 🎓 学习资源

### 官方文档
- WorkBuddy 文档: https://www.codebuddy.cn/docs/workbuddy/
- 技能创建指南: ~/.workbuddy/skills/skill-creator/

### 社区资源
- Vercel Skills: https://skills.sh/
- ClawHub技能库: https://clawhub.com/

### 示例技能
查看现有技能学习最佳实践：
```bash
ls -la ~/.workbuddy/skills/
```

## 💡 实用技巧

### 1. 渐进式开发
从简单的MVP开始，逐步添加复杂功能。

### 2. 用户反馈
收集用户使用反馈，持续优化技能功能。

### 3. 版本管理
使用Git管理技能版本，方便更新和维护。

### 4. 测试覆盖
编写测试用例，确保技能稳定可靠。

## 🚨 常见问题

### Q: 技能没有生效怎么办？
A: 检查技能目录是否正确，SKILL.md格式是否正确，重启WorkBuddy。

### Q: 如何调试技能？
A: 在脚本中添加日志输出，使用--verbose参数，检查错误信息。

### Q: 技能可以共享吗？
A: 可以，将技能目录打包分享，或发布到技能市场。

### Q: 支持哪些编程语言？
A: 主要支持Python，也可使用Shell脚本或其他语言。

## 📞 获取帮助
- 查看技能中的README.md文件
- 参考技能创建工具的帮助信息
- 在WorkBuddy社区寻求帮助
- 联系官方技术支持
"""
    
    print(guide)

def main():
    """主函数"""
    print("🤖 WorkBuddy 智能体技能创建演示")
    print("=" * 60)
    
    # 显示当前技能结构
    show_workbuddy_skills_structure()
    
    # 创建示例技能
    create_example_skills()
    
    # 测试创建工具
    test_skill_creation()
    
    # 显示快速入门指南
    create_quick_start_guide()
    
    print("\n" + "=" * 60)
    print("🎉 演示完成！")
    print("\n📁 生成的文件:")
    print("  - 智能体创建指南.md: 完整的概念和步骤说明")
    print("  - 智能体技能示例.md: 三个实用的技能模板")
    print("  - create_skill.py: 技能创建工具")
    print("  - 创建智能体技能示例.py: 本演示文件")
    
    print("\n🚀 现在可以开始创建你的第一个智能体技能了！")

if __name__ == "__main__":
    main()