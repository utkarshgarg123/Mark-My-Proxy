from selenium import webdriver
import winsound
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

frequency = 2500 
duration = 1000
duration_long = 60000*5

#for online chromedriver
# chromww = webdriver.Chrome(ChromeDriverManager().install())
opt = Options();
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2, 
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 2, 
    "profile.default_content_setting_values.notifications": 2
  })

#download chrome_driver.exe(it should be of same version as of you chrome browser) from https://chromedriver.chromium.org/downloads and place its path below
chromww = webdriver.Chrome(chrome_options=opt, executable_path="C:/Users/utkar/Downloads/chromedriver_win32(1)/chromedriver.exe")
#let it remain as it is ;)
url = 'https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&_ga=2.169474785.1957672599.1596639811-1081232667.1596639811&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
# set the class code
class_code= 'jekj'  
# set Email
user_email = 'xyz@iiita.ac.in'
# set the password
password = 'Yourpassword'
#set message to be typed
roll_number = 'I am present !!!'


def sign_into_meet(user_email,your_password):
    chromww.get(url)
    attendance=0
    try:
        goto_sign=chromww.find_element_by_id("identifierId")
        goto_sign.click()
        goto_sign.send_keys(user_email)
        time.sleep(3)
        nexter = chromww.find_element_by_id("identifierNext")
        nexter.click()
        time.sleep(3)
        goto_sign1=chromww.find_element_by_name("password")
        # goto_sign1.click()
        time.sleep(3)
        goto_sign1.send_keys(password)
        nexter2 = chromww.find_element_by_id("passwordNext")
        time.sleep(3)
        nexter2.click()
        time.sleep(3)
        #sign in complete
    except:
        time.sleep(3)
        sign_into_meet(user_email,password)
    while(attendance==0):
        chromww.get(url)
        try:
            join_class=chromww.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div/div[2]/div[2]/div[2]/div/c-wiz/div[1]/div/div/div[1]")
            join_class.click()
            time.sleep(6)

            #enter class code
            chromww.find_element_by_xpath("//div[3]/div/div[2]/span/div/div[2]/div[1]/div[1]/input").send_keys(class_code)
            chromww.find_element_by_xpath("//div[3]/div/div[2]/span/div/div[4]/div[2]/div/span/span").click()
            time.sleep(5)

            #your microphone is blocked
            # (for offline driver)
            chromww.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div[2]/div[1]/div/span/span").click()
            # (for online driver)
            # chromww.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div[3]/div").click()
            time.sleep(5)

            #join class
            chromww.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]").click()
            time.sleep(5)  
            # /div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/div[2]
            # /html/body/div[1]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]
            # /html/body/div[1]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/div[2]

            #goto chats
            chromww.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[8]/div[3]/div[6]/div[3]/div/div[2]/div[3]").click()
            time.sleep(5);

            #check for roll numbers
            fl = 0
            while(1):
                try:
                    chromww.find_element_by_xpath("//div[text()='IIT2019003']")
                    winsound.Beep(frequency, duration)
                    fl=1
                    print("time to mark attendance...")
                    time.sleep(2)
                except:
                    time.sleep(0.1)
                try:
                    chromww.find_element_by_xpath("//div[text()='IIT2019004']")
                    winsound.Beep(frequency, duration)
                    print("time to mark attendance...")
                    fl=1
                    time.sleep(2)
                except:
                    time.sleep(0.1)
                try:
                    chromww.find_element_by_xpath("//div[text()='IIT201905']")
                    winsound.Beep(frequency, duration)
                    print("time to mark attendance...")
                    fl=1
                    time.sleep(2)
                except:
                    time.sleep(0.1)
                try:
                    chromww.find_element_by_xpath("//div[text()='IIT2019006']")
                    winsound.Beep(frequency, duration)
                    fl=1
                    print("time to mark attendance...")
                    time.sleep(2)
                except:
                    time.sleep(2)

                if fl==1:
                    chromww.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[4]/div[1]/div[1]/div[2]/textarea").send_keys(roll_number)
                    time.sleep(3)
                    chromww.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[4]/div[2]").click()
                    attendance=1
                    break
                    
                if attendance==1:
                    winsound.Beep(frequency, duration_long)
                    break
        except:
            time.sleep(10)


# url_name(url)
sign_into_meet(user_email,password)