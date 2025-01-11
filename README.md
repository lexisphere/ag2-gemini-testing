# AG2 Gemini Integration Testing Suite

This repository provides a comprehensive testing suite and implementation examples for using AG2 (AutoGen) with Google's Gemini model. It includes structured tests, examples, and proper configuration patterns.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure Google Cloud credentials:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/credentials.json"
```

## Project Structure

```
.
├── src/              # Core implementation
├── tests/            # Test suite
├── examples/         # Usage examples
└── docs/             # Additional documentation
```

## Running Tests

Use the CLI to run tests individually or all at once:

```bash
python run_tests.py basic    # Basic chat functionality
python run_tests.py code     # Code execution
python run_tests.py errors   # Error handling
python run_tests.py all      # All tests
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License