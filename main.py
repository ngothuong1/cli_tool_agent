from dotenv import load_dotenv
load_dotenv()

from agent import build_agent

def main():
    agent = build_agent()
    print("CLI TOOL AGENT (type 'exit' to quit)")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == "exit":
            print("Bye")
            break

        response = agent.invoke({"input": user_input})
        print("\nAgent:", response["output"])

if __name__ == "__main__":
    main()