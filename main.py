from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from flask import Flask

# import python files
import launch_tradingview
import cycle_stocks

# starts webdriver with Chrome manager
driver = webdriver.Chrome(ChromeDriverManager().install())

# launches tradingview & logins with google+
try:
    launch_tradingview.launch(driver)
except:
    print("failed")


# infinite loop until error or closed
def start():
    while True:
        try:
            # cycles stock picks
            cycle_stocks.cycle(driver)
        except:
            print("failed")
            break


start()

# below is for flask app
# app = Flask(__name__)

# @app.route("/")
# def webapp():
#     return "Hello World!"
#
#
# if __name__ == '__main__':
#     app.run()
