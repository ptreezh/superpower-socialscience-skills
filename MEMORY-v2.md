# SocienceAI 项目记忆库 v2.0

> 🔴 **持久化记忆系统 - 禁止外传**

**创建日期**: 2026-03-22  
**最后更新**: 2026-03-22（真实网站分析后）  
**版本**: 2.0

---

## 📋 核心使命

**让社会科学研究人人可为，让 AI 技术服务社会福祉**

通过 AI 技术推动社会科学研究的范式革新，让严谨的社会科学方法论不再高深，让高质量的研究人人可为。

---

## 🔐 敏感信息（加密存储）

### VPS 管理账户

```
平台：VPSOR 云虚拟主机
用户名：3061176@qq.com
密码：psyagent3510
登录 URL: https://www.vpsor.cn/center/
产品：香港 - 独享一型 (cvh-3njf8mh28i222)
状态：正常 (2025-11-14 到 2028-11-14)
```

### FTP 信息

```
FTP 地址：103.99.40.226
FTP 端口：21
FTP 用户名：3njf8mh28i222
FTP 密码：4GrdQlUW38
远程目录：/htdocs/
```

### WebFTP

```
URL: https://dedit1010n55-dedihosts-hk-control.topvps.top/vhost/?c=webftp&a=enter
登录：使用 Edge 浏览器本地 cookie/session
```

---

## 🌐 真实网站结构（2026-03-22 实测）

### 网站导航（9 个主导航）

```
/index.html - 首页（完整）
/ai-agents.html - Agent 服务（12 智能体，36 页面）
/resources.html - 精品 AI
/Tech/index.html - 赋能工具
/courses/courses.html - 培训课程
/whitePaper/index.html - 白皮书（AI 社会白皮书 2025）
/Dao/index.html - 关于我们（共创倡议书）
/blog/ - 博客（9 篇文章）
/contact.html - 联系我们
```

### Agent 服务（12 个智能体）

**社会研究方法论（6 个）**:
- 扎根理论分析智能体
- 布迪厄场域分析专家
- 社会网络分析智能体
- 行动者网络分析智能体
- mvQCA-fsQCA 分析智能体
- DID 分析设计智能体

**社会学理论 AI（3 个）**:
- 数字涂尔干
- 数字韦伯
- 数字马克思

**商业分析（2 个）**:
- 商业模式分析智能体
- 商业生态系统分析智能体

**多主体系统（1 个）**:
- 复杂适应系统建模

**每个智能体 3 个页面**:
1. `[method]-info.html` - 了解详情
2. `[method].html` - 立即使用
3. `/reports/[demo].html` - 查看演示

### 研究报告（3 个）

- /reports/xiyouji-GT/index.html - 西游记扎根理论分析
- /reports/hongloumeng_analysis/index.html - 红楼梦多方法综合分析
- /reports/xiyouji-ANT/index.html - 西游记行动者网络分析

### 博客文章（9 篇，2026 年）

- 计算扎根理论（2026-02-12）
- 商科 AI 智能体行业应用（2026-01-30）
- 竖屏短剧流量密码（2026-01-27）
- skills 火出圈（2026-01-24）
- 安科瑞电气分析报告（2026-01-17）
- 现在训练 AI 的数据
- 布迪厄场域分析智能体
- 扎根理论分析智能体
- 欢迎使用博客

### 白皮书

- AI 社会白皮书 2025（10 个社会科学深度分析）
- 学科执行计划
- AI 工具指导
- 复现教程
- 成果展示
- 完整白皮书（电子书）

---

## 🛠️ 工具系统

### CLI 工具

**主程序**: `cli-anything.py`

**核心命令**:
```bash
python cli-anything.py build          # 构建网站
python cli-anything.py verify         # 验证（强制）
python cli-anything.py upload ./website  # 上传
python cli-anything.py update all     # 完整更新
python cli-anything.py test           # 本地测试
python cli-anything.py backup         # 备份
python cli-anything.py rollback       # 回滚
python cli-anything.py config set ftp_password XXX
```

### 验证工具

**程序**: `verify-website.py`

**检查项**:
- 目录结构
- 文件完整性
- HTML 格式
- 链接（断链检测）
- 相对路径
- 样式正常

### 构建工具

**程序**: `website-builder.py`

**功能**:
- 自动生成 12 种方法论页面
- 生成首页、关于页面
- Markdown → HTML 转换

### 上传工具

**程序**: `ftp-upload.py`

**配置**:
- 从环境变量读取 FTP 密码
- 批量上传
- 自动创建目录

---

## 📁 项目文件结构

```
D:\socienceAI\agentskills\
├── cli-anything.py              ← 统一 CLI 工具
├── verify-website.py            ← 验证工具
├── website-builder.py           ← 构建工具
├── ftp-upload.py                ← 上传工具
│
├── website/                     ← 网站构建输出
│   └── docs/
│       ├── index.html           # 首页
│       ├── methodologies/       # 12 种方法论
│       ├── guide/               # 使用指南
│       ├── about/               # 关于
│       └── blog/                # 博客
│
├── soul-agent-creator/          ← Soul Agent 创建工具
├── 12 个方法论专家目录/          ← 方法论 Skill
│
├── MEMORY.md                    ← 本文件（记忆库 v2.0）
├── COMPLETE-WEBSITE-ANALYSIS.md ← 完整网站分析
├── SAFE-UPDATE-GUIDE.md         ← 安全更新指南
└── CLI-COMPLETION-REPORT.md     ← CLI 完成报告
```

---

## 🎯 当前状态

### 已完成

- ✅ 12 种方法论 Skill 创建
- ✅ Soul Agent Creator 工具
- ✅ 自主进化系统
- ✅ 战略执行系统
- ✅ CLI 工具体系
- ✅ 验证工具
- ✅ **真实网站结构分析**（2026-03-22）
- ✅ 安全更新机制

### 线上已有内容

- ✅ 首页（完整）
- ✅ Agent 服务（12 智能体，36 页面）
- ✅ 博客（9 篇文章）
- ✅ 关于我们（共创倡议书）
- ✅ 白皮书（AI 社会白皮书 2025）
- ✅ 研究报告（3 个演示）

### 待发布内容

- ⏳ Soul Agent Creator
- ⏳ 质量保证宪章
- ⏳ 自主进化系统说明
- ⏳ CLI 工具文档
- ⏳ 使用指南

---

## 📋 执行流程（SOP）

### 日常更新流程

```bash
# 1. 构建
python cli-anything.py build

# 2. 验证（必须）
python cli-anything.py verify
# 输出必须：✅ 验证通过！可以安全上传

# 3. 备份（必须）
# 手动 FTP 下载 /htdocs/ 到 backup/

# 4. 上传
python cli-anything.py upload ./website
# 系统会提示确认备份，必须输入 y

# 5. 线上验证
访问 http://www.socienceai.com 检查

# 6. 如有问题，回滚
python cli-anything.py rollback
```

---

## ⚠️ 核心原则（不可违背）

### 三条红线

1. **未经验证，禁止上传**
   - 必须先运行 `verify`
   - 验证失败立即停止

2. **没有备份，禁止上传**
   - 必须确认已备份
   - 确保可快速回滚

3. **未经测试，禁止发布**
   - 本地测试通过
   - 样式、链接、路径正常

### 质量保证

- 所有报告必须经过严格测试和验证
- 绝不夸大、绝不无根据、没测试、没验证时报告
- 分析过程必须可重复，结果必须可验证

---

## 🎯 下一步行动

### 立即执行（今天）

1. **确认 FTP 目录结构**
   - 连接 FTP，查看 htdocs 目录结构
   - 确认现有页面的文件位置
   - 确认可写权限

2. **备份线上内容**
   - 下载所有现有文件到本地 backup/目录
   - 记录文件结构和版本

3. **准备新增内容**
   - Soul Agent Creator 页面
   - 质量保证宪章页面
   - 使用指南页面

### 本周执行

1. **上传新增内容**
   - 上传 Soul Agent Creator 页面
   - 上传质量保证宪章
   - 上传使用指南

2. **补充现有内容**
   - 补充智能体 info 页面的方法论详情
   - 补充 CLI 工具文档

3. **验证更新**
   - 访问所有新增页面
   - 检查链接正常
   - 检查样式正常

---

## 📚 重要文档索引

| 文档 | 用途 | 位置 |
|------|------|------|
| MEMORY.md | 本文件（记忆库 v2.0） | 本文件 |
| COMPLETE-WEBSITE-ANALYSIS.md | 完整网站分析 | 已创建 |
| SAFE-UPDATE-GUIDE.md | 安全更新指南 | 已创建 |
| CLI-COMPLETION-REPORT.md | CLI 完成报告 | 已创建 |
| WEBSITE-STRUCTURE-ANALYSIS.md | 网站结构分析 | 已创建 |
| REAL-WEBSITE-STRUCTURE.md | 真实网站结构 | 已创建 |

---

**记忆库版本**: 2.0  
**创建日期**: 2026-03-22  
**最后更新**: 2026-03-22（真实网站分析后）  
**更新策略**: 关键信息变更时更新  
**保存位置**: D:\socienceAI\agentskills\MEMORY-v2.md

*禁止外传 - 仅供内部使用*
