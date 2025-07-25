from selenium import webdriver
from selenium.webdriver.common.by import By
import string, random, time


driver = webdriver.Chrome()

def random_num():
    return random.randint(1, 50)
def random_user():
    common_usernames = [
    "johnsmith", "janedoe", "mikebrown", "sarahjones", "davidwilson", "emilyclark",
    "chrisjohnson", "laurawilliams", "danielmartin", "ashleylee", "jessicawright",
    "brianthomas", "amandaharris", "kevinmoore", "mariaharris", "jameswhite",
    "oliviaroberts", "williamturner", "emmadavis", "alexandermiller", "sophiebaker",
    "nathanthompson", "hannahgreen", "ryanwalker", "isabellawood", "jackking",
    "graceyoung", "benjaminhill", "lilyscott", "samueladams", "chloemurphy",
    "jacoballen", "ellaevans", "matthewwright", "miaallen", "ethanclark",
    "abigailmartin", "loganrobinson", "madisonrodriguez", "josephlee", "sofiagarcia",
    "andrewhernandez", "avajones", "gabrielmoore", "isabellarodriguez", "jacoblopez",
    "zoewilliams", "christopherlee", "emilythomas", "ryanrodriguez", "charlottegreen",
    "nicholaswalker", "ameliahill", "alexanderyoung", "madelynhernandez",
    "benjaminarthur", "samanthabaker", "joshuaadams", "abigailmorgan",
    "danielleanderson", "zacharyjones", "victorialopez", "danielclark",
    "ellaevans", "ryanrodriguez", "avawilliams", "michaelscott", "oliviasmith",
    "andrewallen", "harperwilson", "nathanmoore", "sofiabrown", "matthewmartin",
    "madisondavis", "joshuagarcia", "isabellaroberts", "christopherthomas",
    "emilyclark", "ryanrodriguez", "charlotteyoung", "nicholashill",
    "ameliawalker", "alexandermartin", "madelynrobinson", "benjaminarthur",
    "samanthabaker", "joshuaadams", "abigailmorgan", "danielleanderson",
    "zacharyjones", "victorialopez", "danielclark", "katiejohnson", "mikelee",
    "stephanieevans", "brianclark", "lindasmith", "kevinwilliams", "marybrown",
    "davidjones", "emilywhite", "robertmoore", "sarahrodriguez", "jamesgarcia",
    "lindawilliams", "paulmartin", "susanmiller", "brianwilson", "lauramartin",
    "kevinbrown", "marythomas", "davidwilson", "emilydavis", "robertjohnson",
    "sarahlee", "jamesclark", "lindajones", "paulwilson", "susandavis", "brianmoore",
    "laurathomas", "kevinrodriguez", "maryjohnson", "davidmartin", "emilyrobinson",
    "robertsmith", "sarahmoore", "jamesbrown", "lindawilson", "pauljohnson",
    "susanrodriguez", "brianmartin", "laurabrown", "kevinwilson", "marymartin",
    "davidclark", "emilyrodriguez", "robertthomas", "sarahjohnson", "jamesmoore",
    "lindabrown", "paulwilson", "susanjones", "brianrodriguez", "laurajones",
    "kevinmartin", "marywilson", "davidbrown", "emilyjohnson", "robertmartin",
    "sarahclark", "jamesrodriguez", "lindamartin", "paulbrown", "susanwilson",
    "brianjohnson", "laurathomas", "kevinclark", "maryrodriguez", "davidwilson",
    "emilybrown", "robertscott", "sarahjohnson", "jamesmartin", "lindawilson",
    "paulbrown", "susanjones", "brianrodriguez", "laurajohnson", "kevinmartin",
    "marywilson", "davidbrown", "emilyjohnson", "robertmartin", "sarahclark",
    "jamesrodriguez", "lindamartin", "paulbrown", "susanwilson"
]

    return random.choice(common_usernames) + str(random_num())
def random_pass():
    common_passwords = [
    "123456", "123456789", "qwerty", "password", "12345678", "111111", "1234567890",
    "1234567", "password1", "12345", "123123", "987654321", "qwertyuiop", "mynoob",
    "123321", "666666", "18atcskd2w", "7777777", "1q2w3e4r", "654321", "123qwe",
    "555555", "3rjs1la7qe", "google", "1q2w3e4r5t", "1234", "qwerty123", "1qaz2wsx",
    "qazwsx", "123", "abc123", "password123", "1q2w3e", "qwert", "123abc", "football",
    "123456a", "dragon", "sunshine", "princess", "letmein", "shadow", "master",
    "66666666", "qwerty1", "11111111", "1234qwer", "123456789a", "superman", "1qazxsw2",
    "zaq1zaq1", "qwe123", "qaz123", "passw0rd", "pokemon", "11111", "123654", "1234567891",
    "12345678910", "000000", "qwertyui", "123456789q", "qwertyuiop123", "football1",
    "welcome", "login", "solo", "flower", "lovely", "sunshine1", "password1!", "asdfgh",
    "zxcvbnm", "asdfghjkl", "222222", "1234567a", "superman1", "121212", "hello", "freedom",
    "whatever", "trustno1", "6543210", "zaq12wsx", "football123", "qwe12345", "1q2w3e4r5t",
    "123456q", "123qweasd", "qweasdzxc", "1q2w3e4r5t6y", "1qaz2wsx3edc", "123qwe123",
    "password12", "password1234", "1q2w3e4r5t6", "1q2w3e4r5t6y7u", "admin", "letmein123",
    "passw0rd1", "12345qwert", "zaq12wsx34", "password!", "admin123", "user123", "hello123",
    "freedom1", "whatever1", "qwerty!", "1234!", "12345!", "123456!", "111111!", "123123!",
    "qwe123!", "abc123!", "1qaz2wsx!", "pass123!", "love123", "welcome123!", "password1!",
    "admin123!", "zaq1zaq1!", "dragon1", "sunshine1!", "princess1", "letmein1", "shadow1",
    "master1", "6666661", "qwerty11", "111111111", "1234qwer1", "football12", "superman12",
    "1234567892", "google123", "football123", "welcome1", "solo1", "flower1", "lovely1",
    "password123!", "admin!", "passw0rd!", "welcome!", "login!", "qazwsx!", "password2",
    "trustno1!", "65432101", "qwerty12", "football1234", "letmein1234", "shadow123",
    "admin12", "pass1234", "abc1234", "dragon12", "sunshine12", "princess12", "qwertyuiop",
    "password11", "12345678910!", "football!", "welcome1234", "login123", "superman123",
    "12345678q", "qwerty1234", "passw0rd12", "admin1234", "letmein12", "shadow12",
    "dragon1234", "sunshine1234", "princess1234", "password1234", "welcome123!",
    "letmein!", "password!", "123456!", "qwertyuiop1234", "admin12345", "qazwsxedc",
    "1q2w3e4r", "qwerty12345", "pass12345", "abc12345", "dragon123!", "sunshine123",
    "princess123", "football123!", "welcome123!", "superman123!", "shadow123!",
    "admin123!", "letmein123!", "password123!", "qwertyuiop1", "1234qwer!", "passw0rd1!",
    "football1!", "baseball", "shadow!", "michael", "password1!", "password2!",
    "123456789!", "1234567890!", "11111111!", "1234qwer!", "admin1", "root", "user",
    "123", "qwerty123!", "letmein123!", "12345678!", "password123!", "admin123!",
    "1234qwer1", "qwertyuiop!", "passw0rd1", "password!", "123qweasd", "password1",
    "123qweasd1", "qweasdzxc1", "password12345!", "letmein1234!", "admin1234!", "root123",
    "user1234"
]
    password = random.choices(common_passwords)
    shuffle = random_num()
    
    # Randomizer
    if shuffle > 25:
        random.shuffle(password)
    return password


for i in range(2000):
    driver.get("http://127.0.0.1:5000/authenticate")    
    username = random_user()
    password = random_pass()

    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, "//input[@type='submit']").click()

    time.sleep(0.2)

driver.quit()
    
