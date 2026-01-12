from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import io
import contextlib
import os
from concurrent.futures import ThreadPoolExecutor, TimeoutError as FuturesTimeoutError
from datetime import datetime, date

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'dev-key-change-in-production')

# 15 Progressive Python Levels
LEVELS = [
    {
        "id": 1,
        "title": "Hello, World!",
        "concept": "Print Statements",
        "description": "Every programmer's journey begins with a simple greeting. The <code>print()</code> function outputs text to the console. It's the most fundamental way to see your program's results.",
        "task": "Write a program that prints exactly: <strong>Hello, World!</strong>",
        "hint": "Use the print() function with text inside quotes: print('Hello, World!')",
        "expected_output": "Hello, World!",
        "solution": "print('Hello, World!')",
        "explanation": "The print() function displays whatever you put inside the parentheses. Text (strings) must be wrapped in quotes - either single ('') or double (\"\")."
    },
    {
        "id": 2,
        "title": "Variables",
        "concept": "Storing Data",
        "description": "Variables are containers for storing data values. In Python, you create a variable simply by assigning a value to a name using the <code>=</code> operator.",
        "task": "Create a variable called <strong>message</strong> with the value <strong>'Python is fun'</strong> and print it.",
        "hint": "First assign the variable: message = 'Python is fun', then use print(message)",
        "expected_output": "Python is fun",
        "solution": "message = 'Python is fun'\nprint(message)",
        "explanation": "Variables store values for later use. The variable name goes on the left of =, and the value on the right. When you print a variable, Python outputs its stored value."
    },
    {
        "id": 3,
        "title": "Math Magic",
        "concept": "Arithmetic Operations",
        "description": "Python excels at mathematical calculations. Use <code>+</code> (add), <code>-</code> (subtract), <code>*</code> (multiply), <code>/</code> (divide), and <code>**</code> (power).",
        "task": "Calculate and print the result of <strong>25 * 4</strong>",
        "hint": "You can print calculations directly: print(25 * 4)",
        "expected_output": "100",
        "solution": "print(25 * 4)",
        "explanation": "Python evaluates mathematical expressions before printing. The * operator performs multiplication. You can combine multiple operations in one expression."
    },
    {
        "id": 4,
        "title": "String Fusion",
        "concept": "String Concatenation",
        "description": "Strings can be joined together using the <code>+</code> operator. This is called concatenation - combining multiple strings into one.",
        "task": "Create variables <strong>first = 'Hello'</strong> and <strong>second = 'Python'</strong>. Print them joined with a space between.",
        "hint": "Join strings with +: print(first + ' ' + second)",
        "expected_output": "Hello Python",
        "solution": "first = 'Hello'\nsecond = 'Python'\nprint(first + ' ' + second)",
        "explanation": "The + operator joins strings end-to-end. Remember to include spaces as separate strings (' ') when you want words separated."
    },
    {
        "id": 5,
        "title": "Number Types",
        "concept": "Integers and Floats",
        "description": "Python has different number types: <code>int</code> (whole numbers like 42) and <code>float</code> (decimals like 3.14). Division always returns a float.",
        "task": "Calculate and print <strong>17 / 2</strong> to see a float result.",
        "hint": "Simply print the division: print(17 / 2)",
        "expected_output": "8.5",
        "solution": "print(17 / 2)",
        "explanation": "Division (/) always returns a float in Python 3. For integer division (no decimal), use // instead. Understanding number types prevents unexpected results."
    },
    {
        "id": 6,
        "title": "User Input",
        "concept": "Input Function",
        "description": "The <code>input()</code> function pauses the program and waits for user input. Whatever the user types becomes a string value.",
        "task": "For this exercise, print <strong>'Enter your name: '</strong> (simulating input prompt).",
        "hint": "Use print() with the exact text: print('Enter your name: ')",
        "expected_output": "Enter your name:",
        "solution": "print('Enter your name:')",
        "explanation": "In real programs, input('Enter your name: ') displays the prompt and waits for typing. The entered value can be stored in a variable for later use."
    },
    {
        "id": 7,
        "title": "Conditionals",
        "concept": "If Statements",
        "description": "The <code>if</code> statement executes code only when a condition is True. Use comparison operators: <code>==</code>, <code>!=</code>, <code>&lt;</code>, <code>&gt;</code>, <code>&lt;=</code>, <code>&gt;=</code>.",
        "task": "Create <strong>score = 85</strong>. If score >= 60, print <strong>'Pass'</strong>.",
        "hint": "Use if with indentation:\nscore = 85\nif score >= 60:\n    print('Pass')",
        "expected_output": "Pass",
        "solution": "score = 85\nif score >= 60:\n    print('Pass')",
        "explanation": "Indentation is crucial in Python - it defines code blocks. The code under 'if' only runs when the condition is True. Always use consistent indentation (4 spaces recommended)."
    },
    {
        "id": 8,
        "title": "Else Branch",
        "concept": "If-Else Statements",
        "description": "The <code>else</code> clause provides an alternative path when the if condition is False. Together they handle two possible outcomes.",
        "task": "Create <strong>age = 15</strong>. Print <strong>'Adult'</strong> if age >= 18, otherwise print <strong>'Minor'</strong>.",
        "hint": "Use if-else:\nif age >= 18:\n    print('Adult')\nelse:\n    print('Minor')",
        "expected_output": "Minor",
        "solution": "age = 15\nif age >= 18:\n    print('Adult')\nelse:\n    print('Minor')",
        "explanation": "The else block runs when the if condition is False. This creates a complete decision structure - one path or the other will always execute."
    },
    {
        "id": 9,
        "title": "Lists",
        "concept": "Data Collections",
        "description": "Lists store multiple items in a single variable. Create them with square brackets <code>[]</code>. Items are separated by commas and can be any type.",
        "task": "Create a list <strong>fruits = ['apple', 'banana', 'cherry']</strong> and print it.",
        "hint": "Create the list and print: fruits = ['apple', 'banana', 'cherry']\nprint(fruits)",
        "expected_output": "['apple', 'banana', 'cherry']",
        "solution": "fruits = ['apple', 'banana', 'cherry']\nprint(fruits)",
        "explanation": "Lists are ordered and changeable. They can hold different data types and are one of Python's most versatile data structures."
    },
    {
        "id": 10,
        "title": "List Access",
        "concept": "Indexing",
        "description": "Access list items using their index (position). Python uses zero-based indexing: the first item is at index <code>0</code>, second at <code>1</code>, etc.",
        "task": "Create <strong>colors = ['red', 'green', 'blue']</strong>. Print the second item (index 1).",
        "hint": "Access with brackets: print(colors[1])",
        "expected_output": "green",
        "solution": "colors = ['red', 'green', 'blue']\nprint(colors[1])",
        "explanation": "Zero-based indexing means counting starts at 0. Use negative indices to count from the end: colors[-1] gives 'blue' (last item)."
    },
    {
        "id": 11,
        "title": "For Loops",
        "concept": "Iteration",
        "description": "The <code>for</code> loop iterates over a sequence (like a list), executing code for each item. The loop variable takes each value in turn.",
        "task": "Loop through <strong>numbers = [1, 2, 3]</strong> and print each number.",
        "hint": "for num in numbers:\n    print(num)",
        "expected_output": "1\n2\n3",
        "solution": "numbers = [1, 2, 3]\nfor num in numbers:\n    print(num)",
        "explanation": "For loops are essential for processing collections. The variable (num) automatically gets each list item. The indented code runs once per item."
    },
    {
        "id": 12,
        "title": "Range Function",
        "concept": "Generating Sequences",
        "description": "The <code>range()</code> function generates a sequence of numbers. <code>range(5)</code> produces 0,1,2,3,4. Use it with for loops.",
        "task": "Use a for loop with <strong>range(4)</strong> to print numbers 0 through 3.",
        "hint": "for i in range(4):\n    print(i)",
        "expected_output": "0\n1\n2\n3",
        "solution": "for i in range(4):\n    print(i)",
        "explanation": "range(n) generates n numbers starting from 0. You can also use range(start, stop) or range(start, stop, step) for more control."
    },
    {
        "id": 13,
        "title": "While Loops",
        "concept": "Conditional Iteration",
        "description": "The <code>while</code> loop repeats code as long as a condition is True. Be careful to update the condition to avoid infinite loops!",
        "task": "Create <strong>count = 0</strong>. While count < 3, print count and increment it.",
        "hint": "while count < 3:\n    print(count)\n    count = count + 1",
        "expected_output": "0\n1\n2",
        "solution": "count = 0\nwhile count < 3:\n    print(count)\n    count = count + 1",
        "explanation": "While loops check the condition before each iteration. Always ensure the condition will eventually become False, or use 'break' to exit."
    },
    {
        "id": 14,
        "title": "Functions",
        "concept": "Code Reusability",
        "description": "Functions are reusable blocks of code defined with <code>def</code>. They can take parameters and return values. Call a function by using its name with parentheses.",
        "task": "Define a function <strong>greet()</strong> that prints <strong>'Hello!'</strong>. Then call it.",
        "hint": "def greet():\n    print('Hello!')\n\ngreet()",
        "expected_output": "Hello!",
        "solution": "def greet():\n    print('Hello!')\n\ngreet()",
        "explanation": "Functions organize code into logical units. Define once, use many times. Parameters let you pass data in; return statements send data back."
    },
    {
        "id": 15,
        "title": "Dictionaries",
        "concept": "Key-Value Storage",
        "description": "Dictionaries store data in <code>key: value</code> pairs using curly braces <code>{}</code>. Access values by their keys, not by index.",
        "task": "Create <strong>person = {'name': 'Alice', 'age': 25}</strong>. Print the name value.",
        "hint": "Access with the key: print(person['name'])",
        "expected_output": "Alice",
        "solution": "person = {'name': 'Alice', 'age': 25}\nprint(person['name'])",
        "explanation": "Dictionaries provide fast lookup by key. Keys must be unique and immutable (strings, numbers). Values can be any type, including other dictionaries."
    }
]

def init_session():
    """Initialize session data for a new user"""
    if 'completed' not in session:
        session['completed'] = []
    if 'streak' not in session:
        session['streak'] = 0
    if 'max_streak' not in session:
        session['max_streak'] = 0
    if 'attempts' not in session:
        session['attempts'] = {}
    if 'score' not in session:
        session['score'] = 0
    if 'last_activity_date' not in session:
        session['last_activity_date'] = None

def _run_code(code, safe_builtins):
    """Helper function to execute code in a thread"""
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        exec(code, {"__builtins__": safe_builtins}, {})
    return output.getvalue().rstrip()

def execute_code(code):
    """Safely execute Python code and capture output with timeout protection"""
    error = None

    # Restricted builtins for safety
    safe_builtins = {
        'print': print,
        'range': range,
        'len': len,
        'str': str,
        'int': int,
        'float': float,
        'list': list,
        'dict': dict,
        'tuple': tuple,
        'set': set,
        'bool': bool,
        'abs': abs,
        'max': max,
        'min': min,
        'sum': sum,
        'sorted': sorted,
        'reversed': reversed,
        'enumerate': enumerate,
        'zip': zip,
        'map': map,
        'filter': filter,
        'True': True,
        'False': False,
        'None': None,
    }

    try:
        # Execute code with 5 second timeout using ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=1) as executor:
            future = executor.submit(_run_code, code, safe_builtins)
            output = future.result(timeout=5)
            return output, None
    except FuturesTimeoutError:
        error = "TimeoutError: Code execution timed out (exceeded 5 seconds)"
        return "", error
    except Exception as e:
        error = f"{type(e).__name__}: {str(e)}"
        return "", error

@app.route('/')
def index():
    init_session()
    return render_template('index.html',
                         levels=LEVELS,
                         completed=session['completed'],
                         streak=session['streak'],
                         max_streak=session['max_streak'],
                         score=session['score'])

@app.route('/level/<int:level_id>')
def level(level_id):
    init_session()

    if level_id < 1 or level_id > len(LEVELS):
        return redirect(url_for('index'))

    # Check if level is unlocked (previous level completed or first level)
    if level_id > 1 and (level_id - 1) not in session['completed']:
        return redirect(url_for('index'))

    current_level = LEVELS[level_id - 1]

    return render_template('level.html',
                         level=current_level,
                         levels=LEVELS,
                         completed=session['completed'],
                         streak=session['streak'],
                         max_streak=session['max_streak'],
                         score=session['score'],
                         total_levels=len(LEVELS))

@app.route('/submit', methods=['POST'])
def submit():
    init_session()

    level_id = int(request.form.get('level_id', 1))
    code = request.form.get('code', '')

    if level_id < 1 or level_id > len(LEVELS):
        return jsonify({'success': False, 'error': 'Invalid level'})

    current_level = LEVELS[level_id - 1]

    # Execute the code
    output, error = execute_code(code)

    if error:
        session.modified = True
        return jsonify({
            'success': False,
            'error': error,
            'output': output,
            'expected': current_level['expected_output'],
            'solution': current_level['solution'],
            'explanation': current_level['explanation'],
            'streak': session['streak'],
            'score': session['score']
        })

    # Compare output
    expected = current_level['expected_output'].strip()
    actual = output.strip()

    if actual == expected:
        # Mark as completed
        if level_id not in session['completed']:
            session['completed'].append(level_id)

        # Increase score for correct answer
        session['score'] += 1

        # Check if it's a new day for streak calculation
        today = date.today().isoformat()
        last_date = session['last_activity_date']

        if last_date != today:
            # Check if streak should continue (yesterday) or reset
            if last_date is None:
                # First time user
                session['streak'] = 1
            else:
                from datetime import timedelta
                yesterday = (date.today() - timedelta(days=1)).isoformat()
                if last_date == yesterday:
                    # Consecutive day - increase streak
                    session['streak'] += 1
                else:
                    # Missed days - reset streak
                    session['streak'] = 1

            # Update last activity date
            session['last_activity_date'] = today

            # Update max streak
            if session['streak'] > session['max_streak']:
                session['max_streak'] = session['streak']

        session.modified = True

        next_level = level_id + 1 if level_id < len(LEVELS) else None

        return jsonify({
            'success': True,
            'output': output,
            'streak': session['streak'],
            'max_streak': session['max_streak'],
            'score': session['score'],
            'next_level': next_level,
            'completed_count': len(session['completed']),
            'total_levels': len(LEVELS)
        })
    else:
        session.modified = True

        return jsonify({
            'success': False,
            'output': output,
            'expected': expected,
            'solution': current_level['solution'],
            'explanation': current_level['explanation'],
            'streak': session['streak'],
            'score': session['score']
        })

@app.route('/reset/<int:level_id>')
def reset_level(level_id):
    init_session()
    
    if level_id in session['completed']:
        session['completed'].remove(level_id)
        # Also remove any levels after this one
        session['completed'] = [l for l in session['completed'] if l < level_id]
        session.modified = True
    
    return redirect(url_for('level', level_id=level_id))

@app.route('/reset_all')
def reset_all():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, port=5001)
