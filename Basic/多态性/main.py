from child import Child 


def main():
	c = Child(100,300)
	c.eat()
	c.play()
	print(c.money, c.faceValue)


if __name__ == "__main__":
	main()