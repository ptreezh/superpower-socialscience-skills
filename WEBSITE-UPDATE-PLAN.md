# SocienceAI 网站内容更新发布计划

> 🔴 **基于真实网站现状的更新计划**

**制定日期**: 2026-03-22
**网站现状**: 已上线，有基础内容
**任务**: 将本地新内容同步到线上

---

## 📊 网站现状分析

### 已上线内容（http://www.socienceai.com）

**主导航（9 个菜单）**:
- 首页
- Agent 服务
- 精品 AI
- 赋能工具
- 培训课程
- 白皮书
- 关于我们
- 博客
- 联系我们

**已展示的方法论**:
- ✅ 扎根理论
- ✅ 社会网络分析
- ✅ 行动者网络分析
- ✅ 布迪厄场域分析
- ✅ 数字马克思
- ✅ 数字韦伯
- ✅ 数字涂尔干
- ✅ QCA/DID 分析

**技术架构**:
- 网站已上线运营
- 有完整的服务展示
- 有 Agent 服务功能
- 有培训课程、白皮书等内容板块

---

## 📁 本地待发布内容

### 已完成但未上线的内容

| 内容类型 | 本地位置 | 状态 | 优先级 |
|---------|---------|------|--------|
| Soul Agent Creator | `soul-agent-creator/` | ✅ 完成 | P0 |
| 12 种方法论 Skill | 各方法论目录 | ✅ 完成 | P0 |
| 自主进化系统 | `autonomous-evolution-engine.py` | ✅ 完成 | P1 |
| 战略执行系统 | `strategic-execution-engine.py` | ✅ 完成 | P1 |
| 质量保证宪章 | `QUALITY-ASSURANCE-CHARTER.md` | ✅ 完成 | P0 |
| 项目宣言 | `MANIFESTO.md` | ✅ 完成 | P0 |
| 网站生成内容 | `website/docs/` | ✅ 14 个页面 | P0 |

### 需要更新到网站的内容

**1. Agent 服务页面增强**
- 现有：服务介绍
- 待添加：Soul Agent Creator 工具、自主进化功能

**2. 方法论页面增强**
- 现有：方法论简介
- 待添加：详细使用指南、案例研究、对标学者

**3. 赋能工具页面**
- 现有：工具导航
- 待添加：本地 12 种方法论工具、质量检查系统

**4. 培训课程页面**
- 现有：课程介绍
- 待添加：方法论教程、视频教程、实操指南

**5. 白皮书页面**
- 现有：白皮书列表
- 待添加：质量保证宪章、自主进化系统文档、战略体系文档

**6. 博客页面**
- 现有：博客入口
- 待添加：10+ 篇方法论文章

---

## 🎯 更新策略

### 方案 A: FTP 直接上传（推荐）

**适用**: 静态内容更新

**步骤**:
1. 使用 FTP 工具（FileZilla/WinSCP）
2. 连接到服务器：`103.99.40.226:21`
3. 上传文件到对应目录
4. 验证更新

**FTP 信息**: （已私密保存）
- FTP 地址：103.99.40.226
- FTP 端口：21
- FTP 用户名：3njf8mh28i222
- FTP 密码：[已私密保存]

### 方案 B: WebFTP 在线管理

**适用**: 小文件快速更新

**URL**: https://dedit1010n55-dedihosts-hk-control.topvps.top/vhost/?c=webftp&a=enter

**步骤**:
1. Edge 浏览器打开 WebFTP
2. 登录（使用本地 cookie/session）
3. 选择文件上传
4. 验证更新

### 方案 C: 管理面板操作

**适用**: 配置修改、数据库操作

**URL**: https://www.vpsor.cn/center/personal/myProduct/girdhost

**步骤**:
1. 登录管理面板
2. 点击"管理面板进去"
3. 选择"云虚拟主机 cvh-3njf8mh28i222"
4. 进行文件管理或配置修改

---

## 📋 更新任务清单

### Phase 1: 准备（Day 1）

**任务**:
- [ ] 确认 FTP 访问正常
- [ ] 备份线上现有内容
- [ ] 整理本地待发布内容
- [ ] 制定文件目录映射

**FTP 目录结构确认**:
```
/ (网站根目录)
├── index.html              # 首页
├── agent-service/          # Agent 服务
├── methods/                # 方法论
├── tools/                  # 赋能工具
├── courses/                # 培训课程
├── whitepaper/             # 白皮书
├── blog/                   # 博客
├── about/                  # 关于我们
└── contact/                # 联系我们
```

### Phase 2: Agent 服务更新（Day 2-3）

**更新内容**:
- [ ] Soul Agent Creator 工具页面
- [ ] 自主进化系统介绍
- [ ] 质量检查系统介绍

**文件清单**:
```
agent-service/
├── soul-agent-creator.html     # 新增
├── autonomous-evolution.html   # 新增
├── quality-assurance.html      # 新增
└── index.html                  # 更新（添加新服务入口）
```

### Phase 3: 方法论页面增强（Day 4-7）

**更新内容**:
- [ ] 12 种方法论详细页面
- [ ] 使用指南
- [ ] 案例研究

**文件清单**:
```
methods/
├── grounded-theory/
│   ├── index.html          # 更新（增加详细内容）
│   ├── guide.html          # 新增
│   └── cases.html          # 新增
├── sna/
│   └── ...                 # 同上
└── ...                     # 其他 10 种方法论
```

### Phase 4: 赋能工具更新（Day 8-9）

**更新内容**:
- [ ] 12 种方法论工具页面
- [ ] 工具使用文档

**文件清单**:
```
tools/
├── index.html                  # 更新（添加新工具）
├── methodology-tools.html      # 新增（12 种工具列表）
└── docs/                       # 新增（使用文档）
```

### Phase 5: 培训课程更新（Day 10-12）

**更新内容**:
- [ ] 方法论教程
- [ ] 视频教程（如有）
- [ ] 实操指南

**文件清单**:
```
courses/
├── index.html                  # 更新
├── methodology-tutorials/      # 新增
│   ├── grounded-theory.html
│   └── ...
└── hands-on-guides/            # 新增
```

### Phase 6: 白皮书更新（Day 13-14）

**更新内容**:
- [ ] 质量保证宪章
- [ ] 自主进化系统文档
- [ ] 战略体系文档

**文件清单**:
```
whitepaper/
├── index.html                      # 更新
├── quality-assurance-charter.pdf   # 新增
├── autonomous-evolution-system.pdf # 新增
└── strategy-system.pdf             # 新增
```

### Phase 7: 博客内容（Day 15-20）

**更新内容**:
- [ ] 10 篇方法论文章

**文章列表**:
1. 什么是扎根理论？
2. 如何编码访谈数据？
3. 社会网络分析入门
4. 行动者网络理论详解
5. 布迪厄场域分析指南
6. QCA 方法实操
7. 混合方法研究设计
8. 数字马克思分析框架
9. 如何选择合适的研究方法？
10. AI 如何辅助社会科学研究

**文件清单**:
```
blog/
├── index.html                  # 更新（添加新文章列表）
└── posts/
    ├── grounded-theory-intro.html
    ├── coding-interview-data.html
    └── ...                     # 其他 8 篇
```

---

## 🔧 执行脚本

### FTP 批量上传脚本（Python）

```python
#!/usr/bin/env python3
"""
SocienceAI 网站内容 FTP 批量上传脚本
"""

from ftplib import FTP
import os
from pathlib import Path

class WebsiteUploader:
    def __init__(self):
        self.ftp = FTP()
        self.host = '103.99.40.226'
        self.port = 21
        self.user = '3njf8mh28i222'
        self.password = '[密码]'  # 从安全存储读取
    
    def connect(self):
        """连接 FTP 服务器"""
        self.ftp.connect(self.host, self.port)
        self.ftp.login(self.user, self.password)
        print("✅ FTP 连接成功")
    
    def upload_file(self, local_path, remote_path):
        """上传单个文件"""
        with open(local_path, 'rb') as f:
            self.ftp.storbinary(f'STOR {remote_path}', f)
        print(f"  ✅ 上传：{remote_path}")
    
    def upload_directory(self, local_dir, remote_dir):
        """上传整个目录"""
        for root, dirs, files in os.walk(local_dir):
            for file in files:
                local_path = Path(root) / file
                relative_path = local_path.relative_to(local_dir)
                remote_path = Path(remote_dir) / relative_path
                
                # 确保远程目录存在
                self.ensure_directory_exists(str(remote_path.parent))
                
                self.upload_file(str(local_path), str(remote_path))
    
    def ensure_directory_exists(self, dir_path):
        """确保远程目录存在"""
        try:
            self.ftp.cwd(dir_path)
        except:
            # 目录不存在，创建
            parent = str(Path(dir_path).parent)
            if parent != '/':
                self.ensure_directory_exists(parent)
            self.ftp.mkd(dir_path)
    
    def close(self):
        """关闭连接"""
        self.ftp.quit()
        print("✅ FTP 连接已关闭")

# 使用示例
if __name__ == '__main__':
    uploader = WebsiteUploader()
    uploader.connect()
    
    # 上传 Agent 服务页面
    uploader.upload_directory(
        './website/docs',
        '/htdocs'
    )
    
    uploader.close()
```

---

## 📊 更新进度追踪

### 进度仪表板

```
╔═══════════════════════════════════════════════════════════╗
║          SocienceAI 网站内容更新进度                       ║
║          更新日期：2026-03-22                              ║
╠═══════════════════════════════════════════════════════════╣
║  Phase 1: 准备                         ████████░░ 80%     ║
║  Phase 2: Agent 服务更新               ░░░░░░░░░░ 0%      ║
║  Phase 3: 方法论页面增强               ░░░░░░░░░░ 0%      ║
║  Phase 4: 赋能工具更新                 ░░░░░░░░░░ 0%      ║
║  Phase 5: 培训课程更新                 ░░░░░░░░░░ 0%      ║
║  Phase 6: 白皮书更新                   ░░░░░░░░░░ 0%      ║
║  Phase 7: 博客内容                     ░░░░░░░░░░ 0%      ║
╠═══════════════════════════════════════════════════════════╣
║  整体进度：███░░░░░░░░░░░░░░░░░ 11%                      ║
╚═══════════════════════════════════════════════════════════╝
```

### 更新日志

| 日期 | 更新内容 | 状态 | 备注 |
|------|---------|------|------|
| 2026-03-22 | 制定更新计划 | ✅ 完成 | 本文档 |
| 2026-03-22 | FTP 连接测试 | ⏳ 待执行 | |
| 2026-03-23 | Phase 1 准备 | ⏳ 待执行 | |
| ... | ... | | |

---

## ⚠️ 注意事项

### 安全事项

1. **FTP 凭证保护**
   - 不要在代码中硬编码密码
   - 使用环境变量或配置文件
   - 定期更换密码

2. **备份策略**
   - 上传前备份线上内容
   - 使用版本控制
   - 保留回滚能力

3. **上传验证**
   - 上传后验证文件完整性
   - 检查网站功能正常
   - 测试链接无 404

### 技术注意事项

1. **文件编码**
   - 确保 UTF-8 编码
   - 中文文件名可能需要特殊处理

2. **路径大小写**
   - Linux 服务器区分大小写
   - 确保路径大小写正确

3. **权限设置**
   - 目录权限：755
   - 文件权限：644

---

## 📞 联系和支持

**项目负责人**: SocienceAI Team
**技术支持**: tech@socienceai.com

---

*基于真实网站现状制定 | 2026-03-22*

*"让社会科学研究人人可为"*
