# SocienceAI 项目持久化记忆库

**版本**: 3.0（最终版）  
**创建日期**: 2026-03-22  
**最后更新**: 2026-03-22  
**保存位置**: `D:\socienceAI\agentskills\PROJECT-MEMORY.md`

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

### 网站管理

```
网站 URL: http://www.socienceai.com
网站类型: 静态网站
部署方式：FTP 上传
网站根目录：/htdocs/
```

---

## 🎯 核心使命

**让社会科学研究人人可为，让 AI 技术服务社会福祉**

通过 AI 技术推动社会科学研究的范式革新，让严谨的社会科学方法论不再高深，让高质量的研究人人可为。

---

## 📊 战略定位

### 目标用户

**核心用户**:
- 📚 社会科学研究生/博士生（论文压力大）
- 👨‍🏫 高校教师/研究员（科研压力）
- 📖 文科本科生（方法论基础弱）
- 🏢 企业研究者/咨询顾问（需要专业工具）

**用户痛点**:
- ❌ 方法论太难学
- ❌ 数据分析没思路
- ❌ 工具太复杂
- ❌ 没人指导

**解决方案**:
- ✅ 保姆级指导
- ✅ 专业方法论
- ✅ 人格化智能体
- ✅ 一键生成
- ✅ 多平台支持

### 价值主张

```
旧：让 AI 智能体为你服务
新：让专业方法论技能在你的 AI 工具中运行
```

### 首推平台（5 个）

| 平台 | 类型 | 推荐度 | 核心卖点 |
|------|------|--------|---------|
| **WorkBuddy** | CLI 工具 | ⭐⭐⭐⭐⭐ | 研究者首选，本地部署，数据安全 |
| **Stigmergy** | CLI 协调器 | ⭐⭐⭐⭐⭐ | 多 CLI 协同，技能通用 |
| **Coze 编程** | 云端 Bot | ⭐⭐⭐⭐⭐ | 免费额度，网页访问 |
| **钉钉悟空** | 企业 Bot | ⭐⭐⭐⭐⭐ | 企业集成，免费使用 |
| **Qwen** | CLI/API | ⭐⭐⭐⭐⭐ | 中文能力强，有免费额度 |

**重要说明**:
- WorkBuddy 和 Stigmergy 需要自备 AI 算力
- Coze、钉钉悟空、Qwen 有免费额度
- Stigmergy 不是 AI 模型，是 CLI 协调器
- Stigmergy 是独立开源项目，与 SocienceAI 无直接关系

---

## 📦 技能包规范

### agentskills.io 规范

```
skill-package/
├── SKILL.md              # 技能定义（必需）
├── skill.yaml            # 技能配置（必需）
├── tools/                # 工具模块（可选）
│   ├── __init__.py
│   └── tool_name.py
├── templates/            # 模板文件（可选）
├── examples/             # 使用示例（可选）
└── README.md             # 使用说明（推荐）
```

### SKILL.md 格式

```markdown
---
name: skill-name
description: |
  技能的触发描述和使用场景。
  当用户想要做 X 时使用此技能。
  触发条件：[具体触发场景]
---

# 技能正文

## 角色定义
你是 XXX 专家，专注于...

## 工作流程
1. 第一步...
2. 第二步...

## 输出规范
- 必须...
- 禁止...
```

### skill.yaml 格式

```yaml
---
name: skill-name
version: 1.0.0
description: 技能的详细描述
author: Author Name
license: MIT

metadata:
  version: "1.0.0"
  type: "methodology"
  category: "social-science"

inputs:
  task:
    type: string
    required: true
    description: 任务描述

outputs:
  result:
    type: object
    description: 执行结果

prompts:
  system: SKILL.md

tools:
  - name: tool-name
    description: 工具描述
    module: tool_module

compatibility:
  - agentskills.io
  - workbuddy
  - stigmergy
  - openclaw

allowed-tools: Read Write Bash --allow
---
```

---

## 📚 可用技能（12 种）

### 质性研究方法（4 种）

| 技能 | 对标学者 | 核心功能 | 文件位置 |
|------|---------|---------|---------|
| **扎根理论** | Kathy Charmaz | 开放编码、轴心编码、选择式编码 | `grounded-theory-expert/` |
| **社会网络分析** | Linton Freeman | 中心性分析、社区检测、结构洞 | `social-network-analysis-expert/` |
| **行动者网络理论** | Bruno Latour | 行动者识别、转译过程、网络追踪 | `actor-network-analysis-expert/` |
| **布迪厄场域分析** | Pierre Bourdieu | 场域识别、资本分析、习性分析 | `bourdieu-field-analysis-expert/` |

### 定量研究方法（4 种）

| 技能 | 对标学者 | 核心功能 | 文件位置 |
|------|---------|---------|---------|
| **QCA** | Charles Ragin | 模糊集校准、真值表、布尔最小化 | `qca-analysis-expert/` |
| **DID** | Angrist & Pischke | 平行趋势检验、双向固定效应 | `did-analysis-expert/` |
| **回归分析** | Ronald Fisher | OLS 估计、假设检验、模型诊断 | `regression-analysis-expert/` |
| **问卷设计** | Don A. Dillman | 问题设计、抽样方法、信效度检验 | `survey-design-expert/` |

### 混合方法与社会理论（4 种）

| 技能 | 对标学者 | 核心功能 | 文件位置 |
|------|---------|---------|---------|
| **混合方法** | John Creswell | 三角验证、互补设计、转换整合 | `mixed-methods-expert/` |
| **数字马克思** | David Harvey | 数字劳动、剩余价值、意识形态批判 | `digital-marx-expert/` |
| **数字涂尔干** | Émile Durkheim | 集体意识、社会团结、神圣世俗 | `digital-durkheim-expert/` |
| **数字韦伯** | Max Weber | 理性化、科层制、祛魅 | `digital-weber-expert/` |

---

## 🚀 网站更新方法

### FTP 上传流程

**步骤 1: 连接 FTP**
```bash
# 使用 FTP 客户端（如 FileZilla）
主机：103.99.40.226
端口：21
用户名：3njf8mh28i222
密码：4GrdQlUW38
```

**步骤 2: 备份线上内容**
```bash
# 下载所有现有文件到本地 backup/目录
# 记录文件结构和版本
```

**步骤 3: 上传新内容**
```bash
# 将本地文件上传到 /htdocs/目录
# 保持目录结构一致
```

**步骤 4: 验证更新**
```bash
# 访问 http://www.socienceai.com
# 检查所有页面正常
# 检查所有链接正常
```

### WebFTP 上传流程

**步骤 1: 打开 WebFTP**
```
URL: https://dedit1010n55-dedihosts-hk-control.topvps.top/vhost/?c=webftp&a=enter
使用 Edge 浏览器（已有 session）
```

**步骤 2: 导航到目标目录**
```
进入 /htdocs/目录
选择对应子目录
```

**步骤 3: 上传文件**
```
点击"上传"按钮
选择本地文件
等待上传完成
```

**步骤 4: 验证**
```
访问 http://www.socienceai.com
检查页面正常
```

### 网站内容结构

```
/htdocs/
├── index.html                    # 首页
├── ai-agents.html                # Agent 服务
├── resources.html                # 精品 AI
├── Tech/
│   ├── index.html                # 赋能工具首页
│   ├── AiProductDesign.html      # AI 产品设计
│   └── AiMarketingTechnology.html # AI 营销技术
├── courses/
│   └── courses.html              # 培训课程
├── whitePaper/
│   ├── index.html                # 白皮书首页
│   ├── disciplines.html          # 学科执行计划
│   ├── tools.html                # AI 工具指导
│   ├── tutorial.html             # 复现教程
│   ├── results_showcase.html     # 成果展示
│   └── comprehensive_social_sciences_ebook_complete.html
├── Dao/
│   ├── index.html                # 关于我们
│   └── Manifesto.html            # 项目使命
├── blog/                         # 博客
├── contact.html                  # 联系我们
└── privacy.html                  # 隐私政策
```

---

## 📖 平台使用教程

### WorkBuddy 使用流程

```bash
# 1. 安装 WorkBuddy
npm install -g workbuddy

# 2. 下载技能
git clone https://github.com/socienceai/agentskills.git

# 3. 加载技能
cp -r grounded-theory-expert ~/.workbuddy/skills/

# 4. 使用技能
workbuddy --skill grounded-theory-expert "任务描述"
```

### Stigmergy 使用流程

```bash
# 1. 安装至少一个 AI CLI 工具（需要 API Key）
npm install -g gemini-cli  # Gemini（有免费额度）
npm install -g qwen-cli    # Qwen（有免费额度）

# 2. 安装 Stigmergy
npm install -g stigmergy@beta

# 3. 安装 SocienceAI 技能
stigmergy skill install socienceai/agentskills

# 4. 使用技能
stigmergy call --skill grounded-theory-expert "任务描述"
```

### Coze 使用流程

```
1. 访问 https://www.coze.cn/
2. 注册/登录
3. 创建 Bot
4. 配置人设（复制 SKILL.md 内容）
5. 添加插件（对应 tools/）
6. 上传知识库（对应 templates/）
7. 发布 Bot
```

### 钉钉悟空使用流程

```
1. 打开钉钉
2. 搜索"悟空助手"
3. 添加到工作台
4. 配置使用
```

### Qwen 使用流程

```bash
# 1. 安装 Qwen CLI
npm install -g qwen-cli

# 2. 配置 API Key（新用户有免费额度）
qwen config --api-key YOUR_API_KEY

# 3. 下载技能
git clone https://github.com/socienceai/agentskills.git
cp -r grounded-theory-expert ~/.qwen/skills/

# 4. 使用技能
qwen --skill grounded-theory-expert "任务描述"
```

---

## 📋 网站更新计划

### Phase 1: 导航调整（第 1 周）

**任务**:
- [ ] 更新导航菜单（首推 5 个平台置顶）
- [ ] 创建技能首页（/skills/）
- [ ] 创建教程首页（/tutorials/）

**文件**:
- `index.html` - 首页更新
- `skills-index.html` - 技能首页（新建）
- `tutorials-index.html` - 教程首页（新建）

### Phase 2: 内容创建（第 2 周）

**任务**:
- [ ] 创建 5 个首推平台教程页面
- [ ] 创建 12 种技能详情页面
- [ ] 创建常见问题页面

**文件**:
- `tutorials/workbuddy.html`
- `tutorials/stigmergy.html`
- `tutorials/coze.html`
- `tutorials/dingtalk.html`
- `tutorials/qwen.html`
- `skills/grounded-theory.html`
- `skills/social-network-analysis.html`
- `...` (其他 10 种技能)
- `faq.html`

### Phase 3: 文案优化（第 3 周）

**任务**:
- [ ] 优化首页文案（保姆级、人格化）
- [ ] 优化技能展示文案
- [ ] 优化用户评价文案

**文件**:
- `index.html` - 首页文案优化

### Phase 4: 测试验证（第 4 周）

**任务**:
- [ ] 测试所有链接
- [ ] 测试所有页面显示
- [ ] 收集用户反馈

---

## 📊 内容运营策略

### SEO 关键词

**核心关键词**:
- 社会科学 AI 助手
- 方法论工具
- 扎根理论软件
- 社会网络分析工具
- QCA 分析软件
- 文科生 AI 工具

**长尾关键词**:
- 社会学论文方法论怎么写
- 访谈数据如何分析
- 扎根理论编码怎么做
- 社会网络分析入门
- QCA 分析教程

### 社群运营

**微信群/QQ 群**:
```
群名：社会科学 AI 研究交流群
群价值：方法论交流、经验分享、问题互助
活动：每周分享、每月研讨、每季讲座
```

**内容输出**:
```
公众号：每周 1 篇教程、每周 1 个案例
知乎：方法论问题回答
B 站：使用教程视频
```

### 用户增长

**增长策略**:
```
1. 内容获客（SEO、知乎、公众号）
2. 社群裂变（邀请有礼、用户推荐）
3. 合作推广（高校合作、学术会议）
```

---

## 📚 重要文档索引

### 战略文档

| 文档 | 文件 | 说明 |
|------|------|------|
| 国内平台指南 | `DOMESTIC-PLATFORMS-TOP5.md` | 5 个首推平台详细指南 |
| 战略调整方案 | `STRATEGY-ADJUSTMENT.md` | 战略调整详细方案 |
| 完成报告 | `DOMESTIC-STRATEGY-COMPLETE-V2.md` | 战略完成总结 |

### 教程文档

| 文档 | 文件 | 说明 |
|------|------|------|
| Stigmergy 教程 | `tutorial-stigmergy-real.md` | Stigmergy 真实使用教程 |
| 通用教程 | `tutorial-general.md` | 多平台通用教程 |
| 技能首页 | `skills-index.md` | 技能包首页 |

### 规范文档

| 文档 | 文件 | 说明 |
|------|------|------|
| agentskills.io 规范 | `AGENTSILLS-IO-COMPATIBILITY.md` | 规范兼容性分析 |
| Stigmergy 真实功能 | `STIGMERGY-REAL-FUNCTIONS.md` | Stigmergy 真实功能分析 |

### 内容文档

| 文档 | 文件 | 说明 |
|------|------|------|
| 网站内容更新方案 | `WEBSITE-CONTENT-UPDATE.md` | 完整的网站内容更新方案 |
| 持久化记忆 | 本文件 | 项目完整记忆库 |

---

## ⚠️ 核心原则（不可违背）

### 三条红线

1. **未经验证，禁止上传**
   - 必须先运行验证
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

### 立即执行（本周）

1. **网站内容更新**
   - [ ] 更新导航菜单
   - [ ] 创建技能首页
   - [ ] 创建教程首页
   - [ ] 上传教程文档

2. **GitHub 仓库准备**
   - [ ] 整理技能包结构
   - [ ] 添加使用文档
   - [ ] 准备发布

3. **内容验证**
   - [ ] 测试所有下载链接
   - [ ] 测试所有教程步骤
   - [ ] 验证平台兼容性

---

**记忆库版本**: 3.0（最终版）  
**创建日期**: 2026-03-22  
**最后更新**: 2026-03-22  
**保存位置**: `D:\socienceAI\agentskills\PROJECT-MEMORY.md`  
**备份位置**: 建议备份到云端（加密）

*让社会科学研究人人可为*
