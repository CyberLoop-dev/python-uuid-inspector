<div align="center">

![Header](https://capsule-render.vercel.app/api?type=waving&color=0:111827,100:0f766e&height=170&section=header&text=UUID%20Inspector&fontSize=34&fontColor=ffffff&animation=twinkling)

[![Typing](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=19&pause=1000&color=14B8A6&center=true&vCenter=true&width=650&lines=Small+tool%2C+clear+insight;Local-first+%E2%80%A2+Beginner-friendly)](https://git.io/typing-svg)

![License](https://img.shields.io/github/license/CyberLoop-dev/python-uuid-inspector)
![Language](https://img.shields.io/github/languages/top/CyberLoop-dev/python-uuid-inspector)
![Stars](https://img.shields.io/github/stars/CyberLoop-dev/python-uuid-inspector)
![Last commit](https://img.shields.io/github/last-commit/CyberLoop-dev/python-uuid-inspector)

![Project mark](assets/mark.svg)

</div>

## 📖 Overview

A small local CLI for extracting UUID strings from text and identifying their version, variant, timestamp when defined, and duplicate occurrences. Input stays on the machine.

## ✨ Features

- 🔎 Find canonical UUID strings in pasted text or local files
- 🏷️ Show UUID version and variant
- 🕒 Decode timestamps for supported time-based UUID versions
- ♻️ Count repeated UUID values
- 🧾 Export JSON for downstream checks

## 🖥️ Demo

No hosted demo is claimed. Run the project locally using the steps below.

## 🚀 Quick Start

```bash
python -m pip install -e .
uuid-inspector 550e8400-e29b-41d4-a716-446655440000
uuid-inspector --file ids.txt --json
```

## 🧰 Tech Stack

Python 3.10+ standard library (`uuid`, `re`, `datetime`, `argparse`).

## 🗂️ Folder Structure

```text
python-uuid-inspector/
├── uuid_inspector.py
├── tests/test_uuid_inspector.py
├── assets/mark.svg
├── pyproject.toml
├── .gitignore
├── LICENSE
└── README.md
```

## 🗺️ Roadmap

- [ ] Add more edge-case examples
- [ ] Improve machine-readable output and documentation
- [ ] Expand the automated test fixtures

## 🤝 Contributing

Issues and pull requests are welcome. Keep changes focused, document behavior, and add a regression test for each bug fix.

## 📄 License

Released under the [MIT License](LICENSE).

<div align="center">

![Footer](https://capsule-render.vercel.app/api?type=waving&color=0:0f766e,100:111827&height=110&section=footer&animation=twinkling)

</div>
