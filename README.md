# Multi-Agent Crypto Research Platform

A sophisticated multi-agent system built with phidata for crypto research and analysis. This platform combines different specialized agents to perform comprehensive cryptocurrency research, analysis, and content creation.

## Features

- **Web Agent**: General web search and information gathering
- **Finance Agent**: Financial data analysis and market insights
- **Crypto Research Team**:
  - Planning Agent: Research strategy and planning
  - Research Agent: Data gathering and analysis
  - Writer Agent: Content creation and blog writing

## Installation

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -U phidata fastapi[standard] sqlalchemy yfinance
```

3. Set up your API keys:
```bash
export OPENAI_API_KEY=your-api-key
phi auth  # For phidata authentication
```

## Usage

### Running the Playground

Start the interactive playground:
```bash
python playground.py
```
Then visit: https://phidata.app/playground?endpoint=localhost%3A7777

### Running Individual Agents

1. Agent Team Example:
```bash
python agent_team.py
```

2. Crypto Research Team:
```bash
python crypto_team.py
```

## Architecture

- **Cost Optimization**: Uses GPT-3.5-turbo for planning and writing tasks, GPT-4 for critical research
- **Structured Output**: Implements Pydantic models for consistent data structure
- **Persistent Storage**: SQLite database for agent memory and conversation history
- **Multi-Modal Capabilities**: Supports text and data analysis

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

MIT License
