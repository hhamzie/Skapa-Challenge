import pandas as pd
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
app.config['DEBUG'] = True

#CSV Reader 
def read_csv(file_path): 
    try:
        df = pd.read_csv(file_path, usecols=[0], header=None, dtype=str)
        all_words = df[0].apply(lambda x: str(x).split(",")[0].strip() if pd.notna(x) else '').tolist()

    except Exception as e:
        print(f"Error reading file {file_path}: {str(e)}")
        return []
    return all_words


# Word loader
def load_words(letters):

    all_words = read_csv("dictionary.csv")

    valid_letters = set(letters)
    valid_words = []
    for word in all_words:

        if len(word) > 3 and letters[0].lower() in word.lower() and (set(word.lower())).issubset(valid_letters):
            valid_words.append(word)
    return set(valid_words)

# Main GET Method 
@app.route('/spellingwords', methods=['GET'])
def get_words():
    required = request.args.get('required')
    optionals = request.args.get('optionals', '')
    if not required:
        return jsonify({'error': 'Required letter is missing'}), 400  

    all_words = load_words(required + optionals)

    response = "\n".join(sorted(all_words))
    return response, 200, {'Content-Type': 'text/plain'}

# Run API
if __name__ == '__main__':
    print("FLASK_ENV:", os.getenv('FLASK_ENV'))
    app.run(debug=True, port=5000)
