# litegrade

**litegrade** is a Python library that gives IPython notebook authors a simple and user friendly method of evaluating the learning retention of notebook readers. A few functionalities include:

  - Implement in Jupyter and Google Colab notebook environments
  - **ask** questions anywhere in an already written notebook
  - **check** answers with an option of providing feedback
  - **handin** and store answers at a selected server location
  - **analyze** learning retention to improve notebook content

# New Features!

  - HTML and JavaScript interactive question formats

You can also:
  - Select database storage locations such as DynamoDB or Google Drive
  - Customize question format and styles with CSS

### How to Use

Install the library into your notebook

```py
[ ] !curl https://www.justinleemorgan.com/litegrade > litegrade.zip; unzip litegrade.zip
```
Import the **ask** library function

```py
[ ] from litegrade import ask
```
![alt text](https://www.justinleemorgan.com/api/litegrade/submit_button "Example use of the ask function")

Invoke the **ask** function to ask the reader a question about the notebook content

```py
[ ] ask("Recursion question")
```
![alt text](https://www.justinleemorgan.com/api/litegrade/recursion_question "Example use of the ask function")

### Development

Want to contribute to the **litegrade** project? Great!

View some of our current [issues](https://github.com/2justinmorgan/litegrade/issues) on GitHub

After pulling the **litegrade** repository, run the developer's setup script located in the project's home diretory. This will install any needed dependencies as well as create symbolic links used for testing.

```sh
$ ./dev_setup.sh
```

To run tests

```sh
$ test/pytest
```
