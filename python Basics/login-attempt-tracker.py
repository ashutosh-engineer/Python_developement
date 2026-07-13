#Build create_login_tracker(max_attempts) jo ek attempt(username, password_correct) function return kare.

'''
Har user ke failed attempts track karo
Agar max_attempts se zyada fail ho — user lock ho jaaye
Lock hone ke baad har call pe return karo {"status": "locked", "user": username}
Successful login pe failed attempts reset ho jaayein
Return karo {"status": "allowed"} ya {"status": "locked"} ya {"status": "failed", "attempts_left": n}
'''

def create_login_tracker(max_attempts):
    failed_attempts = {}   # username -> count of failed attempts
    locked_users = set()   # store locked users

    def attempt(username, password_correct):
        # If user is already locked
        if username in locked_users:
            return {"status": "locked", "user": username}

        # If password is correct, reset failed attempts
        if password_correct:
            failed_attempts[username] = 0
            return {"status": "allowed"}

        # If password is wrong, increment failed attempts
        failed_attempts[username] = failed_attempts.get(username, 0) + 1

        # Check if user exceeded max attempts
        if failed_attempts[username] >= max_attempts:
            locked_users.add(username)
            return {"status": "locked", "user": username}

        # Otherwise, return how many attempts are left
        left_attempts = max_attempts - failed_attempts[username]
        return {"status": "failed", "left_attempts": left_attempts}

    return attempt
