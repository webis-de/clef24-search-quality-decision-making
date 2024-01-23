<!--
[![CI](https://img.shields.io/github/actions/workflow/status/heinrichreimer/algorithmic-quality-decision-making/ci.yml?branch=main&style=flat-square)](https://github.com/heinrichreimer/algorithmic-quality-decision-making/actions/workflows/ci.yml)
[![Code coverage](https://img.shields.io/codecov/c/github/heinrichreimer/algorithmic-quality-decision-making?style=flat-square)](https://codecov.io/github/heinrichreimer/algorithmic-quality-decision-making/)
[![Issues](https://img.shields.io/github/issues/heinrichreimer/algorithmic-quality-decision-making?style=flat-square)](https://github.com/heinrichreimer/algorithmic-quality-decision-making/issues)
[![Commit activity](https://img.shields.io/github/commit-activity/m/heinrichreimer/algorithmic-quality-decision-making?style=flat-square)](https://github.com/heinrichreimer/algorithmic-quality-decision-making/commits)
[![License](https://img.shields.io/github/license/heinrichreimer/algorithmic-quality-decision-making?style=flat-square)](LICENSE)
-->

# 🆚 algorithmic-quality-decision-making

Code and data for the paper "The Impact of Web Search Result Quality on Decision Making".

## Installation

1. Install [Python 3.11](https://python.org/downloads/)
2. Create and activate the virtual environment:

    ```shell
    python3.11 -m venv venv/
    source venv/bin/activate
    ```

3. Install dependencies:

    ```shell
    pip install -e .
    ```

## Testing

After [installing](#installation) all test dependencies (`pip install -e .[tests]`), you can run our approval tests:

```shell script
flake8 algorithmic_quality_decision_making  # Code style
pylint algorithmic_quality_decision_making  # LINT errors
bandit -c pyproject.toml -r algorithmic_quality_decision_making  # Security
pytest algorithmic_quality_decision_making  # Unit tests
```

## License

The source code in this repository is licensed under the [MIT License](LICENSE).
