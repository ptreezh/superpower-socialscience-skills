# SocienceAI 网站更新 - 执行摘要

**制定日期**: 2026-03-22
**网站状态**: ✅ 已上线 (http://www.socienceai.com)
**任务**: 本地新内容同步到线上

---

## 📊 现状分析

### 网站已上线内容

**导航结构**（9 个主菜单）:
- 首页 ✅
- Agent 服务 ✅
- 精品 AI ✅
- 赋能工具 ✅
- 培训课程 ✅
- 白皮书 ✅
- 关于我们 ✅
- 博客 ✅
- 联系我们 ✅

**已展示的方法论**（12 种）:
- ✅ 扎根理论
- ✅ 社会网络分析
- ✅ 行动者网络分析
- ✅ 布迪厄场域分析
- ✅ 数字马克思
- ✅ 数字韦伯
- ✅ 数字涂尔干
- ✅ QCA/DID 分析

**网站定位**: AI + 社会科学双向赋能平台

---

## 📁 本地待发布内容

### 已完成的内容（待上传）

| 内容 | 位置 | 状态 | 优先级 |
|------|------|------|--------|
| Soul Agent Creator | `soul-agent-creator/` | ✅ | P0 |
| 12 种方法论详细文档 | 各方法论目录 | ✅ | P0 |
| 自主进化系统 | `autonomous-evolution-engine.py` | ✅ | P1 |
| 战略执行系统 | `strategic-execution-engine.py` | ✅ | P1 |
| 质量保证宪章 | `QUALITY-ASSURANCE-CHARTER.md` | ✅ | P0 |
| 项目宣言 | `MANIFESTO.md` | ✅ | P0 |
| 网站生成内容 | `website/docs/` | ✅ 14 页 | P0 |
| 90 天计划 | `WEBSITE-90DAY-PLAN.md` | ✅ | P1 |
| 更新计划 | `WEBSITE-UPDATE-PLAN.md` | ✅ | P0 |

---

## 🎯 更新策略

### 服务器信息（已私密保存）

**FTP 方式**（推荐批量上传）:
- FTP 地址：103.99.40.226
- FTP 端口：21
- FTP 用户名：3njf8mh28i222
- FTP 密码：[已私密保存]

**WebFTP 方式**（小文件快速上传）:
- URL: https://dedit1010n55-dedihosts-hk-control.topvps.top/vhost/?c=webftp&a=enter
- 使用 Edge 浏览器 + 本地 cookie/session 登录

**管理面板**（配置管理）:
- URL: https://www.vpsor.cn/center/personal/myProduct/girdhost
- 点击"云虚拟主机 cvh-3njf8mh28i222" → "管理面板进去"

### 服务器目录结构

```
/htdocs/  (网站根目录)
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

---

## 📋 执行步骤

### Step 1: 准备（今天完成）

**任务**:
- [ ] 测试 FTP 连接
- [ ] 备份线上现有内容
- [ ] 准备上传脚本

**FTP 连接测试**:
```bash
# 方式 1: 使用 FTP 客户端（如 FileZilla）
# 主机：103.99.40.226
# 端口：21
# 用户名：3njf8mh28i222
# 密码：[私密保存]

# 方式 2: 使用上传脚本
set FTP_PASSWORD=[密码]  # Windows
python ftp-upload.py ./website/docs
```

### Step 2: Agent 服务页面更新（Day 2-3）

**新增内容**:
- Soul Agent Creator 工具介绍
- 自主进化系统介绍
- 质量保证系统介绍

**上传文件**:
```
htdocs/agent-service/
├── soul-agent-creator.html     # 新增
├── autonomous-evolution.html   # 新增
└── quality-assurance.html      # 新增
```

### Step 3: 方法论页面增强（Day 4-7）

**新增内容**:
- 每种方法论的详细使用指南
- 案例研究
- 对标学者介绍

**上传文件**:
```
htdocs/methods/
├── grounded-theory/
│   ├── index.html          # 更新
│   ├── guide.html          # 新增
│   └── cases.html          # 新增
└── ... (其他 11 种方法论)
```

### Step 4: 赋能工具更新（Day 8-9）

**新增内容**:
- 12 种方法论工具页面
- 工具使用文档

**上传文件**:
```
htdocs/tools/
├── methodology-tools.html    # 新增
└── docs/                     # 新增目录
```

### Step 5: 培训课程更新（Day 10-12）

**新增内容**:
- 方法论教程
- 实操指南

**上传文件**:
```
htdocs/courses/
├── methodology-tutorials/    # 新增
└── hands-on-guides/          # 新增
```

### Step 6: 白皮书更新（Day 13-14）

**新增内容**:
- 质量保证宪章
- 自主进化系统文档
- 战略体系文档

**上传文件**:
```
htdocs/whitepaper/
├── quality-assurance-charter.pdf
├── autonomous-evolution-system.pdf
└── strategy-system.pdf
```

### Step 7: 博客内容（Day 15-20）

**新增内容**:
- 10 篇方法论文章

**上传文件**:
```
htdocs/blog/
└── posts/
    ├── grounded-theory-intro.html
    ├── coding-interview-data.html
    └── ... (其他 8 篇)
```

---

## 🔧 工具脚本

### FTP 批量上传脚本

**文件**: `ftp-upload.py`

**使用方法**:
```bash
# Windows
set FTP_PASSWORD=[你的密码]
python ftp-upload.py ./website/docs

# Linux/Mac
export FTP_PASSWORD=[你的密码]
python ftp-upload.py ./website/docs
```

**功能**:
- ✅ 自动连接 FTP 服务器
- ✅ 批量上传目录
- ✅ 自动创建远程目录
- ✅ 上传进度显示
- ✅ 错误处理和重试

---

## 📊 进度追踪

### 更新仪表板

```
╔═══════════════════════════════════════════════════════════╗
║          SocienceAI 网站内容更新进度                       ║
╠═══════════════════════════════════════════════════════════╣
║  Step 1: 准备                          ████████░░ 80%     ║
║  Step 2: Agent 服务更新                ░░░░░░░░░░ 0%      ║
║  Step 3: 方法论页面增强                ░░░░░░░░░░ 0%      ║
║  Step 4: 赋能工具更新                  ░░░░░░░░░░ 0%      ║
║  Step 5: 培训课程更新                  ░░░░░░░░░░ 0%      ║
║  Step 6: 白皮书更新                    ░░░░░░░░░░ 0%      ║
║  Step 7: 博客内容                      ░░░░░░░░░░ 0%      ║
╠═══════════════════════════════════════════════════════════╣
║  整体进度：███░░░░░░░░░░░░░░░░░ 11%                      ║
╚═══════════════════════════════════════════════════════════╝
```

### 更新日志

| 日期 | 任务 | 状态 | 备注 |
|------|------|------|------|
| 2026-03-22 | 制定更新计划 | ✅ 完成 | 本文档 |
| 2026-03-22 | 创建 FTP 上传脚本 | ✅ 完成 | ftp-upload.py |
| 2026-03-22 | FTP 连接测试 | ⏳ 待执行 | |
| 2026-03-23 | Step 1 准备 | ⏳ 待执行 | |
| ... | ... | | |

---

## ⚠️ 注意事项

### 安全提醒

1. **FTP 凭证保护**
   - ✅ 已私密保存，不分享
   - ✅ 使用环境变量，不硬编码
   - ⚠️ 定期更换密码

2. **备份策略**
   - ⚠️ 上传前必须备份线上内容
   - ⚠️ 保留回滚能力

3. **上传验证**
   - ⚠️ 上传后验证文件完整性
   - ⚠️ 检查网站功能正常

### 技术注意

1. **文件编码**: 确保 UTF-8
2. **路径大小写**: Linux 服务器区分大小写
3. **权限设置**: 目录 755，文件 644

---

## 📞 下一步行动

### 立即执行（今天）

1. **测试 FTP 连接**
   ```bash
   # 使用 FileZilla 或其他 FTP 客户端
   # 或运行：python ftp-upload.py --test
   ```

2. **备份线上内容**
   ```bash
   # 下载线上所有文件到 backup/ 目录
   ```

3. **准备上传文件**
   ```bash
   # 确认 website/docs/ 目录内容完整
   ```

### 本周完成

- [ ] Step 1: 准备
- [ ] Step 2: Agent 服务更新
- [ ] Step 3: 方法论页面增强（部分）

### 下周完成

- [ ] Step 4: 赋能工具更新
- [ ] Step 5: 培训课程更新
- [ ] Step 6: 白皮书更新

### 本月完成

- [ ] Step 7: 博客内容
- [ ] 整体验证
- [ ] 用户反馈收集

---

**执行状态**: 准备中
*基于真实网站现状制定 | 2026-03-22*
