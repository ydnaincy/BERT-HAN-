from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="bert-han-plus-plus",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@domain.com",
    description="A Cross-Lingual Hierarchical Transformer with Adaptive Complexity and SHAP-Attention Fusion",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/bert-han-plus-plus",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "isort>=5.12.0",
            "flake8>=6.0.0",
            "mypy>=1.4.0",
        ],
        "edge": [
            "tensorrt>=8.6.0",
            "onnx>=1.14.0",
            "onnxruntime>=1.15.0",
            "nvidia-ml-py>=12.535.77",
        ],
        "all": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "isort>=5.12.0",
            "flake8>=6.0.0",
            "mypy>=1.4.0",
            "tensorrt>=8.6.0",
            "onnx>=1.14.0",
            "onnxruntime>=1.15.0",
            "nvidia-ml-py>=12.535.77",
        ],
    },
    entry_points={
        "console_scripts": [
            "bert-han-train=bert_han_plus_plus.cli:train",
            "bert-han-eval=bert_han_plus_plus.cli:evaluate",
            "bert-han-deploy=bert_han_plus_plus.cli:deploy",
        ],
    },
    include_package_data=True,
    package_data={
        "bert_han_plus_plus": ["configs/*.yaml", "data/*.json"],
    },
    keywords="bert, attention, transformer, nlp, text-classification, interpretability, quantization",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/bert-han-plus-plus/issues",
        "Source": "https://github.com/yourusername/bert-han-plus-plus",
        "Documentation": "https://bert-han-plus-plus.readthedocs.io/",
    },
)
