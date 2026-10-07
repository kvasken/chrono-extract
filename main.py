import argparse
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()
client = OpenAI()

class HistoricalEvents(BaseModel):
    name:str
    date:str
class HistoricalEventsResponse(BaseModel):
    events:list[HistoricalEvents]
def main():
    #Argument parser object
    parser = argparse.ArgumentParser(
        description="Extract chronological historical events using OpenAI Structured Outputs."
    )

    #Defining argument
    parser.add_argument(
        "topic",
        type=str,
        help="The historical topic or period you want to extract events for (e.g., 'French Revolution')"
    )

    #
    args = parser.parse_args()


    #Prompt generator
    user_input = f"Tell me shortly about the main events of: {args.topic}"


    response = client.responses.parse(
        model="gpt-4o",
        instructions="You are historical data extractor. Extract information about main events that are considered part of the user-requested period of history.Put events chronologically.",
        input=user_input,
        text_format=HistoricalEventsResponse,
    )
    for event in response.output_parsed.events:
        print(f"{event.date}: {event.name}")


if __name__ == "__main__":
    main()