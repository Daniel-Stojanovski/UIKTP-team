from flask import Flask, request, jsonify, send_file
import subprocess
import os

app = Flask(__name__)

os.makedirs("exports", exist_ok=True)

@app.route('/export', methods=['POST'])
def export_pdf():
    data = request.json  # Get data from frontend
    theme = data.get('theme')
    difficulty = data.get('difficulty')
    question = data.get('problem')
    equation = data.get('showProblem')

# # Call the script with arguments
#     subprocess.run(["python", "export_script.py", theme, difficulty, question, equation])
#
#     return jsonify({"message": "PDF Exported!"})
    # Generate text file content
    file_content = f"Theme: {theme}, Difficulty: {difficulty}\n\nQUESTION:\n{question}\n\nEquation:\n{equation}\n"

    file_path = f"exports/problem_{theme}_{difficulty}.txt"

    # Save to a .txt file
    with open(file_path, "w") as file:
        file.write(file_content)

    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)
