# BERT‑HAN++

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Model](https://img.shields.io/badge/Model-BERT--HAN%2B%2B-purple.svg)
![Platform](https://img.shields.io/badge/Platform-Cross--lingual%20NLP-orange.svg)
![Conference](https://img.shields.io/badge/Conference-Scopus--Indexed%20ICACCIS--2025-red.svg)

> **BERT‑HAN++: A Cross‑Lingual Hierarchical Transformer with Adaptive Complexity and SHAP‑Attention Fusion for Efficient & Interpretable Document Classification**

---

## 🧠 Abstract

**BERT‑HAN++** is a hybrid architecture that fuses:

* **BERT** for deep contextual encoding
* **Hierarchical Attention Networks (HAN)** for document‑level structure awareness
* **SHAP‑enhanced interpretability** for faithful token‑level rationales

### Key Contributions

| Innovation                      | Impact                                                     |
| ------------------------------- | ---------------------------------------------------------- |
| Adaptive Complexity Controller  | ⬇️ Latency & FLOPs by dynamically skipping inactive layers |
| Cross‑Lingual Self‑Distillation | 🌐 Robust multilingual representations via *mBERT*         |
| Attn‑SHAP Fusion                | ✅ Faithful, human‑readable explanations                    |
| Edge‑Friendly Quantisation      | ⚡ 8‑bit inference (≤0.3 % ΔAcc) & 2.1× speed‑up            |

---

## 📊 Benchmarks

| Dataset              | Macro‑F1 (↑) | Inference Speed (↓) | Notes                          |
| -------------------- | ------------ | ------------------- | ------------------------------ |
| AG News              | **97.8**     | 1.0×                | English, 4‑class               |
| DBPedia              | **99.3**     | 1.1×                | English, 14‑class              |
| Yahoo Answers        | **80.4**     | 1.0×                | English, 10‑class              |
| 20 NG                | **89.7**     | 1.2×                | English, 20‑class              |
| IMDB                 | **94.1**     | 1.0×                | English, sentiment             |
| Hindi AG News        | **95.6**     | 1.0×                | ✨ Cross‑lingual generalisation |
| Spanish Billion Word | **91.2**     | 1.0×                | ✨ Cross‑lingual generalisation |

*Numbers are averaged over 5 runs; speed reported relative to BERT‑base.*

---

## 🛠️ Core Modules

```
BERT Sentence Encoder   ─┐
                         ├─▶ Hierarchical Document Transformer ─┐
Adaptive Complexity Gates ┘                                     │
Cross‑Lingual KD (mBERT)                                        │
                                                               ▼
                     Attn‑SHAP Fusion  ──▶ INT8 Quantised Head ──▶ Output
```

---

## 📂 Repository Layout

```bash
.
├── models/                  # PyTorch / HF model definitions (BERT‑HAN++)
├── data/                    # Scripts + links for all datasets
├── notebooks/               # End‑to‑end Colab & Jupyter demos
├── utils/                   # Helper utilities (logging, SHAP wrappers)
├── results/                 # Saved weights, logs, figures & tables
├── requirements.txt         # Python deps (PyTorch >=1.13, transformers >=4.40)
├── README.md                # ✨ You are here
└── bert_han_paper.pdf       # Camera‑ready ICACCIS‑2025 paper (optional)
```

---

## 🚀 Quick Start

### 1. Clone & Install

```bash
git clone https://github.com/<YOUR‑ORG>/bert‑han‑plus‑plus.git
cd bert‑han‑plus‑plus
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Train on a Benchmark

```bash
python train.py \
  --dataset ag_news \
  --epochs 5 \
  --adaptive-gating on \
  --int8-ptq off
```

### 3. Evaluate a Checkpoint

```bash
python evaluate.py \
  --dataset ag_news \
  --checkpoint results/ag_news/best.pt \
  --int8-ptq on
```

### 4. Visualise Explanations

```bash
python explain.py \
  --text "OpenAI acquires leading robotics startup." \
  --checkpoint results/ag_news/best.pt
```

A HTML heat‑map will open in your browser showing Attn‑SHAP token importances.

---


---

## 🤝 Contributing

Pull requests are welcome! Please open an issue first to discuss any major changes.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a PR

---

## 🛡️ License

This project is released under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

* Hugging Face 🤗 transformers & datasets
* SHAP Library
* PyTorch Lightning
s
