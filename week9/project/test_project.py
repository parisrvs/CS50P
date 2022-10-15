from project import parse_topic, load_content, search_content

def test_parse_topic():
    assert parse_topic("2. Using the Python Interpreter") == ("2.", "Using the Python Interpreter")
    assert parse_topic("5.4. Sets") == ("5.4.", "Sets")
    assert parse_topic("5.5. Dictionaries") == ("5.5.", "Dictionaries")
    assert parse_topic("6.1.2. The Module Search Path") == ("6.1.2.", "The Module Search Path")
    assert parse_topic("6.4.3. Packages in Multiple Directories") == ("6.4.3.", "Packages in Multiple Directories")
    assert parse_topic("7. Input and Output") == ("7.", "Input and Output")


def test_load_content():
    assert load_content("https://docs.python.org/3/tutorial/index.html/a.html") == False
    assert load_content("hts:/ds.pthon.org/3/tial/index.html/a.html") == False
    assert load_content("https://docs.python.org/3/tutorial/index.html") == True


def test_search_content():
    assert search_content("ejfjejfoe") == None
    assert search_content("set") == [{'number': '5.4.', 'title': 'Sets', 'link': 'https://docs.python.org/3/tutorial/datastructures.html#sets'}]