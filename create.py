# Coded by Farhan Ali
# i.farhanali.dev@gmail.com
# If any one want to contribute, Fork it add features then pull request

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from time import sleep
from random import (choice, choices, randint)
from string import (ascii_letters, digits)

# Generate Random Data
class Data:
    @staticmethod
    def getName():
        return choice(['Aijaz Ali', 'Zulfiqar Ali', 'Kamran Wassan', 'Shoaib Shoaib', 'Muhbbat Wassan', 'Rana Waseem', 'Paras Paras', 'Rana Mohsin', 'Aliali Aliali', 'Ali Ali', 'Ghulam Ghulam', 'Waqar Lakho', 'Junaid Chandia', 'Asif Jan', 'Ali Gulam', 'Malik Saab', 'Rana Zakir', 'Zameer Ali', 'Irshad Jan', 'Gulam Shabir', 'Tariq Rajput', 'Sajid Ali', 'Shamshad Ali', 'Mola Bux', 'Awais Rao', 'Shahbaz Ali', 'Rana Sahil', 'Khadam Faqir', 'Mukhtiar Magsi', 'Ghulam Ali', 'Shah Mohammed', 'Rawal Ali', 'ستار دادا', 'Abdul Majeed', 'Mer Muhammad', 'Ali Rajput', 'Rana Farman', 'Ahtisham Rajput', 'Alideno Khoso', 'Own Rana', 'Suhail Ahmed', 'Gulzar Ahmed', 'Ahamd Jam', 'Tasawar Rajput', 'Fida Qureshi', 'Shamshad Rahu', 'سوشل ميڍيا', 'Sheeraz Abbasi', 'Bashir Ustad', 'Zubair Rao', 'Zafar Ali', 'Yaqoob Ali', 'M Soomar', 'Altaf Hussain', 'Bahadur Ali', 'Farman Ali', 'Waris Ali', 'Rana Qurban', 'Muhammad Khan', 'Asad Asad', 'Sartaaj Sartaaj', 'Rana Kabir', 'Rana Abdul', 'Ghulam Hussain', 'Kirshan Kumar', 'Adil Rajpoot', 'Sahoowal Sahoowal', 'عبد الجبار', 'Imran Ali', 'Faz Mahammad', 'Safeel Nawaz', 'ريا ض', 'Haroon Rana', 'Amjad Ali', 'Kashii Rajpoot', 'Junejo Sahib', 'Altaf Pahore', 'Ali Rajput', 'Zeeshan Ali', 'Muhammad Muktiar', 'Iftikhar Ahmand', 'Shahzeb Ali', 'Faiz Jutt', 'Chanesar Khan', 'Ali Shar', 'Zuhair Ahmed', 'محب علی', 'Siraj Khaskheli', 'Rana Dilshad', 'Ghazanfar Ali', 'Rao Awais', 'Jaan Jaan', 'Syed Junaid', 'Abdul Ghaffar', 'Kirshan Kumar', 'ابومحمد احمد', 'Nisar Hussain', 'Nasir Dahri', 'Hakim Khan', 'Ahsan Raza', 'Nadir Rind', 'Sålmàñ Çh', 'GhulamNabi Khaskhali', 'Umar Lal', 'NabeelHy Ka', 'Dilshad Magsi', 'Haaji Anwar', 'Nisar Ahmed', 'Barkat Ali', 'Irfan Ali', 'Aslam Khan', 'Hashim Khoso', 'Abdul Malik', 'Masroor Zardari', 'Rao Bilal', 'Nisarkhoso Nisarkhoso', 'مرجع الناطق', 'Sajawal Rajput', 'Rana Muhammad', 'Rana Dilshad', 'Rana Imran', 'Daniyal Kazmi', 'Faqeer Baboo', 'Azan Jan', 'Gul Hassan', 'Nadir Jan', 'NadeemRind Rind', 'Angel Rodriguez', 'Allahbux Rang', 'Ghullam Muhammad', 'Talib Hussain', 'Abid Ali', 'Rana Noushad', 'Ghulam Hussain', 'Samir Samir', 'Shahid Rana', 'Janib Janib', 'Maria Albuquerque', 'Rana Qasim', 'Faizan Ali', 'Ali Gul', 'Madeji Power', 'Rajput Faisal', 'Mansoor Sahito', 'Ali Dero', 'Razaq Khaskheli', 'Muneer Ali', 'Imran Ali', 'Sakhawat Ali', 'Khadim Baloch', 'Rana Taswar', 'Raouf Chadhar', 'Umar Shahzad', 'Shah Mir', 'Irfsn Irfsn', 'Abbas King', 'Aftab Ali', 'M Raju', 'Ghulam Mustafa', 'Gul Sher', 'Nazim Hussain', 'Malik Jawed', 'Deedar Hussain', 'Maham Khan', 'Junaid Rajput', 'Sawan Ali', 'Sajwal Rao', 'Ayaz Ali', 'Irfan Irfan', 'Hut Khan', 'Ana Mendez', 'Shakeel Khosa', 'Javed Javed', 'Dil E', 'Rana Adil', 'Rahil Ali', 'Innayat Ali', 'Aijaz Abbasi', 'Jamil Jan', 'Fidah Khoso', 'Rana Abdul', 'Rana Junaid', 'Malik Sajid', 'Ghulam Ali', 'Ahsan Ali', 'Imtiaz Ali', 'Islam Baloch', 'Hashim Khoso', 'Sattar Buledi', 'Nanik Ram', 'Gul Wali', 'Rahman Khan', 'Ali Hassan', 'Sooraj Kumar', 'GhulamAbbas Channa', 'Muhammad Saleh', 'Ali Ali', 'Ayazaliayaz Ayazaliayaz', 'Asif Baloch', 'Mujeeb Bds', 'Rana Mustak', 'Ali Rind', 'Amjad Ali', 'سلامدين سلامدين', 'Himat Ali', 'Amanullah Abro', 'Shookat Ali', 'Mushoque Malokhani', 'Zulifqar Ali', 'Fareed Abro', 'Zuhaib Ali', 'Rasmyh Rasmyh', 'Zubair Ali', 'Waheed Ali', 'Mohsin Shaikh', 'Muzamil Rajput', 'Gul Bahar', 'Zaffar Khoso', 'Akram Ali', 'Rana Sajids', 'Noor Highlights', 'Basher Baloch', 'Musam Aill', 'Jamshed Rana', 'علی مولا', 'Hero G', 'Rematullha Rajpoot', 'Ustad Hanif', 'Zubair Ali', 'Rana Abdul', 'Kamran Ali', 'Kosar Vighamal', 'Mansoor Ali', 'Nadeem Raza', 'Niaz Hussan', 'Awais Malik', 'Ammar Shoz', 'Atta Mohmad', 'Naeem Khan', 'Sanju Bhai', 'Waseem Abass', 'Ghulam M', 'Muhammad Urs', 'Zahid Hussain', 'Rana Rajput', 'Meer Jan', 'Waris Ali', 'Inayat Np', 'Sher Muhhammd', 'Rana Muzfar', 'Beni Solis', 'Suba Ali', 'Umesh Kumar', 'Basit Kahout', 'Rafiq Khaskali', 'Saira Khan', 'Rizwan Ali', 'Shahbaz Ali', 'Ail Aagsr', 'M Rafiq', 'Alom Alahaj', 'Muhmmad Waris', 'Sameer Ali', 'Rana Qaser', 'Fkgkodfj Xkxnxuc', 'Saijad Ali', 'Nadeem Jan', 'Ajkhoso Ajkhoso', 'Huzaifa Ansari', 'Mazhar Abbas', 'Molaa Bux', 'Mashuq Ali', 'Aneel Kumar', 'Zahid Hussain', 'Alihyder Kalhoro', 'Rana Rana', 'Bashir Ahmed', 'Khalid Hussein', 'Mumtaz Ali', 'Arif Memon', 'Ayoub Baloch', 'Tehmoor Ali', 'Imran Ali', 'Shamshad Ali', 'Ghulam Hussain', 'Sajjad Panhwar', 'Mole Deno', 'Farooq Bhaijan', 'Israr Jakhrani', 'Imtyaz Ali', 'Adeel Masih', 'Gull Hassan', 'Tando Adam', 'منظور راهو', 'Rana Rehman', 'Mamtaz Sehto', 'Amjid Ali', 'Rana Mubashir', 'Hamidullah Mangsi', 'Ghulam Nabi', 'Ahmed Ali', 'Syedjaved Shah', 'Rao Hassan', 'Papoo Kumar', 'Mehtab Ali', 'Rana Kashif', 'Rana Wnus', 'Farman Ali', 'Zulifiqar Zulifqar', 'Sadam Chandio', 'Mitho Mallah', 'کاشف راجپوت', 'Shamshaad Rahoo', 'Hajan Abbasi', 'Muneer Zaib', 'Ayaz Ayaz', 'Zain Ali', 'Ghulam Muhammad', 'Rao Bilal', 'Babu Khan', 'Rana Ikram', 'Rana Nasir', 'Amen Rajpot', 'Fardeen Panhwar', 'نگاھ حبيب', 'Nadeem Ali', 'Najaf Ali', 'عمران عباسی', 'Sahil Shah', 'Ali Hassan', 'Sonu Jani', 'Ajmal Abbasi', 'Abn Rajab', 'Imtiyaz Yousufzai', 'Dildar Ali', 'Adil Rao', 'Badshah Yt', 'Sawan Ali', 'Ali Ahmed', 'Amir Ali', 'Amjad Ali', 'Shahid Khan', 'Siama Khan', 'Gulam Shabir', 'Tehmoor Hassan', 'Ghulam Ali', 'Masum Ali', 'Dedar Ali', 'Shani Jutt', 'Rintu Kumar', 'Sikandar Shah', 'Furqan Jutt', 'Rahil Ali', 'Rana Shehzad', 'Nisha Kumari', 'Jamshed Khan', 'Zawar Safdar', 'Murtaza Ali', 'Muhammad Aijaz', 'Punhal Ali', 'Bisharat Mirbahar', 'Xtylíśh Shahmir', 'نصيراحمد ميمڻ', 'Darya Khan', 'Imdad Khoso', 'Allyas Allyas', 'Amjad Ali', 'Bhatti G', 'Faizan Aziz', 'Rashad Baloch', 'Abdul Jabar', 'Rana Shafiq', 'Hamadullah Lakho', 'Ziafat Khan', 'Faqeer N', 'Rana Ibrar', 'Shafi Muhmmad', 'Awees Ali', 'Amir Ali', 'Ali Khan', 'QaMar ZaMan', 'Rana Naveed', 'فرینا فرینا', 'Ghul Sher', 'Safeer Khaskhali', 'Rana Asim', 'Farhan Ali', 'Ghulam Abbas', 'Zulfiqar Ali', 'Zakir Ali', 'Rhman Ali', 'Rana Ali', 'Muneer Khan', 'Mumtaz Ali', 'Nadeem Ali', 'Zameer Shah', 'Faheem Ahmad', 'Pordip Mandal', 'Shahzaib Rahman', 'Zidi Bacha', 'Waqar Rajput', 'Ali Akbar', 'Ali Raza', 'Sabir Ali', 'Rana Qurban', 'Ali Bahte', 'Sajad Ali', 'Ahadattaullah Malik', 'Muzammil Hussain', 'Jan Muhammad', 'Fasial S', 'Ameer NaNa', 'Makro Sharif', 'Mithal Khaskheli', 'محمدموسا محمدموسا', 'Mitho Mallah', 'Muzzamil Ali', 'Ahmad Hassan', 'Babar Babar', 'Zawar Muhammad', 'Rana Nadir', 'Mazhar Ali', 'Rana Irfan', 'Bilal Abbasi', 'Ghulam Jaffar', 'Asif Rana', 'Mœhäməd Řhæ', 'M Nawaz', 'Farooq Ali', 'Ashfaq Rahoo', 'Azmat Ali', 'Mateen Rana', 'Shan Ali', 'Çhårîyē Çhøkrī', 'Parwez Ali', 'Azhar Hussain', 'Shahabaz Ali', 'Syed Ghot', 'Zahid Hussain', 'Mir Babu', 'Zarik M', 'Shakel Ansari', 'Hafiz Imran', 'Shah Zaib', 'Bilal Jan', 'Asif Asif', 'Asif Asif', 'Muzafar Rajbut', 'Makhdoom Ghulam', 'Rana Farooq', 'Gulam Yaseen', 'Ashiqe Jatt', 'Arshad Brohi', 'Nazeer Ahmed', 'Sajad Ali', 'Mircho Mal', 'Rana Junaid', 'Lakho Mal', 'Sajid Ali', 'Raees Rahat', 'Irfan Ali', 'Rana Imran', 'Ali Mughal', 'Riaz Khan', 'Ahsan Bozdar', 'Shahidalisolangi Shahidalisolangi', 'Tariq Tariq', 'Rao Nasir', 'Zahid Ali', 'Shahzad Madni', 'Sarfaraz Rahu', 'Mubashair Rana', 'Ahsan Khoso', 'Jalger Bhatti', 'Rana Wajid', 'Lala Aziz', 'Shakir Abbasi', 'Ali Asgar', 'Ruble Hasan', 'Abdul Rehman', 'Azizullah Soomro', 'Abbas Ali', 'Muhammad Ali', 'Rana Wajid', 'Rana Musharaf', 'Rashid Qureshi', 'Shahmeer Chandio', 'Shan Ali', 'Ahmed Qureshi', 'Zaheer Abbas', 'Imran Ali', 'Asif Khan', 'Shahid Ali', 'Mangii Mangii', 'Momin Ali', 'Meer Shan', 'Muqu Poiro', 'Umar Shahzad', 'Waris Ali', 'Numwar Ali', 'Muhammad Tahir', 'AKhtar Ali', 'Rana Sajid', 'Sarfarazmemon Attad', 'Salim Junejo', 'Mashque Ali', 'Hassnan Ali', 'Irfan Ali', 'Adv Ali', 'Himmat Ali', 'Khalid Jamil', 'Mohsin Rajput', 'Syed Nadir', 'Raheem Punho', 'Rana Abdullah', 'Rana Noaman', 'Mansoor Solangi', 'Imran Jaan', 'Waris Ali', 'Rana Mubasher', 'Mujahid Ali', 'Hussnain Rajpoot', 'Chaudhary Abdul', 'Haider Baloch', 'Ali Dino', 'Mir Khan', 'Irfan Fatima', 'Arshad Baloch', 'Shakir Abbasi', 'Naveed Rind', 'Gul Muhammad', 'Meer Murtaza', 'Papo Papo', 'Nisar Ali', 'Gbhs Bhit', 'Sadoro Jan', 'Rana Moon', 'Ramzan Jan', 'Rana Zakir', 'Rao Waqas', 'M Waqas', 'Rana Rana', 'Rukhsar Haidry', 'RaNa BOby', 'M Juman', 'Sadiq Ali', 'Manik Khan', 'Ran A', 'Ghulab Hussain', 'Ronaq Ali', 'Tarique Ali', 'Abdul Qadir', 'Zawar Sohana', 'Mehran Rajput', 'Sikandar Ali', 'Ãtîf Â', 'Meer Shahzeb', 'Sajjad Abbasi', 'Rana Naeem', 'Bashir Ahmed', 'Rafeh Rajpoot', 'ẞk KhÄñ', 'Imtiaz Khoso', 'Alex Shahzad', 'Aman Abbasi', 'Mehran Rajput', 'Raja Rajpot', 'Bahdur Ali', 'Hammad Ali', 'Salman Salman', 'Shahzad Shahzad', 'AtaullAh Khan', 'Rafique Mirani', 'Arbab Ali', 'Nisar Ali', 'Zahid Hussain', 'Rana Shahzad', 'Rana Ramzan', 'Noro Mohmad', 'Riaz Rajput', 'Mahbat Khan', 'Ahsan Ali', 'Rana Ikram', 'Qamar Abbas', 'Jahanzib Ali', 'Rana Sunny', 'Rao Yasir', 'Muhammad Mithal', 'Ashiq Hussain', 'Ha Ni', 'Abdul Latif', 'Meer Mortaz', 'Meer Zohaib', 'Zahid Bhatti', 'Awais Rajput', 'Ali Bux', 'Abdul Hakeem', 'Hassnain Muavia', 'Syed Junaid', 'Riaz Machi', 'Ahsan Abro', 'Hyder Ali', 'Sattar Sattar', 'Sayed Sharafat', 'Syed Bilalarif', 'Lal Muhmmad', 'Mohsin Ali', 'Asif Ali', 'Juleed Shah', 'Hayat Khan', 'Ali Bux', 'पवन अल्लापुर', 'Ghulam Nabi', 'Zaheer Ali', 'Soomar Bughio', 'Madad Ali', 'Naeem Chohan', 'Javed Javed', 'Waseem Raza', 'Saorg Khan', 'Zeeshan Zeeshan', 'Aliza Chaudhary', 'Rana Shuaib', 'Ali Khan', 'Rao Shabbir', 'Commandos King', 'Arshad Sli', 'Rana Shahrukh', 'Ratan Kumar', 'Umar Khan', 'Ali Bhnoo', 'Shahzaib Shah', 'Aqib Gakhar', 'Rana Ishaq', 'Bilal Rajput', 'Asif Khan', 'Hazrat Hussain', 'Zohair Ali', 'Parvez Ali', 'Altaf Hussain', 'Mashooq Ali', 'Dilshad Magsi', 'Gulam Mustafa', 'Safdiar Khan', 'Tofiq Khan', 'Sudheer Ahmad', 'Suhrab Pardesi', 'Syed Badshah', 'Ashok Kumar', 'Ssbri Chandio', 'Yaseen Ali', 'Rimsha Shehzadi', 'Meer Aamir', 'Lakhiar Adeel', 'Ariz Muhammad', 'عبداللہ کوھارو', 'Yameen Ali', 'Sahil Gadehi', 'Sahab Ali', 'Naimatullah Ali', 'Baqir Sajjad', 'مير حارث', 'M Slutan', 'Sadaqat Ali', 'Fahad Ali', 'Muhammed Shabeer', 'Khalifo Chandio', 'Zohaib Ali', 'Ab Ghani', 'Ibrahim Baloch', 'Rehmatullah Mastoi', 'Mohammed Younis', 'Shahzadi Kiran', 'Ahmad Khan', 'Arshad SooMro', 'Sadam Solangi', 'Yamen Ali', 'Majid Khan', 'Ab Aziz', 'Sabir Khuharo', 'Nazeer Chandio', 'Md Samer', 'Kaif Qureshi', 'MuHammad HaaDi', 'Altaf Khan', 'Majid Ali', 'Muhammad Abraim', 'Noor Ahmed', 'Abid Hussain', 'Ashraf Buriro', 'Rajib Ali', 'Ahsan Ali', 'Aakash Khuharo', 'Hassan Ali', 'Awaiz Memon', 'Asharf Malah', 'Muslim Chandio', 'Haji Saddam', 'Rashid Ali', 'Assadullah Kolachi', 'Kashif Ali', 'Irfan Ali', 'Zulfqar Soomro', 'Ghafar Chandio', 'Younis Ali', 'Meer Murtiza', 'Majahd Ali', 'Rao Arslan', 'Rana Tsawar', 'Akbar Rajput', 'Rana Yasir', 'Rana Waqar', 'Rana Umer', 'Rao Zeeshan', 'Rana Aqib', 'Rana Mudassar', 'Rana Zubair', 'Rana Zohaib', 'Rana Rana', 'Rao Shoaib', 'Nokhaiz Rao', 'Rana G', 'Saeed Somro', 'Rana Muklish', 'Muzamil Rajput', 'Râõ Zêshãñ', 'Rana Nasrullah', 'Rana Naveed', 'Hamza Rajpoot', 'Rana Naveed', 'Rana Zahid', 'Rao Ali', 'Rao Ishfaq', 'Ehsan Rana', 'Ahsan Rana', 'Mohammed Akmal', 'Rana Naeem', 'Rana Ahmad', 'Rana Shani', 'Rao Nasir', 'Rao M', 'Rana Imran', 'Rao Arshad', 'Rao Sanaullah', 'Ali Rana', 'Rao Muhammad', 'Rana Gulraiz', 'Salal Rajput', 'Rana Muhammad', 'Ijaz Rajpoot', 'M Farman', 'Rao Raees', 'Rana Umar', 'Umair Rana', 'Shafiq Rajpoot', 'Rana Numan', 'Rao Shb', 'Rana Yousif', 'Rana Liaqat', 'Rana Asad', 'Zafar Rajpoot', 'Rao Hamza', 'Abubakar Rajput', 'Rao M', 'Rana Ishaq', 'Waqas Rajpoot', 'Amir Sohail', 'Rao Sohaib', 'Rana Shazil', 'Rao Bilal', 'Rao Altaf', 'Rao Nabeel', 'Hamza Rao', 'Asif Rana', 'Rana Umair', 'Raokashif Ali', 'Rao Qaiser', 'Rana Attual', 'Rana Shabaz', 'Rao Salman', 'Rao Samad', 'Rao Shoaib', 'Rana A', 'Rao Kashif', 'Rao Zarar', 'Rana Tayyub', 'Raja Kamal', 'Amir Rajput', 'RaoAlizaman RaoAlizaman', 'Hamza Rao', 'Rana Falak', 'Sikandar Khan', 'Rao Shahbaz', 'Rana Talha', 'Kashif Rajpoot', 'Hammad Rana', 'Hamza Rao', 'Roa Zahid', 'Rana Hamza', 'Rao Saleem', 'Rao Faryad', 'Rao Abubakar', 'Bilal Rajput', 'Rao Waseem', 'Sonu Rao', 'Rana Rizwan', 'Bilal Rao', 'Rans Maqsood', 'Rana Furqan', 'Rao Ali', 'Rana Muzamil', 'M Asif', 'Rao Sohail', 'Rana Bahadur', 'Rana Muhmmad', 'Shahzada Gs', 'Rao Farhan', 'Zahgim Ali', 'Abaid Raja', 'Rana Waseem', 'Rana Ajmal', 'Rao Latif', 'Rao Aqib', 'Rana Ramzan', 'Wajid Rana', 'Sabir Rajpoot', 'Rana Shehryar', 'Rana Yaqub', 'Rao Abdul', 'Rajput Sab', 'Rana Tasawar', 'Rana Waseem', 'Rana Babar', 'Rana Shahid', 'Rana Maviya', 'Rana Saeed', 'Waheed Rajput', 'Junaid Rajpoot', 'Rao Saqib', 'Rao Azeem', 'Rana Ali', 'Muhammad Nadeem', 'Rana Majid', 'Rana Sahab', 'Abubakar Jatoi', 'Sabir Dogar', 'Ameen Rana', 'Rana Shakeel', 'Rao Tasleem', 'Pʀɩŋcɘ Nʌsɩʀ', 'Rana Mani', 'Rana Jee', 'Zidi Rana', 'Rana Kamran', 'Rana Zabi', 'Mehtab Rao', 'حسن راو', 'Rana Sajid', 'Rao Aftab', 'Rana Muhammad', 'Muhammad Muhammad', 'Rao Abdulrazaq', 'Rao MubeenRao', 'Rao Nazeer'])

    @staticmethod
    def getNumber():
        num = "".join(choices(digits, k=7))
        code = str(randint(0, 4)) + str(randint(0, 9))
        return "+923%s%s" % (code, num)
    
    @staticmethod
    def getBirthday():
        day = str(randint(0, 27))
        month = str(randint(0, 12))
        year = "19" + str(randint(60, 99))

        return day, month, year
    
    @staticmethod
    def getPassword():
        return "".join(choices(ascii_letters + digits, k=15))
    
class Creator:
    HOME = "https://web.facebook.com/"
    REG = "https://www.facebook.com/r.php?locale=en_US&display=page"
    content = ""

    def __init__(self) -> None:
        service = Service(executable_path="E:\\msys64\\usr\\bin\\chromedriver.exe")
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options, service=service)
        self.driver.maximize_window()
    
    def go(self, url):
        self.driver.get(url)
        self.content = self.driver.page_source
    
    def find(self, by, data):
        return self.driver.find_element(by, data)
    
    def create(self) -> None:
        self.go(self.REG)
        sleep(1)
        first_name, last_name = Data.getName().split(" ")
        number = Data.getNumber()
        day, month, year = Data.getBirthday()
        password = Data.getPassword()

        sleep(2)
        self.find(By.NAME, "firstname").send_keys(first_name)
        sleep(2)
        self.find(By.NAME, "lastname").send_keys(last_name)
        sleep(2)
        self.find(By.NAME, "reg_email__").send_keys(number)
        sleep(2)
        self.find(By.NAME, "reg_passwd__").send_keys(password)
        sleep(2)
        month_input = Select(self.find(By.NAME, "birthday_month"))
        month_input.select_by_value(month)
        sleep(2)
        day_input = Select(self.find(By.NAME, "birthday_day"))
        day_input.select_by_value(day)
        sleep(2)
        year_input = Select(self.find(By.NAME, "birthday_year"))
        year_input.select_by_value(year)
        sleep(2)
        self.find(By.XPATH, "//label[text()='Male']").click()
        sleep(2)
        self.find(By.NAME, "websubmit").click()

        self.handle_checkpoint()
    
    def handle_checkpoint(self):
        # i got recaptcha problem here, :) so I discontinued this
        sleep(2)
        if "We need more information" in self.content:
            self.find(By.XPATH, "//span[text()='Continue']").click()

if __name__ == "__main__":
    c = Creator()
    c.create()
