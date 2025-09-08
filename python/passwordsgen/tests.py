import random 

characters=['q','b','s','e','z','t','y','j','o','2','1','6','7','8','9','0','/','!','@','$','#']

def generate_password(passwords_lenght=10):
	password=''
	for i in range(passwords_lenght):
		password+=random.choice(characters)
	return password


def main():
	password=generate_password()
	print(f"the password generated is {password}")

if __name__=="__main__":
	main()
	