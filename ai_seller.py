import openai

# Replace with your actual OpenAI API key
openai.api_key = "your-api-key-here"

# Mock product catalog
products = {
    "laptop": "A high-performance laptop with 16GB RAM and 512GB SSD.",
    "headphones": "Noise-canceling over-ear headphones with long battery life.",
    "smartphone": "Latest model with OLED display and powerful camera.",
    "keyboard": "Mechanical keyboard with RGB lighting.",
    "mouse": "Wireless ergonomic mouse with high precision sensor."
}

def ask_openai(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an online sales assistant helping customers choose products."},
            {"role": "user", "content": question}
        ]
    )
    return response['choices'][0]['message']['content']

def suggest_product(query):
    for item, description in products.items():
        if item.lower() in query.lower():
            return f"Our recommendation: {item.capitalize()} - {description}"
    return None

if __name__ == "__main__":
    print("Welcome to ShopMate AI! Type 'exit' to quit.")
    while True:
        user_input = input("Customer: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Agent: Thank you for visiting! Have a great day!")
            break

        product_suggestion = suggest_product(user_input)
        if product_suggestion:
            print("Agent:", product_suggestion)
        else:
            response = ask_openai(user_input)
            print("Agent:", response)
