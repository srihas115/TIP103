## Learning with AI ✨

### Welcome

Welcome to your CodePath course! This course expects you to use AI tools like ChatGPT to help you learn and grow as a software engineer. This guide will introduce our new AI Tutor, as well as help you understand how to effectively use AI in your learning journey.

  

### AI Tutor

**[🔗 CodePath AI Tutor](https://go.codepath.org/tiptutor)**

Consistent, independent LeetCode practice is a staple of the TIP courses, but it can be challenging to unstuck yourself when completing a difficult problem alone. The AI Tutor is a Chrome extension that you can interact with directly in your browser, offering personalized guidance - using the UMPIRE methodology - to help you work through any LeetCode problem.

We recommend giving it a try!

  

Now we'll cover how to engage with AI (**🥸 AI roles**) outside of the AI Tutor, how to use AI effectively (**🟩 green flags**), and how to avoid common pitfalls (**🟥 red flags**), and show some example prompts to help you get started learning with AI!

  

### AI Roles

***✨ Regardless of which AI tool you use, it's important to consider how you want to use the AI tool in your learning journey. The roles below are some great examples of how AI should fit smoothly into your learning process.***

  

#### 😎 Virtual TA

- Ask for customized explanations
- Ask for additional learning materials

  

#### 🥸 Debugging / Planning Partner

- Talk through your thoughts
- Ask it to find areas for you to probe at
- Practice pair programming with it

  

#### 🧐 Research Assistant

- Ask it to find materials that will help
- Ask it to summarize key information in large references
- Ask it to list available commands or methods for a given topic, to help **you** choose the best one

  

***Tip:** These roles are most useful as prompt framing. You can constrain what the tool produces by stating the role explicitly. For example: **"Act as a virtual TA. Do not write any code — instead, ask me questions that help me work through the problem myself."** The more specific your instructions, the more reliably the output follows them.*

  

### AI Green Flags

***✨ These are some of the best ways to use AI in your learning journey. These are not the only ways to use AI in this course, but they are also some of the most effective ways to use AI throughout your software engineering career!***

  

#### 🟩 1. Brainstorm ideas/pair programming

- **Why:** Sometimes, it helps to have a brainstorming colleague who can help you run through different scenarios/use cases and can help you come up with new/insightful ideas. Additionally, you can use AI for pair programming by assigning it the role of a navigator or driver.
- **How:** Your AI tool will often produce output before you've provided all the necessary context — so you must be *very specific* about what you want it to do *(and not do!)*
- **Example Prompt:**
  - *I'd like to work on a pair programming assignment with some specific requirements. Could you be the navigator, and I will be the driver? Please do not write any code yourself.*

  

#### 🟩 2. Mock data generation

- **Why:** At times, you may have to create custom data models to be able to test your program. You can ask ChatGPT to generate this data for you, saving your time for more important tasks.
- **How:** Make sure you are *very specific* about the amount of data needed, and it may not be able to generate real-world data. For example, it can't provide real movie poster URLs. It can generate sample URLs, but they will be fictional.
- **Example Prompt:**
  - *"I have a Swift struct Movie data model with the following properties (title: String, description: String, rating: Double). Can you generate 10 movies and create an Array of movies?"*

  

#### 🟩 3. Simplifying difficult concepts

- **Why:** The pacing of the course can be fast at times, and instructors will have to prioritize which concepts to spend time on. When you feel confused about a term or phrase that gets glazed over, feel free to consult ChatGPT for more insightful explanations.
- **How:** When asking ChatGPT to define things for you, it can often get carried away. For example, not adding the part about 2-4 sentences means you might get a 3-4 paragraph answer. That might be what you want, but maybe it's not. Be specific!
- **Example Prompt**
  - *What is a protocol in Swift? Explain briefly in 2-4 sentences, and use an analogy to help it make sense.*

  

#### 🟩 4. Optimizing code

- **Why:** A great way to have ChatGPT improve your apps is to give it your code and ask for ideas around refactoring code, improving your algorithm to be more efficient, structuring your code to fit modern app architecture styles, etc.
- **How:** When asking for code optimization, it's crucial to be specific about what you'd like to improve. Whether it's speed, memory usage, or readability, stating your goals will lead to more relevant suggestions. ChatGPT can't run or test code, so you'll need to implement and verify the changes yourself.
- **Example Prompt**
  - *I have a Swift function for finding the largest element in an array that takes O(n^2) time. Can you help me optimize it to be faster?*

  

#### 🟩 5. Test/Debugging code

- **Why:** ChatGPT can help you find errors in your code and suggest improvements. It can also help you write unit tests for your code, which is a great way to ensure that your code works as expected.
- **How:** When asking ChatGPT to help you debug your code, have a direct desired outcome. Otherwise, you may get irrelevant suggestions. "Make this better" is not necessarily a good prompt. Additionally, the more context you can give, the better the advice it provides you.
- **Example Prompt**
  - *Take a look at my method `publishPost`. When the `publishPost` method is invoked, sometimes the view doesn't automatically reload as expected. Can you provide suggestions for ways I could revise this method so that it always updates the view? (Add additional context here)*

  

### AI Red Flags

***✨ These are some of the most ineffective ways to use AI in your learning journey. You might be tempted to use AI in these ways, but beware -- they will not help you learn and grow as a software engineer!***

  

#### 🟥 1. Using AI as the source of truth

- **Why:** While AI can generate code, it has limitations. Without sufficient context, it often produces incorrect or outdated information.
- **How to Avoid:** Always refer to direct guides (like Apple Developer guides, Google Android guides, or other official resources) as the source of truth. AI should be used as a supplementary tool, not the primary source of information.

  

#### 🟥 2. Copying and pasting code without understanding

- **Why:** Copying and pasting code without understanding it can lead to a lack of comprehension of the underlying concepts. This approach can result in you not learning how to solve problems on your own.
- **How to Avoid:** When using AI-generated code, take the time to understand how it works. Break down the code into smaller parts, ask questions about each section, and ensure you grasp the logic behind it. This will help you build a solid foundation in programming.

  

#### 🟥 3. Over-reliance on AI for solutions

- **Why:** While AI can provide quick solutions, it may not always offer the best or most efficient approach. Over-reliance can lead to a lack of creativity and innovation in your coding practices.
- **How to Avoid:** Use AI as a brainstorming partner, but don't let it dictate your coding style or approach. Experiment with different solutions, and use AI to explore alternative methods or optimizations.

  

#### 🟥 4. Ignoring best practices

- **Why:** AI-generated code may not always adhere to best practices or industry standards. Following poor coding practices can lead to maintainability issues and technical debt in your projects.
- **How to Avoid:** Always review AI-generated code for adherence to best practices. Ensure that it follows coding conventions, is well-structured, and is maintainable. Use AI as a tool to enhance your understanding of best practices rather than replace them.

  

#### 🟥 5. Confirmation Bias

- **Why:** If you're using AI to confirm your chosen approach, you might be missing out on other possible perspectives. AI can provide those as well when prompted, so it's essential to think critically about its suggestions.
- **How to Avoid:** When using AI, be open to exploring different viewpoints and solutions. Don't just seek validation for your existing ideas; instead, challenge yourself to consider alternative approaches. This will help you broaden your understanding and improve your problem-solving skills.

  

Finally, remember that AI is just a tool! It's not inherently good or bad. Remember to use all of your outside resources as well when problem-solving. Google, Stack Overflow, classmates, TFs/TAs, and instructors are still incredibly helpful and necessary!
