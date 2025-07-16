# 🔍 GitHub Actions Test Prioritization Tool

This tool enhances your CI efficiency by prioritizing previously failed test cases using GitHub Actions. It speeds up feedback loops, reduces redundant test runs, and saves compute resources—especially useful for repositories with extensive test suites.
## 🧭 Workflow Overview

![Workflow Overview](images/workflow_Overview.png)

## 📊 GitHub Action Sequence Diagram

![GitHub Action Sequence](images/githubactionsequence_diagram.png)
## 🚀 What It Does
- Runs only the failed tests from the previous workflow run.
- If they pass, runs the remaining test cases.
- Stores and retrieves test results using GitHub Artifacts.
- Supports PR-specific scoping and matrix configurations.

## 🛠️ How It Works
The tool uses a history-based test prioritization strategy:

### 🔄 First-Time Pull Request Execution
- When a PR is created for the first time, the workflow runs **all test cases**.
- The results—including failed and passed tests—are stored as a JSON artifact named `pr-<PR_ID>-test-results`.

### 🔁 Consecutive Runs on Same PR
- On subsequent pushes to the same PR:
  - GitHub Actions checks for the previous test result artifact.
  - If found, it extracts only the **previously failed tests**.
  - These are re-executed first.
  - If **all failed tests pass**, the remaining test cases are executed.
  - If **any test fails again**, the workflow exits early, saving time and compute.


### 📦 Artifact Scoping
- Artifacts are scoped per PR using the path `artifacts/pr-<PR_ID>/`.
- For matrix configurations, the path becomes `artifacts/pr-<PR_ID>/<WORKFLOW_ID>/`.
- This ensures correct separation of test results by environment and PR.

> ℹ️ Note: This repository demonstrates a single-job implementation.  
> For a matrix setup (e.g., OS × Python version), refer to the [Pytest fork implementation](https://github.com/ShubhamDesai/pytest/blob/main/.github/workflows/test.yml).  
> In matrix jobs with many test cases, passing long lists of test names as command-line arguments can trigger the "argument list too long" error. To avoid this, we divide the tests into batches and run them in groups. See the batching script [here](https://github.com/ShubhamDesai/pytest/blob/main/scripts/generate_pytest_commands.py).





## 📁 Repo Structure
```
├── .github/workflows/
│   └── windows-tests.yml
├── artifacts/
│   └── pr-1234/
│       └── test_results.json
├── images/
│   └── execution_time_chart.png
└── README.md
```



