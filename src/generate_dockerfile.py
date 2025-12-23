import ollama

PROMPT = """
ONLY generate an ideal Dockerfile for {language} following best practices.
Do NOT add explanations or comments outside the Dockerfile.

Must include:
- Base image
- Installing dependencies
- Setting working directory
- Adding source code
- Running the application
"""

def generate_dockerfile(language):
    response = ollama.chat(
        model="llama3.1:8b",
        messages=[
            {"role": "user", "content": PROMPT.format(language=language)}
        ]
    )
    return response.message.content

if __name__ == "__main__":
    language = input("Enter the programming language: ")
    dockerfile = generate_dockerfile(language)

    print("\nGenerated Dockerfile:\n")
    print(dockerfile)

    # Save to file
    with open("Dockerfile", "w") as f:
        f.write(dockerfile)

    print("\nDockerfile saved successfully.")
