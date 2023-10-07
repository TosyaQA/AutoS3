import yaml
import time
import pytest
from module import Site

with open('./config.yaml') as f:
    config = yaml.safe_load(f)

site = Site(config['address'])
text = 'my_autotest'

def test_post_create_and_delete():
    inputs = site.find_elements('css', '#login .mdc-text-field__input')
    inputs[0].send_keys(config['login'])
    inputs[1].send_keys(config['password'])

    site.find_element('css', '#login .submit button').click()
    time.sleep(2)

    site.find_element('css', '#create-btn').click()
    time.sleep(1)

    create_item_inputs = site.find_elements('css', '#create-item .mdc-text-field__input')
    create_item_inputs[0].send_keys(text)
    create_item_inputs[1].send_keys(text)
    create_item_inputs[2].send_keys(text)
    site.find_element('css', '#create-item button[type=submit]').click()
    time.sleep(3)
    assert site.find_element('css', 'h1').text == text

def test_post_removed():
    site.find_element('xpath', '//button[text()="delete"]').click()
    time.sleep(3)
    try:
        site.find_element('xpath', f'//*[text()="{text}"]')
        assert False
    except:
        assert True

def test_contact_us():
   site.find_element('css', 'a[href^="/contact"]').click()
   time.sleep(2)
   inputs = site.find_elements('css', '#contact .mdc-text-field__input')
   inputs[0].send_keys('test')
   inputs[1].send_keys('text@text.ru')
   inputs[2].send_keys('text')
   site.find_element('css', '.mdc-button__label').click()
   time.sleep(3)
   alert = site.driver.switch_to.alert
   assert alert.text == 'Form successfully submitted'
   

if __name__ == '__main__':
    pytest.main('-v')