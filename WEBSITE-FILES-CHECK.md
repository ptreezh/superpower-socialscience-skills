# SocienceAI 本地网站文件核查报告

**核查日期**: 2026-03-22  
**核查范围**: D:\socienceAI\agentskills\website\

---

## ✅ 网站文件结构

### 完整目录结构

```
website/
├── docs/
│   ├── .vitepress/          # VitePress 配置
│   │   └── config.mts       # 配置文件
│   ├── about/               # 关于页面
│   ├── blog/                # 博客页面
│   ├── guide/               # 使用指南
│   ├── methodologies/       # 方法论页面
│   ├── tools/               # 工具页面
│   ├── index.html           # 首页（已生成）
│   └── index.md             # 首页源码
├── build-state.json         # 构建状态
├── package.json             # NPM 配置
└── README.md                # 说明文档
```

### 关键文件

| 文件 | 路径 | 状态 | 说明 |
|------|------|------|------|
| **首页源码** | `website/docs/index.md` | ✅ 存在 | Markdown 格式 |
| **首页 HTML** | `website/docs/index.html` | ✅ 存在 | 已生成的 HTML |
| **VitePress 配置** | `website/docs/.vitepress/config.mts` | ✅ 存在 | 网站配置 |
| **方法论页面** | `website/docs/methodologies/` | ✅ 存在 | 方法论技能页面目录 |
| **使用指南** | `website/docs/guide/` | ✅ 存在 | 教程目录 |

---

## 📋 微调方案

### 方案 A: 修改 index.md（推荐）

**优点**:
- ✅ Markdown 格式，易于编辑
- ✅ 修改后重新生成 HTML
- ✅ 符合 VitePress 工作流

**步骤**:
1. 编辑 `website/docs/index.md`
2. 修改关键内容（智能体→技能）
3. 重新生成 HTML：`npm run build`
4. 上传生成的 `index.html`

### 方案 B: 直接修改 index.html

**优点**:
- ✅ 直接修改，立即生效
- ✅ 无需重新构建

**缺点**:
- ⚠️ HTML 文件较大
- ⚠️ 下次构建会被覆盖

**步骤**:
1. 编辑 `website/docs/index.html`
2. 搜索替换关键内容
3. 上传到服务器

---

## 🎯 微调内容

### 修改 1: Hero 区 CTA 按钮

**位置**: `website/docs/index.md` 或 `website/docs/index.html`

**原文案**:
```
智能体协同平台
```

**修改为**:
```
技能协同平台
```

### 修改 2: 服务板块第一卡片

**原文案**:
```
社会科学专业技能
扎根理论分析、场域分析、社会网络分析等专业技能...
```

**修改为**:
```
社会科学专业技能（12 种方法论技能）
扎根理论、社会网络分析、行动者网络理论、布迪厄场域分析、QCA、DID 等 12 种专业方法论技能...

🔥 首推平台：WorkBuddy（研究者首选）| Stigmergy（多 CLI 协同）| Coze（免费额度）| 钉钉悟空（企业集成）| Qwen（中文能力强）

📚 技能列表：扎根理论 | 社会网络分析 | 行动者网络理论 | 布迪厄场域分析 | QCA | DID | 回归分析 | 问卷设计 | 混合方法 | 数字马克思 | 数字涂尔干 | 数字韦伯

[查看全部 12 种技能 →](/skills/)
```

### 修改 3: 页脚链接

**原文案**:
```
Agent 服务
```

**修改为**:
```
方法论技能
```

---

## 🚀 执行步骤

### Step 1: 编辑文件

**使用文本编辑器打开**:
```
D:\socienceAI\agentskills\website\docs\index.md
```

或
```
D:\socienceAI\agentskills\website\docs\index.html
```

### Step 2: 搜索替换

**搜索**: `智能体`  
**替换为**: `技能`

**搜索**: `Agent 服务`  
**替换为**: `方法论技能`

### Step 3: 增加技能栏目

在"社会科学专业技能"卡片中增加：
```markdown
**🔥 首推平台**: WorkBuddy（研究者首选）| Stigmergy（多 CLI 协同）| Coze（免费额度）| 钉钉悟空（企业集成）| Qwen（中文能力强）

**📚 技能列表**: 扎根理论 | 社会网络分析 | 行动者网络理论 | 布迪厄场域分析 | QCA | DID | 回归分析 | 问卷设计 | 混合方法 | 数字马克思 | 数字涂尔干 | 数字韦伯

[查看全部 12 种技能 →](/skills/)
```

### Step 4: 重新构建（如果修改 index.md）

```bash
cd D:\socienceAI\agentskills\website
npm run build
```

### Step 5: FTP 上传

**上传文件**:
- `website/docs/index.html` → `/htdocs/index.html`

**FTP 信息**:
```
FTP 地址：103.99.40.226
FTP 用户名：3njf8mh28i222
FTP 密码：4GrdQlUW38
```

---

## ✅ 验证清单

- [ ] Hero 区"智能体协同平台"改为"技能协同平台"
- [ ] 服务板块第一卡片增加 12 种方法论技能说明
- [ ] 服务板块第一卡片增加首推平台
- [ ] 服务板块第一卡片增加技能列表
- [ ] 页脚"Agent 服务"改为"方法论技能"
- [ ] 页面样式正常
- [ ] 链接正常

---

**核查日期**: 2026-03-22  
**核查者**: SocienceAI Soul  
**状态**: 文件完整，准备微调

*立即行动，快速执行*
