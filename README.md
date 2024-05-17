<!--
[![CI](https://img.shields.io/github/actions/workflow/status/heinrichreimer/search-quality-decision-making/ci.yml?branch=main&style=flat-square)](https://github.com/heinrichreimer/search-quality-decision-making/actions/workflows/ci.yml)
[![Code coverage](https://img.shields.io/codecov/c/github/heinrichreimer/search-quality-decision-making?style=flat-square)](https://codecov.io/github/heinrichreimer/search-quality-decision-making/)
[![Issues](https://img.shields.io/github/issues/heinrichreimer/search-quality-decision-making?style=flat-square)](https://github.com/heinrichreimer/search-quality-decision-making/issues)
[![Commit activity](https://img.shields.io/github/commit-activity/m/heinrichreimer/search-quality-decision-making?style=flat-square)](https://github.com/heinrichreimer/search-quality-decision-making/commits)
[![License](https://img.shields.io/github/license/heinrichreimer/search-quality-decision-making?style=flat-square)](LICENSE)
-->

# 🆚 search-quality-decision-making

Code and data for the paper "The Impact of Web Search Result Quality on Decision Making".

## Data

In this repository, you'll find all annotations and study responses that were collected as part of this research:

|File|Description|
|:--|:--|
|`01-quality-agreement.xlsx`|Fleiss' kappa values per quality aspects.|
|`02-quality.xlsx`|Quality annotations for each criterion's aspects|
|`03-quality-recoded.xlsx`|Recoded quality annotations to separate combined fields.|
|`04-quality-recoded-majority-vote.xlsx`|Final quality annotations after majority voting.|
|`05-survey.xlsx`|Raw user study survey responses and topics.|
|`06-study.xlsx`|Bundled topics, archived search results, quality assessments, and user study survey responses.|

## Code

We use Python notebooks to evaluate the quality assessments and user study responses. Follow the steps below to [install](#installation) and [run](#usage) the notebooks.

### Installation

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

### Usage

Once you have installed the required dependencies, you can launch the notebooks by running the following command (where `<FILE>` is a path from the list below):

```shell
jupyter-notebook notebooks/<FILE>
```

|File|Description|
|:--|:--|
|`agreement.ipynb`|Measuring the inter-rater agreement for the quality assessments.|
|`evaluation_quality.ipynb`|Evaluation of the quality assessments.|
|`evaluation_user_study.ipynb`|Evaluation of the user study responses and hypothesis tests.|

## License

The source code in this repository is licensed under the [MIT License](LICENSE).
