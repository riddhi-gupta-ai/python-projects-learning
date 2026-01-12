# Python Projects - Learn by Building

A project-based Python learning platform featuring 15 hands-on coding challenges. Progress from simple beginner projects to advanced games while mastering Python fundamentals through real-world applications.

## Overview

Unlike traditional concept-based learning, this platform teaches Python through building complete, working applications. Each project is a self-contained challenge that teaches multiple concepts while creating something practical and fun. From simple calculators to complete games like Blackjack and Hangman, you'll learn by doing.

## Philosophy

**Learn by building, not by memorizing.** This platform emphasizes practical application over theoretical knowledge. Each project combines multiple Python concepts to create real, functional programs. You'll learn variables, loops, functions, and data structures naturally as you solve real problems.

## Features

- **15 Progressive Projects**: Build real applications from Name Tag Generator to Hangman
- **Project-Based Learning**: Each challenge creates a complete, working program
- **Real-World Applications**: Build calculators, games, ciphers, and practical tools
- **Interactive Code Editor**: Write and test code directly in your browser with Tab key support
- **Instant Feedback System**:
  - Get immediate results from your code
  - See expected vs. actual output
  - Access hints when stuck
  - View complete solutions with explanations
- **Progress Tracking**:
  - Daily streak counter for consistent learning
  - Score system based on completed projects
  - Completion badges and achievements
  - Maximum streak tracking
- **Difficulty Progression**: Beginner → Intermediate → Advanced
- **Sequential Unlocking**: Complete projects in order to build skills progressively
- **Learning Goals**: Each project clearly lists what you'll learn
- **Code Safety**: Sandboxed execution environment with timeout protection
- **Responsive Design**: Works on desktop, tablet, and mobile devices

## Prerequisites

- **Python 3.7 or higher** - [Download Python](https://www.python.org/downloads/)
- **pip** - Python package manager (included with Python 3.4+)
- **Basic Python knowledge** - Recommended to complete PyLearn first (see parent directory)

## Installation

### Quick Start

1. **Clone or download this repository**

2. **Navigate to the project-site directory:**
```bash
cd /Users/riddhiairan/Developer/pythonwebsite/project-site
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

Or install Flask directly:
```bash
pip install Flask==3.0.0 Werkzeug==3.0.1
```

4. **Run the application:**
```bash
python app.py
```

5. **Open your browser and visit:**
```
http://localhost:5002
```

### Virtual Environment Setup (Recommended)

Using a virtual environment is the best practice for Python projects:

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

To deactivate the virtual environment when done:
```bash
deactivate
```

## Project Structure

```
project-site/
├── app.py                 # Flask app with 15 project definitions & execution engine
├── requirements.txt       # Python dependencies (Flask 3.0.0, Werkzeug 3.0.1)
├── README.md             # This file
└── templates/            # HTML templates
    ├── base.html         # Base template with navigation & styling
    ├── index.html        # Project list homepage with grid layout
    └── level.html        # Individual project page with code editor
```

## Complete Project List

### Beginner Projects (1-5)
Projects that introduce fundamental Python concepts through simple, practical applications.

**1. Name Tag Generator**
- **Concepts**: Variables, String Concatenation, Print Statements
- **Build**: A personalized greeting generator
- **Learn**: How to store and combine text data

**2. Tip Calculator**
- **Concepts**: Arithmetic Operations, Functions, Rounding
- **Build**: Calculate tips and split bills among friends
- **Learn**: Mathematical operations and the `round()` function

**3. Love Calculator**
- **Concepts**: String Methods, Counting, Case Conversion
- **Build**: A fun compatibility calculator based on names
- **Learn**: String manipulation with `.lower()` and `.count()`

**4. BMI Calculator**
- **Concepts**: Conditionals, Health Calculations, if-elif-else
- **Build**: Body Mass Index calculator with health categories
- **Learn**: Decision-making with comparison operators

**5. Pizza Order**
- **Concepts**: Multiple Inputs, Nested Conditionals, Price Calculation
- **Build**: A pizza ordering system with customizable toppings
- **Learn**: Complex conditional logic and variable updates

### Intermediate Projects (6-10)
More complex projects involving game logic, loops, and data structures.

**6. Treasure Island**
- **Concepts**: Logical Operators (AND/OR), Complex Conditionals, Game Logic
- **Build**: A choose-your-own-adventure game
- **Learn**: Combining multiple conditions with logical operators

**7. Rock Paper Scissors**
- **Concepts**: Complex Logic, Multiple OR Conditions, Game Rules
- **Build**: The classic hand game with win/lose/draw logic
- **Learn**: Implementing game rules with complex conditionals

**8. Caesar Cipher**
- **Concepts**: For Loops, String Building, Character Manipulation
- **Build**: An encryption tool using the Caesar Cipher algorithm
- **Learn**: `ord()` and `chr()` functions for character conversion

**9. Secret Auction**
- **Concepts**: Dictionaries, Key-Value Pairs, Finding Maximum Values
- **Build**: An auction system that tracks and determines the highest bidder
- **Learn**: Dictionary operations and the `max()` function

**10. Calculator**
- **Concepts**: Function Definition, Parameters, Return Statements
- **Build**: A basic calculator with arithmetic operations
- **Learn**: Creating reusable functions with parameters and returns

### Advanced Projects (11-15)
Challenging projects featuring complex game logic, data structures, and algorithms.

**11. Blackjack Game**
- **Concepts**: List Operations, `sum()`, `in` Operator, Game Logic
- **Build**: Core Blackjack logic with Ace handling
- **Learn**: Working with lists and implementing card game rules

**12. Number Guessing Game**
- **Concepts**: While Loops, `break` Statement, Loop Control, Game State
- **Build**: An interactive guessing game with higher/lower hints
- **Learn**: Loop control flow and early termination

**13. Higher or Lower Game**
- **Concepts**: Nested Data Structures, Lists of Dictionaries, Data Comparison
- **Build**: Compare social media follower counts
- **Learn**: Accessing nested data with multiple brackets

**14. Coffee Machine**
- **Concepts**: Dictionary Iteration, Resource Management, Boolean Flags
- **Build**: A coffee machine simulator with resource tracking
- **Learn**: Complex logic with resource validation

**15. Hangman**
- **Concepts**: String Building, List Membership, Game State Display
- **Build**: The classic word-guessing game with letter revealing
- **Learn**: Building display strings based on game state

## Usage Guide

### Getting Started

1. **Launch the application** at `http://localhost:5002`
2. **Browse the project grid** - See all 15 projects organized by difficulty
3. **Start with Project 1** - Begin with the Name Tag Generator
4. **Read the project description** - Understand what you're building
5. **Review the task** - See the specific requirements and examples
6. **Write your code** - Use the interactive editor (Tab key inserts 4 spaces)
7. **Run your code** - Click "Run Code" to execute and see output
8. **Check results** - Compare your output with the expected result
9. **Use hints** - Toggle hints if you need guidance
10. **View solutions** - See complete solutions with detailed explanations
11. **Unlock next project** - Complete each project to unlock the next

### Building Your Streak

- Complete projects consistently to build your daily streak
- Your streak increases when you code on consecutive days
- Track your maximum streak as a personal best
- Maintain motivation by watching your progress grow

### Learning Strategy

**For Best Results:**
1. Try to solve each project yourself first
2. Use hints only when genuinely stuck
3. Read the explanation even after completing a project
4. Experiment with the code to understand how it works
5. Modify projects to add your own features
6. Review previous projects to reinforce learning

**Time Investment:**
- Beginner projects: 10-20 minutes each
- Intermediate projects: 20-40 minutes each
- Advanced projects: 30-60 minutes each

## Configuration

### Port Configuration

The application runs on **port 5002** by default to avoid conflicts with the PyLearn platform (port 5001).

To change the port, modify the last line in `app.py`:
```python
app.run(debug=debug_mode, port=5002)  # Change to your desired port
```

### Debug Mode

Enable Flask debug mode for development:

```bash
# Set environment variable
export FLASK_DEBUG=True   # macOS/Linux
set FLASK_DEBUG=True      # Windows

# Run the app
python app.py
```

Debug mode provides:
- Auto-reload when code changes
- Detailed error pages
- Interactive debugger

### Secret Key Configuration

For production deployment, set a secure secret key:

**Option 1: Environment Variable (Recommended)**
```bash
export FLASK_SECRET_KEY='your-secure-random-secret-key-here'
```

**Option 2: Direct in app.py**
```python
app.secret_key = 'your-secure-random-secret-key-here'
```

Generate a secure key with:
```python
import secrets
print(secrets.token_hex(32))
```

## Troubleshooting

### Port Already in Use

**Error:** `OSError: [Errno 48] Address already in use`

**Solutions:**
```bash
# Option 1: Find and kill the process using port 5002
lsof -ti:5002 | xargs kill -9   # macOS/Linux
netstat -ano | findstr :5002    # Windows (then use taskkill)

# Option 2: Change port in app.py to 5003 or another available port

# Option 3: Stop the other application using the port
```

### Module Not Found

**Error:** `ModuleNotFoundError: No module named 'flask'`

**Solution:**
```bash
# Activate virtual environment if you created one
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Verify installation
pip list | grep Flask
```

### Templates Not Found

**Error:** `jinja2.exceptions.TemplateNotFound`

**Solution:** Ensure the `templates/` directory exists with all required files:
- `base.html` - Base template
- `index.html` - Project list page
- `level.html` - Individual project page

All template files should be in the `templates/` directory relative to `app.py`.

### Code Execution Timeout

**Error:** `TimeoutError: Code execution timed out (exceeded 5 seconds)`

**Causes:**
- Infinite loops in your code
- Very large computations
- Waiting for input (input() function doesn't work in this environment)

**Solutions:**
- Check for infinite loops in your code
- Ensure loop conditions eventually become False
- Use print statements for debugging instead of input()

### Wrong Output

**Issue:** Your output doesn't match the expected output

**Debugging Steps:**
1. **Check for typos** - Output must match exactly (including capitalization and spaces)
2. **Review the task** - Make sure you understand what's required
3. **Use print for debugging** - Add print statements to see variable values
4. **Check your logic** - Verify your conditional statements and calculations
5. **Use hints** - Toggle hints for guidance
6. **Study the solution** - Learn from the working code

### Session Not Persisting

**Issue:** Progress resets when you refresh the page

**Cause:** Sessions are browser-based and may clear on browser restart

**Note:** This is expected behavior. The app uses session storage, which is temporary. To keep permanent progress, you would need to implement user accounts with database storage.

## Technical Details

### Code Execution Safety

The platform uses multiple layers of security:

**Restricted Built-ins:**
Only safe Python functions are available:
- Basic: `print`, `range`, `len`, `str`, `int`, `float`
- Collections: `list`, `dict`, `tuple`, `set`
- Math: `abs`, `max`, `min`, `sum`, `round`
- Iteration: `sorted`, `reversed`, `enumerate`, `zip`, `map`, `filter`
- Character: `ord`, `chr`

**What's NOT Available:**
- File operations (`open`, `write`, etc.)
- System operations (`os`, `sys`)
- Network operations (`urllib`, `requests`)
- Dangerous functions (`eval`, `exec` on user strings)

**Timeout Protection:**
- 5-second maximum execution time
- Prevents infinite loops from hanging the server
- Uses ThreadPoolExecutor for safe isolated execution

**Isolated Namespace:**
- Each code execution runs in its own namespace
- No access to Flask application internals
- No shared state between executions

### Session Management

**What's Stored:**
- `completed`: List of completed project IDs
- `streak`: Current consecutive days of coding
- `max_streak`: Personal best streak
- `score`: Total points earned
- `last_activity_date`: Last date you completed a project
- `attempts`: Track of attempts per project

**Session Lifecycle:**
- Created automatically on first visit
- Persists across page refreshes
- Clears when browser is closed (or after timeout)
- Can be manually reset via `/reset_all` route

**Reset Options:**
- **Single Project:** `/reset/<project_id>` - Reset a specific project
- **All Progress:** `/reset_all` - Clear all progress and start fresh

## Comparison with PyLearn

Both platforms complement each other:

| Feature | **PyLearn** (Parent Directory) | **Python Projects** (This Project) |
|---------|-------------------------------|-----------------------------------|
| **Focus** | Fundamental concepts | Complete projects |
| **Teaching Style** | Concept explanation → Practice | Problem → Solution → Understanding |
| **Projects** | 15 concept-focused exercises | 15 real-world applications |
| **Difficulty Curve** | Gentle, concept-by-concept | Steeper, combines concepts |
| **Best For** | Complete beginners | Learners with basic knowledge |
| **Port** | 5001 | 5002 |
| **Time per Exercise** | 5-10 minutes | 15-60 minutes |
| **Learning Outcome** | Understand Python syntax | Build working programs |

**Recommended Path:**
1. Start with **PyLearn** to learn Python fundamentals
2. Move to **Python Projects** to build real applications
3. Go back and forth as needed to reinforce concepts

## Contributing

Contributions are welcome! Here's how you can help:

### Add New Projects
- Create projects that teach new concepts
- Ensure clear task descriptions
- Provide working solutions with explanations
- Include helpful hints

### Improve Existing Projects
- Clarify task descriptions
- Enhance explanations
- Add better hints
- Fix any bugs

### Enhance Features
- Add syntax highlighting to the code editor
- Implement code saving functionality
- Add project difficulty ratings
- Create a hint system with multiple levels
- Add keyboard shortcuts (Ctrl+Enter to run)
- Implement theme switching (light/dark)
- Add project categories/tags
- Create user authentication for permanent progress

### Code Quality
- Write unit tests for the application
- Improve error handling
- Optimize code execution safety
- Add code coverage

## Future Enhancements

Planned features for future versions:

**Learning Features:**
- Multiple test cases per project
- Progressive hints (reveal more as you struggle)
- Video explanations for each project
- Alternative solutions with different approaches
- Bonus challenges for completed projects

**Platform Features:**
- User accounts with database storage
- Persistent progress across devices
- Social features (share solutions, discuss)
- Leaderboards and competitions
- Achievement badges and certificates
- Mobile app version

**Content Expansion:**
- Additional 15-20 projects (30+ total)
- Project variations for practice
- Challenge mode with time limits
- Custom project creator for teachers
- Integration with external APIs

**Technical Improvements:**
- Real-time code collaboration
- Code syntax highlighting
- Autocomplete in the editor
- Git integration to save solutions
- Export progress as portfolio

## Educational Use

### For Teachers

This platform is perfect for:
- Classroom coding exercises
- Homework assignments
- Assessment tools
- Self-paced learning modules

**Customization:**
- Modify projects in `app.py` to match your curriculum
- Add or remove projects as needed
- Adjust difficulty levels
- Create custom project sequences

### For Students

**Learning Tips:**
- Complete projects in order for best results
- Don't just copy solutions - understand them
- Experiment with code modifications
- Help classmates understand concepts (teaching reinforces learning)
- Build a portfolio by expanding on these projects

### For Self-Learners

**Maximize Your Learning:**
- Set a daily goal (1-2 projects per day)
- Join online communities to discuss solutions
- Create variations of projects for practice
- Share your completed projects on GitHub
- Build a portfolio showcasing your work

## License

This project is released under the MIT License and is free to use for educational purposes.

```
MIT License

Copyright (c) 2024 Python Projects - Learn by Building

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Support & Resources

### Getting Help

**Within the Platform:**
- Read project descriptions carefully
- Use the hint system
- Study solution explanations
- Review previous projects

**External Resources:**
- [Python Official Documentation](https://docs.python.org/3/)
- [Python Tutorial for Beginners](https://www.python.org/about/gettingstarted/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Real Python Tutorials](https://realpython.com/)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/python)

### Practice Beyond This Platform

- [LeetCode](https://leetcode.com/) - Algorithm challenges
- [HackerRank](https://www.hackerrank.com/domains/python) - Python practice
- [Project Euler](https://projecteuler.net/) - Mathematical programming
- [Codewars](https://www.codewars.com/) - Kata challenges
- Build your own projects - The best way to learn!

## Credits

**Built With:**
- **Flask 3.0.0** - Python web framework
- **Werkzeug 3.0.1** - WSGI utility library
- **HTML5, CSS3, JavaScript** - Frontend technologies
- **Python 3.7+** - Programming language

**Inspired By:**
- Project-based learning methodologies
- Boot camp coding challenges
- Interactive coding platforms
- Real-world application development

**Designed For:**
- Students learning Python programming
- Self-learners building practical skills
- Developers transitioning to Python
- Anyone who learns best by building

## Acknowledgments

Thanks to the Python and Flask communities for creating excellent tools and documentation. Special appreciation to educators worldwide who inspire project-based learning approaches.

## FAQ

**Q: Do I need to complete projects in order?**
A: Yes, projects unlock sequentially. This ensures you build foundational skills before tackling complex challenges.

**Q: Can I skip projects?**
A: No, but you can use hints and solutions to learn and progress. Understanding is more important than struggling indefinitely.

**Q: How long does it take to complete all projects?**
A: Typically 8-15 hours total, depending on experience level. Beginners may take longer.

**Q: Can I use this for teaching?**
A: Absolutely! It's perfect for classrooms, coding clubs, and self-paced learning.

**Q: Is there a certificate upon completion?**
A: Not currently, but this feature is planned for future versions.

**Q: Can I add my own projects?**
A: Yes! Edit the `LEVELS` list in `app.py` to add custom projects.

**Q: Does this cover all Python concepts?**
A: It covers fundamentals. For advanced topics (OOP, decorators, generators, etc.), additional resources are needed.

**Q: Can I save my code?**
A: Currently, no. Code is executed temporarily. Consider copying solutions to your own files for future reference.

---

**Ready to Build? Start Your Python Project Journey Today! 🚀**

*Learn Python by building real projects. From calculators to games, master coding through practical application.*
