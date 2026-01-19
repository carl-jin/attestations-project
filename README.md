# Python GUI 测试应用

一个简单的 Python GUI 应用，用于演示 GitHub Actions + Artifact Attestation 的安全发布流程。

## 功能

- 显示测试页面
- 点击按钮弹出 "Hello World!" 对话框

## 本地运行

```bash
python app.py
```

## 下载

从 [Releases](../../releases) 页面下载对应平台的可执行文件。

## 验证软件来源

下载后，使用 GitHub CLI 验证文件来源：

```bash
gh attestation verify ./testapp-linux --repo your-org/your-repo
```

验证成功表示该软件确实由官方 CI 构建。

## 发布新版本

```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```
