import logging
import os
import time
from UserAgenter import UserAgent
from playwright.sync_api import sync_playwright
from core import settings

logger = logging.getLogger(__name__)


class HHClient:
    def __init__(self):
        self.url = settings.BASE_URL
        self.username = settings.LOGIN
        self.password = settings.PASSWORD
        self.session_file = settings.FILE_PATH
        self.ua = UserAgent().RandomChromeAgent()
        self.win = {"width": 1280, "height": 720}

    def get_context(self, browser):
        if os.path.exists(self.session_file):
            logger.info("Загружаются сохраненные cookie...")
            context = browser.new_context(
                storage_state=self.session_file,
                user_agent=self.ua,
                viewport=self.win
            )
            if self.is_session_valid(context):
                logger.info("Сессия валидна.")
                return context
            else:
                logger.info("Сессия невалидна. Удаляем файл и повторяем авторизацию.")
                os.remove(self.session_file)
                return self.create_new_session(browser)
        else:
            logger.info("Cookie не найдено. Создаем новую сессию.")
            return self.create_new_session(browser)

    def create_new_session(self, browser):
        """Создает новую сессию с авторизацией"""
        context = browser.new_context(user_agent=self.ua, viewport=self.win)
        page = context.new_page()
        try:
            page.goto(f'{self.url}/account/login?backurl=%2F&hhtmFrom=main', wait_until="domcontentloaded")
            time.sleep(2)

            page.click('span[data-qa="expand-login-by-password-text"]')
            time.sleep(1)

            page.fill('input[data-qa="login-input-username"]', self.username)
            page.fill('input[data-qa="login-input-password"]', self.password)

            page.click('button[data-qa="account-login-submit"]')

            page.wait_for_selector('div[data-qa="mainmenu_applicantProfile"]', timeout=10000)

            context.storage_state(path=self.session_file)
            logger.info("Сессия успешно сохранена в файл.")
            return context

        except Exception as e:
            logger.error(f"Ошибка при авторизации: {e}")
            page.close()
            raise

    def is_session_valid(self, context):
        """Проверяет валидность сессии"""
        page = context.new_page()
        try:
            page.goto(f'{self.url}/applicant/settings', wait_until="domcontentloaded")
            page.wait_for_selector('h1[data-qa="bloko-header-1"]', timeout=5000)
            return True
        except Exception:
            logger.info("Сессия невалидна, требуется повторная авторизация.")
            return False
        finally:
            page.close()

    def get_resumes(self, context):
        """Открывает страницу с резюме и нажимает на кнопки обновления"""
        page = context.new_page()
        try:
            page.goto(f'{self.url}/applicant/resumes', wait_until="domcontentloaded")
            time.sleep(2)

            update_buttons = page.query_selector_all(
                'button[data-qa="resume-update-button resume-update-button_actions"]')

            if not update_buttons:
                logger.info("Кнопки обновления резюме не найдены.")
                return

            for button in update_buttons:
                button.click()
                time.sleep(2)

            logger.info("Все резюме обновлены.")

        except Exception as e:
            logger.error(f"Ошибка при обновлении резюме: {e}")
        finally:
            page.close()

    def process(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
            context = self.get_context(browser)
            self.get_resumes(context)
            logger.info("Процесс завершен.")
            browser.close()


client = HHClient()
