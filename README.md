# Bitlet

**Bitlet** is a lightweight, cross-device file and clipboard sharing utility app for Windows.  
It allows you to transfer text or files between a PC and a cloud-synced folder (like iCloud Drive, Dropbox, OneDrive etc), enabling quick and easy sharing with mobile devices or other systems.

---

## 🚀 Features

- 🔁 One-tap text or file transfer to a cloud folder (e.g., iCloud)
- 📋 Global hotkeys for copying and pasting bits
- 📁 One-time setup with automatic config file generation
- 📦 Lightweight and runs invisibly in the background
- ✨ Clean vector icon and native `.ico` integration

---

## 🧰 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/moddog1025/bitlet.git
cd bitlet
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🛠 Running Bitlet

### Dev Entry Point

```bash
python src/bitlet_core/main.py
```

> First-time use will prompt for your cloud directory and create config files in:
> `%LOCALAPPDATA%\BitletApp`

---

## 🧪 Hotkeys (Default)

| Hotkey             | Action                     |
|--------------------|-----------------------------|
| `Ctrl + Alt + Z`   | Transfer current clipboard as a Bit  |
| `Ctrl + Shift + Z` | Fetch latest incoming TextBit or FileBit  |

---

## 📁 Project Structure

```
bitlet/
├── assets/           # App icons (.ico, .png)
├── src/bitlet_core/  # Main source code
├── requirements.txt
├── pyproject.toml
├── README.md
├── LICENSE
└── .gitignore
```

---

## 📦 Packaging

To build a distributable `.exe`:

```bash
pip install build
python -m build
```

To build an installer (with PyInstaller or Inno Setup), see the packaging section (coming soon).

---

## 📄 License

Licensed under the MIT License.  
© 2025 Cooper Petit
