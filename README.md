# Jev TypeSafe AI

Jev TypeSafe AI is a small tutorial project demonstrating how to use the TypeSafe AI SDK to classify a user's response and choose an appropriate reply. The interactive lost-and-found example asks whether the user lost something, evaluates the answer, and routes the response based on the `lost_something` score:

- Above `0.8`: directs the user to the lost-and-found counter.
- Below `0.2`: asks what else the user needs help with.
- From `0.2` through `0.8`, inclusive: asks the user to clarify.

## Requirements

- Python 3.13 or newer
- [uv](https://docs.astral.sh/uv/) for managing the project and its dependencies
- TypeSafe API configuration for the interactive example

The project dependencies are declared in `pyproject.toml` and installed by uv:

- `typesafe-sdk` for the TypeSafe client and decision model
- `python-dotenv` (imported as `dotenv`) to load configuration from a `.env` file

## Setup

From the project root, install the dependencies:

```powershell
uv sync
```

Create a `.env` file in the project root with your TypeSafe configuration:

```dotenv
TYPESAFE_API_KEY=your_api_key
TYPESAFE_DEFAULT_MODEL=your_model
TYPESAFE_BASE_URL=your_base_url
```

Use the model name and base URL for your TypeSafe service. Keep the API key private and do not commit the `.env` file.

## Run

Run the interactive lost-and-found example:

```powershell
uv run python src/jev_typesafe_ai/lost_found.py
```

Enter a response when prompted. Type `exit` to quit; press Ctrl+C to exit as well.

The top-level `main.py` is a separate starter stub that prints a greeting; it does not launch the interactive example. Run it with:

```powershell
uv run python main.py
```
