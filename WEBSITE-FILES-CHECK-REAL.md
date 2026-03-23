# SocienceAI 网站文件核查报告

**核查日期**: 2026-03-22  
**网站根目录**: `D:\socienceAI\`  
**核查状态**: ✅ 文件完整

---

## 📁 网站文件结构

### 完整目录结构

```
D:\socienceAI\
├── index.html                    # 首页
├── ai-agents.html                # Agent 服务
├── resources.html                # 精品 AI
├── styles.css                    # 样式文件
├── favicon.ico                   # 网站图标
├── logo.svg                      # Logo 文件
│
├── Tech/                         # 赋能工具目录
│   ├── index.html                # 工具首页
│   ├── heterogeneous-agent-collaboration-system/
│   │   └── index.html            # Stigmergy 页面
│   ├── AiProductDesign.html      # AI 产品设计
│   └── AiMarketingTechnology.html # AI 营销技术
│
├── agents/                       # Agent 服务目录
│   └── dist/
│       └── index.html            # Agent 服务页面
│
├── courses/                      # 培训课程
│   └── courses.html
│
├── whitePaper/                   # 白皮书
│   ├── index.html
│   ├── disciplines.html
│   ├── tools.html
│   ├── tutorial.html
│   └── results_showcase.html
│
├── Dao/                          # 关于我们
│   ├── index.html
│   └── Manifesto.html
│
├── blog/                         # 博客
│
├── contact.html                  # 联系我们
└── privacy.html                  # 隐私政策
```

---

## 🎯 微调方案

### 修改文件：`D:\socienceAI\index.html`

### 修改 1: Hero 区 CTA 按钮

**搜索**: `智能体协同平台`  
**替换为**: `技能协同平台`

**位置**: 约第 150-200 行

### 修改 2: 服务板块第一卡片

**搜索**: `社会科学专业技能`  
**修改标题为**: `社会科学专业技能（12 种方法论技能）`

**搜索**: `扎根理论分析、场域分析、社会网络分析等专业技能`  
**替换为**: `扎根理论、社会网络分析、行动者网络理论、布迪厄场域分析、QCA、DID 等 12 种专业方法论技能，一键加载，手把手教你做研究。`

**增加内容**（在卡片描述后）:
```html
<p style="margin-top: 1rem; padding: 0.5rem; background: #f0f9ff; border-radius: 0.25rem; font-size: 0.875rem;">
<strong>🔥 首推平台：</strong>WorkBuddy（研究者首选）| Stigmergy（多 CLI 协同）| Coze（免费额度）| 钉钉悟空（企业集成）| Qwen（中文能力强）
</p>
<p style="margin-top: 0.5rem; font-size: 0.875rem;">
<strong>📚 技能列表：</strong>扎根理论 | 社会网络分析 | 行动者网络理论 | 布迪厄场域分析 | QCA | DID | 回归分析 | 问卷设计 | 混合方法 | 数字马克思 | 数字涂尔干 | 数字韦伯
</p>
<p style="margin-top: 0.5rem;">
<a href="/skills/" style="color: #2563eb; text-decoration: none; font-weight: 600;">查看全部 12 种技能 →</a>
</p>
```

### 修改 3: 页脚链接

**搜索**: `Agent 服务`  
**替换为**: `方法论技能`

**搜索**: `/ai-agents.html`  
**替换为**: `/skills/`（或新建的技能页面）

---

## 🚀 执行步骤

### Step 1: 备份原文件

```bash
# 复制原文件
copy D:\socienceAI\index.html D:\socienceAI\backup\index-2026-03-22-backup.html
```

### Step 2: 修改文件

**使用文本编辑器打开**:
```
D:\socienceAI\index.html
```

**搜索替换**:
1. `智能体协同平台` → `技能协同平台`
2. `社会科学专业技能` → `社会科学专业技能（12 种方法论技能）`
3. `Agent 服务` → `方法论技能`

### Step 3: 验证修改

**打开本地文件**:
```
D:\socienceAI\index.html
```
在浏览器中打开，检查修改是否正确。

### Step 4: FTP 上传

**上传文件**: `D:\socienceAI\index.html`  
**远程路径**: `/htdocs/index.html`

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

## 📂 相关目录

### 技能页面（新建）

**建议创建**: `D:\socienceAI\skills\index.html`

**内容**: 12 种方法论技能详情页

**链接**: 从首页"查看全部 12 种技能"链接到该页面

---

**核查日期**: 2026-03-22  
**核查者**: SocienceAI Soul  
**状态**: 文件完整，准备微调

*立即行动，快速执行*
