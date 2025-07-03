from datetime import datetime
from playwright.sync_api import sync_playwright
from utils.logger import *
import allure
from allure_commons.types import AttachmentType
import os


def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(
        headless=True,
        args=['--start-maximized'],
        slow_mo=200
    )
    context.ctx = context.browser.new_context(
        no_viewport=True,
        record_video_dir='allure-results/',
        ignore_https_errors=True
    )


def before_scenario(context, scenario):
    context.page = context.ctx.new_page()
    context.page.goto('https://www.saucedemo.com/')


def after_scenario(context, scenario):
    log_message('info', f'Closing the page for scenario {scenario.name}')

    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    scenario_name = '_'.join(scenario.name.split('--')[0].split(' '))

    # Screenshot path
    screenshot_path = f"allure-results/{scenario_name}_{timestamp}.png"
    context.page.screenshot(path=screenshot_path)
    log_message('info', 'Screenshot saved.')

    # Attach screenshot
    with open(screenshot_path, 'rb') as f:
        allure.attach(f.read(), name='Screenshot', attachment_type=AttachmentType.PNG)

    # Close the page to ensure video finalizes
    context.page.close()

    # Attach video only if scenario failed
    if scenario.status == 'failed':
        log_message('error', f'{scenario.name} failed')

        # Get the last video file in the allure-results folder
        try:
            videos = [
                os.path.join('allure-results', f) for f in os.listdir('allure-results')
                if f.endswith('.webm')
            ]
            if videos:
                latest_video = max(videos, key=os.path.getctime)
                with open(latest_video, 'rb') as video_file:
                    allure.attach(video_file.read(), name="Failure Video", attachment_type=AttachmentType.MP4)
                log_message('info', f'Attached video: {latest_video}')
            else:
                log_message('error', 'No video file found to attach.')
        except Exception as e:
            log_message('error', f'Error attaching video: {str(e)}')


def after_all(context):
    log_message('info', 'Closing browser and context')
    context.ctx.close()
    context.browser.close()
    context.playwright.stop()
