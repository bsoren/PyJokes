from joke_service import JokeService

if __name__ == "__main__":
    js = JokeService()
    print(f'Sending emails to {js.to_emails}')
    js.send_joke()
    print(f'Joke sent successfully on {js.get_unique_dt_str()}')