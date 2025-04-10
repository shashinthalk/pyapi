from playwright.sync_api import sync_playwright

def get_instagram_profile(login_username, login_password, target_username):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.instagram.com/accounts/login/", timeout=60000)
        page.wait_for_timeout(3000)  # Let the page load

        # Accept cookies if popup shows
        try:
            page.click("text=Only allow essential cookies", timeout=5000)
        except:
            pass

        page.fill("input[name='username']", login_username)
        page.fill("input[name='password']", login_password)

        # Try to click the submit button, retrying if blocked by overlay
        try:
            submit_button = page.locator("button[type='submit']")
            submit_button.scroll_into_view_if_needed()
            submit_button.click(timeout=15000)
        except Exception as e:
            print("Error clicking submit:", e)

        # Wait for page to load after login
        page.wait_for_load_state("networkidle", timeout=15000)

        # Dismiss Save Info? popup if present
        try:
            page.click("text=Not Now", timeout=5000)
        except:
            pass

        # Dismiss Turn on Notifications popup if present
        try:
            page.click("text=Not Now", timeout=5000)
        except:
            pass

        # Go to the target user's profile page
        page.goto(f"https://www.instagram.com/{target_username}/")
        page.wait_for_timeout(5000)

        profile_data = {
            "username": target_username
        }

        try:
            # Get number of posts, followers, and following
            stats = page.locator("header section ul li span span").all_inner_texts()
            if len(stats) >= 3:
                profile_data["posts"] = stats[0]
                profile_data["followers"] = stats[1]
                profile_data["following"] = stats[2]

            # Get full name (h1) and bio
            try:
                profile_data["full_name"] = page.locator("header section h1").inner_text(timeout=3000)
            except:
                profile_data["full_name"] = ""

            try:
                profile_data["bio"] = page.locator("header section div.-vDIg span").inner_text(timeout=3000)
            except:
                profile_data["bio"] = ""

        except Exception as e:
            print("Failed to fetch some details:", e)

        browser.close()
        return profile_data
