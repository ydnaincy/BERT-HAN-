# Contributing to BERT-HAN++

Thank you for your interest in contributing to BERT-HAN++! This document provides guidelines for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Submitting Changes](#submitting-changes)
- [Style Guidelines](#style-guidelines)
- [Testing](#testing)
- [Documentation](#documentation)

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct:

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Respect different viewpoints and experiences
- Show empathy towards other community members

## Getting Started

### Types of Contributions

We welcome several types of contributions:

- **Bug Reports**: Help us identify and fix issues
- **Feature Requests**: Suggest new functionality
- **Code Contributions**: Implement new features or fix bugs
- **Documentation**: Improve or expand documentation
- **Testing**: Add or improve test coverage
- **Examples**: Create tutorials or example notebooks

### Before You Start

1. Check if there's already an issue or PR for what you want to work on
2. For large changes, please open an issue first to discuss your approach
3. Make sure you understand the project structure and coding style

## Development Setup

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/yourusername/bert-han-plus-plus.git
cd bert-han-plus-plus

# Add the original repository as upstream
git remote add upstream https://github.com/originaluser/bert-han-plus-plus.git
```

### 2. Set Up Development Environment

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Install the package in development mode
pip install -e .
```

### 3. Verify Installation

```bash
# Run tests to ensure everything is working
pytest tests/

# Check code style
black --check bert_han_plus_plus/
isort --check-only bert_han_plus_plus/
flake8 bert_han_plus_plus/
mypy bert_han_plus_plus/
```

## Making Changes

### 1. Create a Branch

```bash
# Create a new branch for your changes
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-number-description
```

### 2. Development Workflow

- Make your changes in small, logical commits
- Write clear commit messages
- Add tests for new functionality
- Update documentation as needed
- Ensure all tests pass

### 3. Keep Your Branch Updated

```bash
# Regularly sync with upstream
git fetch upstream
git rebase upstream/main
```

## Submitting Changes

### 1. Pre-submission Checklist

- [ ] All tests pass (`pytest tests/`)
- [ ] Code follows style guidelines (`black`, `isort`, `flake8`, `mypy`)
- [ ] Documentation is updated
- [ ] Commit messages are clear and descriptive
- [ ] No merge conflicts with main branch

### 2. Create a Pull Request

1. Push your branch to your fork
2. Go to the original repository on GitHub
3. Click "New Pull Request"
4. Choose your branch and provide a clear description

### 3. Pull Request Guidelines

**Title**: Use a clear, descriptive title
- ✅ "Add cross-lingual evaluation metrics"
- ❌ "Fix bug"

**Description**: Include:
- What changes you made and why
- Any relevant issue numbers
- Testing steps
- Screenshots (if applicable)

**Example**:
```markdown
## Summary
This PR adds support for cross-lingual evaluation metrics as requested in #123.

## Changes
- Added new metrics in `bert_han_plus_plus/metrics.py`
- Updated evaluation script to use new metrics
- Added tests for new functionality

## Testing
- All existing tests pass
- Added new tests for cross-lingual metrics
- Manually tested on Hindi and Spanish datasets

Closes #123
```

## Style Guidelines

### Code Style

We use the following tools to maintain code quality:

- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting
- **mypy**: Type checking

### Formatting Commands

```bash
# Format code
black bert_han_plus_plus/
isort bert_han_plus_plus/

# Check for issues
flake8 bert_han_plus_plus/
mypy bert_han_plus_plus/
```

### Code Standards

- Use type hints for all functions
- Add docstrings for all public functions and classes
- Follow PEP 8 naming conventions
- Keep functions small and focused
- Use descriptive variable names

### Example Function

```python
def calculate_attention_weights(
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    mask: Optional[torch.Tensor] = None
) -> Tuple[torch.Tensor, torch.Tensor]:
    """
    Calculate attention weights using scaled dot-product attention.
    
    Args:
        query: Query tensor of shape (batch_size, seq_len, dim)
        key: Key tensor of shape (batch_size, seq_len, dim)
        value: Value tensor of shape (batch_size, seq_len, dim)
        mask: Optional attention mask
        
    Returns:
        Tuple of (attention_output, attention_weights)
    """
    # Implementation here
    pass
```

## Testing

### Running Tests

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_model.py

# Run with coverage
pytest --cov=bert_han_plus_plus tests/
```

### Writing Tests

- Write tests for all new functionality
- Use descriptive test names
- Include edge cases and error conditions
- Use fixtures for common setup

### Test Structure

```python
import pytest
from bert_han_plus_plus.model import BERTHANPlusPlus

class TestBERTHANPlusPlus:
    """Test suite for BERT-HAN++ model."""
    
    @pytest.fixture
    def model(self):
        """Create a test model instance."""
        return BERTHANPlusPlus(num_classes=4)
    
    def test_model_initialization(self, model):
        """Test that model initializes correctly."""
        assert model.num_classes == 4
        assert model.adaptive_complexity is True
    
    def test_forward_pass(self, model):
        """Test forward pass with sample input."""
        # Test implementation
        pass
```

## Documentation

### Docstring Style

We use Google-style docstrings:

```python
def process_document(
    text: str,
    max_length: int = 512,
    return_attention: bool = False
) -> Dict[str, Any]:
    """
    Process a document for classification.
    
    Args:
        text: Input document text
        max_length: Maximum sequence length
        return_attention: Whether to return attention weights
        
    Returns:
        Dictionary containing processed features
        
    Raises:
        ValueError: If text is empty or too long
        
    Example:
        >>> model = BERTHANPlusPlus()
        >>> result = model.process_document("Hello world")
        >>> print(result['logits'])
    """
```

### README Updates

If your changes affect usage:
- Update the README.md
- Add examples if introducing new features
- Update the API documentation

## Issue Guidelines

### Reporting Bugs

When reporting bugs, please include:

1. **Environment**: Python version, OS, library versions
2. **Steps to reproduce**: Minimal code example
3. **Expected behavior**: What should happen
4. **Actual behavior**: What actually happens
5. **Error messages**: Full stack traces

### Feature Requests

For feature requests, please include:

1. **Use case**: Why is this feature needed?
2. **Proposed solution**: How should it work?
3. **Alternatives**: Any workarounds you've considered?

## Release Process

Releases are managed by maintainers:

1. Version numbers follow semantic versioning
2. Changelog is updated for each release
3. Tags are created for stable releases
4. PyPI packages are published automatically

## Questions?

If you have questions about contributing:

1. Check existing issues and discussions
2. Open a new issue with the "question" label
3. Join our community discussions
4. Contact maintainers directly

Thank you for contributing to BERT-HAN++! 🎉
