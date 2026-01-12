from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import io
import contextlib
import os
from concurrent.futures import ThreadPoolExecutor, TimeoutError as FuturesTimeoutError
from datetime import datetime, date

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'project-learning-secret-key')

# 15 Project-Based Python Levels (Basic to Advanced)
LEVELS = [
    {
        "id": 1,
        "title": "Name Tag Generator",
        "difficulty": "Beginner",
        "description": "Create a personalized name tag generator that welcomes users with a custom greeting.",
        "task": "Write a program that creates variables for <strong>name = 'Sarah'</strong> and <strong>city = 'NYC'</strong>, then prints: <strong>Hello Sarah from NYC!</strong>",
        "hint": "Use string concatenation: print('Hello ' + name + ' from ' + city + '!')",
        "expected_output": "Hello Sarah from NYC!",
        "solution": "name = 'Sarah'\ncity = 'NYC'\nprint('Hello ' + name + ' from ' + city + '!')",
        "explanation": "This project teaches variable creation and string concatenation. Variables store data that can be reused, and the + operator joins strings together.",
        "learning_goals": ["Variables", "String Concatenation", "Print Statements"]
    },
    {
        "id": 2,
        "title": "Tip Calculator",
        "difficulty": "Beginner",
        "description": "Calculate how much tip to leave at a restaurant and split the bill among friends.",
        "task": "Given <strong>bill = 150</strong>, <strong>tip_percent = 15</strong>, and <strong>people = 3</strong>, calculate and print the amount each person pays (rounded to 2 decimals). Formula: total = bill * (1 + tip_percent/100) / people",
        "hint": "Calculate: total = bill * (1 + tip_percent/100) / people, then use round(total, 2)",
        "expected_output": "57.5",
        "solution": "bill = 150\ntip_percent = 15\npeople = 3\ntotal = bill * (1 + tip_percent/100) / people\nprint(round(total, 2))",
        "explanation": "This project combines arithmetic operations with the round() function. The formula calculates the tip, adds it to the bill, then divides by the number of people.",
        "learning_goals": ["Arithmetic Operations", "Variables", "round() Function"]
    },
    {
        "id": 3,
        "title": "Love Calculator",
        "difficulty": "Beginner",
        "description": "Calculate a 'love score' between two names based on the count of special letters.",
        "task": "For <strong>name1 = 'Angela'</strong> and <strong>name2 = 'Jack'</strong>, count how many times the letters 'L','O','V','E' appear (case insensitive) in both names combined. Print that count.",
        "hint": "Combine names: combined = (name1 + name2).lower(), then use combined.count() for each letter and sum them",
        "expected_output": "2",
        "solution": "name1 = 'Angela'\nname2 = 'Jack'\ncombined = (name1 + name2).lower()\nscore = combined.count('l') + combined.count('o') + combined.count('v') + combined.count('e')\nprint(score)",
        "explanation": "This uses string methods: .lower() converts to lowercase, .count() counts occurrences of a character. We sum the counts of L-O-V-E letters.",
        "learning_goals": ["String Methods", "count()", "lower()", "Arithmetic"]
    },
    {
        "id": 4,
        "title": "BMI Calculator",
        "difficulty": "Beginner",
        "description": "Calculate Body Mass Index and determine if someone is underweight, normal, or overweight.",
        "task": "Given <strong>weight = 70</strong> kg and <strong>height = 1.75</strong> m, calculate BMI = weight / (height ** 2). If BMI < 18.5 print <strong>'Underweight'</strong>, if BMI < 25 print <strong>'Normal'</strong>, else print <strong>'Overweight'</strong>.",
        "hint": "Calculate BMI first, then use if-elif-else to check ranges",
        "expected_output": "Normal",
        "solution": "weight = 70\nheight = 1.75\nbmi = weight / (height ** 2)\nif bmi < 18.5:\n    print('Underweight')\nelif bmi < 25:\n    print('Normal')\nelse:\n    print('Overweight')",
        "explanation": "BMI is calculated using the formula weight/height². We use if-elif-else to categorize the result into three ranges.",
        "learning_goals": ["Conditionals", "if-elif-else", "Arithmetic", "Comparison Operators"]
    },
    {
        "id": 5,
        "title": "Pizza Order",
        "difficulty": "Beginner",
        "description": "Calculate the total cost of a pizza order based on size and extra toppings.",
        "task": "Pizza prices: Small=$15, Medium=$20, Large=$25. Extra pepperoni: +$2 for S/M, +$3 for L. Extra cheese: +$1 any size. Given <strong>size='L'</strong>, <strong>pepperoni='Y'</strong>, <strong>cheese='Y'</strong>, calculate and print the total bill.",
        "hint": "Start with base price, then add extras based on conditions",
        "expected_output": "29",
        "solution": "size = 'L'\npepperoni = 'Y'\ncheese = 'Y'\nbill = 0\nif size == 'S':\n    bill = 15\nelif size == 'M':\n    bill = 20\nelse:\n    bill = 25\nif pepperoni == 'Y':\n    if size == 'L':\n        bill += 3\n    else:\n        bill += 2\nif cheese == 'Y':\n    bill += 1\nprint(bill)",
        "explanation": "This project uses multiple conditionals to build up a price. We start with the base pizza price, then add extras based on conditions.",
        "learning_goals": ["Nested Conditionals", "Multiple If Statements", "Variable Updates"]
    },
    {
        "id": 6,
        "title": "Treasure Island",
        "difficulty": "Intermediate",
        "description": "Create a choose-your-own-adventure game where choices lead to different outcomes.",
        "task": "Create a simple game: <strong>choice1='left'</strong>, <strong>choice2='swim'</strong>. If choice1 is 'left' AND choice2 is 'swim', print <strong>'You Win!'</strong>, otherwise print <strong>'Game Over'</strong>.",
        "hint": "Use nested if statements or logical AND operator",
        "expected_output": "You Win!",
        "solution": "choice1 = 'left'\nchoice2 = 'swim'\nif choice1 == 'left' and choice2 == 'swim':\n    print('You Win!')\nelse:\n    print('Game Over')",
        "explanation": "This introduces logical operators (AND). Both conditions must be True for the win condition. The 'and' operator combines multiple conditions.",
        "learning_goals": ["Logical Operators", "and/or", "Complex Conditionals", "Game Logic"]
    },
    {
        "id": 7,
        "title": "Rock Paper Scissors",
        "difficulty": "Intermediate",
        "description": "Build the classic Rock-Paper-Scissors game with win/lose/draw logic.",
        "task": "Given <strong>user='rock'</strong> and <strong>computer='scissors'</strong>, determine the winner. Rock beats scissors, scissors beats paper, paper beats rock. Print <strong>'You win'</strong>, <strong>'You lose'</strong>, or <strong>'Draw'</strong>.",
        "hint": "Use if-elif to check all winning combinations for the user",
        "expected_output": "You win",
        "solution": "user = 'rock'\ncomputer = 'scissors'\nif user == computer:\n    print('Draw')\nelif (user == 'rock' and computer == 'scissors') or (user == 'scissors' and computer == 'paper') or (user == 'paper' and computer == 'rock'):\n    print('You win')\nelse:\n    print('You lose')",
        "explanation": "This uses complex logical operators to check multiple winning conditions. The 'or' operator means any one condition being True makes the whole expression True.",
        "learning_goals": ["Complex Logic", "or Operator", "Game Rules", "Multiple Conditions"]
    },
    {
        "id": 8,
        "title": "Caesar Cipher",
        "difficulty": "Intermediate",
        "description": "Encrypt a message by shifting each letter by a fixed number (Caesar Cipher encryption).",
        "task": "Create <strong>text = 'abc'</strong> and <strong>shift = 1</strong>. Shift each letter forward by 1 (a→b, b→c, c→d). Print the encrypted text: <strong>bcd</strong>",
        "hint": "Loop through each character, convert to number with ord(), add shift, convert back with chr()",
        "expected_output": "bcd",
        "solution": "text = 'abc'\nshift = 1\nresult = ''\nfor char in text:\n    new_char = chr(ord(char) + shift)\n    result += new_char\nprint(result)",
        "explanation": "This uses ord() to get ASCII code of a character, adds the shift value, then chr() converts back to a character. We build the result string character by character.",
        "learning_goals": ["For Loops", "String Building", "ord() and chr()", "Character Manipulation"]
    },
    {
        "id": 9,
        "title": "Secret Auction",
        "difficulty": "Intermediate",
        "description": "Track multiple bids in an auction and find the highest bidder.",
        "task": "Given <strong>bids = {'Alice': 50, 'Bob': 75, 'Charlie': 60}</strong>, find and print the name of the highest bidder: <strong>Bob</strong>",
        "hint": "Use max() with a key parameter: max(bids, key=bids.get)",
        "expected_output": "Bob",
        "solution": "bids = {'Alice': 50, 'Bob': 75, 'Charlie': 60}\nwinner = max(bids, key=bids.get)\nprint(winner)",
        "explanation": "Dictionaries store key-value pairs. The max() function with key=bids.get finds the key with the maximum value. This is a powerful pattern for finding extremes in dictionaries.",
        "learning_goals": ["Dictionaries", "max() Function", "Key-Value Pairs", "Dictionary Methods"]
    },
    {
        "id": 10,
        "title": "Calculator",
        "difficulty": "Intermediate",
        "description": "Build a calculator that can perform basic arithmetic operations using functions.",
        "task": "Define a function <strong>add(a, b)</strong> that returns <strong>a + b</strong>. Call it with <strong>add(10, 5)</strong> and print the result: <strong>15</strong>",
        "hint": "Use def to define the function with return statement",
        "expected_output": "15",
        "solution": "def add(a, b):\n    return a + b\n\nresult = add(10, 5)\nprint(result)",
        "explanation": "Functions are reusable code blocks. The 'def' keyword defines them, parameters go in parentheses, and 'return' sends a value back to the caller.",
        "learning_goals": ["Function Definition", "Parameters", "return Statement", "Function Calls"]
    },
    {
        "id": 11,
        "title": "Blackjack Game",
        "difficulty": "Advanced",
        "description": "Implement core Blackjack logic: calculate hand value and determine if it's a bust (over 21).",
        "task": "Given <strong>cards = [10, 11, 5]</strong>, calculate the total. If total > 21 and there's an 11 (Ace), convert it to 1. Print the final total: <strong>16</strong>",
        "hint": "Sum the cards, then check if sum > 21 and 11 in cards, if so: subtract 10",
        "expected_output": "16",
        "solution": "cards = [10, 11, 5]\ntotal = sum(cards)\nif total > 21 and 11 in cards:\n    total -= 10\nprint(total)",
        "explanation": "This uses sum() to add list elements and the 'in' operator to check membership. Ace handling (11→1 when busting) is a key Blackjack rule.",
        "learning_goals": ["List Operations", "sum()", "in Operator", "Game Logic"]
    },
    {
        "id": 12,
        "title": "Number Guessing Game",
        "difficulty": "Advanced",
        "description": "Create a game that gives hints (higher/lower) based on guesses until the correct number is found.",
        "task": "Given <strong>secret = 42</strong>, <strong>guesses = [30, 50, 42]</strong>, loop through guesses. For each: if too low print <strong>'Higher'</strong>, if too high print <strong>'Lower'</strong>, if correct print <strong>'Correct!'</strong> and stop.",
        "hint": "Use a for loop with if-elif-else, and 'break' to stop when correct",
        "expected_output": "Higher\nLower\nCorrect!",
        "solution": "secret = 42\nguesses = [30, 50, 42]\nfor guess in guesses:\n    if guess < secret:\n        print('Higher')\n    elif guess > secret:\n        print('Lower')\n    else:\n        print('Correct!')\n        break",
        "explanation": "The 'break' statement exits a loop early. This is essential for game logic where you want to stop when a condition is met (like guessing correctly).",
        "learning_goals": ["While Loops Concept", "break Statement", "Loop Control", "Game State"]
    },
    {
        "id": 13,
        "title": "Higher or Lower Game",
        "difficulty": "Advanced",
        "description": "Compare two items and determine which has the higher value, tracking score.",
        "task": "Given <strong>data = [{'name': 'Instagram', 'followers': 500}, {'name': 'Twitter', 'followers': 400}]</strong>. Print the name of the account with more followers: <strong>Instagram</strong>",
        "hint": "Access dictionary values: if data[0]['followers'] > data[1]['followers']",
        "expected_output": "Instagram",
        "solution": "data = [{'name': 'Instagram', 'followers': 500}, {'name': 'Twitter', 'followers': 400}]\nif data[0]['followers'] > data[1]['followers']:\n    print(data[0]['name'])\nelse:\n    print(data[1]['name'])",
        "explanation": "This combines lists and dictionaries: a list of dictionary objects. Access nested data with multiple brackets: data[0]['followers'].",
        "learning_goals": ["Nested Data Structures", "Lists of Dictionaries", "Data Comparison"]
    },
    {
        "id": 14,
        "title": "Coffee Machine",
        "difficulty": "Advanced",
        "description": "Simulate a coffee machine that tracks resources and processes orders.",
        "task": "Given <strong>resources = {'water': 300, 'coffee': 100}</strong> and <strong>order = {'water': 50, 'coffee': 18}</strong>. Check if enough resources exist. If yes, print <strong>'Here is your coffee'</strong>, otherwise print <strong>'Not enough resources'</strong>.",
        "hint": "Check each resource: if resources[item] >= order[item] for all items",
        "expected_output": "Here is your coffee",
        "solution": "resources = {'water': 300, 'coffee': 100}\norder = {'water': 50, 'coffee': 18}\nenough = True\nfor item in order:\n    if resources[item] < order[item]:\n        enough = False\n        break\nif enough:\n    print('Here is your coffee')\nelse:\n    print('Not enough resources')",
        "explanation": "This demonstrates iteration over dictionary keys and resource management logic. We check all requirements before proceeding with the order.",
        "learning_goals": ["Dictionary Iteration", "Resource Management", "Boolean Flags", "Complex Logic"]
    },
    {
        "id": 15,
        "title": "Hangman",
        "difficulty": "Advanced",
        "description": "Build the classic word-guessing game, revealing letters and tracking wrong guesses.",
        "task": "Given <strong>word = 'python'</strong>, <strong>guessed = ['p', 'y', 't']</strong>. Create a display string showing guessed letters and '_' for others. Print: <strong>pyt___</strong>",
        "hint": "Loop through word, if letter in guessed show it, else show '_'",
        "expected_output": "pyt___",
        "solution": "word = 'python'\nguessed = ['p', 'y', 't']\ndisplay = ''\nfor letter in word:\n    if letter in guessed:\n        display += letter\n    else:\n        display += '_'\nprint(display)",
        "explanation": "This combines string building, list membership checking, and loops. Building strings character by character based on conditions is a common pattern in text-based games.",
        "learning_goals": ["String Building", "List Membership", "Game State Display", "Complex Loops"]
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
        'round': round,
        'ord': ord,
        'chr': chr,
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
    port = int(os.environ.get('PORT', 5002))
    app.run(debug=debug_mode, host='0.0.0.0', port=port)
