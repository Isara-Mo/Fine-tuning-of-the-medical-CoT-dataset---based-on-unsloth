# Fine-tuning of the Medical CoT Dataset - Based on Unsloth

[中文](#中文版本) | [English](#english-version)

---

## English Version

### Project Overview

This project provides a comprehensive fine-tuning framework for medical Chain-of-Thought (CoT) datasets using the efficient [Unsloth](https://github.com/unslothai/unsloth) library. It enables the training of high-quality medical reasoning models with optimized memory usage and computation speed.

### Features

- **Efficient Fine-tuning**: Leverages Unsloth for 2-5x faster training with reduced memory consumption
- **Medical CoT Datasets**: Support for multiple medical reasoning and chain-of-thought datasets
- **Flexible Architecture**: Easy-to-customize notebooks and scripts for various use cases
- **Inference Support**: Pre-built inference capabilities for model evaluation and deployment

### Project Structure

```
├── 1.py                          # Utility script
├── fine_turning.ipynb            # Basic fine-tuning notebook
├── full_fine_turning.ipynb       # Complete fine-tuning pipeline
├── Medical_inference.ipynb       # Inference and model evaluation
├── unsloth.ipynb                 # Unsloth setup and examples
└── Model_weight/                 # Directory for storing model weights
    └── sample/                   # Sample model weights
```

### Datasets

#### medical-o1-reasoning-SFT Dataset

A comprehensive dataset for medical reasoning and supervised fine-tuning:
- **Source**: [medical-o1-reasoning-SFT on Hugging Face](https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT)
- **Description**: High-quality medical chain-of-thought reasoning examples
- **Use Case**: Fine-tuning medical language models with reasoning capabilities

**Download & Usage**:
```python
from datasets import load_dataset

dataset = load_dataset("FreedomIntelligence/medical-o1-reasoning-SFT")
```

### Documentation

For more details about Unsloth optimization techniques, visit:
- [Unsloth GitHub Repository](https://github.com/unslothai/unsloth)
- [Unsloth Documentation](https://github.com/unslothai/unsloth/wiki)

### License

Please refer to the original dataset and model licenses on Hugging Face.

---

## 中文版本 {#chinese-version}

### 项目概述

本项目提供了一套基于高效 [Unsloth](https://github.com/unslothai/unsloth) 库的医学思维链（CoT）数据集微调框架。它使你能够训练高质量的医学推理模型，同时具有优化的内存使用和计算速度。

### 项目特性

- **高效微调**：利用 Unsloth 实现 2-5 倍的训练速度提升和显著的内存节省
- **医学 CoT 数据集**：支持多个医学推理和思维链数据集
- **灵活的架构**：易于定制的 Notebook 和脚本，适应各种用途
- **推理支持**：内置的推理功能用于模型评估和部署

### 项目结构

```
├── 1.py                          # 实用工具脚本
├── fine_turning.ipynb            # 基础微调 Notebook
├── full_fine_turning.ipynb       # 完整微调管道
├── Medical_inference.ipynb       # 推理和模型评估
├── unsloth.ipynb                 # Unsloth 设置和示例
└── Model_weight/                 # 模型权重存储目录
    └── sample/                   # 示例模型权重
```

### 数据集

#### medical-o1-reasoning-SFT 数据集

用于医学推理和监督微调的综合数据集：
- **来源**：[Hugging Face - medical-o1-reasoning-SFT](https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT)
- **描述**：高质量的医学思维链推理示例
- **用途**：使用推理能力微调医学语言模型

**下载与使用**：
```python
from datasets import load_dataset

dataset = load_dataset("FreedomIntelligence/medical-o1-reasoning-SFT")
```


### 相关文档

有关 Unsloth 优化技术的更多详情，请访问：
- [Unsloth GitHub 仓库](https://github.com/unslothai/unsloth)
- [Unsloth 文档](https://github.com/unslothai/unsloth/wiki)

### 许可证

请参考 Hugging Face 上原始数据集和模型的许可证。

---

**Last Updated**: 2025-11-16
