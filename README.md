# **litegrade**

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

Install the library 


```py
[ ] !pip install litegrade
```

Import the **begin** and **ask** library functions


```py
[ ] from litegrade import begin, ask
```

Invoke the **begin** function to get the "Demo" assignment questions that will be asked


```py
[ ] begin("Demo")
```


Invoke the **ask** function to ask the reader a question about the notebook content


```py
[ ] ask("Recursion question")
```

Multiple checkbox selections is another available question format


```py
[ ] ask("Multi-selection question")
```

### Development

Want to contribute to the **litegrade** project? Great!

View some of our current [issues](https://github.com/2justinmorgan/litegrade/issues) on GitHub

After pulling the **litegrade** repository, run the developer's setup script located in the project's home diretory. This will install any needed dependencies as well as create symbolic links used for testing.

```sh
$ ./dev_setup.sh
```

To run tests

```sh
$ pytest test/
```

To deploy to PyPi

```sh
$ . package/release
```

