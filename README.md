# PYTEST: TEST PYRAMID - Battery Module Disassembly Case

## 1 - To prepare the environment for a local check, simply run the `python3 install_local_env.py` file

## 2 - UNIT TESTS: To run this testing layer, use this command:

```bash
    pytest tests/unit
```

If you need more detailed logs or run specific test cases, simply run one of these commands:
```bash
    pytest tests/unit -v --log-cli-level=INFO
    pytest tests/unit/test_vision.py -v --log-cli-level=INFO
    pytest tests/unit/test_plc_handshake.py -v --log-cli-level=INFO
```

## 3 - INTEGRATION TESTS: To run this testing layer, use this command:

```bash
    pytest tests/integration

    # OR if you need to check more log details:
    pytest tests/integration -v --log-cli-level=INFO
```

## 4 - E2E TESTS: To run this testing layer in BDD format, you can call the scenarios using these commands:

The simple way:
```bash
    pytest tests/e2e

    # OR if you need to check more log details:
    pytest tests/e2e -v --log-cli-level=INFO --gherkin-terminal-reporter -v
```

By passing the BDD tag from an identified scenario:
```bash
    pytest tests/e2e -m "happy-path"

    # OR if you need to check more log details:
    pytest tests/e2e -m "happy-path" -v --log-cli-level=INFO --gherkin-terminal-reporter -v
```

## 5 - UI TESTS (Selenium): To run this testing layer in BDD format, you can call the scenarios using these commands:

### 5.1 - SELENIUM tests:
The simple way:
```bash
    pytest tests/ui/se

    # OR if you need to check more log details:
    pytest tests/ui/se -v --log-cli-level=INFO --gherkin-terminal-reporter -v
```

By passing the BDD tag from an identified scenario:
```bash
    pytest tests/ui/se -m "ui"

    # OR if you need to check more log details:
    pytest tests/ui/se -m "smoke" -v --log-cli-level=INFO --gherkin-terminal-reporter -v
```

### 5.2 - PLAYWRIGHT tests:
The simple way:
```bash
    pytest tests/ui/pw

    # OR if you need to check more log details:
    pytest tests/ui/pw -v --log-cli-level=INFO --gherkin-terminal-reporter -v
```

By passing the BDD tag from an identified scenario:
```bash
    pytest tests/ui/pw -m "ui"

    # OR if you need to check more log details:
    pytest tests/ui/pw -m "smoke" -v --log-cli-level=INFO --gherkin-terminal-reporter -v
```

## 6 - ALL LAYERS: Use simply this command:

```bash
    pytest tests/unit tests/integration tests/e2e tests/ui/se tests/ui/pw -v --log-cli-level=INFO
```

## 7 - CI files are tested locally using ACT (open-source tool: 'brew install act')

The tests were passing successfully:
```bash
    act -j tests
    act -j e2e
    act -j ui_se
    act -j ui_pw
    act schedule -j nightly
```

## 8 - Run Tests using Dockerfile

Build the image first:
```bash
    docker build -t calangobotics-qa .
```

Run the full test suite (all levels)
```bash
    docker run --rm calangobotics-qa

    # OR only the UI Tests, e.g.:
    docker run --rm calangobotics-qa pytest tests/ui
```
