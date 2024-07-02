import os.path

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

from db import (
    create_and_seed_db,
    fetch_saved_waiting_list_persons,
    save_new_persons_to_db,
)

PATH_TO_DB = "./waitinglist.db"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
# options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)


def main():

    login_to_member_system()

    goto_waitinglist_page()

    persons_on_waiting_list = extract_persons_on_waiting_list()
    saved_persons_on_waiting_list = fetch_saved_waiting_list_persons()

    # TODO: This whole section sucks ass - ie. it's confusing - so refactor that thang ..
    persons_not_in_saved_waiting_list = []
    if os.path.exists(PATH_TO_DB):
        for person in persons_on_waiting_list:
            if person not in saved_persons_on_waiting_list:
                persons_not_in_saved_waiting_list.append(person)

    else:
        create_and_seed_db(persons_on_waiting_list)

    if persons_not_in_saved_waiting_list:
        save_new_persons_to_db(persons_not_in_saved_waiting_list)

        with open("./persons_not_on_waiting_list.txt", "a") as f:
            for person in persons_not_in_saved_waiting_list:
                f.write(person[0])


def login_to_member_system() -> None:
    driver.get("https://members.codingpirates.dk/account/login/?next=/")

    creds = get_credentials()

    fill_form_element(By.ID, "id_username", creds[0])
    fill_form_element(By.ID, "id_password", creds[1])
    click_btn(By.CLASS_NAME, "block-button")


def get_credentials() -> list[str]:
    with open("./credentials.txt") as f:
        return f.read().split(" ")


def goto_waitinglist_page() -> None:
    driver.get("https://members.codingpirates.dk/admin/members/waitinglist/")


def fill_form_element(by: str, value: str, text: str) -> None:
    element = driver.find_element(by, value)
    element.send_keys(text)


def click_btn(by: str, value: str) -> None:
    element = driver.find_element(by, value)
    element.click()


def extract_persons_on_waiting_list() -> list[tuple]:

    html = driver.page_source

    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", {"id": "result_list"})
    tbody = table.find("tbody")
    trs = tbody.find_all("tr")

    persons_on_list = []
    for tr in trs:
        person = (tr.find("td", {"class": "field-person_link"}).a.text,)
        persons_on_list.append(person)

    return persons_on_list


if __name__ == "__main__":
    main()
