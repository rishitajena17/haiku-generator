from ai import call_gpt

def main():
    name = input("Enter your name: ")
    topic = input("Enter a topic: ")
    print("Creating your haiku... ")
    prompt = f"Write a haiku that includes or is inspired by the name '{name}' and the topic '{topic}'. A haiku has three lines with 5, 7, and 5 syllables. Keep it poetic and nature-themed."
    haiku = call_gpt(prompt)
    print(haiku)

    


if __name__ == "__main__":
    main()
