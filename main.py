import ast
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def main():
    urlLogin = 'https://mbasic.facebook.com/login/'
    urlGroup1 = 'https://mbasic.facebook.com/groups/817620721658179'
    accountId = 'andy19970213@gmail.com'
    accountPwd = 'ryan860213'

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")  
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    driver.get(urlLogin)
    
    loginAccount = driver.find_element_by_xpath('//*[@id="m_login_email"]')
    loginAccount.clear()
    loginAccount.send_keys(accountId)

    loginPassword = driver.find_element_by_xpath('//*[@id="password_input_with_placeholder"]/input')
    loginPassword.clear()
    loginPassword.send_keys(accountPwd)

    submit = driver.find_element_by_xpath('//*[@id="login_form"]/ul/li[3]/input')
    submit.click()

    driver.get(urlGroup1)
    storyContainer = driver.find_element_by_xpath('//*[@id="m_group_stories_container"]/section')

    soup = BeautifulSoup(driver.page_source, "lxml")
    articles = soup.find_all('article')

    for article in articles[1:]:
        meta = ast.literal_eval(article.get('data-ft'))
        footer = article.find("footer")
        firstDiv = footer.find('div')
        secondDiv = firstDiv.findNext('div')
        span = secondDiv.find('span')
        reactions = span.find('a')
        likeBtn = reactions.findNext('a')
        reactBtn = likeBtn.findNext('a')
        comments = reactBtn.findNext('a')

        print(f"https://facebook.com/groups/817620721658179/permalink/{meta['mf_story_key']}")
        print(reactions.get('aria-label'))
        print(comments.string)
        print()

    time.sleep(10)

if __name__ == "__main__":
    main()