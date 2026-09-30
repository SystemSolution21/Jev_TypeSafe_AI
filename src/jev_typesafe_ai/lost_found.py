# built-in
import os

# third-party
from dotenv import load_dotenv
from typesafe_sdk import Noul, TypeSafeClient

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
base_url: str | None = os.getenv(key="TYPESAFE_BASE_URL")
api_key: str | None = os.getenv(key="TYPESAFE_API_KEY")
default_model: str | None = os.getenv(key="TYPESAFE_DEFAULT_MODEL")

# Initialize the TypeSafeClient with the environment variables
client = TypeSafeClient(
    api_key=api_key, model=default_model, timeout=120, base_url=base_url
)


def ask_question() -> None:
    """
    Ask a question to the TypeSafe AI model and return the answer.

    Args:
        question (str): The question to ask.

    Returns:
        str: The answer from the TypeSafe AI model.
    """

    while True:
        try:
            answer: str = input(
                "Did you lose something? (Type 'exit' to quit): "
            ).strip()
            if answer.lower() == "exit":
                print("Goodbye, please feel free to ask if you need any assistance.")
                break
            if not answer:
                print("Please type what you have lost.")
                continue

            # Send the answer to the TypeSafe AI model for evaluation
            response = client.system_one(
                state=answer,
                questions={
                    "lost_something": Noul(
                        instructions="Is the answer from the user affirmative?"
                    ),
                },
            )

            # Check the response from the TypeSafe AI model
            lost_something: float = response.nouls["lost_something"].noul

            # Debugging output to check the lost_something score
            print(f"Debug: lost_something score = {lost_something}")

            # Respond to the user based on the lost_something score
            respond_to_lost_item(lost_something=lost_something)

        except KeyboardInterrupt:
            print("\nGoodbye, please feel free to ask if you need any assistance.")
            break


def respond_to_lost_item(lost_something: float) -> None:
    """
    Respond to the user based on whether they lost something.

    Args:
        lost_something (float): The score indicating whether the user lost something.
    """

    if lost_something > 0.8:
        print("You can find the lost and found counter on the right.")
    elif lost_something < 0.2:
        print("Okay. What can I help you with?")
    else:
        print("I am not sure if you lost something. Can you please clarify?")


def main() -> None:
    """
    Main function to run the lost and found question loop.
    """
    ask_question()


if __name__ == "__main__":
    main()
