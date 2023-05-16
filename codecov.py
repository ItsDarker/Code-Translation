import openai

# Set up OpenAI API
openai.api_key = 'YOUR_API_KEY'

def convert_code(source_code, source_language, target_language):
    # Define the prompt for GPT-3 API
    prompt = f"Convert the following {source_language} code to {target_language}:\n\n{source_code}"

    # Make API request
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.8
    )

    # Extract the converted code from API response
    converted_code = response.choices[0].text.strip()

    return converted_code

def save_code_to_file(code, file_path):
    with open(file_path, 'w') as file:
        file.write(code)

# Read the input code from file
input_file_path = 'input.txt'
with open(input_file_path, 'r') as file:
    source_code = file.read()

# Specify the source language
source_language = 'LANGUAGE'

# Convert code to different languages and save to files
languages = ['python', 'c', 'cpp', 'java', 'javascript', 'rust', 'swift', 'ruby', 'csharp', 'php']
for language in languages:
    converted_code = convert_code(source_code, source_language, language)
    output_file_path = f'output_{language}.txt'
    save_code_to_file(converted_code, output_file_path)
